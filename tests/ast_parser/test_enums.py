# pylint: disable=missing-docstring
import unittest

from handsdown.ast_parser.enums import RenderPart


class TestRenderPart(unittest.TestCase):
    def test_is_line_break(self):
        self.assertTrue(RenderPart.LINE_BREAK.is_line_break())
        self.assertTrue(RenderPart.LINE_INDENT.is_line_break())
        self.assertTrue(RenderPart.LINE_UNINDENT.is_line_break())
        self.assertFalse(RenderPart.MULTI_LINE_BREAK.is_line_break())
        self.assertFalse(RenderPart.MULTI_LINE_INDENT.is_line_break())
        self.assertFalse(RenderPart.MULTI_LINE_UNINDENT.is_line_break())
