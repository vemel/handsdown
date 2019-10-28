# pylint: disable=missing-docstring
import unittest
from unittest.mock import MagicMock

import handsdown.ast_parser.smart_ast as ast
from handsdown.ast_parser.enums import RenderPart
from handsdown.ast_parser.analyzers.expression_analyzer import ExpressionAnalyzer


class TestClassAnalyzer(unittest.TestCase):
    def test_init(self):
        analyzer = ExpressionAnalyzer()
        self.assertEqual(analyzer.parts, [])

    def test_visit_Str(self):
        node = MagicMock()
        node.s = "value"
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_Str(node))
        self.assertEqual(analyzer.parts, ["'value'"])

        node.s = b"value"
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_Str(node))
        self.assertEqual(analyzer.parts, ["'value'"])

    def test_visit_Bytes(self):
        node = MagicMock()
        node.s = b"value"
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_Bytes(node))
        self.assertEqual(analyzer.parts, ["b'value'"])

    def test_visit_Num(self):
        node = MagicMock()
        node.n = 123.456
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_Num(node))
        self.assertEqual(analyzer.parts, ["123.456"])

    def test_visit_Name(self):
        node = MagicMock()
        node.id = "name"
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_Name(node))
        self.assertEqual(analyzer.parts, ["name"])

    def test_visit_NameConstant(self):
        node = MagicMock()
        node.value = "node_value"
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_NameConstant(node))
        self.assertEqual(analyzer.parts, ["'node_value'"])

    def test_visit_Subscript(self):
        node = MagicMock()
        node.value = "node_value"
        node_slice_value = MagicMock()
        node_slice_value.mock_add_spec(ast.Tuple)
        node_slice_value.elts = ["el1", "el2"]
        node_slice = MagicMock()
        node_slice.mock_add_spec(ast.Index)
        node_slice.value = node_slice_value
        node.slice = node_slice
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_Subscript(node))
        self.assertEqual(
            analyzer.parts,
            [
                "node_value",
                "[",
                RenderPart.MULTI_LINE_INDENT,
                "el1",
                ",",
                RenderPart.SINGLE_LINE_SPACE,
                RenderPart.MULTI_LINE_BREAK,
                "el2",
                RenderPart.MULTI_LINE_COMMA,
                RenderPart.MULTI_LINE_UNINDENT,
                "]",
            ],
        )

        node.slice = "node_slice"
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_Subscript(node))
        self.assertEqual(analyzer.parts, ["node_value", "[", "node_slice", "]"])

    def test_visit_Attribute(self):
        node = MagicMock()
        node.value = "node_value"
        node.attr = "node_attr"
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_Attribute(node))
        self.assertEqual(analyzer.parts, ["node_value", ".", "node_attr"])

    def test_visit_List(self):
        node = MagicMock()
        node.elts = ["el1", "el2"]
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_List(node))
        self.assertEqual(
            analyzer.parts,
            [
                "[",
                RenderPart.MULTI_LINE_INDENT,
                "el1",
                ",",
                RenderPart.SINGLE_LINE_SPACE,
                RenderPart.MULTI_LINE_BREAK,
                "el2",
                RenderPart.MULTI_LINE_COMMA,
                RenderPart.MULTI_LINE_UNINDENT,
                "]",
            ],
        )

    def test_visit_Set(self):
        node = MagicMock()
        node.elts = ["el1", "el2"]
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_Set(node))
        self.assertEqual(
            analyzer.parts,
            [
                "{",
                RenderPart.MULTI_LINE_INDENT,
                "el1",
                ",",
                RenderPart.SINGLE_LINE_SPACE,
                RenderPart.MULTI_LINE_BREAK,
                "el2",
                RenderPart.MULTI_LINE_COMMA,
                RenderPart.MULTI_LINE_UNINDENT,
                "}",
            ],
        )

    def test_visit_Tuple(self):
        node = MagicMock()
        node.elts = ["el1", "el2"]
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_Tuple(node))
        self.assertEqual(
            analyzer.parts,
            [
                "(",
                RenderPart.MULTI_LINE_INDENT,
                "el1",
                ",",
                RenderPart.SINGLE_LINE_SPACE,
                RenderPart.MULTI_LINE_BREAK,
                "el2",
                RenderPart.MULTI_LINE_COMMA,
                RenderPart.MULTI_LINE_UNINDENT,
                ")",
            ],
        )

    def test_visit_Call(self):
        pass

    def test_visit_Starred(self):
        node = MagicMock()
        node.value = "node_value"
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_Starred(node))
        self.assertEqual(analyzer.parts, ["*", "node_value"])

    def test_visit_keyword(self):
        node = MagicMock()
        node.arg = "node_arg"
        node.value = "node_value"
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_keyword(node))
        self.assertEqual(analyzer.parts, ["node_arg", "=", "node_value"])

        node.arg = None
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_keyword(node))
        self.assertEqual(analyzer.parts, ["**", "node_value"])
