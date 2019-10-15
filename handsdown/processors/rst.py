import re

from handsdown.processors.base import BaseDocstringProcessor


class RSTDocstringProcessor(BaseDocstringProcessor):
    """
    Docstring processor for restructured text docstring format.
    """

    line_re_map = {
        re.compile(
            r"^:(?P<section>param|parameter)\s+(?P<type>\w+)\s+(?P<param>\w+)\s*:\s*(?P<desc>.+)$"
        ): "- `{param}` *{type}* - {desc}",
        re.compile(
            r"^:(?P<section>param|parameter)\s+(?P<param>\w+)\s*:\s*(?P<desc>.+)$"
        ): "- `{param}` - {desc}",
        re.compile(
            r"^:(?P<section>param|parameter)\s+(?P<type>\w+)\s+(?P<param>\w+)\s*:$"
        ): "- `{param}` *{type}*",
        re.compile(
            r"^:(?P<section>param|parameter)\s+(?P<param>\w+)\s*:$"
        ): "- `{param}`",
        re.compile(r":(?P<section>returns?)\s*:\s*(?P<desc>.*)?$"): "{desc}",
        re.compile(r":(?P<section>returns?)\s+(?P<type>[^:]+):$"): "Type: *{type}*",
        re.compile(
            r":(?P<section>returns?)\s+(?P<type>[^:]+)\s*:\s*(?P<desc>.+)$"
        ): "Type: *{type}*\n{desc}",
        re.compile(r":(?P<section>rtype)\s*:\s+(?P<type>[^:]+)$"): "Type: *{type}*",
        re.compile(r":(?P<section>raises?)\s+(?P<type>\w+)\s*:$"): "- `{type}`",
        re.compile(
            r":(?P<section>raises?)\s+(?P<type>\w+)\s*:(?P<desc>.+)$"
        ): "- `{type}` - {desc}",
    }

    section_name_map = {
        "raise": "Raises",
        "raises": "Raises",
        "rtype": "Returns",
        "return": "Returns",
        "returns": "Returns",
        "param": "Arguments",
        "parameter": "Arguments",
    }
