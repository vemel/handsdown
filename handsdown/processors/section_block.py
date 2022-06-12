"""
`Section` block.
"""
from typing import Iterable

from handsdown.utils.indent_trimmer import IndentTrimmer


class SectionBlock:
    """
    `Section` block.

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
