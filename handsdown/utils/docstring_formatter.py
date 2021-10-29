"""
Translator of docstrings to Markdown format.
"""
from handsdown.utils.indent_trimmer import IndentTrimmer

__all__ = ["DocstringFormatter"]


class DocstringFormatter:
    """
    Translator of docstrings to Markdown format.

    Arguments:
        docstring -- Raw docstring.
    """

    def __init__(self, docstring: str) -> None:
        docstring = self._cleanup(docstring)
        docstring = IndentTrimmer.trim_empty_lines(docstring)
        docstring = IndentTrimmer.trim_text(docstring)
        lines = docstring.split("\n")
        self._lines = IndentTrimmer.trim_lines(lines)

    @staticmethod
    def _cleanup(docstring: str) -> str:
        """
        Fix multiline docstrings starting with no newline after quotes.

        Arguments:
            docstring -- Raw docstring.

        Returns:
            Aligned docstring.
        """
        if "\n" in docstring and docstring[0] != "\n":
            lines = docstring.split("\n")
            next_line_index = 1
            next_line = lines[next_line_index]
            while not next_line.strip() and next_line_index < len(lines) - 1:
                next_line_index += 1
                next_line = lines[next_line_index]

            indent = IndentTrimmer.get_line_indent(next_line)
            line_indent = " " * indent
            docstring = f"\n{line_indent}{docstring}"

        return IndentTrimmer.trim_text(docstring)

    def _parse_flask_title(self) -> None:
        lines = list(self._lines)
        for index, line in enumerate(lines):
            if line.startswith("~~~~"):
                if index:
                    self._lines[index - 1] = f"# {self._lines[index - 1]}"
                self._lines.pop(index)

    def render(self) -> str:
        """
        Get Markdown-friendly docstring.

        Returns:
            A cleaned up docstring.
        """
        self._parse_flask_title()
        return "\n".join(self._lines)
