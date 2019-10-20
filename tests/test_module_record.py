import unittest

from handsdown.module_record import ModuleRecord


class TestModuleRecord(unittest.TestCase):
    def setUp(self):
        self.module_record = ModuleRecord(
            source_path="source_path",
            output_path="output_path",
            module="module",
            title="Title",
            import_string="my_module.utils.parsers",
            objects=[],
            docstring="my docstring",
        )

    def test_init(self):
        self.assertEqual(self.module_record.docstring, "my docstring")
        self.assertEqual(repr(self.module_record), "<ModuleRecord title=Title>")

    def test_get_import_string_parts(self):
        self.assertEqual(
            self.module_record.get_import_string_parts(),
            ["my_module", "utils", "parsers"],
        )

        self.module_record.import_string = "my_module.__main__"
        self.assertEqual(
            self.module_record.get_import_string_parts(), ["my_module", "__main__"]
        )

        self.module_record.import_string = "my_module.my_lib"
        self.assertEqual(
            self.module_record.get_import_string_parts(), ["my_module", "my_lib"]
        )

    def test_get_title_parts(self):
        self.module_record.title = ""
        self.assertEqual(
            self.module_record.get_title_parts(), ["My Module", "Utils", "Parsers"]
        )

        self.module_record.import_string = "my_module.__main__"
        self.assertEqual(self.module_record.get_title_parts(), ["My Module", "Main"])

        self.module_record.import_string = "my_module.my_lib"
        self.module_record.title = "MyLibrary"
        self.assertEqual(
            self.module_record.get_title_parts(), ["My Module", "MyLibrary"]
        )

    def test_get_reference_objects(self):
        self.assertEqual(self.module_record.get_reference_objects(), [])
