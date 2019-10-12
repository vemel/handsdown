from abc import abstractmethod
from collections import defaultdict
from typing import Text, Iterable, Optional, Dict, List, Pattern

from handsdown.type_defs import SectionMap


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
            indent = self._get_line_indent(line)
            parsed_line = self._parse_line(self._strip_indent(line, indent).rstrip())
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

            section_indent = self._get_lines_indent(section_lines)
            for line in section_lines:
                if not line.strip():
                    lines.append("")
                    continue

                lines.append(self._strip_indent(line, section_indent))

            if lines[-1]:
                lines.append("")

        return "\n".join(lines)

    @abstractmethod
    def _parse_line(self, line: Text) -> Optional[Text]:
        pass

    @staticmethod
    def _strip_indent(line: Text, indent: int) -> Text:
        if not line[:indent].strip():
            return line[indent:]

        return line

    @staticmethod
    def _get_line_indent(line: Text) -> int:
        return len(line) - len(line.lstrip())

    @classmethod
    def _get_lines_indent(cls, lines: Iterable[Text]) -> int:
        indents = [cls._get_line_indent(i) for i in lines if i.strip()]
        return min(indents, default=0)
