import unittest
from unittest.mock import MagicMock, patch

import handsdown.ast_parser.smart_ast as ast
from handsdown.ast_parser.node_records.function_record import FunctionRecord


class TestFunctionRecord(unittest.TestCase):
    def test_init(self):
        node = MagicMock()
        node.name = "name"
        node.body = ["body"]
        node.mock_add_spec(ast.FunctionDef)
        record = FunctionRecord(node, is_method=True)
        self.assertEqual(record.name, "name")
        self.assertEqual(record.title, "name")
        self.assertTrue(record.is_method)
        self.assertFalse(record.is_classmethod)
        self.assertFalse(record.is_staticmethod)
        self.assertEqual(record.line_number, 1)

        record.line_number = 10
        self.assertEqual(record.line_number, 10)

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
        self.assertEqual(
            record.related_names,
            {"argument_1_related", "argument_1_related_2", "argument_2_related"},
        )
        self.assertTrue(record.is_classmethod)
        self.assertTrue(record.is_staticmethod)

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
        self.assertEqual(argument_1.type_hint.name, "arg1")
        self.assertEqual(argument_2.type_hint.name, "arg2[type, type2]")
        self.assertEqual(record.return_type_hint.name, "return")

        lines = [
            "",
            "",
            "line # type: (extra_arg, new_arg1[type, type2], new_arg2) -> new_return",
        ]
        record.parse_type_comments(lines)
        self.assertEqual(argument_1.type_hint.name, "new_arg1[type, type2]")
        self.assertEqual(argument_2.type_hint.name, "new_arg2")
        self.assertEqual(record.return_type_hint.name, "new_return")

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
        self.assertEqual(
            record.render(),
            "@my_deco@classmethoddef name(, ) -> :",
        )

        node.mock_add_spec(ast.AsyncFunctionDef)
        record = FunctionRecord(node, is_method=True)
        self.assertEqual(
            record.render(),
            "@my_deco@classmethodasync def name(, ) -> :",
        )
