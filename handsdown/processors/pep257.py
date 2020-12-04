"""
# PEP 257 Docstring Processor

Docstring processor for PEP 257 and Google docstring format.

## Links

- [Supported section names](
    https://sphinxcontrib-napoleon.readthedocs.io/en/latest/index.html#docstring-sections
  )

## Supported features

- `<known_section>:` starts a new section `<known_section>`
- `<name>: <description>` formatted in Markdown style and added to named sections
- `<name> (<?type>): <description>` formatted in Markdown style and added to named sections
- `<name> (<?type>,optonal): <description>` formatted in Markdown
  style and added to named sections
- `<name> -- <description>` formatted in Markdown style and
  added to named sections
- `<name> {<type>} -- <description>` formatted in Markdown style and added to named sections
- `<name> {[<type>]} -- <description>` formatted in Markdown style and added to named sections
- `<name> <?type>, optonal: <description>` formatted
  in Markdown style and added to named sections
- `<name> -- <description>` formatted in Markdown style
"""

import re

from handsdown.processors.base import BaseDocstringProcessor


class PEP257DocstringProcessor(BaseDocstringProcessor):
    """
    Docstring processor for PEP 257 and Google docstring format.
    """

    named_section_line_re_map = (
        # Google non-typed
        (re.compile(r"^\s*(?P<param>\S+):\s+(?P<desc>.+)$"), "- `{param}` - {desc}"),
        # Google typed with parentheses
        (
            re.compile(r"^\s*(?P<param>\S+)\s+\((?P<type>\S+(?:,\s+optional)?)\):\s+(?P<desc>.+)$"),
            "- `{param}` *{type}* - {desc}",
        ),
        # Google typed without parentheses
        (
            re.compile(r"^\s*(?P<param>\S+)\s+(?P<type>\S+(?:,\s+optional)?):\s+(?P<desc>.+)$"),
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
            re.compile(r"^\s*(?P<param>\S+)\s+\{\[(?P<type>\S+)\]\}\s+--\s+(?P<desc>.+)$"),
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

    def _parse_regular_line(self, line: str) -> None:
        # If there is a line with a section name - set this section as active
        if line in self.section_name_map:
            self.current_section_name = self.section_name_map[line]
            return

        # format line using `line_re_map` regexps
        # multiline result supported
        # only works in named sections
        if self.current_section_name:
            for line_re, line_format in self.named_section_line_re_map:
                match = line_re.match(line)
                if not match:
                    continue

                match_dict = match.groupdict()
                formatted_line = line_format.format(**match_dict)
                for line_part in formatted_line.split("\n"):
                    self._add_line(line_part)
                return

        super()._parse_regular_line(line)
