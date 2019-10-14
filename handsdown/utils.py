import re

from collections import UserDict
from typing import Text


anchor_re = re.compile(r"[^a-z0-9_-]+")


class OSEnvironMock(UserDict):
    """
    Mock for `os.environ` that returns `env` string isntead of undefined variables.
    """

    def __missing__(self, key: Text) -> Text:
        return "env"
