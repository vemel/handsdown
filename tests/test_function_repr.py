import unittest
from typing import Text, Union

from handsdown.function_repr import FunctionRepr, ClassRepr


class TestFunctionRepr(unittest.TestCase):
    def test_init(self):
        def my_func(_arg1, _default_arg=123, _typed: Text = "text") -> None:
            pass

        def my_func_typed(
            _arg1,  # type: Union[Text, int]
            _default_arg=123,  # type: int
            _typed="text",  # type: Text
        ) -> None:
            # type: () -> None
            pass

        def my_func_typed2(_arg1, _default_arg=123, _typed="text") -> None:
            # type: (Union[Text, int], int, Text) -> None
            pass

        function_repr = FunctionRepr(my_func)
        self.assertEqual(
            function_repr.render(),
            "def my_func(_arg1, _default_arg=123, _typed: str = 'text') -> None",
        )

        type_hints = function_repr.get_type_hints()
        self.assertEqual(set(type_hints.keys()), {"_typed", "return"})

        defaults = function_repr.get_defaults()
        self.assertEqual(set(defaults.keys()), {"_default_arg", "_typed"})

        function_repr = FunctionRepr(my_func_typed)
        self.assertEqual(
            function_repr.render(),
            "def my_func_typed(\n"
            "    _arg1: Union[Text, int],\n"
            "    _default_arg: int = 123,\n"
            "    _typed: Text = 'text',\n"
            ") -> None",
        )
        function_repr = FunctionRepr(my_func_typed2)
        self.assertEqual(
            function_repr.render(),
            "def my_func_typed2(\n"
            "    _arg1: Union[Text, int],\n"
            "    _default_arg: int = 123,\n"
            "    _typed: Text = 'text',\n"
            ") -> None",
        )


class TestClassRepr(unittest.TestCase):
    def test_init(self):
        class MyClass:
            def __init__(
                self,
                _loooooooooooooooooooooong_arg,
                _default_arg=123,
                _typed: Text = "text",
            ) -> None:
                pass

        class_repr = ClassRepr(MyClass)
        self.assertEqual(
            class_repr.render(),
            "class MyClass(\n"
            "    _loooooooooooooooooooooong_arg,\n"
            "    _default_arg=123,\n"
            "    _typed: str = 'text',\n"
            ") -> None",
        )
