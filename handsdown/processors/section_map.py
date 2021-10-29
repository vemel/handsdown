"""
Module for splitting docstring into `Section` groups.
"""
from typing import Iterable, Iterator, List

from handsdown.utils.indent_trimmer import IndentTrimmer


class SectionBlock:
    """
    Dataclass representing a `Section` block.

    Arguments:
        lines -- List of lines.
    """

    def __init__(self, lines: Iterable[str]) -> None:
        self.lines = list(lines)

    def render(self) -> str:
        """
        Render trimmed block lines.

        Returns:
            Block lines as a text.
        """
        lines = IndentTrimmer.trim_lines(self.lines)
        return "\n".join(lines)


class Section:
    """
    Dataclass representing a section in a `SectionMap`.

    Arguments:
        title -- Section title.
        blocks -- List of line blocks.
    """

    def __init__(self, title: str, blocks: Iterable[SectionBlock]) -> None:
        self.title = title
        self.blocks = list(blocks)

    def render(self) -> str:
        """
        Render all Section block lines.

        Returns:
            Section lines as a text.
        """
        result = []
        for block in self.blocks:
            result.append(block.render())

        return "\n\n".join(result)


class SectionMap(dict):
    """
    Dict-based storage for parsed `Section` list for
    `handsdown.processors.base.BaseDocstringProcessor`

    Key is a `Section` title.
    Value is a related `Section` instance.
    """

    def __init__(self) -> None:
        super().__init__()
        self._order: List[str] = []

    def add_line_indent(self, section_name: str, line: str) -> None:
        """
        Add line respecting indent of the current section block.

        Arguments:
            section_name -- Target section title
            line -- Line to add
        """
        if section_name in self:
            section = self[section_name]
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
        if section_name not in self:
            if not line:
                return

            self._order.append(section_name)
            self[section_name] = Section(title=section_name, blocks=[])

        section = self[section_name]
        if not section.blocks:
            section.blocks.append(SectionBlock(lines=[]))

        self[section_name].blocks[-1].lines.append(line)

    def add_block(self, section_name: str) -> None:
        """
        Add new `SectionBlock` to section `section_name`.

        If `Section` does not exist - it is not created.

        Arguments:
            section_name -- Target section title
        """
        if section_name not in self:
            return

        self[section_name].blocks.append(SectionBlock(lines=[]))

    def trim_block(self, section_name: str) -> None:
        """
        Delete last empty lines from the last `SectionBlock`.
        If `Section` does not exist - it is not created.

        Arguments:
            section_name -- Target section title.
        """
        if section_name not in self:
            return

        lines = self[section_name].blocks[-1].lines
        while lines and not lines[-1].strip():
            lines.pop()

    @property
    def sections(self) -> Iterator[Section]:
        """
        Iterate over existing `Section` objects.

        Yields:
            `Section` objects in order of appearance.
        """
        for section_name in self._order:
            yield self[section_name]
