import importlib
from importlib.machinery import ModuleSpec
from pathlib import Path
import sys
import pyclbr
import inspect
from unittest.mock import patch
import typing
import os
from typing import Optional, Text, Any, Callable, Generator, Tuple, Iterable

from handsdown.signature import SignatureBuilder
from handsdown.indent_trimmer import IndentTrimmer
from handsdown.utils import OSEnvironMock


class LoaderError(Exception):
    pass


class Loader:
    """
    Loader for python source code.

    Examples:

        ```python
        loader = Loader(['path/to/my_module/'])
        my_module_utils = loader.import_module('my_module.utils')
        ```

    Arguments:
        import_paths -- List of import paths for `import_module` lookup.
    """

    def __init__(self, import_paths: Iterable[Path]) -> None:
        self._import_paths = import_paths
        self._environ_mock = OSEnvironMock(os.environ)

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
        return IndentTrimmer.trim_text(cls._get_docstring(obj))

    def import_module(self, import_string: Text) -> Any:
        """
        Import module using `import_paths` list. Clean up path afterwards.
        Patch `os.environ` to avoid failing on undefined variables.
        Set `typing.TYPE_CHECKING` to `True` while importing.

        Arguments:
            import_string -- Module import string.

        Returns:
            Imported module object.
        """
        temp_import_paths = []
        for import_path in self._import_paths:
            if import_path not in sys.path:
                sys.path.append(import_path.as_posix())
                temp_import_paths.append(import_path.as_posix())

        real_type_checking = typing.TYPE_CHECKING
        typing.TYPE_CHECKING = True

        with patch("os.environ", self._environ_mock):
            try:
                module = importlib.import_module(import_string)
            except Exception as e:
                raise LoaderError(f"Cannot import {import_string}: {e}")

        if module.__spec__ is None:
            module.__spec__ = ModuleSpec(name="__main__", loader=None, origin=None)

        typing.TYPE_CHECKING = real_type_checking

        for import_path in temp_import_paths:
            sys.path.remove(import_path)

        return module

    @staticmethod
    def _get_inspect_predicate(object_name: Text) -> Callable[[Any], bool]:
        def predicate(method: Any) -> bool:
            if not inspect.isroutine(method) or not method.__doc__:
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

    def get_module_objects(
        self, import_string: Text
    ) -> Generator[Tuple[Text, Any, int], None, None]:
        """
        Yield (`name`, `object`, `level`) for every object in a module. `name` is object name.
        `object` - object iteslf. `level` - deepness of the object. Maximum `level` is 1.

        Arguments:
            import_string -- Module import string.

        Returns:
            A generator that yields tuples of (`name`, `object`, `level`).
        """
        inspect_module = self.import_module(import_string)

        obj_names = pyclbr.readmodule_ex(import_string)
        for obj_name in obj_names:
            if obj_name.startswith("__"):
                continue

            inspect_object = getattr(inspect_module, obj_name)
            if not inspect.isclass(inspect_object) and inspect_object.__doc__ is None:
                continue

            yield (obj_name, inspect_object, 0)

            for method_name, inspect_method in inspect.getmembers(
                inspect_object, self._get_inspect_predicate(obj_name)
            ):
                title = f"{obj_name}().{method_name}"
                try:
                    class_method = inspect_object.__dict__[method_name]
                except KeyError:
                    continue

                if isinstance(class_method, (staticmethod, classmethod)):
                    title = f"{obj_name}.{method_name}"

                yield (title, inspect_method, 1)

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
            A line number.
        """
        source_code_info = inspect.findsource(obj)
        return source_code_info[1] + 1
