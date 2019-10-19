# -*- coding: future_fstrings -*-
import inspect
import re


__all__ = ["FunctionRepr", "ClassRepr"]


class TypeHintData:
    _split_re = re.compile(r"[\]\[ ,]")

    def __init__(self, type_hint):
        self.type_hint = type_hint

    def render(self):
        if isinstance(self.type_hint, str):
            return self.type_hint

        if hasattr(self.type_hint, "__name__"):
            return self.type_hint.__name__

        return str(self.type_hint)

    def __str__(self):
        return self.render()

    def __repr__(self):
        return self.render()

    def get_class_names(self):
        s = self.render()
        class_names = self._split_re.split(s)
        class_names = [i for i in class_names if i]
        return class_names


class NotSetValue:
    pass


class ParameterData:
    def __init__(self, name):
        self.name = name
        self.default = NotSetValue
        self.type_hint = NotSetValue

    def render(self):
        if self.type_hint is not NotSetValue:
            if self.default is not NotSetValue:
                return f"{self.name}: {self.type_hint} = {self.default}"

            return f"{self.name}: {self.type_hint}"

        if self.default is not NotSetValue:
            return f"{self.name}={self.default}"

        return f"{self.name}"

    def __str__(self):
        return self.render()


class FunctionData:
    def __init__(self, name):
        self.name = name
        self.definition = "def"
        self.parameters = []
        self.return_type_hint = None

    def render(self, multi_line=False):
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
        self.name = func.__name__
        self.func = func
        self._function_data = None

    def _get_parameters_data(self):
        parameters_data = []
        names = []
        defaults = tuple()
        args_count = 0

        if hasattr(inspect, "getfullargspec"):
            try:
                arg_spec = inspect.getfullargspec(self.func)
            except TypeError:
                pass
            else:
                names = arg_spec.args + [arg_spec.varargs, arg_spec.varkw]
                args_count = len(arg_spec.args)
                defaults = arg_spec.defaults or tuple()
        else:
            try:
                arg_spec = getattr(inspect, "getargspec")(self.func)
            except TypeError:
                pass
            else:
                names = arg_spec.args + [arg_spec.varargs, arg_spec.keywords]
                args_count = len(arg_spec.args)
                defaults = arg_spec.defaults or tuple()

        names = [i for i in names if i]

        for name in names:
            parameters_data.append(ParameterData(name))

        for index, value in enumerate(defaults):
            parameter_index = args_count - len(defaults) + index
            if parameter_index < len(parameters_data):
                parameters_data[parameter_index].default = value

        if parameters_data:
            if parameters_data[0].name in ("self", "cls"):
                parameters_data.pop(0)

        return parameters_data

    def _add_defaults(self):
        defaults = ()
        if getattr(self.func, "__defaults__", None):
            defaults = self.func.__defaults__ + defaults
        if getattr(self.func, "__kwdefaults__", None):
            defaults = self.func.__kwdefaults__ + defaults

        parameters = self._function_data.parameters
        for index, value in enumerate(defaults):
            parameter_index = len(parameters) - len(defaults) + index
            parameters[parameter_index].default = value

    def _get_type_hints(self):
        type_hints = {}
        if getattr(self.func, "__annotations__", None):
            type_hints.update(self.func.__annotations__)

        srclines = []
        try:
            srclines = inspect.getsourcelines(self.func)[0]
        except (TypeError, OSError):
            pass

        parameter_index = 0
        for line in srclines:
            match = self._return_type_re.match(line)
            if match:
                arg_types, return_type = match.groups()
                type_hints["return"] = TypeHintData(return_type)
                arg_types = [i.strip() for i in arg_types.split(",") if i != "..."]
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

    def get_type_hints(self):
        result = {}
        for parameter in self._function_data.parameters:
            if parameter.type_hint is not NotSetValue:
                result[parameter.name] = parameter.type_hint
        return result

    def _add_type_hints(self):
        type_hints = self._get_type_hints()

        parameters = self._function_data.parameters
        for parameter in parameters:
            if parameter.name in type_hints:
                type_hint = type_hints[parameter.name]
                parameter.type_hint = TypeHintData(type_hint)

        if "return" in type_hints:
            type_hint = type_hints["return"]
            self._function_data.return_type_hint = TypeHintData(type_hint)

    def _get_function_data(self):
        function_data = FunctionData(self.name)

        function_data.parameters = self._get_parameters_data()
        return function_data

    def render(self):
        self._function_data = self._get_function_data()
        self._function_data.definition = self._definition
        self._add_defaults()
        self._add_type_hints()

        result = self._function_data.render(multi_line=False)
        if len(result) > self._line_lenght:
            result = self._function_data.render(multi_line=True)
        return result

    def __str__(self):
        return self.render()


class ClassRepr(FunctionRepr):
    _definition = "class"

    def __init__(self, inspect_class):
        if hasattr(inspect_class, "__init__"):
            super(ClassRepr, self).__init__(inspect_class.__init__)
        else:
            super(ClassRepr, self).__init__(inspect_class)
        self.name = inspect_class.__name__
