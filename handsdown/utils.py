"""
Handful utils that do not deserve a separate module.
"""
from collections import UserDict
from typing import Text


class OSEnvironMock(UserDict):
    """
    Mock for `os.environ` that returns `env` string isntead of undefined variables.
    """

    def __missing__(self, key: Text) -> Text:
        return "env"


def get_title_from_path_part(path_part: Text) -> Text:
    """
    Convert `pathlib.Path` part to a human-readable title.
    Replace underscores with spaces and capitalize result.

    Arguments:
        path_part -- Part of filename path.

    Returns:
        A human-readable title as a string.
    """
    parts = path_part.replace(".", "_").split("_")
    parts = [i.strip().capitalize() for i in parts if i.strip()]
    return " ".join(parts)
