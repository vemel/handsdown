"""
Handful utils that do not deserve a separate module.
"""
import traceback
from typing import Text, Any, Dict, TYPE_CHECKING

from handsdown.path_finder import Path
from handsdown.settings import ASSETS_PATH


def make_title(path_part):
    # type: (Text) -> Text
    """
    Convert `pathlib.Path` part or any other string to a human-readable title.
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
    content = (Path(ASSETS_PATH) / name).read_text()
    content = content.format(**format_dict)
    target_path.write_text(content)
