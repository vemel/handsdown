from typing import Iterable, Text, List


class IndentTrimmer:
    """
    Utility class for removing indentation for sections and lines.
    """

    @classmethod
    def trim_text(cls, text: Text) -> Text:
        """
        Trim minimum indent from each line of text.

        Examples:

            ```python
            IndentTrimmer.trim_text('  asd\\n asd\\n   asd\\n')
            # ' asd\\nasd\\n  asd\\n'
            ```

        Arguments:
            text -- Multiline text.

        Returns:
            A text with trimmed indent.
        """
        new_lines = IndentTrimmer.trim_lines(text.split("\n"))
        return "\n".join(new_lines)

    @classmethod
    def trim_lines(cls, lines: Iterable[Text]) -> List[Text]:
        """
        Trim minimum indent from each line of text.

        Examples:

            ```python
            IndentTrimmer.trim_lines([
                '  asd',
                ' asd',
                '   asd',
            )
            # [
            #     ' asd',
            #     'asd',
            #     '  asd',
            # ]
            ```

        Arguments:
            lines -- List of lines.

        Returns:
            A list of liens with trimmed indent.
        """
        indent = cls._get_lines_indent(lines)
        new_lines = []
        for line in lines:
            new_lines.append(cls.trim_line(line, indent))

        return new_lines

    @staticmethod
    def trim_line(line: Text, indent: int) -> Text:
        """
        Trim indent from line if it is empty.

        Examples:

            ```python
            IndentTrimmer.trim_line('     test', 2) # '   test'
            IndentTrimmer.trim_line('     test', 6) # 'test'
            IndentTrimmer.trim_line('     test', 1) # '    test'
            ```

        Arguments:
            line -- A line of text.

        Returns:
            A line with removed indent.
        """
        if not line[:indent].strip():
            return line[indent:]

        return line

    @staticmethod
    def get_line_indent(line: Text) -> int:
        """
        Get indent length of the line.

        Examples:

            ```python
            IndentTrimmer.get_line_indent('   test') # 3
            IndentTrimmer.get_line_indent('test') # 0
            ```

        Arguments:
            line -- Line of text.

        Returns:
            A number of indentation characters in a beginning of the line.
        """
        return len(line) - len(line.lstrip())

    @classmethod
    def _get_lines_indent(cls, lines: Iterable[Text]) -> int:
        indents = [cls._get_line_indent(i) for i in lines if i.strip()]
        return min(indents, default=0)

    @staticmethod
    def _get_line_indent(line: Text) -> int:
        return len(line) - len(line.lstrip())
