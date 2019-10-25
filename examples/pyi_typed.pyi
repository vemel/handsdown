# pylint: disable=all
from typing import Text, List, Union, Any, Dict, Tuple, Type, Set

class MyValue: ...

def func(
    _list: Tuple[List[Text], ...], _my_value_cls: Type[MyValue], **_kwargs: None
) -> Any: ...
def func_any(
    _list: Tuple[List[Text], ...], _my_value_cls: Any, **_kwargs: None
) -> Any: ...
