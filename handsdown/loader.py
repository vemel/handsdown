import importlib
from unittest.mock import patch
from collections import defaultdict
from typing import Optional, Text, Any

from handsdown.signature import SignatureBuilder
from handsdown.indent_trimmer import IndentTrimmer


class Loader:
    """
    Expects absolute identifiers to import with #import_object_with_scope().
    """

    def get_object_signature(self, obj: Any) -> Optional[Text]:
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

    def get_object_docstring(self, obj: Any) -> Text:
        """
        Get trimmed object docstring or an empty string.

        Arguments:
            obj -- Object to inspect.

        Returns:
            A string with object docsting.
        """
        return IndentTrimmer.trim_text(self._get_docstring(obj))

    @staticmethod
    def safe_import_module(import_string: Text) -> Any:
        with patch("os.environ", defaultdict(lambda: "env")):
            module = importlib.import_module(import_string)

        return module

    @staticmethod
    def _get_docstring(obj: Any) -> Text:
        if isinstance(obj, (staticmethod, classmethod)):
            return obj.__func__.__doc__ or ""
        if hasattr(obj, "__name__") or isinstance(obj, property):
            return obj.__doc__ or ""
        if hasattr(obj, "__call__"):
            return obj.__call__.__doc__ or ""

        return obj.__doc__ or ""