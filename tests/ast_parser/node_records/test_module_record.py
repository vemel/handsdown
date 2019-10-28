# pylint: disable=missing-docstring
import unittest
from unittest.mock import MagicMock, patch

import handsdown.ast_parser.smart_ast as ast
from handsdown.ast_parser.node_records.module_record import ModuleRecord


class TestFunctionRecord(unittest.TestCase):
    def test_init(self):
        node = MagicMock()
        node.name = "name"
        node.body = ["body"]
        node.mock_add_spec(ast.Module)
        record = ModuleRecord(node)
        self.assertEqual(record.name, "module")
        self.assertEqual(record.title, "")
        self.assertEqual(record.import_string.value, "")

    @patch("handsdown.ast_parser.node_records.module_record.ast.parse")
    def test_create_from_source(self, parse_mock):
        source_path = MagicMock()
        source_path.read_text.return_value = "line1\nline2"
        import_string = MagicMock()
        import_string.parts = ["my_dir", "my_module"]
        node = MagicMock()
        node.body = ["body"]
        node.mock_add_spec(ast.Module)
        parse_mock.return_value = node
        record = ModuleRecord.create_from_source(source_path, import_string)
        self.assertIsInstance(record, ModuleRecord)
        self.assertEqual(record.import_string, import_string)
        self.assertEqual(record.name, "my_module")
        self.assertEqual(record.title, "")
        self.assertEqual(record.source_path, source_path)
        self.assertEqual(record.source_lines, ["line1", "line2"])

    def test_find_record(self):
        node = MagicMock()
        node.name = "name"
        node.body = ["body"]
        node.mock_add_spec(ast.Module)
        record = ModuleRecord(node)
        record.import_string = "module_import"
        record.import_string_map = {"test": "test_object"}
        self.assertEqual(record.find_record("test"), "test_object")
        self.assertEqual(record.find_record("module_import"), record)
        self.assertIsNone(record.find_record("non_existing"))

    def test_iter_records(self):
        node = MagicMock()
        node.name = "name"
        node.body = ["body"]
        node.mock_add_spec(ast.Module)
        record = ModuleRecord(node)
        self.assertEqual(list(record.iter_records()), [])

        class_record = MagicMock()
        class_record.name = "class_record"
        class_record.iter_records.return_value = ["class_method"]
        private_class_record = MagicMock()
        private_class_record.name = "private_class_record"
        private_class_record.iter_records.return_value = ["private_class_method"]
        record.class_records = [class_record, private_class_record]
        function_record = MagicMock()
        function_record.name = "function_record"
        private_function_record = MagicMock()
        private_function_record.name = "private_function_record"
        record.function_records = [function_record, private_function_record]
        attribute_record = MagicMock()
        record.attribute_records = [attribute_record]
        self.assertEqual(
            list(record.iter_records()),
            [
                class_record,
                "class_method",
                private_class_record,
                "private_class_method",
                function_record,
                private_function_record,
            ],
        )

        record.all_names = ["class_record", "function_record"]
        self.assertEqual(
            list(record.iter_records()), [class_record, "class_method", function_record]
        )

    @patch("handsdown.ast_parser.node_records.module_record.ModuleAnalyzer")
    def test_build_children(self, ModuleAnalyzerMock):
        node = MagicMock()
        node.name = "name"
        node.body = ["body"]
        node.mock_add_spec(ast.Module)
        record = ModuleRecord(node)
        record.name = "class_node"
        class_node = MagicMock()
        class_node.name = "ClassNode"
        class_node.body = ["class_body"]
        class_node.decorator_list = []
        class_node.bases = []
        class_node.mock_add_spec(ast.ClassDef)
        function_node = MagicMock()
        function_node.decorator_list = []
        function_node.name = "function_node"
        function_node.body = ["function_body"]
        function_node.mock_add_spec(ast.FunctionDef)
        attribute_node = MagicMock()
        attribute_target = MagicMock()
        attribute_target.id = "attribute_target"
        attribute_target.mock_add_spec(ast.Name)
        attribute_node.targets = [attribute_target]
        attribute_node.value = "attribute_value"
        attribute_node.mock_add_spec(ast.Assign)
        import_node = MagicMock()
        import_name = MagicMock()
        import_name.name = "import_name"
        import_name_2 = MagicMock()
        import_name_2.name = "import_name_2"
        import_node.names = [import_name, import_name_2]
        import_node.mock_add_spec(ast.Import)
        ModuleAnalyzerMock().class_nodes = [class_node]
        ModuleAnalyzerMock().function_nodes = [function_node]
        ModuleAnalyzerMock().attribute_nodes = [attribute_node]
        ModuleAnalyzerMock().import_nodes = [import_node]
        self.assertIsNone(record.build_children())
        self.assertEqual(record.title, "ClassNode")
        self.assertEqual(record.class_records[0].node, class_node)
        self.assertEqual(record.function_records[0].node, function_node)
        self.assertEqual(record.attribute_records[0].node, attribute_node)
        self.assertEqual(record.import_records[0].node, import_node)
        self.assertEqual(record.import_records[0].name, "import_name")
        self.assertEqual(record.import_records[1].node, import_node)
        self.assertEqual(record.import_records[1].name, "import_name_2")
