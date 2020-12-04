# pylint: disable=missing-docstring
"""
# PEP 484 - type annotations examples

## Links

[PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/)
"""
from typing import List, Union, Any, Dict, Tuple, Type


class MyValue:
    pass


class Typed:
    def __init__(
        self,
        _value: Union[List[str], str, MyValue] = MyValue(
            {
                "key1": "value1",
                "key2": "value2",
                "key3": "value3",
                "key4": "value4",
                "key5": "value5",
                "key6": "value6",
            }
        ),
        *,
        _name: str = "default",
    ) -> Dict[str, MyValue]:
        pass

    @classmethod
    def classmethod(cls, _my_value: MyValue, *_args: str, **_kwargs: Any) -> None:
        pass

    async def async_method(self, _value: str) -> str:
        return await self.classmethod(_value)


def my_deco(key):
    return key


@my_deco(key="value")
def func(
    _list: Tuple[List[str], ...],
    _my_value_cls: Type[MyValue] = MyValue,
    **_kwargs: None,
) -> Any:
    pass
