"""
Module for splitting docstring into `Section` groups.
"""
from typing import Dict, Iterator, List

from handsdown.processors.section import Section
from handsdown.processors.section_block import SectionBlock
from handsdown.utils.indent_trimmer import IndentTrimmer


class SectionMap:
    """
    Dict-based storage for parsed `Section` list.

    Used for `handsdown.processors.base.BaseDocstringProcessor`.

    Key is a `Section` title.
    Value is a related `Section` instance.
    """

    def __init__(self) -> None:
        super().__init__()
        self._order: List[str] = []
        self.sections: Dict[str, Section] = {}

    def add_line_indent(self, section_name: str, line: str) -> None:
        """
        Add line respecting indent of the current section block.

        Arguments:
            section_name -- Target section title
            line -- Line to add
        """
        if section_name in self.sections:
            section = self.sections[section_name]
            if section.blocks and section.blocks[-1].lines:
                indent = IndentTrimmer.get_line_indent(section.blocks[-1].lines[-1])
                line = IndentTrimmer.indent_line(line, indent)

        self.add_line(section_name, line)

    def add_line(self, section_name: str, line: str) -> None:
        """
        Add new `line` to the last `SectionBlock` of section `section_name`.

        If line and section are empty - section is not created.

        Arguments:
            section_name -- Target section title
            line -- Line to add
        """
        if section_name not in self.sections:
            if not line:
                return

            self._order.append(section_name)
            self.sections[section_name] = Section(title=section_name, blocks=[])

        section = self.sections[section_name]
        if not section.blocks:
            section.blocks.append(SectionBlock(lines=[]))

        self.sections[section_name].blocks[-1].lines.append(line)

    def add_block(self, section_name: str) -> None:
        """
        Add new `SectionBlock` to section `section_name`.

        If `Section` does not exist - it is not created.

        Arguments:
            section_name -- Target section title
        """
        if section_name not in self.sections:
            return

        self.sections[section_name].blocks.append(SectionBlock(lines=[]))

    def trim_block(self, section_name: str) -> None:
        """
        Delete last empty lines from the last `SectionBlock`.

        If `Section` does not exist - it is not created.

        Arguments:
            section_name -- Target section title.
        """
        if section_name not in self.sections:
            return

        lines = self.sections[section_name].blocks[-1].lines
        while lines and not lines[-1].strip():
            lines.pop()

    def __iter__(self) -> Iterator[Section]:
        """
        Iterate over existing `Section` objects.

        Yields:
            `Section` objects in order of appearance.
        """
        for section_name in self._order:
            section = self.sections[section_name]
            yield section
