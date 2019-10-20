"""
Handful utils that do not deserve a separate module.
"""
import traceback
from typing import Text, Any, Dict, TYPE_CHECKING

from handsdown.settings import ASSETS_PATH


if TYPE_CHECKING:
    from path_finder import Path


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
    Helper to turn on or off `TYPE_CHECKING` to avoid sircular imports.

    Returns `True` for usage from the `target_file_path`.

    Examples::

        import_string = fet_import_string_from_path(file_path)
        with patch("typing.TYPE_CHECKING", TypeCheckingMock(file_path)):
            module = importlib.import_module(import_string)

    Arguments:
        target_file_path -- Source path where `typing.TYPE_CHECKING` should be `True`
    """

    def __init__(self, target_file_path):
        # type: (Path) -> None
        self.target_file_path_str = target_file_path.as_posix()

    def __bool__(self):
        # type: () -> bool
        """
        Check if TYPE_CHECKING should be enabled.

        Returns:
            Returns `True` for usage from the `target_file_path`.
        """
        call_stack = traceback.extract_stack(limit=2)
        caller_file_path_str = call_stack[0].filename
        if caller_file_path_str == self.target_file_path_str:
            return True

        return False

    __nonzero__ = __bool__


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


def render_asset(name, target_path, format_dict):
    # type: (Text, Path, Dict[Text, Text]) -> None
    """
    Render `assets/<name>` file to `target_path`.

    Arguments:
        name -- Asset file name.
        target_path -- Path of output file.
        format_dict -- Format asset with values from the dict before writing.
    """
    content = (ASSETS_PATH / name).read_text()
    content = content.format(**format_dict)
    target_path.write_text(content)
