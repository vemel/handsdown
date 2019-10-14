from abc import abstractmethod
from typing import Text, Optional, Dict, Pattern

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

    line_re_map: Dict[Pattern, Text] = {}

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
        section_map = SectionMap()

        for line in content.split("\n"):
            indent = IndentTrimmer.get_line_indent(line)
            parsed_line = self._parse_line(
                IndentTrimmer.trim_line(line, indent).rstrip()
            )
            if parsed_line is None:
                continue
            for line_part in parsed_line.split("\n"):
                section_map.add_line(
                    self.current_section_name, f'{" " * indent}{line_part}'
                )

        return section_map

    @abstractmethod
    def _parse_line(self, line: Text) -> Optional[Text]:
        pass
