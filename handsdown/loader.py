import importlib
import pyclbr
import inspect
from unittest.mock import patch
from collections import defaultdict
from typing import Optional, Text, Any, Callable, Generator, Tuple

from handsdown.signature import SignatureBuilder
from handsdown.indent_trimmer import IndentTrimmer


class Loader:
    """
    A utility class that is responsible for working with python source code.
    """

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

    @staticmethod
    def import_module(import_string: Text) -> Any:
        """
        Path os.environ to avoid failing on undefined variables.

        Arguments:
            import_string -- Module import string.

        Returns:
            Imported module object.
        """
        with patch("os.environ", defaultdict(lambda: "env")):
            module = importlib.import_module(import_string)

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

    @classmethod
    def get_module_objects(
        cls, import_string: Text
    ) -> Generator[Tuple[Text, Any, int], None, None]:
        """
        Yield (`name`, `object`, `level`) for every object in a module. `name` is object name.
        `object` - object iteslf. `level` - deepness of the object. Maximum `level` is 1.

        Arguments:
            import_string -- Module import string.

        Returns:
            A generator that yields tuples of (`name`, `object`, `level`).
        """
        inspect_module = cls.import_module(import_string)
        try:
            obj_names = pyclbr.readmodule_ex(import_string)
        except AttributeError:
            return
        for obj_name in obj_names:
            if obj_name.startswith("__"):
                continue

            inspect_object = getattr(inspect_module, obj_name)
            if not inspect.isclass(inspect_object) and inspect_object.__doc__ is None:
                continue

            yield (obj_name, inspect_object, 0)

            for method_name, inspect_method in inspect.getmembers(
                inspect_object, cls._get_inspect_predicate(obj_name)
            ):
                title = f"{obj_name}().{method_name}"
                class_method = inspect_object.__dict__[method_name]
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
