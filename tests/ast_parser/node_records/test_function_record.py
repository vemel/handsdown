from unittest.mock import MagicMock, patch

import handsdown.ast_parser.smart_ast as ast
from handsdown.ast_parser.node_records.function_record import FunctionRecord


class TestFunctionRecord:
    def test_init(self):
        node = MagicMock()
        node.name = "name"
        node.body = ["body"]
        node.mock_add_spec(ast.FunctionDef)
        record = FunctionRecord(node, is_method=True)
        assert record.name == "name"
        assert record.title == "name"
        assert record.is_method
        assert not record.is_classmethod
        assert not record.is_staticmethod
        assert record.line_number == 1

        record.line_number = 10
        assert record.line_number == 10

    @patch("handsdown.ast_parser.node_records.function_record.FunctionAnalyzer")
    def test_parse(self, FunctionAnalyzerMock):
        node = MagicMock()
        node.name = "name"
        node.body = ["body"]
        node.mock_add_spec(ast.FunctionDef)
        record = FunctionRecord(node, is_method=False)

        argument_1 = MagicMock()
        argument_1.related_names = ["argument_1_related", "argument_1_related_2"]
        argument_2 = MagicMock()
        argument_2.related_names = ["argument_2_related"]

        decorator_1 = MagicMock()
        decorator_1.related_names = ["decorator_1_related", "decorator_1_related_2"]
        decorator_2 = MagicMock()
        decorator_2.mock_add_spec(ast.Name)
        decorator_2.id = "staticmethod"
        decorator_3 = MagicMock()
        decorator_3.mock_add_spec(ast.Name)
        decorator_3.id = "classmethod"

        FunctionAnalyzerMock().argument_records = [argument_1, argument_2]
        FunctionAnalyzerMock().decorator_nodes = [decorator_1, decorator_2, decorator_3]
        FunctionAnalyzerMock().return_type_hint = "return_type_hint"
        record.parse()
        assert record.related_names == {
            "argument_1_related",
            "argument_1_related_2",
            "argument_2_related",
        }
        assert record.is_classmethod
        assert record.is_staticmethod

    @patch("handsdown.ast_parser.node_records.function_record.FunctionAnalyzer")
    def test_parse_type_comments(self, FunctionAnalyzerMock):
        node = MagicMock()
        node.name = "name"
        node.body = ["body"]
        node.mock_add_spec(ast.FunctionDef)
        record = FunctionRecord(node, is_method=False)

        argument_1 = MagicMock()
        argument_1.related_names = ["argument_1_related", "argument_1_related_2"]
        argument_1.line_number = 3
        argument_1.type_hint = None
        argument_2 = MagicMock()
        argument_2.related_names = ["argument_2_related"]
        argument_2.line_number = 5
        argument_2.type_hint = None

        FunctionAnalyzerMock().argument_records = [argument_1, argument_2]
        FunctionAnalyzerMock().decorator_nodes = []
        FunctionAnalyzerMock().return_type_hint = "return_type_hint"
        record.parse()
        record.line_number = 2
        lines = [
            "",
            "",
            "line # type: arg1",
            "line # type:arg2[type, type2]",
            "): # type: (...) -> return",
        ]
        record.parse_type_comments(lines)
        assert argument_1.type_hint.name == "arg1"
        assert argument_2.type_hint.name == "arg2[type, type2]"
        assert record.return_type_hint.name == "return"

        lines = [
            "",
            "",
            "line # type: (extra_arg, new_arg1[type, type2], new_arg2) -> new_return",
        ]
        record.parse_type_comments(lines)
        assert argument_1.type_hint.name == "new_arg1[type, type2]"
        assert argument_2.type_hint.name == "new_arg2"
        assert record.return_type_hint.name == "new_return"

    @patch("handsdown.ast_parser.node_records.function_record.FunctionAnalyzer")
    def test_render(self, FunctionAnalyzerMock):
        node = MagicMock()
        node.name = "name"
        node.body = ["body"]
        node.mock_add_spec(ast.FunctionDef)
        record = FunctionRecord(node, is_method=True)

        argument_1 = MagicMock()
        argument_1.render.return_value = "arg1"
        argument_2 = MagicMock()
        argument_2.render.return_value = "arg3"
        argument_3 = MagicMock()
        argument_3.render.return_value = "arg3"

        decorator_1 = MagicMock()
        decorator_1.mock_add_spec(ast.Name)
        decorator_1.id = "my_deco"
        decorator_1.related_names = ["decorator_1_related", "decorator_1_related_2"]
        decorator_2 = MagicMock()
        decorator_2.mock_add_spec(ast.Name)
        decorator_2.id = "classmethod"

        FunctionAnalyzerMock().argument_records = [argument_1, argument_2, argument_3]
        FunctionAnalyzerMock().decorator_nodes = [decorator_1, decorator_2]
        FunctionAnalyzerMock().return_type_hint = "return_type_hint"
        assert record.render() == "def name()"

        node.mock_add_spec(ast.AsyncFunctionDef)
        record = FunctionRecord(node, is_method=True)
        assert record.render() == "def name()"
