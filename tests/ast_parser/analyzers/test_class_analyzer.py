# pylint: disable=missing-docstring
import unittest
from unittest.mock import MagicMock

import handsdown.ast_parser.smart_ast as ast
from handsdown.ast_parser.analyzers.class_analyzer import ClassAnalyzer


class TestClassAnalyzer(unittest.TestCase):
    def test_init(self):
        analyzer = ClassAnalyzer()
        self.assertEqual(analyzer.base_records, [])
        self.assertEqual(analyzer.decorator_records, [])
        self.assertEqual(analyzer.method_records, [])
        self.assertEqual(analyzer.attribute_records, [])

    def test_visit_ClassDef(self):
        analyzer = ClassAnalyzer()
        node = MagicMock()
        node.decorator_list = ["decorator"]
        node.bases = ["base", "base2"]
        node.body = ["body_element"]
        self.assertIsNone(analyzer.visit_ClassDef(node))
        self.assertEqual(len(analyzer.decorator_records), 1)
        self.assertEqual(len(analyzer.base_records), 2)

    def test_visit_FunctionDef(self):
        analyzer = ClassAnalyzer()
        node = MagicMock()
        node.mock_add_spec(ast.FunctionDef)
        node.name = "my_func"
        node.body = ["body_record"]
        self.assertIsNone(analyzer.visit_FunctionDef(node))
        self.assertEqual(len(analyzer.method_records), 1)
        self.assertEqual(analyzer.method_records[0].name, "my_func")
        self.assertEqual(analyzer.method_records[0].is_method, True)

        node.name = "_private_method"
        self.assertIsNone(analyzer.visit_FunctionDef(node))
        self.assertEqual(len(analyzer.method_records), 1)

        node.name = "__magic_method__"
        self.assertIsNone(analyzer.visit_FunctionDef(node))
        self.assertEqual(len(analyzer.method_records), 1)

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
        self.assertEqual(len(analyzer.attribute_records), 1)
        self.assertEqual(analyzer.attribute_records[0].name, "attr")

        node.targets = [target, target]
        self.assertIsNone(analyzer.visit_Assign(node))
        self.assertEqual(len(analyzer.attribute_records), 1)

        node.targets = ["not_name"]
        self.assertIsNone(analyzer.visit_Assign(node))
        self.assertEqual(len(analyzer.attribute_records), 1)

        target.id = "_pravate_attr"
        node.targets = [target]
        self.assertIsNone(analyzer.visit_Assign(node))
        self.assertEqual(len(analyzer.attribute_records), 1)
