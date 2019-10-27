# pylint: disable=missing-docstring
import unittest
from unittest.mock import MagicMock, patch
from handsdown.ast_parser import smart_ast as ast


from handsdown.ast_parser.analyzers.function_analyzer import FunctionAnalyzer


class TestFunctionAnalyzer(unittest.TestCase):
    def test_init(self):
        analyzer = FunctionAnalyzer()
        self.assertEqual(analyzer.argument_records, [])
        self.assertEqual(analyzer.decorator_nodes, [])
        self.assertEqual(analyzer.return_type_hint, None)
        analyzer.generic_visit("node")

    @patch("handsdown.ast_parser.analyzers.function_analyzer.FunctionAnalyzer.visit")
    def test_visit_FunctionDef(self, visit_mock):
        analyzer = FunctionAnalyzer()
        node = MagicMock()
        node.decorator_list = ["decorator"]
        node.returns = None
        node.args = "args"
        self.assertIsNone(analyzer.visit_FunctionDef(node))
        self.assertEqual(analyzer.decorator_nodes, ["decorator"])
        self.assertEqual(analyzer.return_type_hint, None)
        visit_mock.assert_called_once_with("args")

        node.returns = "returns"
        self.assertIsNone(analyzer.visit_FunctionDef(node))
        self.assertEqual(analyzer.return_type_hint, "returns")

    def test_visit_arguments(self):
        analyzer = FunctionAnalyzer()
        node = MagicMock()
        ast3_arg = MagicMock()
        ast3_arg.mock_add_spec(ast.Name)
        ast3_arg.id = "ast3_arg"
        ast2_arg = "ast2_arg"
        ast3_arg_2 = MagicMock()
        ast3_arg_2.mock_add_spec(ast.Name)
        ast3_arg_2.id = "ast3_arg_2"
        vararg = MagicMock()
        vararg.mock_add_spec(ast.Name)
        vararg.id = "vararg"
        node.vararg = vararg
        kwarg = MagicMock()
        vararg.mock_add_spec(ast.Name)
        kwarg.arg = "kwarg"
        node.kwarg = kwarg
        node.args = [ast2_arg]
        node.posonlyargs = [ast3_arg]
        node.kwonlyargs = [ast3_arg_2]
        default = MagicMock()
        default.mock_add_spec(ast.expr)
        default.node = "default"
        default1 = MagicMock()
        default1.mock_add_spec(ast.expr)
        default1.node = "default1"
        node.defaults = [default, default1]
        self.assertIsNone(analyzer.visit_arguments(node))
        self.assertEqual(len(analyzer.argument_records), 5)

        self.assertEqual(analyzer.argument_records[0].name, "ast3_arg")
        self.assertEqual(analyzer.argument_records[0].default, None)
        self.assertEqual(analyzer.argument_records[0].prefix, "")
        self.assertEqual(analyzer.argument_records[0].type_hint, None)

        self.assertEqual(analyzer.argument_records[1].name, "ast2_arg")
        self.assertEqual(analyzer.argument_records[1].default.node, default)
        self.assertEqual(analyzer.argument_records[1].prefix, "")
        self.assertEqual(analyzer.argument_records[1].type_hint, None)

        self.assertEqual(analyzer.argument_records[2].name, "ast3_arg_2")
        self.assertEqual(analyzer.argument_records[2].default.node, default1)
        self.assertEqual(analyzer.argument_records[2].prefix, "")
        self.assertEqual(analyzer.argument_records[2].type_hint, None)

        self.assertEqual(analyzer.argument_records[3].name, "vararg")
        self.assertEqual(analyzer.argument_records[3].default, None)
        self.assertEqual(analyzer.argument_records[3].prefix, "*")
        self.assertEqual(analyzer.argument_records[3].type_hint, None)

        self.assertEqual(analyzer.argument_records[4].name, "kwarg")
        self.assertEqual(analyzer.argument_records[4].default, None)
        self.assertEqual(analyzer.argument_records[4].prefix, "**")
        self.assertEqual(analyzer.argument_records[4].type_hint.node, kwarg.annotation)
