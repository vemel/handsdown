"""
Handful utils that do not deserve a separate module.
"""
import traceback
from typing import Text, Any, Dict, Tuple, List, TYPE_CHECKING

from handsdown.path_finder import Path
from handsdown.settings import ASSETS_PATH


def make_title(path_part):
    # type: (Text) -> Text
    """
    Convert `pathlib.Path` part or any other string to a human-readable title.
    Replace underscores with spaces and capitalize result.

    Examples::

        make_title("my_path.py")
        "My Path Py"

        make_title("my_title")
        "My Title"

        make_title("__init__.py")
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


def extract_md_title(content):
    # type: (Text) -> Tuple[Text, Text]
    """
    Extract title from the first line of content.
    If title is present -  return a title and a remnaing content.
    if not - return an empty title and untouched content.

    Examples::

        extract_md_title('# Title\\ncontent')
        ('Title', 'content')

        extract_md_title('no title\\ncontent')
        ('', 'no title\\ncontent')

    Returns:
        A tuple fo title and remaining content.
    """
    title = ""
    if content.startswith("# "):
        if "\n" not in content:
            content = "{}\n".format(content)

        title_line, content = content.split("\n", 1)
        title = title_line.split(" ", 1)[-1]

    return title, content


def split_import_string(import_string):
    # type: (Text) -> List[Text]
    """
    Split import string by dots.

    Examples::

        split_import_string('my_module.new_class.NewClass')
        ['my_module', 'new_class', 'NewClass']

    Arguments:
        import_string -- Python import string.

    Returns:
        A list of import string parts.
    """
    return import_string.split(".")


def isinstance_str(value):
    # type: (Any) -> bool
    """
    Check if object is a string.

    `py27` compatible.

    Examples::

        isinstance_str('my string')
        True

        isinstance_str(u'my string')
        True

        isinstance_str(123)
        False

    Arguments:
        value -- Object to check.

    Returns:
        True if `value` is a string.
    """
    return isinstance(value, ("".__class__, u"".__class__))
