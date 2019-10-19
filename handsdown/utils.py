"""
Handful utils that do not deserve a separate module.
"""
from typing import Text, Any


class OSEnvironMock(dict):
    """
    Mock for `os.environ` that returns `env` string instead of undefined variables.
    """

    def __getitem__(self, key):
        # type: (Text) -> Any
        if key not in self:
            return self.__missing__(key)
        return super(OSEnvironMock, self).__getitem__(key)

    def __missing__(self, key):
        # type: (Text) -> Text
        return "env"


class TypeCheckingMock:
    """
    Helper to turn on anf off `TYPE_CHECKING`.

    Returns `True` for the first call, `False` for subsequent.
    """

    def __init__(self):
        # type: () -> None
        self._value = True

    def __bool__(self):
        # type: () -> bool
        """
        Check if TYPE_CHECKING should be enabled.

        Returns:
            `True` for the first call, `False` for subsequent.
        """
        result = self._value
        self._value = False
        return result


def get_title_from_path_part(path_part):
    # type: (Text) -> Text
    """
    Convert `pathlib.Path` part to a human-readable title.
    Replace underscores with spaces and capitalize result.

    Examples::

        get_title_from_path_part("my_path.py")
        "My Path Py"

        get_title_from_path_part("my_title")
        "My Title"

        get_title_from_path_part("__init__.py")
        "Init Py"

    Arguments:
        path_part -- Part of filename path.

    Returns:
        A human-readable title as a string.
    """
    parts = path_part.replace(".", "_").split("_")
    parts = [i.strip().capitalize() for i in parts if i.strip()]
    return " ".join(parts)
