"""
Mock for `os.environ` that returns `env` string instead of undefined variables.
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
