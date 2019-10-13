import importlib
from importlib.machinery import ModuleSpec
from pathlib import Path
import sys
import pyclbr
import inspect
from unittest.mock import patch
import os
from typing import Optional, Text, Any, Callable, Generator

from handsdown.signature import SignatureBuilder
from handsdown.indent_trimmer import IndentTrimmer
from handsdown.utils import OSEnvironMock
from handsdown.module_record import ModuleRecord, ModuleObjectRecord


class LoaderError(Exception):
    pass


class Loader:
    """
    Loader for python source code.

    Examples:

        ```python
        loader = Loader(Path('path/to/my_module/'))
        my_module_utils = loader.import_module('my_module.utils')
        ```

    Arguments:
        import_paths -- List of import paths for `import_module` lookup.
    """

    DJANGO_SETTINGS_ENV_VAR = "DJANGO_SETTINGS_MODULE"

    def __init__(self, root_path: Path) -> None:
        self._root_path = root_path
        self._sys_path_dirty = False
        self._os_environ_patch = patch("os.environ", OSEnvironMock(os.environ))
        self._type_checking_patch = patch("typing.TYPE_CHECKING", True)
        self._sys_path_patch = patch(
            "sys.path", sys.path + [self._root_path.as_posix()]
        )

        if os.environ.get(self.DJANGO_SETTINGS_ENV_VAR):
            self._setup_django()

    def get_md_name(self, path: Path) -> Text:
        relative_path = path.relative_to(self._root_path)
        name_parts = []
        for part in relative_path.parts:
            if part == "__init__.py":
                part = "index"
            stem = part.split(".")[0]
            name_parts.append(stem)

        if not name_parts:
            return "stub.md"

        return f"{'_'.join(name_parts)}.md"

    def get_module_record(self, source_path: Path) -> Optional[ModuleRecord]:
        """
        Build `ModuleRecord` for given `source_path`.

        Arguments:
            source_path -- Absolute path to source file.

        Returns:
            A new `ModuleRecord` instance or None if there is ntohing to import.

        Raises:
            LoaderError -- If module or any of it's objects cannot be imported.
        """
        if not (source_path.parent / "__init__.py").exists():
            return None

        if source_path.name == "__init__.py" and source_path.parent == self._root_path:
            return None

        file_import = self.get_import_string(source_path)
        output_file_name = self.get_md_name(source_path)

        try:
            inspect_module = self.import_module(source_path)
        except Exception as e:
            raise LoaderError(f"Cannot import {source_path.name}: {e}")

        module_record = ModuleRecord(
            module=inspect_module,
            output_file_name=output_file_name,
            source_path=source_path,
            import_string=file_import,
            objects=[],
        )

        try:
            module_object_records = list(self._discover_module_objects(module_record))
        except Exception as e:
            raise LoaderError(
                f"Cannot import module objects from {source_path.name}: {e}"
            )

        for module_object_record in module_object_records:
            module_record.objects.append(module_object_record)

        return module_record

    def _setup_django(self):
        self._os_environ_patch.start()
        self._sys_path_patch.start()
        django = importlib.import_module("django")
        django.setup()
        self._os_environ_patch.stop()
        self._sys_path_patch.stop()

    @staticmethod
    def get_object_signature(obj: Any) -> Optional[Text]:
        """
        Get class, method or function signature. If object is not callable -
        returns None.

        Arguments:
            obj -- Object to inspect.

        Returns:
            A string with object signature or None.
        """
        if not callable(obj):
            return None

        return SignatureBuilder(obj).build()

    @classmethod
    def get_object_docstring(cls, obj: Any) -> Text:
        """
        Get trimmed object docstring or an empty string.

        Arguments:
            obj -- Object to inspect.

        Returns:
            A string with object docsting.
        """
        docstring = cls._get_docstring(obj)

        # Fix multiline docstrings starting with no newline after quotes
        if "\n" in docstring and docstring[0] != "\n":
            lines = docstring.split("\n")
            indent = IndentTrimmer.get_line_indent(lines[1])
            docstring = f"\n{' ' * indent}{docstring}"

        return IndentTrimmer.trim_text(docstring)

    def get_import_string(self, path: Path) -> Text:
        relative_path = path.relative_to(self._root_path)
        name_parts = []
        for part in relative_path.parts:
            stem = part.split(".")[0]
            if stem == "__init__":
                continue
            name_parts.append(stem)

        return f"{'.'.join(name_parts)}"

    def import_module(self, file_path: Path) -> Any:
        """
        Import module using `import_paths` list. Clean up all patches afterwards.

        - Patch `sys.path` to add current repo to it.
        - Patch `os.environ` to avoid failing on undefined variables.
        - Patch `typing.TYPE_CHECKING` to `True`.

        Arguments:
            file_path -- Abslute path to source file.

        Returns:
            Imported module object.
        """
        self._sys_path_patch.start()
        self._os_environ_patch.start()
        self._type_checking_patch.start()

        import_string = self.get_import_string(file_path)
        try:
            module = importlib.import_module(import_string)
        except Exception as e:
            raise LoaderError(f"Cannot import {import_string}: {e}")

        self._sys_path_patch.stop()
        self._os_environ_patch.stop()
        self._type_checking_patch.stop()

        if module.__spec__ is None:
            module.__spec__ = ModuleSpec(name="__main__", loader=None, origin=None)

        return module

    @staticmethod
    def _get_inspect_predicate(object_name: Text) -> Callable[[Any], bool]:
        def predicate(method: Any) -> bool:
            if not inspect.isroutine(method) or not method.__doc__:
                return False

            if not hasattr(method, "__qualname__"):
                return False

            parent_name = method.__qualname__.split(".")[0]
            method_name = method.__qualname__.split(".")[-1]

            # skip magic methods
            if method.__qualname__ == parent_name:
                return False

            # skip private methods
            if method_name.startswith("_"):
                return False

            # skip inherited methods
            if parent_name != object_name:
                return False

            # skip built-in inherited methods
            if object_name not in repr(method):
                return False

            return True

        return predicate

    def _discover_module_objects(
        self, module_record: ModuleRecord
    ) -> Generator[ModuleObjectRecord, None, None]:
        """
        Get `ModuleObjectRecord` for every object in a module.

        Arguments:
            module_record -- `ModuleRecord` instance.

        Returns:
            A generator that yields `ModuleObjectRecord` instances.
        """
        import_string = module_record.import_string
        obj_names = pyclbr.readmodule_ex(import_string)

        for obj_name in obj_names:
            if obj_name.startswith("__"):
                continue

            inspect_object = getattr(module_record.module, obj_name)
            if not inspect.isclass(inspect_object) and inspect_object.__doc__ is None:
                continue

            yield ModuleObjectRecord(
                import_string=obj_name,
                level=0,
                object=inspect_object,
                title=obj_name,
                source_path=module_record.source_path,
                output_file_name=module_record.output_file_name,
                source_line_number=self.get_source_line_number(inspect_object),
            )

            for method_name, inspect_method in inspect.getmembers(
                inspect_object, self._get_inspect_predicate(obj_name)
            ):
                try:
                    class_method = inspect_object.__dict__[method_name]
                except KeyError:
                    continue

                import_string = f"{obj_name}.{method_name}"
                title = f"{obj_name}().{method_name}"
                if isinstance(class_method, (staticmethod, classmethod)):
                    title = f"{obj_name}.{method_name}"

                yield ModuleObjectRecord(
                    import_string=import_string,
                    level=1,
                    object=inspect_method,
                    title=title,
                    source_path=module_record.source_path,
                    output_file_name=module_record.output_file_name,
                    source_line_number=self.get_source_line_number(inspect_method),
                )

    @staticmethod
    def _get_docstring(obj: Any) -> Text:
        if isinstance(obj, (staticmethod, classmethod)):
            return obj.__func__.__doc__ or ""
        if hasattr(obj, "__name__") or isinstance(obj, property):
            return obj.__doc__ or ""
        if hasattr(obj, "__call__"):
            return obj.__call__.__doc__ or ""

        return obj.__doc__ or ""

    @staticmethod
    def get_source_line_number(obj: Any) -> int:
        """
        Get line number in source file where `obj` is declared.

        obj -- Object to inspect.

        Returns:
            A line number as an integer, starting for 1.
        """
        source_code_info = inspect.findsource(obj)
        return source_code_info[1] + 1
