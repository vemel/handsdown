"""
# Base Docstring Processor

Base class for all docstring processors:

## Links

- `handsdown.processors.pep257.PEP257DocstringProcessor`
- `handsdown.processors.rst.RSTDocstringProcessor`
- `handsdown.processors.smart.SmartDocstringProcessor`

## Supported features

- `<triple_backticks><?language>` starts a new Markdown-style code block,
  ended with triple backticks
- `<line>::` starts a new Markdown-style Python code block, ended with unindent
- `<triple_tildes><?language>` starts a new Markdown-style block, ends with `<triple_tildes>`
- `>>>` starts a new Markdown-style Python block, ended with unindent
  or line not starting with `>>>` or `...`
"""

from typing import Dict, Optional, Pattern, Tuple

from handsdown.processors.section_map import SectionMap
from handsdown.utils.indent_trimmer import IndentTrimmer


class BaseDocstringProcessor:
    """
    Base docstring processor. All docstring processors are based on top of it.

    Attributes:
        line_re_map -- Mapping of line regexp to format string for it
        section_name_map -- Mapping of Section search key to Section title
        replace_map -- Mapping of string to replace to replacer
    """

    line_re_map: Tuple[Tuple[Pattern[str], str], ...] = tuple()
    section_name_map: Dict[str, str] = {}
    replace_map: Dict[str, str] = {}

    def __init__(self) -> None:
        self.current_section_name = ""
        self._in_codeblock = False
        self._in_doctest_block = False
        self._in_tilde_block = False
        self._in_md_codeblock = False
        self._in_indent_codeblock = False
        self._codeblock_indent = 0
        self._codeblock_lines_count = 0
        self.section_map = SectionMap()
        self._current_indent = 0

    def _reset(self) -> None:
        self.current_section_name = ""
        self._in_codeblock = False
        self._in_doctest_block = False
        self._in_tilde_block = False
        self._in_md_codeblock = False
        self._in_indent_codeblock = False
        self.section_map = SectionMap()
        self._current_indent = 0
        self._codeblock_indent = 0
        self._codeblock_lines_count = 0

    def build_sections(self, content: str) -> SectionMap:
        """
        Parse docstring and split it to sections with arrays of strings.

        Arguments:
            content -- Object docstring.

        Returns:
            A dictionary where key is a section name and value is a list of string sof this
            section.
        """
        self._reset()

        for line in content.split("\n"):
            self._current_indent = IndentTrimmer.get_line_indent(line)
            line = line.strip()

            # adding new lines to a doctest code block
            if self._in_doctest_block:
                self._parse_doctest_line(line)
                continue

            # adding new lines to a tilde block
            if self._in_tilde_block:
                self._parse_tilde_block_line(line)
                continue

            # adding new lines to a code block
            if self._in_md_codeblock:
                self._parse_md_codeblock_line(line)
                continue

            # adding new lines to an indented code block
            if self._in_indent_codeblock:
                self._parse_indent_codeblock_line(line)
                continue

            # adding new block on empty line outside of a code block
            if not line:
                self._add_block()
                continue

            self._parse_line(line)

        if self._in_indent_codeblock or self._in_doctest_block:
            self._trim_empty_lines()
            self._add_line("```", indent=0)

        return self.section_map

    def _parse_doctest_line(self, line: str) -> None:
        # end doctest codeblock
        if not line:
            self._in_doctest_block = False
            self._in_codeblock = False
            self._trim_empty_lines()
            self._add_line("```", indent=0)
            self._add_block()
            return

        # end doctest section
        if self._current_indent < self._codeblock_indent:
            self._in_doctest_block = False
            self._in_codeblock = False
            self._trim_empty_lines()
            self._add_line("```", indent=0)
            self._add_block()
            self._parse_line(line)
            return

        self._add_line(line, indent=self._current_indent - self._codeblock_indent)

    def _parse_md_codeblock_line(self, line: str) -> None:
        if not line and self._codeblock_lines_count == 0:
            return

        if self._codeblock_lines_count == 0:
            self._codeblock_indent = max(self._codeblock_indent, self._current_indent)

        # end MD-style codeblock
        if line.startswith("```"):
            self._in_codeblock = False
            self._in_md_codeblock = False
            self._add_line("```", indent=0)
            self._add_block()
            return

        self._add_line(line, indent=self._current_indent - self._codeblock_indent)
        self._codeblock_lines_count += 1

    def _parse_indent_codeblock_line(self, line: str) -> None:
        if not line and self._codeblock_lines_count == 0:
            return

        if self._codeblock_lines_count == 0:
            self._codeblock_indent = max(self._codeblock_indent, self._current_indent)

        # escape MD-style codeblock end
        if line.startswith("```"):
            line = f"'{line[1:]}"

        # this is actually a doctest block as it starts with `>>>`
        if self._codeblock_lines_count == 0 and line.startswith(">>>"):
            self._in_doctest_block = True
            self._in_indent_codeblock = False
            self._codeblock_indent = self._current_indent
            self._parse_doctest_line(line)
            return

        # end RST-style codeblock
        if line and self._current_indent < self._codeblock_indent:
            self._in_codeblock = False
            self._in_indent_codeblock = False
            self._trim_empty_lines()
            self._add_line("```", indent=0)
            self._add_block()
            self._parse_line(line)
            return

        self._add_line(line, indent=self._current_indent - self._codeblock_indent)
        self._codeblock_lines_count += 1

    def _parse_tilde_block_line(self, line: str) -> None:
        if not line and self._codeblock_lines_count == 0:
            return

        if self._codeblock_lines_count == 0:
            self._codeblock_indent = max(self._codeblock_indent, self._current_indent)

        # end tilde block
        if line.startswith("~~~"):
            self._add_line("~~~", indent=0)
            self._add_block()
            self._in_tilde_block = False
            return

        self._add_line(line, indent=self._current_indent - self._codeblock_indent)
        self._codeblock_lines_count += 1

    def _add_line(self, line: str, indent: Optional[int] = None) -> None:
        indent_str = " " * self._current_indent
        if indent is not None:
            indent_str = " " * indent

        self.section_map.add_line(self.current_section_name, f"{indent_str}{line}")

    def _add_block(self) -> None:
        self.section_map.add_block(self.current_section_name)

    def _trim_empty_lines(self) -> None:
        self.section_map.trim_block(self.current_section_name)

    def _parse_codeblock_start(self, line: str) -> None:
        # MD-style codeblock starts with triple backticks
        if line.startswith("```"):
            self._in_codeblock = True
            self._in_md_codeblock = True
            self._codeblock_indent = self._current_indent
            self._codeblock_lines_count = 0
            self._add_block()
            self._add_line(f"```{line.replace('`', '')}", indent=0)
            return

        # Tilde block starts with triple tildes
        if line.startswith("~~~"):
            self._in_codeblock = True
            self._in_tilde_block = True
            self._codeblock_indent = self._current_indent
            self._codeblock_lines_count = 0
            self._add_block()
            self._add_line(f"~~~{line.replace('~', '')}", indent=0)
            return

        # Doctest line starts with `>>>` and continues with `...` and output lines
        if line.startswith(">>>"):
            self._in_codeblock = True
            self._in_doctest_block = True
            self._codeblock_indent = self._current_indent
            self._codeblock_lines_count = 0
            self._add_block()
            self._add_line("```python", indent=0)
            self._parse_doctest_line(line)
            return

    def _parse_line(self, line: str) -> None:
        self._parse_codeblock_start(line)

        if self._in_codeblock:
            return

        self._parse_regular_line(line)

    def _parse_regular_line(self, line: str) -> None:
        # If section name ends with `::` - add section and start RST code block
        if line.endswith("::") and line[:-1] in self.section_name_map:
            self.current_section_name = self.section_name_map[line[:-1]]
            self._in_codeblock = True
            self._in_indent_codeblock = True
            self._codeblock_indent = self._current_indent + 1
            self._codeblock_lines_count = 0
            self._add_line("```python", indent=0)
            return

        # replace occurences from `replace_map`
        for target_str, replace_str in self.replace_map.items():
            line = line.replace(target_str, replace_str)

        # format line using `line_re_map` regexps
        # multiline result supported
        # if `section` found in match - set this section as active
        for line_re, line_format in self.line_re_map:
            match = line_re.match(line)
            if not match:
                continue

            match_dict = match.groupdict()

            if "section" in match_dict and match_dict["section"] in self.section_name_map:
                self.current_section_name = self.section_name_map[match_dict["section"]]

            formatted_line = line_format.format(**match_dict)
            for line_part in formatted_line.split("\n"):
                self._add_line(line_part)
            return

        # RST-style codeblock start with `::` in the end of the line
        if line.endswith("::"):
            self._in_codeblock = True
            self._in_indent_codeblock = True
            self._codeblock_indent = self._current_indent + 1
            self._codeblock_lines_count = 0
            self._add_line(line[:-2])
            self._add_block()
            self._add_line("```python", indent=0)
            return

        self._add_line(line)
