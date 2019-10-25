"""
Enums for AST parsing.
"""
import enum


class RenderPart(enum.Enum):
    """
    Special render part for `handsdown.ast_parser.node_records.node_record.NodeRecord.render`
    function.
    """

    # Replaced with a line break for a multi-line render, does not change indent
    MULTI_LINE_BREAK = "MULTI_LINE_BREAK"

    # Replaced with a line break for a multi-line render, adds one indent level
    MULTI_LINE_INDENT = "MULTI_LINE_INDENT"

    # Replaced with a line break for a multi-line render, removes one indent level
    MULTI_LINE_UNINDENT = "MULTI_LINE_UNINDENT"

    # Replaced with a line break, does not change indent
    LINE_BREAK = "LINE_BREAK"

    # Replaced with a line break, adds one indent level
    LINE_INDENT = "LINE_INDENT"

    # Replaced with a line break, removes one indent level
    LINE_UNINDENT = "LINE_UNINDENT"

    # Replaced with a space in a single-line render
    SINGLE_LINE_SPACE = "SINGLE_LINE_SPACE"

    # Replaced with a comma in a multi-line render
    MULTI_LINE_COMMA = "MULTI_LINE_COMMA"

    def is_line_break(self):
        # type: () -> bool
        """
        Check if it is a mandatory line break.

        Returns:
            True if part is a line break.
        """
        return self in (RenderPart.LINE_BREAK, self.LINE_INDENT, self.LINE_UNINDENT)
