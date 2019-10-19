from typing import Text, List, Union, Any, Dict, Tuple, Type


class MyValue:
    pass


class Typed:
    def __init__(
        self,
        _value=MyValue(),  # type: Union[List[Text], Text, MyValue]
        _name="default",  # type: Text
    ):
        # type: (...) -> Dict[Text, MyValue]
        pass

    @classmethod
    def classmethod(cls, _my_value, *_args, **_kwargs) -> None:
        # type: (MyValue, Text, Any) -> Dict[Text, MyValue]
        pass


def func(_list, _my_value_cls=MyValue, **_kwargs):
    # type: (Tuple[List[Text], ...], Type[MyValue], None) -> Any
    pass


def func_any(_list, _my_value_cls=MyValue, **_kwargs):
    # type: (Tuple[List[Text], ...], Any, None) -> Any
    pass
