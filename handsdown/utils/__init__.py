"""
Handful utils that do not deserve a separate module.
"""
from pathlib import Path
from typing import Dict, List, Tuple

from handsdown.settings import ASSETS_PATH


def make_title(file_stem: str) -> str:
    """
    Convert `pathlib.Path` part or any other string to a human-readable title.
    Replace underscores with spaces and capitalize result.

    Examples::

        make_title(Path("my_module/my_path.py").stem)
        "My Path"

        make_title("my_title")
        "My Title"

        make_title("__init__.py")
        "Init Py"

        make_title(Path("my_module/__main__.py").stem)
        "Module"

    Arguments:
        file_stem -- Stem from path.

    Returns:
        A human-readable title as a string.
    """
    if file_stem == "__main__":
        return "Module"

    parts = file_stem.replace(".", "_").split("_")
    name_parts: List[str] = []
    for part in parts:
        if not part:
            continue
        name_part = part.strip().capitalize()
        name_parts.append(name_part)

    return " ".join(name_parts)


def render_asset(name: str, target_path: Path, format_dict: Dict[str, str]) -> None:
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


def extract_md_title(content: str) -> Tuple[str, str]:
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
