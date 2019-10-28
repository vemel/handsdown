# pylint: disable=missing-docstring
import unittest
from unittest.mock import MagicMock, patch, ANY

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
        # TODO: add test
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

    def test_visit_Dict(self):
        node = MagicMock()
        node.keys = ["key1", "key2"]
        node.values = ["value1", "value2"]
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_Dict(node))
        self.assertEqual(
            analyzer.parts,
            [
                "{",
                RenderPart.MULTI_LINE_INDENT,
                "key1",
                ": ",
                "value1",
                ",",
                RenderPart.SINGLE_LINE_SPACE,
                RenderPart.MULTI_LINE_BREAK,
                "key2",
                ": ",
                "value2",
                RenderPart.MULTI_LINE_COMMA,
                RenderPart.MULTI_LINE_UNINDENT,
                "}",
            ],
        )

    @patch("handsdown.ast_parser.analyzers.expression_analyzer.get_logger")
    def test_visit_Compare(self, get_logger_mock):
        node = MagicMock()
        node.left = "left"
        node.comparators = ["middle", "right"]
        node.ops = [ast.LtE(), ast.IsNot()]
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_Compare(node))
        self.assertEqual(
            analyzer.parts,
            ["left", " ", "<=", " ", "middle", " ", "is not", " ", "right"],
        )

        node.ops = [ast.LtE(), ast.Import]
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_Compare(node))
        self.assertEqual(
            analyzer.parts, ["left", " ", "<=", " ", "middle", " ", "...", " ", "right"]
        )
        get_logger_mock().warning.assert_called_once_with(ANY)

    @patch("handsdown.ast_parser.analyzers.expression_analyzer.get_logger")
    def test_visit_BinOp(self, get_logger_mock):
        node = MagicMock()
        node.left = "left"
        node.right = "right"
        node.op = ast.LShift()

        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_BinOp(node))
        self.assertEqual(analyzer.parts, ["left", " ", "<<", " ", "right"])

        node.op = ast.Import()
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_BinOp(node))
        self.assertEqual(analyzer.parts, ["left", " ", "...", " ", "right"])
        get_logger_mock().warning.assert_called_once_with(ANY)

    @patch("handsdown.ast_parser.analyzers.expression_analyzer.get_logger")
    def test_visit_BoolOp(self, get_logger_mock):
        node = MagicMock()
        node.values = ["left", "right"]
        node.op = ast.And()

        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_BoolOp(node))
        self.assertEqual(analyzer.parts, ["left", " ", "and", " ", "right"])

        node.op = ast.Or()
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_BoolOp(node))
        self.assertEqual(analyzer.parts, ["left", " ", "or", " ", "right"])

        node.op = ast.Import()
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_BoolOp(node))
        self.assertEqual(analyzer.parts, ["left", " ", "...", " ", "right"])
        get_logger_mock().warning.assert_called_once_with(ANY)

    @patch("handsdown.ast_parser.analyzers.expression_analyzer.get_logger")
    def test_visit_UnaryOp(self, get_logger_mock):
        node = MagicMock()
        node.operand = "operand"
        node.op = ast.Not()

        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_UnaryOp(node))
        self.assertEqual(analyzer.parts, ["not", " ", "operand"])

        node.op = ast.Invert()
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_UnaryOp(node))
        self.assertEqual(analyzer.parts, ["~", "operand"])

        node.op = ast.UAdd()
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_UnaryOp(node))
        self.assertEqual(analyzer.parts, ["+", "operand"])

        node.op = ast.USub()
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_UnaryOp(node))
        self.assertEqual(analyzer.parts, ["-", "operand"])

        node.op = ast.Import()
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_UnaryOp(node))
        self.assertEqual(analyzer.parts, ["...", "operand"])
        get_logger_mock().warning.assert_called_once_with(ANY)

    def test_visit_Lambda(self):
        node = MagicMock()
        node.args = "args"
        node.body = "body"

        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_Lambda(node))
        self.assertEqual(analyzer.parts, ["lambda ", "args", ": ", "body"])

    def test_visit_arguments(self):
        # TODO: add test
        pass

    def test_visit_arg(self):
        node = MagicMock()
        node.arg = "arg"
        node.annotation = "annotation"

        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_arg(node))
        self.assertEqual(analyzer.parts, ["arg", ": ", "annotation"])

        node.annotation = None
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_arg(node))
        self.assertEqual(analyzer.parts, ["arg"])

    def test_visit_Index(self):
        node = MagicMock()
        node.value = "value"

        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_Index(node))
        self.assertEqual(analyzer.parts, ["value"])

        node_value = MagicMock()
        node_value.mock_add_spec(ast.Tuple)
        node_value.elts = ["el1", "el2"]
        node.value = node_value
        self.assertIsNone(analyzer.visit_Index(node))
        self.assertEqual(
            analyzer.parts,
            [
                "value",
                RenderPart.MULTI_LINE_INDENT,
                "el1",
                ",",
                RenderPart.SINGLE_LINE_SPACE,
                RenderPart.MULTI_LINE_BREAK,
                "el2",
                RenderPart.MULTI_LINE_COMMA,
                RenderPart.MULTI_LINE_UNINDENT,
            ],
        )

    def test_visit_Ellipsis(self):
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_Ellipsis("node"))
        self.assertEqual(analyzer.parts, ["..."])

    def test_visit_Slice(self):
        node = MagicMock()
        node.lower = "lower"
        node.upper = "upper"
        node.step = "step"

        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_Slice(node))
        self.assertEqual(analyzer.parts, ["lower", ":", "upper", ":", "step"])

        node.upper = None
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_Slice(node))
        self.assertEqual(analyzer.parts, ["lower", ":", ":", "step"])

        node.step = None
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_Slice(node))
        self.assertEqual(analyzer.parts, ["lower", ":"])

        node.lower = None
        node.upper = None
        node.step = "step"
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_Slice(node))
        self.assertEqual(analyzer.parts, [":", ":", "step"])

    def test_visit_JoinedStr(self):
        node = MagicMock()
        node_value = MagicMock()
        node_value.mock_add_spec(ast.Str)
        node_value.s = "node_value"
        node_value_2 = MagicMock()
        node_value_2.s = b"node_value_2"
        node_value_2.mock_add_spec(ast.Str)
        node_value_3 = "not_str"
        node.values = [node_value, node_value_2, node_value_3]

        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_JoinedStr(node))
        self.assertEqual(
            analyzer.parts, ["f'", "node_value", "node_value_2", "not_str", "'"]
        )

    def test_visit_FormattedValue(self):
        node = MagicMock()
        node.value = "value"

        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_FormattedValue(node))
        self.assertEqual(analyzer.parts, ["{", "value", "}"])

    def test_visit_comprehension(self):
        node = MagicMock()
        node.target = "target"
        node.iter = "iter"
        node.ifs = ["if1", "if2"]

        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_comprehension(node))
        self.assertEqual(
            analyzer.parts,
            ["for ", "target", " in ", "iter", " if ", "if1", " if ", "if2"],
        )

    def test_visit_DictComp(self):
        node = MagicMock()
        node.key = "key"
        node.value = "value"
        node.generators = ["generator1", "generator2"]

        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_DictComp(node))
        self.assertEqual(
            analyzer.parts,
            ["{", "key", ": ", "value", " ", "generator1", "generator2", "}"],
        )

    def test_visit_ListComp(self):
        node = MagicMock()
        node.elt = "elt"
        node.generators = ["generator1", "generator2"]

        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_ListComp(node))
        self.assertEqual(
            analyzer.parts, ["[", "elt", " ", "generator1", "generator2", "]"]
        )

    def test_visit_SetComp(self):
        node = MagicMock()
        node.elt = "elt"
        node.generators = ["generator1", "generator2"]

        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_SetComp(node))
        self.assertEqual(
            analyzer.parts, ["{", "elt", " ", "generator1", "generator2", "}"]
        )

    def test_visit_GeneratorExp(self):
        node = MagicMock()
        node.elt = "elt"
        node.generators = ["generator1", "generator2"]

        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_GeneratorExp(node))
        self.assertEqual(
            analyzer.parts, ["(", "elt", " ", "generator1", "generator2", ")"]
        )

    @patch("handsdown.ast_parser.analyzers.expression_analyzer.get_logger")
    def test_generic_visit(self, get_logger_mock):
        node = MagicMock()
        node.mock_add_spec(ast.Import)

        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.generic_visit(node))
        self.assertEqual(analyzer.parts, ["..."])
        get_logger_mock().warning.assert_called_once_with(ANY)
