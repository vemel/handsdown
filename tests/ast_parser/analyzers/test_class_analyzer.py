# pylint: disable=missing-docstring
import unittest
from unittest.mock import MagicMock

import handsdown.ast_parser.smart_ast as ast
from handsdown.ast_parser.analyzers.class_analyzer import ClassAnalyzer


class TestClassAnalyzer(unittest.TestCase):
    def test_init(self):
        analyzer = ClassAnalyzer()
        self.assertEqual(analyzer.base_nodes, [])
        self.assertEqual(analyzer.decorator_nodes, [])
        self.assertEqual(analyzer.method_nodes, [])
        self.assertEqual(analyzer.attribute_nodes, [])

    def test_visit_ClassDef(self):
        analyzer = ClassAnalyzer()
        node = MagicMock()
        node.decorator_list = ["decorator"]
        node.bases = ["base", "base2"]
        self.assertIsNone(analyzer.visit_ClassDef(node))
        self.assertEqual(analyzer.decorator_nodes, ["decorator"])
        self.assertEqual(analyzer.base_nodes, ["base", "base2"])

    def test_visit_FunctionDef(self):
        analyzer = ClassAnalyzer()
        node = MagicMock()
        node.mock_add_spec(ast.FunctionDef)
        node.name = "FunctionDef"
        node.body = ["body_node"]
        self.assertIsNone(analyzer.visit_FunctionDef(node))
        self.assertEqual(analyzer.method_nodes, [node])

        node.name = "_private_method"
        self.assertIsNone(analyzer.visit_FunctionDef(node))
        self.assertEqual(len(analyzer.method_nodes), 1)

        node.name = "__magic_method__"
        self.assertIsNone(analyzer.visit_FunctionDef(node))
        self.assertEqual(len(analyzer.method_nodes), 1)

    def test_visit_Assign(self):
        analyzer = ClassAnalyzer()
        node = MagicMock()
        node.mock_add_spec(ast.Assign)
        node.value = "value"
        target = MagicMock()
        target.mock_add_spec(ast.Name)
        target.id = "attr"
        node.targets = [target]
        self.assertIsNone(analyzer.visit_Assign(node))
        self.assertEqual(analyzer.attribute_nodes, [node])

        node.targets = [target, target]
        self.assertIsNone(analyzer.visit_Assign(node))
        self.assertEqual(len(analyzer.attribute_nodes), 1)

        node.targets = ["not_name"]
        self.assertIsNone(analyzer.visit_Assign(node))
        self.assertEqual(len(analyzer.attribute_nodes), 1)

        target.id = "_pravate_attr"
        node.targets = [target]
        self.assertIsNone(analyzer.visit_Assign(node))
        self.assertEqual(len(analyzer.attribute_nodes), 1)
