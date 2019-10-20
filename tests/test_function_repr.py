import unittest
from typing import Text, Union

from mock import MagicMock

from handsdown.function_repr import (
    FunctionRepr,
    ClassRepr,
    TypeHintData,
    DefaultValueData,
    ParameterData,
    FunctionData,
)


class TestTypeHintData(unittest.TestCase):
    def test_render(self):
        self.assertEqual(TypeHintData("type_hint").render(), "type_hint")

        type_hint = MagicMock()
        type_hint.__name__ = "type_hint_name"
        self.assertEqual(TypeHintData(type_hint).render(), "type_hint_name")

        type_hint = MagicMock()
        type_hint.__name__ = ""
        type_hint.__str__ = lambda self: "type_hint_str"
        self.assertEqual(TypeHintData(type_hint).render(), "type_hint_str")

    def test_get_class_names(self):
        self.assertEqual(
            TypeHintData(
                "typing.Union[typing.List, my_class.MyClass]"
            ).get_class_names(),
            [
                "Union",
                "typing.Union",
                "List",
                "typing.List",
                "MyClass",
                "my_class.MyClass",
            ],
        )


class TestDefaultValueData(unittest.TestCase):
    def test_render(self):
        self.assertEqual(DefaultValueData("default").render(), "'default'")

        default = MagicMock()
        default.__repr__ = lambda self: "<function name at 0x1234>"
        self.assertEqual(DefaultValueData(default).render(), "<function name>")

        default.__repr__ = lambda self: "u'Test'"
        self.assertEqual(DefaultValueData(default).render(), "'Test'")

    def test_get_class_names(self):
        self.assertEqual(
            DefaultValueData("my_class.MyClass(Test)").get_class_names(),
            ["MyClass", "my_class.MyClass", "Test"],
        )


class TestParameterData(unittest.TestCase):
    def test_render(self):
        data = ParameterData("name")
        self.assertEqual(data.render(), "name")
        self.assertEqual(str(data), "name")
        data.type_hint = "type_hint"
        self.assertEqual(data.render(), "name: type_hint")
        data.default = "default"
        self.assertEqual(data.render(), "name: type_hint = default")
        data.default = "default"
        data.type_hint = ParameterData.NOT_SET
        self.assertEqual(data.render(), "name=default")


class TestFunctionData(unittest.TestCase):
    def test_render(self):
        parameter_mock = MagicMock()
        parameter_mock.render.return_value = "param"

        data = FunctionData("name")
        self.assertEqual(data.render(), "def name():")
        self.assertEqual(data.render(multi_line=True), "def name():")

        data.return_type_hint = "ReturnType"
        self.assertEqual(data.render(), "def name() -> ReturnType:")

        data.parameters = [parameter_mock, parameter_mock]
        self.assertEqual(data.render(), "def name(param, param) -> ReturnType:")
        self.assertEqual(
            data.render(multi_line=True),
            "def name(\n    param,\n    param,\n) -> ReturnType:",
        )

        data.name = ""
        data.parameters = []
        self.assertEqual(data.render(), "lambda:")

        data.parameters = [parameter_mock, parameter_mock]
        self.assertEqual(data.render(), "lambda param, param:")


class TestFunctionRepr(unittest.TestCase):
    def test_init(self):
        # def my_func(_arg1, _default_arg=123, _typed: Text = "text") -> None:
        #     pass

        # function_repr = FunctionRepr(my_func)
        # self.assertEqual(
        #     function_repr.render(),
        #     "def my_func(_arg1, _default_arg=123, _typed: str = 'text') -> None",
        # )

        def my_func_typed(
            _arg1,  # type: Union[Text, int]
            _default_arg=123,  # type: int
            _typed="text",  # type: Text
        ):
            # type: () -> None
            pass

        function_repr = FunctionRepr(my_func_typed)
        self.assertEqual(
            function_repr.render(),
            "def my_func_typed(\n"
            "    _arg1: Union[Text, int],\n"
            "    _default_arg: int = 123,\n"
            "    _typed: Text = 'text',\n"
            ") -> None:",
        )

        type_hints = function_repr.get_type_hints()
        self.assertEqual(
            set(type_hints.keys()), {"_arg1", "_default_arg", "_typed", "return"}
        )

        defaults = function_repr.get_defaults()
        self.assertEqual(set(defaults.keys()), {"_default_arg", "_typed"})

        def my_func_typed2(_arg1, _default_arg=123, _typed="text"):
            # type: (Union[Text, int], int, Text) -> None
            pass

        function_repr = FunctionRepr(my_func_typed2)
        self.assertEqual(
            function_repr.render(),
            "def my_func_typed2(\n"
            "    _arg1: Union[Text, int],\n"
            "    _default_arg: int = 123,\n"
            "    _typed: Text = 'text',\n"
            ") -> None:",
        )


class TestClassRepr(unittest.TestCase):
    def test_init(self):
        class MyClass:
            def __init__(
                self, _loooooooooooooooooooooong_arg, _default_arg=123, _typed="text"
            ):
                # type: (Union[Text, int], int, Text) -> None
                pass

        class_repr = ClassRepr(MyClass)
        self.assertEqual(
            class_repr.render(),
            "class MyClass(\n"
            "    _loooooooooooooooooooooong_arg: Union[Text, int],\n"
            "    _default_arg: int = 123,\n"
            "    _typed: Text = 'text',\n"
            ") -> None:",
        )
