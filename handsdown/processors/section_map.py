from collections import UserDict
from dataclasses import dataclass
from typing import Text, List
from handsdown.indent_trimmer import IndentTrimmer


@dataclass
class SectionBlock:
    """
    Dataclass representing a `Section` block.

    Attributes:
        lines -- List of lines.
    """

    lines: List[Text]


@dataclass
class Section:
    """
    Dataclass representing a section in a `SectionMap`.

    Attributes:
        title -- Section title.
        blocks -- List of line blocks.
    """

    title: Text
    blocks: List[SectionBlock]


class SectionMap(UserDict):
    """
    Storage for parsed section for `handsdown.processors.base.BaseProcessor`
    """

    def add_line(self, section_name: Text, line: Text) -> None:
        """
        Add new `line` to the last `SectionBlock` of section `section_name`.
        If line and section are empty - section is not created.

        Arguments:
            section_name -- Target section title
            line -- Line to add
        """
        if section_name not in self:
            if not line:
                return

            self[section_name] = Section(title=section_name, blocks=[])

        section = self[section_name]
        if not section.blocks:
            section.blocks.append(SectionBlock(lines=[]))

        self[section_name].blocks[-1].lines.append(line)

    def add_block(self, section_name: Text) -> None:
        """
        Add new `SectionBlock` to section `section_name`.

        Arguments:
            section_name -- Target section title
        """
        if section_name not in self:
            self[section_name] = Section(title=section_name, blocks=[])

        self[section_name].blocks.append(SectionBlock(lines=[]))

    def trim_block(self, section_name: Text) -> None:
        """
        Delete last empty lines from the last `SectionBlock`.

        Arguments:
            section_name - Target section title.
        """
        if section_name not in self:
            return

        lines = self[section_name].blocks[-1].lines
        while lines and not lines[-1].strip():
            lines.pop()

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
        for section in self.values():
            if section.title:
                lines.append(f"{header} {section.title}")

            for block in section.blocks:
                block_lines = IndentTrimmer.trim_lines(block.lines)
                lines.append("\n".join(block_lines))

        return "\n\n".join(lines)
