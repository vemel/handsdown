import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import MagicMock, patch

import pytest

import handsdown.ast_parser.smart_ast as ast
from handsdown.ast_parser.node_records.module_record import ModuleRecord
from handsdown.utils.import_string import ImportString
from handsdown.utils.nice_path import NicePath


class TestFunctionRecord:
    source_path: NicePath

    @pytest.fixture
    def set_source_path(self):
        self.source_path = NicePath(TemporaryDirectory().name)
        self.source_path.mkdir(exist_ok=True, parents=True)
        yield
        self.source_path.rmtree()

    def test_init(self):
        node = MagicMock()
        node.name = "name"
        node.body = ["body"]
        node.mock_add_spec(ast.Module)
        record = ModuleRecord(node)
        assert record.name == "module"
        assert record.title == ""
        assert record.import_string.value == ""

    def test_create_from_source(self, set_source_path):
        source_path = self.source_path / "path.py"
        source_path.write_text("a = 5\nb = 7")
        import_string = ImportString("my_dir.my_module")
        record = ModuleRecord.create_from_source(source_path, import_string)
        assert isinstance(record, ModuleRecord)
        assert record.import_string == import_string
        assert record.name == "my_module"
        assert record.title == ""
        assert record.source_path == source_path
        assert record.source_lines == ["a = 5", "b = 7"]

    def test_find_record(self):
        node = MagicMock()
        node.name = "name"
        node.body = ["body"]
        node.mock_add_spec(ast.Module)
        record = ModuleRecord(node)
        record.import_string = "module_import"
        record.import_string_map = {"test": "test_object"}
        assert record.find_record("test") == "test_object"
        assert record.find_record("module_import") == record
        assert record.find_record("non_existing") is None

    def test_iter_records(self):
        node = MagicMock()
        node.name = "name"
        node.body = ["body"]
        node.mock_add_spec(ast.Module)
        record = ModuleRecord(node)
        assert list(record.iter_records()) == []

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
        assert list(record.iter_records()) == [
            class_record,
            private_class_record,
            function_record,
            private_function_record,
        ]

        record.all_names = ["class_record", "function_record"]
        assert list(record.iter_records()) == [class_record, function_record]

    @patch("handsdown.ast_parser.node_records.module_record.ModuleAnalyzer")
    def test_build_children(self, ModuleAnalyzerMock):
        node = MagicMock()
        node.name = "name"
        node.body = ["body"]
        node.mock_add_spec(ast.Module)
        record = ModuleRecord(node)
        record.import_string = ImportString("my_module")
        record.name = "class_node"
        class_node = MagicMock()
        class_node.name = "ClassNode"
        method_node = MagicMock()
        method_node.name = "class_method"
        method_node.body = ["class_method"]
        method_node.mock_add_spec(ast.FunctionDef)
        class_node.body = [method_node]
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
        assert record.build_children() is None
        assert record.title == "ClassNode"
        assert record.class_records[0].node == class_node
        assert record.function_records[0].node == function_node
        assert record.attribute_records[0].node == attribute_node
        assert record.import_records[0].node == import_node
        assert record.import_records[0].name == "import_name"
        assert record.import_records[1].node == import_node
        assert record.import_records[1].name == "import_name_2"
        assert record.class_records[0].import_string.value == "my_module.ClassNode"
        assert (
            record.class_records[0].method_records[0].import_string.value
            == "my_module.ClassNode.class_method"
        )
        assert record.function_records[0].import_string.value == "my_module.function_node"

    def test_parse(self):
        node = MagicMock()
        node.name = "name"
        node.body = ["body"]
        node.mock_add_spec(ast.Module)
        record = ModuleRecord(node)

        record.source_lines = [
            "# attribute docstring",
            "# attribute docstring 2",
            "# FIXME: ingored",
            "",
            "function_line 1",
            "function_line 2",
            "function body line",
        ]

        attribute_record = MagicMock()
        attribute_record.node.mock_add_spec(ast.Assign)
        attribute_record.node.lineno = 4
        record.attribute_records = [attribute_record]

        method_record = MagicMock()
        method_record.name = "method_record"
        method_record.node.mock_add_spec(ast.FunctionDef)
        method_record_body = MagicMock()
        method_record_body.lineno = 999
        method_record.node.body = [method_record_body]
        method_record.is_classmethod = False
        method_record.is_staticmethod = False
        static_method_record = MagicMock()
        static_method_record.name = "static_method_record"
        static_method_record_body = MagicMock()
        static_method_record_body.lineno = 999
        static_method_record.node.body = [static_method_record_body]
        static_method_record.node.mock_add_spec(ast.FunctionDef)
        static_method_record.is_classmethod = True
        static_method_record.is_staticmethod = False

        class_record = MagicMock()
        class_record.name = "class_record"
        class_record.node.mock_add_spec(ast.ClassDef)
        class_attribute_record = MagicMock()
        class_attribute_record.node.mock_add_spec(ast.Assign)
        class_attribute_record.node.lineno = 999
        class_record.attribute_records = [class_attribute_record]
        class_record.method_records = [method_record, static_method_record]
        record.class_records = [class_record]

        function_record = MagicMock()
        function_record.line_number = 5
        body_mock = MagicMock()
        body_mock.lineno = 7
        function_record.node.body = [body_mock]
        function_record.node.lineno = 7
        function_record.node.mock_add_spec(ast.FunctionDef)
        record.function_records = [function_record]

        assert record.parse() is None
        assert attribute_record.docstring == "attribute docstring\n  attribute docstring 2"
        assert class_attribute_record.docstring == ""

        assert method_record.title == "class_record().method_record"
        assert static_method_record.title == "class_record.static_method_record"

        function_record.parse_type_comments.assert_called_once_with(
            ["function_line 1", "function_line 2"]
        )

    def test_render(self):
        node = MagicMock()
        node.name = "name"
        node.body = ["body"]
        node.mock_add_spec(ast.Module)
        record = ModuleRecord(node)
        record.parse()
        record.class_records = ["class_record"]
        record.function_records = ["function_record"]
        record.import_records = ["import_record"]

        assert record.render() == "module module"
