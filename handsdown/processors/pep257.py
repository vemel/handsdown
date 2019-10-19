"""
Docstring processor for PEP 257 and Google docstring format.
"""

import re

from handsdown.processors.base import BaseDocstringProcessor


class PEP257DocstringProcessor(BaseDocstringProcessor):
    """
    Docstring processor for PEP 257 and Google docstring format.
    """

    line_re_map = (
        # Google non-typed
        (re.compile(r"^\s*(?P<param>\S+):\s+(?P<desc>.+)$"), "- `{param}` - {desc}"),
        # Google typed with parentheses
        (
            re.compile(
                r"^\s*(?P<param>\S+)\s+\((?P<type>\S+(?:,\s+optional)?)\):\s+(?P<desc>.+)$"
            ),
            "- `{param}` *{type}* - {desc}",
        ),
        # Google typed without parentheses
        (
            re.compile(
                r"^\s*(?P<param>\S+)\s+(?P<type>\S+(?:,\s+optional)?):\s+(?P<desc>.+)$"
            ),
            "- `{param}` *{type}* - {desc}",
        ),
        # PEP257 non-typed
        (
            re.compile(r"^\s*(?P<param>\S+)\s+--\s+(?P<desc>.+)$"),
            "- `{param}` - {desc}",
        ),
        # PEP257 typed with curly brackets
        (
            re.compile(r"^\s*(?P<param>\S+)\s+\{(?P<type>\S+)\}\s+--\s+(?P<desc>.+)$"),
            "- `{param}` *{type}* - {desc}",
        ),
        # PEP257 typed
        (
            re.compile(
                r"^\s*(?P<param>\S+)\s+\{\[(?P<type>\S+)\]\}\s+--\s+(?P<desc>.+)$"
            ),
            "- `{param}` *{type}* - {desc}",
        ),
    )

    section_name_map = {
        "Args:": "Arguments",
        "Arguments:": "Arguments",
        "Attributes:": "Attributes",
        "Example:": "Examples",
        "Examples:": "Examples",
        "Keyword Args:": "Arguments",
        "Keyword args:": "Arguments",
        "Keyword Arguments:": "Arguments",
        "Keyword arguments:": "Arguments",
        "Methods:": "Methods",
        "Note:": "Notes",
        "Notes:": "Notes",
        "Other Parameters:": "Arguments",
        "Other parameters:": "Arguments",
        "Parameters:": "Arguments",
        "Return:": "Returns",
        "Returns:": "Returns",
        "Raises:": "Raises",
        "References:": "References",
        "See Also:": "See Also",
        "Todo:": "Todo",
        "Warning:": "Warnings",
        "Warnings:": "Warnings",
        "Warns:": "Warns",
        "Yield:": "Yields",
        "Yields:": "Yields",
    }
