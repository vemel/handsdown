from typing import Text, List, Union, Any, Dict, Tuple, Type


class MyValue:
    pass


class Typed:
    def __init__(
        self,
        _value: Union[List[Text], Text, MyValue] = MyValue(
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
        _name: Text = "default",
    ) -> Dict[Text, MyValue]:
        pass

    @classmethod
    def classmethod(cls, _my_value: MyValue, *_args: Text, **_kwargs: Any) -> None:
        pass


def func(
    _list: Tuple[List[Text], ...],
    _my_value_cls: Type[MyValue] = MyValue,
    **_kwargs: None,
) -> Any:
    pass
