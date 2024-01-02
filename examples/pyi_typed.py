"""
# Stub file type annotations examples

## Links

[Stub files](https://mypy.readthedocs.io/en/latest/stubs.html)
"""


from dataclasses import dataclass


class MyValue:
    pass


def func(_list, _my_value_cls=MyValue, **_kwargs):
    pass


def func_an(_list, _my_value_cls=MyValue, **_kwargs):
    pass


class Aasdas:
    """
    Test class.
    """

    b: int
    # This comment should also appear in the docs
    c: str
    d = 5
