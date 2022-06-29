"""
Wrapper for python import strings.
"""
from typing import Any, List, TypeVar

from handsdown.exceptions import ImportStringError

_R = TypeVar("_R", bound="ImportString")


class ImportString:
    """
    Wrapper for python import strings.

    Arguments:
        value -- Import string.
    """

    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        """
        Get string value.

        Examples::

            str(ImportString("my_module"))
            "my_module"

        Returns:
            Original import string.
        """
        return self.value

    def __hash__(self) -> int:
        return hash(self.value)

    def __add__(self, other: str) -> "ImportString":
        """
        Add new import part.

        Examples::

            ImportString("my_module") + "MyClass"
            ImportString("my_module.MyClass")

            ImportString("") + "MyClass"
            ImportString("MyClass")

        Arguments:
            other -- Import string part.

        Returns:
            A new `ImportString` instance.
        """
        if self.value:
            return ImportString(f"{self.value}.{other}")

        return ImportString(other)

    def __bool__(self) -> bool:
        """
        Check if not empty.

        Examples::

            bool(ImportString("my_module"))
            True

            bool(ImportString(""))
            False

        Returns:
            True if not empty.
        """
        return bool(self.value)

    def __eq__(self, other: Any) -> bool:
        """
        Compare to another `ImportString` or a string.

        Examples::

            ImportString("my_module.MyClass") == ImportString("my_module.MyClass")
            True

            ImportString("my_module.MyClass") == ImportString("my_module.OtherClass")
            False

            ImportString("my_module.MyClass") == "my_module.MyClass"
            True

            ImportString("my_module.MyClass") == "my_module"
            False

            ImportString("my_module.MyClass") == b"my_module.MyClass"
            False

        Arguments:
            other - ImportString instance or a string.

        Returns:
            True if import strings are equal.
        """
        if isinstance(other, str):
            return self.value == other

        if isinstance(other, ImportString):
            return self.value == other.value

        return False

    @property
    def parts(self) -> List[str]:
        """
        Parts of import string splitted by dots.

        Examples::

            ImportString("my_module.MyClass")
            ["my_module", "MyClass"]

            ImportString("")
            []

        Returns:
            A list of import string parts.
        """
        return self.value.split(".")

    def is_top_level(self) -> bool:
        """
        Check if import string has no parents.

        Returns:
            True if it has no parents.
        """
        return "." not in self.value

    @property
    def parent(self: _R) -> _R:
        """
        Parent import string.

        Returns:
            A new `ImportString` instance.
        """
        if self.is_top_level():
            raise ImportStringError("Import string is top level and has no parents.")

        parent_import_string_parts = self.value.split(".")[:-1]
        return self.__class__(".".join(parent_import_string_parts))

    def startswith(self: _R, import_string: _R) -> bool:
        """
        Check if it starts with `import_string`.

        Returns:
            True if it is a child.
        """
        return self.value.startswith(f"{import_string}.")

    def get_parents(self: _R) -> List[_R]:
        """
        Get all parents.

        Returns:
            A list of `ImportString` instances.
        """
        if self.is_top_level():
            return []

        parents = []
        import_string = self
        while not import_string.is_top_level():
            parents.append(import_string.parent)
            import_string = import_string.parent

        parents.reverse()
        return parents

    @property
    def length(self) -> int:
        """
        Length of import string parts.

        Returns:
            Length of import string.
        """
        return len(self.parts)

    @property
    def name(self) -> str:
        """
        Last part of the import string.
        """
        return self.parts[-1] if self.parts else "empty"
