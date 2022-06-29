from unittest.mock import MagicMock, patch

from handsdown.ast_parser import smart_ast as ast
from handsdown.ast_parser.analyzers.function_analyzer import FunctionAnalyzer


class TestFunctionAnalyzer:
    def test_init(self):
        analyzer = FunctionAnalyzer()
        assert analyzer.argument_records == []
        assert analyzer.decorator_nodes == []
        assert analyzer.return_type_hint == None
        analyzer.generic_visit("node")

    @patch("handsdown.ast_parser.analyzers.function_analyzer.FunctionAnalyzer.visit")
    def test_visit_FunctionDef(self, visit_mock):
        analyzer = FunctionAnalyzer()
        node = MagicMock()
        node.decorator_list = ["decorator"]
        node.returns = None
        node.args = "args"
        assert analyzer.visit_FunctionDef(node) is None
        assert analyzer.decorator_nodes == ["decorator"]
        assert analyzer.return_type_hint == None
        visit_mock.assert_called_once_with("args")

        node.returns = "returns"
        assert analyzer.visit_FunctionDef(node) is None
        assert analyzer.return_type_hint == "returns"

    @patch("handsdown.ast_parser.analyzers.function_analyzer.FunctionAnalyzer.visit")
    def test_visit_AsyncFunctionDef(self, visit_mock):
        analyzer = FunctionAnalyzer()
        node = MagicMock()
        node.decorator_list = ["decorator"]
        node.returns = None
        node.args = "args"
        assert analyzer.visit_AsyncFunctionDef(node) is None
        assert analyzer.decorator_nodes == ["decorator"]
        assert analyzer.return_type_hint == None
        visit_mock.assert_called_once_with("args")

        node.returns = "returns"
        assert analyzer.visit_AsyncFunctionDef(node) is None
        assert analyzer.return_type_hint == "returns"

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
        kw_only_arg = MagicMock()
        kw_only_arg.mock_add_spec(ast.Name)
        kw_only_arg.id = "kw_only_arg"
        vararg = MagicMock()
        vararg.mock_add_spec(ast.Name)
        vararg.id = "vararg"
        node.vararg = vararg
        kwarg = MagicMock()
        vararg.mock_add_spec(ast.Name)
        kwarg.arg = "kwarg"
        node.kwarg = kwarg
        node.args = [ast2_arg, ast3_arg_2]
        node.posonlyargs = [ast3_arg]
        node.kwonlyargs = [kw_only_arg]
        default = MagicMock()
        default.mock_add_spec(ast.expr)
        default.node = "default"
        default1 = MagicMock()
        default1.mock_add_spec(ast.expr)
        default1.node = "default1"
        kw_default1 = MagicMock()
        kw_default1.mock_add_spec(ast.expr)
        kw_default1.node = "default1"
        node.defaults = [default, default1]
        node.kw_defaults = [kw_default1]
        assert analyzer.visit_arguments(node) is None
        assert len(analyzer.argument_records) == 6

        assert analyzer.argument_records[0].name == "ast3_arg"
        assert analyzer.argument_records[0].default == None
        assert analyzer.argument_records[0].prefix == ""
        assert analyzer.argument_records[0].type_hint == None

        assert analyzer.argument_records[1].name == "ast2_arg"
        assert analyzer.argument_records[1].default.node == default
        assert analyzer.argument_records[1].prefix == ""
        assert analyzer.argument_records[1].type_hint == None

        assert analyzer.argument_records[2].name == "ast3_arg_2"
        assert analyzer.argument_records[2].default.node == default1
        assert analyzer.argument_records[2].prefix == ""
        assert analyzer.argument_records[2].type_hint == None

        assert analyzer.argument_records[3].name == "kw_only_arg"
        assert analyzer.argument_records[3].default.node == kw_default1
        assert analyzer.argument_records[3].prefix == ""
        assert analyzer.argument_records[3].type_hint == None

        assert analyzer.argument_records[4].name == "vararg"
        assert analyzer.argument_records[4].default == None
        assert analyzer.argument_records[4].prefix == "*"
        assert analyzer.argument_records[4].type_hint == None

        assert analyzer.argument_records[5].name == "kwarg"
        assert analyzer.argument_records[5].default == None
        assert analyzer.argument_records[5].prefix == "**"
        assert analyzer.argument_records[5].type_hint.node == kwarg.annotation
