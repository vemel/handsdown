# pylint: disable=missing-docstring,no-self-use,dangerous-default-value
"""
# PEP 484 - comment-based type annotations examples

## Links

[PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/)
"""
from typing import Text, List, Union, Any, Dict, Tuple, Type, Set


class MyValue:
    pass


class Typed:
    one = 1

    # comment here
    two = 2
    args = []  # type: List[Text]
    extras = {}  # type: Dict[Text, Text]

    def __init__(
        self,
        my_bool=(one & ~two == "three") and not -4,  # type: bool
        my_lambda=lambda x, y=15, *args, **kwargs: x + y,
        my_set={1, 2, [3, 4], {5: 6}, (7, 8)},  # type: Set
        _value=MyValue(
            "asd", kwarg=123, *args, **extras
        ),  # type: Union[List[Text], Text, MyValue]
        _name="default",  # type: Text
    ):
        # type: (...) -> Dict[Text, MyValue]
        pass

    @classmethod
    def classmethod(cls, _my_value, *_args, **_kwargs):
        # type: (MyValue, Text, Any) -> Typed
        pass


def func(_list, _my_value_cls=MyValue, **_kwargs):
    # type: (Tuple[List[Text], ...], Type[MyValue], None) -> Any
    pass


def func_any(_list, _my_value_cls=MyValue, **_kwargs):
    # type: (Tuple[List[Text], ...], Any, None) -> Any
    pass
