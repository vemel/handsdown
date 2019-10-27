# pylint: disable=missing-docstring
import unittest
from unittest.mock import MagicMock

import handsdown.ast_parser.smart_ast as ast
from handsdown.ast_parser.analyzers.module_analyzer import ModuleAnalyzer


class TestModuleAnalyzer(unittest.TestCase):
    def test_init(self):
        analyzer = ModuleAnalyzer()
        self.assertEqual(analyzer.all_names, [])
        self.assertEqual(analyzer.import_nodes, [])
        self.assertEqual(analyzer.function_nodes, [])
        self.assertEqual(analyzer.attribute_nodes, [])
        self.assertEqual(analyzer.class_nodes, [])

    def test_visit_Import(self):
        analyzer = ModuleAnalyzer()
        node = "import_node"
        self.assertIsNone(analyzer.visit_Import(node))
        self.assertEqual(len(analyzer.import_nodes), 1)
        self.assertEqual(analyzer.import_nodes[0], node)

    def test_visit_ImportFrom(self):
        analyzer = ModuleAnalyzer()
        node = "import_from_node"
        self.assertIsNone(analyzer.visit_ImportFrom(node))
        self.assertEqual(len(analyzer.import_nodes), 1)
        self.assertEqual(analyzer.import_nodes[0], "import_from_node")

    def test_visit_ClassDef(self):
        analyzer = ModuleAnalyzer()
        node = MagicMock()
        node.name = "MyClass"
        self.assertIsNone(analyzer.visit_ClassDef(node))
        self.assertEqual(len(analyzer.class_nodes), 1)
        self.assertEqual(analyzer.class_nodes[0], node)

        node.name = "_PrivateClass"
        self.assertIsNone(analyzer.visit_ClassDef(node))
        self.assertEqual(len(analyzer.class_nodes), 1)

    def test_visit_FunctionDef(self):
        analyzer = ModuleAnalyzer()
        node = MagicMock()
        node.name = "my_func"
        self.assertIsNone(analyzer.visit_FunctionDef(node))
        self.assertEqual(len(analyzer.function_nodes), 1)
        self.assertEqual(analyzer.function_nodes[0], node)

        node.name = "_private_func"
        self.assertIsNone(analyzer.visit_FunctionDef(node))
        self.assertEqual(len(analyzer.function_nodes), 1)

    def test_visit_Assign(self):
        analyzer = ModuleAnalyzer()
        node = MagicMock()
        node.mock_add_spec(ast.Assign)
        node.value = "value"
        target = MagicMock()
        target.mock_add_spec(ast.Name)
        target.id = "attr"
        node.targets = [target]
        self.assertIsNone(analyzer.visit_Assign(node))
        self.assertEqual(len(analyzer.attribute_nodes), 1)
        self.assertEqual(analyzer.attribute_nodes[0], node)

        node.targets = [target, target]
        self.assertIsNone(analyzer.visit_Assign(node))
        self.assertEqual(len(analyzer.attribute_nodes), 1)

        node.targets = ["not_name_target"]
        self.assertIsNone(analyzer.visit_Assign(node))
        self.assertEqual(len(analyzer.attribute_nodes), 1)

        target.id = "_private_attr"
        node.targets = [target]
        self.assertIsNone(analyzer.visit_Assign(node))
        self.assertEqual(len(analyzer.attribute_nodes), 1)

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
        self.assertIsNone(analyzer.visit_Assign(node))
        self.assertEqual(len(analyzer.attribute_nodes), 1)
        self.assertEqual(analyzer.all_names, ["MyClass", "my_func"])
