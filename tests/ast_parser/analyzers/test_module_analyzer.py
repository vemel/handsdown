from unittest.mock import MagicMock

import handsdown.ast_parser.smart_ast as ast
from handsdown.ast_parser.analyzers.module_analyzer import ModuleAnalyzer


class TestModuleAnalyzer:
    def test_init(self):
        analyzer = ModuleAnalyzer()
        assert analyzer.all_names == []
        assert analyzer.import_nodes == []
        assert analyzer.function_nodes == []
        assert analyzer.attribute_nodes == []
        assert analyzer.class_nodes == []

    def test_visit_Import(self):
        analyzer = ModuleAnalyzer()
        node = "import_node"
        assert analyzer.visit_Import(node) is None
        assert len(analyzer.import_nodes) == 1
        assert analyzer.import_nodes[0] == node

    def test_visit_ImportFrom(self):
        analyzer = ModuleAnalyzer()
        node = "import_from_node"
        assert analyzer.visit_ImportFrom(node) is None
        assert len(analyzer.import_nodes) == 1
        assert analyzer.import_nodes[0] == "import_from_node"

    def test_visit_ClassDef(self):
        analyzer = ModuleAnalyzer()
        node = MagicMock()
        node.name = "MyClass"
        assert analyzer.visit_ClassDef(node) is None
        assert len(analyzer.class_nodes) == 1
        assert analyzer.class_nodes[0] == node

        node.name = "_PrivateClass"
        assert analyzer.visit_ClassDef(node) is None
        assert len(analyzer.class_nodes) == 1

    def test_visit_FunctionDef(self):
        analyzer = ModuleAnalyzer()
        node = MagicMock()
        node.name = "my_func"
        assert analyzer.visit_FunctionDef(node) is None
        assert len(analyzer.function_nodes) == 1
        assert analyzer.function_nodes[0] == node

        node.name = "_private_func"
        assert analyzer.visit_FunctionDef(node) is None
        assert len(analyzer.function_nodes) == 1

    def test_visit_AsyncFunctionDef(self):
        analyzer = ModuleAnalyzer()
        node = MagicMock()
        node.name = "my_func"
        assert analyzer.visit_AsyncFunctionDef(node) is None
        assert len(analyzer.function_nodes) == 1
        assert analyzer.function_nodes[0] == node

        node.name = "_private_func"
        assert analyzer.visit_AsyncFunctionDef(node) is None
        assert len(analyzer.function_nodes) == 1

    def test_visit_Assign(self):
        analyzer = ModuleAnalyzer()
        node = MagicMock()
        node.mock_add_spec(ast.Assign)
        node.value = "value"
        target = MagicMock()
        target.mock_add_spec(ast.Name)
        target.id = "attr"
        node.targets = [target]
        assert analyzer.visit_Assign(node) is None
        assert len(analyzer.attribute_nodes) == 1
        assert analyzer.attribute_nodes[0] == node

        node.targets = [target, target]
        assert analyzer.visit_Assign(node) is None
        assert len(analyzer.attribute_nodes) == 1

        node.targets = ["not_name_target"]
        assert analyzer.visit_Assign(node) is None
        assert len(analyzer.attribute_nodes) == 1

        target.id = "_private_attr"
        node.targets = [target]
        assert analyzer.visit_Assign(node) is None
        assert len(analyzer.attribute_nodes) == 1

        target.id = "__all__"
        node.targets = [target]
        name_1 = MagicMock()
        name_1.mock_add_spec(ast.Str)
        name_1.s = "MyClass"
        name_2 = MagicMock()
        name_2.mock_add_spec(ast.Str)
        name_2.s = b"my_func"
        value = MagicMock()
        value.mock_add_spec(ast.List)
        value.elts = [name_1, name_2, "not_name"]
        node.value = value
        assert analyzer.visit_Assign(node) is None
        assert len(analyzer.attribute_nodes) == 1
        assert analyzer.all_names == ["MyClass", "my_func"]
