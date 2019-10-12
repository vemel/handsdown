import inspect
import enum
import re
import importlib
from unittest.mock import patch
from collections import defaultdict
from typing import get_type_hints, Type, Optional, Text, Any, Dict
from types import MappingProxyType


class Config:
    BREAK_LINES = False
    MAX_LINE_LENGTH = 100


class ProxyDefaultValue:
    "Helper class to represent function parameter default value in signature"
    _hex_code_re = re.compile(r" at 0x[a-f0-9]+")

    def __init__(self, original: Type) -> None:
        self._original = original

    def __repr__(self) -> Text:
        if isinstance(self._original, enum.Enum):
            return f"{self._original.value}"
            # return f'{self._original.__class__.__name__}.{self._original.value}'

        result = repr(self._original)
        if " at 0x" in result:
            result = self._hex_code_re.sub("", result)
        return result


class ProxyParameter(inspect.Parameter):
    "Helper class to represent function parameters in signature"

    def __init__(self, type_hint: Optional[Type], *args: Any, **kwargs: Any) -> None:
        super(ProxyParameter, self).__init__(*args, **kwargs)
        if isinstance(self._annotation, str) and type_hint:
            self._annotation = type_hint
        if self._default is not inspect._empty:  # pylint: disable=protected-access
            self._default = ProxyDefaultValue(self._default)

    def __str__(self) -> Text:
        parent_value = super(ProxyParameter, self).__str__()
        if not Config.BREAK_LINES:
            return parent_value
        return f"\n    {parent_value}"

    @classmethod
    def create(
        cls, parameter: inspect.Parameter, type_hint: Optional[Type]
    ) -> ProxyParameter:
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


class Loader:
    """
    Expects absolute identifiers to import with #import_object_with_scope().
    """

    def get_object_signature(self, obj: Any) -> Optional[Text]:
        """
        Get class, method or function signature. If object is not callable -
        returns None.

        Arguments:
            obj -- Object to inspect.

        Returns:
            A string with object signature or None.
        """
        if not callable(obj):
            return None

        return self._get_signature(obj)

    def get_object_docstring(self, obj: Any) -> Text:
        """
        Get trimmed object docstring or an empty string.

        Arguments:
            obj -- Object to inspect.

        Returns:
            A string with object docsting.
        """
        return self._trim(self._get_docstring(obj))

    @staticmethod
    def safe_import_module(import_string: Text) -> Any:
        with patch("os.environ", defaultdict(lambda: "env")):
            module = importlib.import_module(import_string)

        return module

    @staticmethod
    def _get_docstring(obj: Any) -> Text:
        if isinstance(obj, (staticmethod, classmethod)):
            return obj.__func__.__doc__ or ""
        if hasattr(obj, "__name__") or isinstance(obj, property):
            return obj.__doc__ or ""
        if hasattr(obj, "__call__"):
            return obj.__call__.__doc__ or ""

        return obj.__doc__ or ""

    @staticmethod
    def _trim(docstring: Text) -> Text:
        if not docstring:
            return ""

        lines = [line for line in docstring.split("\n")]
        indent = 0

        for line in lines[1:]:
            if not line.strip():
                continue

            indent = len(line) - len(line.lstrip())
            break

        result = []
        for line in docstring.split("\n"):
            if not line[:indent].strip():
                line = line[indent:]
            result.append(line)

        return "\n".join(result)

    def _get_type_hints(self, func: Any) -> Dict[Text, Any]:
        type_hints = get_type_hints(func)
        for key, value in type_hints.items():
            if value is type(None):
                type_hints[key] = None

        return type_hints

    def _enrich_signature(self, signature: Any, type_hints: Dict[Text, Any]) -> None:
        clean_parameters = {}
        for key, value in signature.parameters.items():
            if key == "self":
                continue
            clean_parameters[key] = ProxyParameter.create(value, type_hints.get(key))

        signature._parameters = MappingProxyType(  # pylint: disable=protected-access
            clean_parameters
        )

        if isinstance(signature.return_annotation, str) and "return" in type_hints:
            signature._return_annotation = type_hints[  # pylint: disable=protected-access
                "return"
            ]

    def _get_signature(self, module_object: Any) -> Optional[Text]:
        isclass = inspect.isclass(module_object)

        name_parts = []
        if hasattr(module_object, "__name__"):
            name_parts.append(module_object.__name__)
        else:
            name_parts.append(type(module_object).__name__)
            name_parts.append("__call__")
            module_object = module_object.__call__

        name = ".".join(name_parts)

        if isclass:
            module_object = module_object.__init__

        try:
            signature = inspect.signature(module_object, follow_wrapped=True)
        except ValueError:
            return None
        definition = "def"
        if isclass:
            definition = "class"

        type_hints = self._get_type_hints(module_object)
        self._enrich_signature(signature, type_hints)

        Config.BREAK_LINES = False
        result = f"{definition} {name}{signature}"
        if len(result) < Config.MAX_LINE_LENGTH:
            return result

        Config.BREAK_LINES = True
        signature_repr = f"{signature}"
        end_index = signature_repr.rfind(")")
        signature_repr = f"{signature_repr[:end_index]}, \n{signature_repr[end_index:]}"
        signature_repr = "\n".join([i.rstrip() for i in signature_repr.split("\n")])
        if isclass:
            signature_repr = signature_repr.replace(" -> None", "")
        result = f"{definition} {name}{signature_repr}"
        return result
