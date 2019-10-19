# -*- coding: future_fstrings -*-
import inspect
import re
from typing import Text, List, Any, Dict, Optional, Union

from handsdown.sentinel import Sentinel


__all__ = ["FunctionRepr", "ClassRepr"]


class TypeHintData:
    _split_re = re.compile(r"[\]\[ ,]")

    def __init__(self, type_hint):
        # type: (Any) -> None
        self.type_hint = type_hint

    def render(self):
        # type: () -> Text
        if isinstance(self.type_hint, str):
            return self.type_hint

        if hasattr(self.type_hint, "__name__"):
            return self.type_hint.__name__

        result = str(self.type_hint)
        result = result.replace("typing.", "")
        return result

    def __str__(self):
        # type: () -> Text
        return self.render()

    def get_class_names(self):
        # type: () -> List[Text]
        s = self.render()
        result = []
        for class_name in self._split_re.split(s):
            class_name = class_name.strip()
            if class_name == "..." or not class_name:
                continue
            parts = class_name.split(".")
            parts.reverse()
            import_parts = []  # type: List[Text]
            for part in parts:
                import_parts = [part] + import_parts
                import_string = ".".join(import_parts)
                result.append(import_string)

        return result


class DefaultValueData:
    _split_re = re.compile(r"[\(\) ,'\"<>]")

    def __init__(self, value):
        # type: (Any) -> None
        self.value = value

    def render(self):
        # type: () -> Text
        s = repr(self.value)

        if s.startswith("<") and " at 0x" in s:
            s = s.split(" at ", 1)[0] + ">"

        # fix unicode strings
        if s.startswith("u'"):
            s = s[1:]

        return s

    def __str__(self):
        # type: () -> Text
        return self.render()

    def get_class_names(self):
        # type: () -> List[Text]
        s = self.render()
        class_names = self._split_re.split(s)
        result = []
        for class_name in class_names:
            if not class_name:
                continue

            parts = class_name.split(".")
            parts.reverse()
            import_parts = []  # type: List[Text]
            for part in parts:
                import_parts = [part] + import_parts
                import_string = ".".join(import_parts)
                result.append(import_string)
        return result


class ParameterData:
    NOT_SET = Sentinel()

    def __init__(self, name):
        # type: (Text) -> None
        self.name = name
        self.default = self.NOT_SET  # type: Union[Sentinel, DefaultValueData]
        self.type_hint = self.NOT_SET  # type: Union[Sentinel, TypeHintData]

    def render(self):
        # type: () -> Text
        if self.type_hint is not self.NOT_SET:
            if self.default is not self.NOT_SET:
                return f"{self.name}: {self.type_hint} = {self.default}"

            return f"{self.name}: {self.type_hint}"

        if self.default is not self.NOT_SET:
            return f"{self.name}={self.default}"

        return f"{self.name}"

    def __str__(self):
        # type: () -> Text
        return self.render()


class FunctionData:
    def __init__(self, name):
        # type: (Text) -> None
        self.name = name
        self.definition = "def"
        self.parameters = []  # type: List[ParameterData]
        self.return_type_hint = None  # type: Optional[TypeHintData]

    def render(self, multi_line=False):
        # type: (bool) -> Text
        rendered_parameters = []
        for parameter in self.parameters:
            rendered_parameters.append(parameter.render())

        result = f"{self.definition} {self.name}("
        if multi_line:
            parameters = ",\n    ".join(rendered_parameters)
            result = f"{result}\n    {parameters},\n)"
        else:
            parameters = ", ".join(rendered_parameters)
            result = f"{result}{parameters})"

        if self.return_type_hint:
            result = f"{result} -> {self.return_type_hint}"

        return result


class FunctionRepr(object):
    _single_type_re = re.compile(r".+#\s*type:\s*(.+)")
    _return_type_re = re.compile(r".*#\s*type:\s+\((.*)\)\s*->\s*(.+)")
    _line_lenght = 79
    _definition = "def"

    def __init__(self, func):
        # type: (Any) -> None
        self.name = func.__name__
        self.func = func
        self._function_data = FunctionData(self.name)

        self._arg_spec = None
        try:
            getargspec = getattr(inspect, "getfullargspec", inspect.getargspec)
            self._arg_spec = getargspec(self.func)
        except TypeError:
            pass

    def _get_argument_names(self):
        # type: () -> List[Text]
        if not self._arg_spec:
            return []

        names = self._arg_spec.args
        if self._arg_spec.varargs:
            names.append(self._arg_spec.varargs)
        if getattr(self._arg_spec, "keywords", None):
            names.append(getattr(self._arg_spec, "keywords"))
        if getattr(self._arg_spec, "varkw", None):
            names.append(getattr(self._arg_spec, "varkw"))

        return names

    def _get_defaults(self):
        # type: () -> List[Any]
        if not self._arg_spec:
            return []

        if not self._arg_spec.defaults:
            return []

        return list(self._arg_spec.defaults)

    def _get_parameters_data(self):
        # type: () -> List[ParameterData]
        parameters_data = []  # type: List[ParameterData]
        names = self._get_argument_names()
        defaults = self._get_defaults()  # type: List[Any]
        args_count = 0

        # skip inherited from object
        if names == ["self", "args", "kwargs"]:
            names = []

        for name in names:
            parameters_data.append(ParameterData(name))

        for index, value in enumerate(defaults):
            parameter_index = args_count - len(defaults) + index
            if parameter_index < len(parameters_data):
                parameters_data[parameter_index].default = DefaultValueData(value)

        if parameters_data:
            if parameters_data[0].name in ("self", "cls"):
                parameters_data.pop(0)

        return parameters_data

    def _get_type_hints(self):
        # type: () -> Dict[Text, Any]
        type_hints = {}  # type: Dict[Text, Any]
        if getattr(self.func, "__annotations__", None):
            type_hints.update(self.func.__annotations__)

        srclines = []  # type: List[Text]
        try:
            srclines = inspect.getsourcelines(self.func)[0]
        except (TypeError, OSError):
            pass

        parameter_index = 0
        for line in srclines:
            match = self._return_type_re.match(line)
            if match:
                arg_type, return_type = match.groups()
                type_hints["return"] = return_type
                arg_types = self._strip_arg_type(arg_type)
                for arg_type in arg_types:
                    if len(self._function_data.parameters) <= parameter_index:
                        continue
                    parameter = self._function_data.parameters[parameter_index]
                    type_hints[parameter.name] = arg_type.strip()
                    parameter_index += 1
                continue
            match = self._single_type_re.match(line)
            if match:
                arg_type = match.group(1)
                if len(self._function_data.parameters) <= parameter_index:
                    continue
                parameter = self._function_data.parameters[parameter_index]
                type_hints[parameter.name] = arg_type.strip()
                parameter_index += 1

        return type_hints

    @staticmethod
    def _strip_arg_type(arg_type):
        # type: (Text) -> List[Text]
        bracket_count = 0
        result = [""]
        for c in arg_type:
            if c == "," and bracket_count == 0:
                result.append("")
                continue
            if c == "[":
                bracket_count += 1
            if c == "]":
                bracket_count -= 1

            result[-1] = f"{result[-1]}{c}"

        return [i.strip() for i in result]

    def get_type_hints(self):
        # type: () -> Dict[Text, TypeHintData]
        result = {}
        for parameter in self._function_data.parameters:
            if isinstance(parameter.type_hint, TypeHintData):
                result[parameter.name] = parameter.type_hint
        return result

    def get_defaults(self):
        # type: () -> Dict[Text, DefaultValueData]
        result = {}
        for parameter in self._function_data.parameters:
            if isinstance(parameter.default, DefaultValueData):
                result[parameter.name] = parameter.default
        return result

    def _add_type_hints(self):
        # type: () -> None
        type_hints = self._get_type_hints()

        parameters = self._function_data.parameters
        for parameter in parameters:
            if parameter.name in type_hints:
                type_hint = type_hints[parameter.name]
                parameter.type_hint = TypeHintData(type_hint)

        if "return" in type_hints:
            type_hint = type_hints["return"]
            self._function_data.return_type_hint = TypeHintData(type_hint)

    def render(self):
        # type: () -> Text
        self._function_data.parameters = self._get_parameters_data()
        self._function_data.definition = self._definition
        self._add_type_hints()

        result = self._function_data.render(multi_line=False)
        if len(result) > self._line_lenght:
            result = self._function_data.render(multi_line=True)
        return result

    def __str__(self):
        # type: () -> Text
        return self.render()


class ClassRepr(FunctionRepr):
    _definition = "class"

    def __init__(self, inspect_class):
        # type: (Any) -> None
        if hasattr(inspect_class, "__init__"):
            super(ClassRepr, self).__init__(inspect_class.__init__)
        else:
            super(ClassRepr, self).__init__(inspect_class)
        self.name = inspect_class.__name__
        self._function_data.name = self.name
