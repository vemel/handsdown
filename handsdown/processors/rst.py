"""
# reStructuredText Docstring Processor

Docstring processor for restructured text docstring format.

Supported features:

- `:param <name> <?type>: <?description>` directive is added to `Arguments` section
- `:type: <?description>` directive transformed to `Type: <type>`
- `:returns <?type>: <?description>` directive is added to `Returns` section
- `:rtype: <?description>` directive transformed to `Type: <type>`
- `:raises: <?description>` directive is added to `Raises` section
- `.. seealso::` directive is added to `See also` section
- `.. note::` directive is added to `Notes` section
- `.. warning:: <version>` directive is added to `Warnings` section
- `.. versionadded:: <version>` directive is formatted in Sphinx-style and added
  to `Notes` section
- `.. versionchanged:: <version>` directive is formatted in Sphinx-style and added
  to `Notes` section
- `.. deprecated::` directive is formatted in Sphinx-style and added to `Notes` section
- `.. code-block::` directive is formatted as Markdown Python codeblock
- `.. code-block:: <language>` directive is formatted as Markdown codeblock
- `.. math::` directive is formatted as Markdown Python codeblock
- `.. highlight::` directive is formatted as Markdown Python codeblock
- `.. highlight:: <language>` directive is formatted as Markdown codeblock
"""

import re

from handsdown.processors.base import BaseDocstringProcessor


class RSTDocstringProcessor(BaseDocstringProcessor):
    """
    Docstring processor for restructured text docstring format.
    """

    _section_re = re.compile(r"^\.\. (?P<section>\S+)::(?: (?P<body>.*))?")

    line_re_map = (
        # PEP 287 arg typed with description
        (
            re.compile(
                r"^:(?P<section>param|parameter)\s+(?P<type>\w+)"
                r"\s+(?P<param>\w+)\s*:\s*(?P<desc>.+)$"
            ),
            "- `{param}` *{type}* - {desc}",
        ),
        # PEP 287 arg with description
        (
            re.compile(r"^:(?P<section>param|parameter)\s+(?P<param>\w+)\s*:\s*(?P<desc>.+)$"),
            "- `{param}` - {desc}",
        ),
        # PEP 287 arg typed
        (
            re.compile(r"^:(?P<section>param|parameter)\s+(?P<type>\w+)\s+(?P<param>\w+)\s*:$"),
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

    section_directive_map = {
        "seealso": "See also",
        "note": "Notes",
        "warning": "Warnings",
    }

    version_directive_map = {
        "versionadded": "Added",
        "versionchanged": "Changed",
        "deprecated": "Deprecated",
    }

    def _parse_regular_line(self, line: str) -> None:
        section_match = self._section_re.match(line)
        if section_match:
            directive_name = section_match.groupdict()["section"]
            body = section_match.groupdict()["body"]

            if directive_name in self.section_directive_map:
                self.current_section_name = self.section_directive_map[directive_name]
                self._add_line("")

            if directive_name in self.version_directive_map:
                self.current_section_name = "Notes"
                line = self.version_directive_map[directive_name]
                if body:
                    line = f"{line} in version {body}"
                self._add_line("")
                self._add_line(line)
                return

            if directive_name in ("code-block", "math", "highlight"):
                self._in_codeblock = True
                self._in_indent_codeblock = True
                self._codeblock_indent = self._current_indent
                self._codeblock_lines_count = 0
                self._add_block()
                self._add_line("")
                self._add_line(f"```{body or 'python'}")
                return

            if body is None:
                return

            line = body

        super()._parse_regular_line(line)
