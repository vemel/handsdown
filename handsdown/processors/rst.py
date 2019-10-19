"""
Docstring processor for restructured text docstring format.
"""

import re

from handsdown.processors.base import BaseDocstringProcessor


class RSTDocstringProcessor(BaseDocstringProcessor):
    """
    Docstring processor for restructured text docstring format.
    """

    line_re_map = (
        # PEP 287 arg typed with description
        (
            re.compile(
                r"^:(?P<section>param|parameter)\s+(?P<type>\w+)\s+(?P<param>\w+)\s*:\s*(?P<desc>.+)$"
            ),
            "- `{param}` *{type}* - {desc}",
        ),
        # PEP 287 arg with description
        (
            re.compile(
                r"^:(?P<section>param|parameter)\s+(?P<param>\w+)\s*:\s*(?P<desc>.+)$"
            ),
            "- `{param}` - {desc}",
        ),
        # PEP 287 arg typed
        (
            re.compile(
                r"^:(?P<section>param|parameter)\s+(?P<type>\w+)\s+(?P<param>\w+)\s*:$"
            ),
            "- `{param}` *{type}*",
        ),
        # PEP 287 arg
        (
            re.compile(r"^:(?P<section>param|parameter)\s+(?P<param>\w+)\s*:$"),
            "- `{param}`",
        ),
        # PEP 287 return
        (re.compile(r":(?P<section>returns?)\s*:\s*(?P<desc>.*)?$"), "{desc}"),
        # PEP 287 return typed
        (re.compile(r":(?P<section>returns?)\s+(?P<type>[^:]+):$"), "Type: *{type}*"),
        # PEP 287 return typed with description
        (
            re.compile(r":(?P<section>returns?)\s+(?P<type>[^:]+)\s*:\s*(?P<desc>.+)$"),
            "Type: *{type}*\n{desc}",
        ),
        # PEP 287 rtype
        (re.compile(r":(?P<section>rtype)\s*:\s+(?P<type>[^:]+)$"), "Type: *{type}*"),
        # PEP 287 raises typed
        (re.compile(r":(?P<section>raises?)\s+(?P<type>\w+)\s*:$"), "- `{type}`"),
        # PEP 287 raises typed with description
        (
            re.compile(r":(?P<section>raises?)\s+(?P<type>\w+)\s*:(?P<desc>.+)$"),
            "- `{type}` - {desc}",
        ),
    )

    replace_map = {
        ":attr:`": "attribute `",
        ":data:`": "`",
        ":class:``~": "class ``",
        ":class:`~": "class `",
        ":class:`": "class `",
        ":exc:`": "exception `",
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
