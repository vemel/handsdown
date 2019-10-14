from collections import UserDict
from typing import Text
from handsdown.indent_trimmer import IndentTrimmer


class SectionMap(UserDict):
    """
    Storage for parsed section for `handsdown.processors.base.BaseProcessor`
    """

    def add_line(self, section_name: Text, line: Text) -> None:
        """
        Add new `line` to section `section_name`.
        If line and section are empty - sections is not created.

        Arguments:
            section_name - Target section title
            line - Line to add
        """
        if section_name not in self:
            if not line:
                return
            self[section_name] = []
        self[section_name].append(line)

    def render(self, header_level: int) -> Text:
        """
        Render sections to a string.

        Arguments:
            header_level -- Level of section title header.

        Returns:
            A markdown string.
        """
        lines = []
        header = "#" * header_level
        for section_name, section_lines in self.items():
            if section_name:
                lines.extend([f"{header} {section_name}", ""])

            section_lines = IndentTrimmer.trim_lines(section_lines)
            lines.append("\n".join(section_lines))

        return "\n".join(lines)
