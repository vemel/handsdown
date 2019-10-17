from __future__ import annotations

import re
import enum
import inspect
from typing import get_type_hints, Text, Type, Optional, Any, Dict
from types import MappingProxyType


class Config:
    BREAK_LINES = False
    MAX_LINE_LENGTH = 100


class DefaultValue:
    """
    Represent function parameter default value in signature

    Arguments:
        original -- Original default value.
    """

    _hex_code_re = re.compile(r" at 0x[a-f0-9]+")

    def __init__(self, original: Type) -> None:
        self._original = original

    def __str__(self) -> Text:
        if isinstance(self._original, enum.Enum):
            return f"{self._original.value}"
            # return f'{self._original.__class__.__name__}.{self._original.value}'

        result = repr(self._original)
        if " at 0x" in result:
            result = self._hex_code_re.sub("", result)
        return result


class Parameter(inspect.Parameter):
    """
    Represent function parameters in signature
    """

    _empty = getattr(inspect, "_empty")
    _VAR_POSITIONAL = getattr(inspect, "_VAR_POSITIONAL")
    _VAR_KEYWORD = getattr(inspect, "_VAR_KEYWORD")

    def __init__(self, type_hint: Optional[Type], *args: Any, **kwargs: Any) -> None:
        super(Parameter, self).__init__(*args, **kwargs)
        self._default: Type = self._default
        self._name: Text = self._name
        if type_hint:
            self._annotation = type_hint
        self._proxy_default = DefaultValue(self._default)

    def __str__(self) -> Text:
        kind = self.kind
        formatted = self._name

        # Add annotation and default value
        if self._annotation is not self._empty:
            annotation = inspect.formatannotation(self._annotation)
            formatted = f"{formatted}: {annotation}"

        if self._default is not self._empty:
            if self._annotation is not self._empty:
                formatted = f"{formatted} = {self._proxy_default}"
            else:
                formatted = f"{formatted}={self._proxy_default}"

        if kind == self._VAR_POSITIONAL:
            formatted = "*" + formatted
        elif kind == self._VAR_KEYWORD:
            formatted = "**" + formatted

        if Config.BREAK_LINES:
            return f"\n    {formatted}"
        return formatted

    @classmethod
    def create(
        cls, parameter: inspect.Parameter, type_hint: Optional[Type]
    ) -> Parameter:
        """
        Create `ProxyParameter` for original `inspect.Parameter`

        Arguments:
            parameter -- original `inspect.Parameter`
            type_hint -- resoled type hint that should replace a lazy annotation
        """
        obj = cls(
            name=parameter.name,
            kind=parameter.kind,
            default=parameter.default,
            annotation=parameter.annotation,
            type_hint=type_hint,
        )
        return obj


class SignatureBuilder:
    """
    Renderer for object signature. Support lazy type annotations and tries
    to beautify result by splitting lines.

    Arguments:
        obj -- Object to inspect.
    """

    def __init__(self, obj: Any):
        self._obj = obj
        self._is_class = inspect.isclass(self._obj)

    @staticmethod
    def _get_type_hints(func: Any) -> Dict[Text, Any]:
        try:
            type_hints = get_type_hints(func)
        except NameError:
            return {}
        for key, value in type_hints.items():
            if value is type(None):
                type_hints[key] = None

        return type_hints

    @staticmethod
    def _enrich_signature(signature: Any, type_hints: Dict[Text, Any]) -> None:
        clean_parameters = {}
        for key, value in signature.parameters.items():
            if key == "self":
                continue
            clean_parameters[key] = Parameter.create(value, type_hints.get(key))

        signature._parameters = MappingProxyType(  # pylint: disable=protected-access
            clean_parameters
        )

        if isinstance(signature.return_annotation, str) and "return" in type_hints:
            signature._return_annotation = type_hints[  # pylint: disable=protected-access
                "return"
            ]

    def _get_obj_name(self) -> Text:
        if hasattr(self._obj, "__name__"):
            return self._obj.__name__

        return f"{type(self._obj).__name__}.__call__"

    def _get_defintion(self) -> Text:
        if self._is_class:
            return "class"

        return "def"

    def build(self) -> Text:
        """
        Render signature to string.

        Returns:
            A string with functions signature.
        """
        module_object = self._obj

        if not hasattr(module_object, "__name__"):
            module_object = module_object.__call__

        if self._is_class:
            module_object = module_object.__init__

        signature = inspect.signature(module_object, follow_wrapped=True)
        type_hints = self._get_type_hints(module_object)
        self._enrich_signature(signature, type_hints)
        return self._render_signature(signature)

    def _render_signature(self, signature: inspect.Signature) -> Text:
        name = self._get_obj_name()
        definition = self._get_defintion()

        Config.BREAK_LINES = False
        signature_repr = f"{signature}"
        result = f"{definition} {name}{signature_repr}"
        if len(result) > Config.MAX_LINE_LENGTH:
            Config.BREAK_LINES = True
            signature_repr = f"{signature}"
            end_index = signature_repr.rfind(")")
            signature_repr = (
                f"{signature_repr[:end_index]}, \n{signature_repr[end_index:]}"
            )
            signature_repr = "\n".join([i.rstrip() for i in signature_repr.split("\n")])

        if self._is_class:
            signature_repr = signature_repr.replace(" -> None", "")
        result = f"{definition} {name}{signature_repr}"
        return result
