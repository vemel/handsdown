"""
Module for splitting docstring into `Section` groups.
"""

from collections import UserDict
from dataclasses import dataclass
from typing import Text, List, Generator

from handsdown.indent_trimmer import IndentTrimmer


@dataclass
class SectionBlock:
    """
    Dataclass representing a `Section` block.

    Attributes:
        lines -- List of lines.
    """

    lines: List[Text]

    def render(self) -> Text:
        """
        Render trimmed block lines.

        Returns:
            Block lines as a text.
        """
        lines = IndentTrimmer.trim_lines(self.lines)
        return "\n".join(lines)


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
    Dict-based storage for parsed `Section` list for
    `handsdown.processors.base.BaseProcessor`

    Key is a `Section` title.
    Value is a related `Section` instance.
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
        If `Section` does not exist - it is not created.

        Arguments:
            section_name -- Target section title
        """
        if section_name not in self:
            return

        self[section_name].blocks.append(SectionBlock(lines=[]))

    def trim_block(self, section_name: Text) -> None:
        """
        Delete last empty lines from the last `SectionBlock`.
        If `Section` does not exist - it is not created.

        Arguments:
            section_name - Target section title.
        """
        if section_name not in self:
            return

        lines = self[section_name].blocks[-1].lines
        while lines and not lines[-1].strip():
            lines.pop()

    @property
    def sections(self) -> Generator[Section, None, None]:
        """
        Iterate over existing `Section` objects.

        Yields:
            `Section` objects in order of appearance.
        """
        for section in self.values():
            yield section
