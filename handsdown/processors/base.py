from typing import Text, Dict, Pattern, Optional

from handsdown.processors.section_map import SectionMap
from handsdown.indent_trimmer import IndentTrimmer


class BaseDocstringProcessor:
    """
    Base docstring processor. All docstring processors are based on top of it:

    - `handsdown.processors.pep257.PEP257DocstringProcessor`
    - `handsdown.processors.rst.RSTDocstringProcessor`
    - `handsdown.processors.smart.SmartDocstringProcessor`
    """

    def __init__(self) -> None:
        self.current_section_name: Text = ""
        self.in_codeblock = False
        self._codeblock_indent = 0
        self._codeblock_lines_count = 0
        self.section_map = SectionMap()
        self._current_indent = 0

    line_re_map: Dict[Pattern, Text] = {}
    section_name_map: Dict[Text, Text] = {}

    def build_sections(self, content: Text) -> SectionMap:
        """
        Parse docstring and split it to sections with arrays of strings.

        Arguments:
            content - Object docstring.

        Returns:
            A dictionary where key is a section name and value is a list of string sof this
            section.
        """
        self.current_section_name = ""
        self.in_codeblock = False
        self.section_map = SectionMap()
        self._current_indent = 0
        self._codeblock_indent = 0
        self._codeblock_lines_count = 0

        for line in content.split("\n"):
            self._current_indent = IndentTrimmer.get_line_indent(line)
            line = line.strip()
            if self.in_codeblock:
                self._parse_code_line(line)
            else:
                self._parse_line(line)

        if self.in_codeblock:
            self._strip_empty_lines()
            self._add_line("```", indent=0)

        return self.section_map

    def _parse_code_line(self, line: Text) -> bool:
        # end RST-style codeblock
        if line and self._current_indent < self._codeblock_indent:
            self.in_codeblock = False
            self._strip_empty_lines()
            self._add_line("```", indent=0)
            self._parse_line(line)
            return

        # end MD-style codeblock
        if line.strip().startswith("```"):
            self._add_line("```", indent=0)
            self.in_codeblock = False
            return

        if not line and self._codeblock_lines_count == 0:
            return

        self._add_line(line, indent=self._current_indent - self._codeblock_indent)
        self._codeblock_lines_count += 1

    def _add_line(self, line: Text, indent: Optional[int] = None) -> None:
        indent_str = " " * self._current_indent
        if indent is not None:
            indent_str = " " * indent

        self.section_map.add_line(self.current_section_name, f"{indent_str}{line}")

    def _strip_empty_lines(self):
        lines = self.section_map[self.current_section_name]
        while lines and not lines[-1].strip():
            lines.pop()

    def _parse_line(self, line: Text) -> None:
        # MD-style codeblock
        if line.strip().startswith("```"):
            self.in_codeblock = not self.in_codeblock
            self._codeblock_indent = self._current_indent
            self._codeblock_lines_count = 0
            self._add_line(line)
            return

        if line in self.section_name_map:
            self.current_section_name = self.section_name_map[line]
            return

        for line_re, line_format in self.line_re_map.items():
            match = line_re.match(line)
            if not match:
                continue

            match_dict = match.groupdict()

            if "section" in match_dict:
                self.current_section_name = self.section_name_map[match_dict["section"]]

            self._add_line(line_format.format(**match_dict))
            return

        # RST-style codeblock
        if line.endswith("::"):
            self.in_codeblock = True
            self._codeblock_indent = self._current_indent + 4
            self._codeblock_lines_count = 0
            self._add_line(line[:-2])
            self._add_line("")
            self._add_line("```python")
            return

        self._add_line(line)
