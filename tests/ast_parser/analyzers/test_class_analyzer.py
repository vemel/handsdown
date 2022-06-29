from unittest.mock import MagicMock, patch

import handsdown.ast_parser.smart_ast as ast
from handsdown.ast_parser.analyzers.class_analyzer import ClassAnalyzer


class TestClassAnalyzer:
    def test_init(self):
        analyzer = ClassAnalyzer()
        assert analyzer.base_nodes == []
        assert analyzer.decorator_nodes == []
        assert analyzer.method_nodes == []
        assert analyzer.attribute_nodes == []
        analyzer.generic_visit("node")

    @patch("handsdown.ast_parser.analyzers.class_analyzer.ClassAnalyzer.visit")
    def test_visit_ClassDef(self, visit_mock):
        analyzer = ClassAnalyzer()
        node = MagicMock()
        node.decorator_list = ["decorator"]
        node.bases = ["base", "base2"]
        node.body = ["body1", "body2"]
        assert analyzer.visit_ClassDef(node) is None
        assert analyzer.decorator_nodes == ["decorator"]
        assert analyzer.base_nodes == ["base", "base2"]
        visit_mock.assert_any_call("body1")
        visit_mock.assert_any_call("body2")

    def test_visit_FunctionDef(self):
        analyzer = ClassAnalyzer()
        node = MagicMock()
        node.mock_add_spec(ast.FunctionDef)
        node.name = "FunctionDef"
        node.body = ["body_node"]
        assert analyzer.visit_FunctionDef(node) is None
        assert analyzer.method_nodes == [node]

        node.name = "_private_method"
        assert analyzer.visit_FunctionDef(node) is None
        assert len(analyzer.method_nodes) == 1

        node.name = "__magic_method__"
        assert analyzer.visit_FunctionDef(node) is None
        assert len(analyzer.method_nodes) == 1

    def test_visit_AsyncFunctionDef(self):
        analyzer = ClassAnalyzer()
        node = MagicMock()
        node.mock_add_spec(ast.FunctionDef)
        node.name = "FunctionDef"
        node.body = ["body_node"]
        assert analyzer.visit_AsyncFunctionDef(node) is None
        assert analyzer.method_nodes == [node]

    def test_visit_Assign(self):
        analyzer = ClassAnalyzer()
        node = MagicMock()
        node.mock_add_spec(ast.Assign)
        node.value = "value"
        target = MagicMock()
        target.mock_add_spec(ast.Name)
        target.id = "attr"
        node.targets = [target]
        assert analyzer.visit_Assign(node) is None
        assert analyzer.attribute_nodes == [node]

        node.targets = [target, target]
        assert analyzer.visit_Assign(node) is None
        assert len(analyzer.attribute_nodes) == 1

        node.targets = ["not_name"]
        assert analyzer.visit_Assign(node) is None
        assert len(analyzer.attribute_nodes) == 1

        target.id = "_pravate_attr"
        node.targets = [target]
        assert analyzer.visit_Assign(node) is None
        assert len(analyzer.attribute_nodes) == 1
