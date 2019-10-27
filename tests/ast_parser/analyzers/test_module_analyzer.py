# pylint: disable=missing-docstring
import unittest
from unittest.mock import MagicMock

import handsdown.ast_parser.smart_ast as ast
from handsdown.ast_parser.analyzers.module_analyzer import ModuleAnalyzer


class TestModuleAnalyzer(unittest.TestCase):
    def test_init(self):
        analyzer = ModuleAnalyzer()
        self.assertEqual(analyzer.all_names, [])
        self.assertEqual(analyzer.import_records, [])
        self.assertEqual(analyzer.function_records, [])
        self.assertEqual(analyzer.attribute_records, [])
        self.assertEqual(analyzer.class_records, [])

    def test_visit_Import(self):
        analyzer = ModuleAnalyzer()
        node = MagicMock()
        node.mock_add_spec(ast.Import)
        alias = MagicMock()
        alias.name = "real_name"
        alias.asname = "local_name"
        alias2 = MagicMock()
        alias2.name = "real_name2"
        alias2.asname = "local_name2"
        node.names = [alias, alias2]
        self.assertIsNone(analyzer.visit_Import(node))
        self.assertEqual(len(analyzer.import_records), 2)
        self.assertEqual(analyzer.import_records[0].source, None)
        self.assertEqual(analyzer.import_records[0].name, "real_name")
        self.assertEqual(analyzer.import_records[0].local_name, "local_name")
        self.assertEqual(analyzer.import_records[1].source, None)
        self.assertEqual(analyzer.import_records[1].name, "real_name2")
        self.assertEqual(analyzer.import_records[1].local_name, "local_name2")

    def test_visit_ImportFrom(self):
        analyzer = ModuleAnalyzer()
        node = MagicMock()
        node.mock_add_spec(ast.ImportFrom)
        node.module = "my_module"
        alias = MagicMock()
        alias.name = "real_name"
        alias.asname = "local_name"
        alias2 = MagicMock()
        alias2.name = "real_name2"
        alias2.asname = "local_name2"
        node.names = [alias, alias2]
        self.assertIsNone(analyzer.visit_ImportFrom(node))
        self.assertEqual(len(analyzer.import_records), 2)
        self.assertEqual(analyzer.import_records[0].source, "my_module")
        self.assertEqual(analyzer.import_records[0].name, "real_name")
        self.assertEqual(analyzer.import_records[0].local_name, "local_name")
        self.assertEqual(analyzer.import_records[1].source, "my_module")
        self.assertEqual(analyzer.import_records[1].name, "real_name2")
        self.assertEqual(analyzer.import_records[1].local_name, "local_name2")

    def test_visit_ClassDef(self):
        analyzer = ModuleAnalyzer()
        node = MagicMock()
        node.mock_add_spec(ast.ClassDef)
        node.name = "MyClass"
        node.body = ["body"]
        self.assertIsNone(analyzer.visit_ClassDef(node))
        self.assertEqual(len(analyzer.class_records), 1)
        self.assertEqual(analyzer.class_records[0].name, "MyClass")

        node.name = "_PrivateClass"
        self.assertIsNone(analyzer.visit_ClassDef(node))
        self.assertEqual(len(analyzer.class_records), 1)

    def test_visit_FunctionDef(self):
        analyzer = ModuleAnalyzer()
        node = MagicMock()
        node.mock_add_spec(ast.FunctionDef)
        node.name = "my_func"
        node.body = ["body"]
        self.assertIsNone(analyzer.visit_FunctionDef(node))
        self.assertEqual(len(analyzer.function_records), 1)
        self.assertEqual(analyzer.function_records[0].name, "my_func")

        node.name = "_private_func"
        self.assertIsNone(analyzer.visit_FunctionDef(node))
        self.assertEqual(len(analyzer.function_records), 1)

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
        self.assertEqual(len(analyzer.attribute_records), 1)
        self.assertEqual(analyzer.attribute_records[0].name, "attr")

        node.targets = [target, target]
        self.assertIsNone(analyzer.visit_Assign(node))
        self.assertEqual(len(analyzer.attribute_records), 1)

        node.targets = ["not_name_target"]
        self.assertIsNone(analyzer.visit_Assign(node))
        self.assertEqual(len(analyzer.attribute_records), 1)

        target.id = "_private_attr"
        node.targets = [target]
        self.assertIsNone(analyzer.visit_Assign(node))
        self.assertEqual(len(analyzer.attribute_records), 1)

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
        self.assertEqual(len(analyzer.attribute_records), 1)
        self.assertEqual(analyzer.all_names, ["MyClass", "my_func"])
