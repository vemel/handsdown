from abc import abstractmethod
from collections import defaultdict
from typing import Text, Optional, Dict, List, Pattern

from handsdown.type_defs import SectionMap
from handsdown.indent_trimmer import IndentTrimmer


class BaseDocstringProcessor:
    """
    This class implements the preprocessor for PEP257 and Google style.
    """

    def __init__(self) -> None:
        self.current_section_name: Text = ""
        self.sections: SectionMap = defaultdict(list)
        self.in_codeblock = False

    line_re_map: Dict[Pattern, Text] = {}

    section_name_map = {
        "Args:": "Arguments",
        "Arguments:": "Arguments",
        "Attributes:": "Attributes",
        "Example:": "Examples",
        "Examples:": "Examples",
        "Keyword Args:": "Arguments",
        "Keyword Arguments:": "Arguments",
        "Methods:": "Methods",
        "Note:": "Notes",
        "Notes:": "Notes",
        "Other Parameters:": "Arguments",
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
        sections: SectionMap = defaultdict(list)
        self.in_codeblock = False

        for line in content.split("\n"):
            indent = IndentTrimmer.get_line_indent(line)
            parsed_line = self._parse_line(
                IndentTrimmer.trim_line(line, indent).rstrip()
            )
            if parsed_line is None:
                continue
            for line_part in parsed_line.split("\n"):
                sections[self.current_section_name].append(f'{" " * indent}{line_part}')

        return sections

    def render_sections(self, sections: Dict[Text, List[Text]]) -> Text:
        """
        Render sections produced by `render_sections` to a string.

        Arguments:
            sections - Built sections.

        Returns:
            Markdown string.
        """
        lines = []
        for section_name, section_lines in sections.items():
            not_empty_lines = [i for i in section_lines if i.strip()]
            if not not_empty_lines:
                continue

            if section_name:
                lines.extend([f"#### {section_name}", ""])

            while section_lines and not section_lines[0].strip():
                section_lines = section_lines[1:]

            section_lines = IndentTrimmer.trim_lines(section_lines)
            lines.extend(section_lines)

            if lines[-1]:
                lines.append("")

        return "\n".join(lines)

    @abstractmethod
    def _parse_line(self, line: Text) -> Optional[Text]:
        pass
