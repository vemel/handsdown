import unittest

from mock import patch

from handsdown.module_record import ModuleRecord, ModuleObjectRecord


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


class TestModuleObjectRecord(unittest.TestCase):
    def setUp(self):
        self.record = ModuleObjectRecord(
            source_path="source_path",
            source_line_number="source_line_number",
            output_path="output_path",
            obj="obj",
            import_string="import_string",
            level="level",
            title="Title",
            docstring="docstring",
            is_class=False,
            is_related="is_related",
            module_record="module_record",
        )

    def test_init(self):
        self.assertEqual(repr(self.record), "<ModuleObjectRecord title=Title>")

    @patch("handsdown.module_record.ClassRepr")
    @patch("handsdown.module_record.FunctionRepr")
    def test_signature(self, FunctionReprMock, ClassReprMock):
        def my_func(_test):
            pass

        class MyClass:
            @property
            def my_prop(self):
                pass

            @my_prop.setter
            def my_prop(self):
                pass

            def my_method(self):
                pass

        FunctionReprMock().render.return_value = "rendered_function"
        ClassReprMock().render.return_value = "rendered_class"

        self.record.obj = my_func
        self.assertEqual(self.record.signature, "rendered_function")
        FunctionReprMock.assert_called_with(my_func)

        self.record.obj = MyClass.my_method
        self.assertEqual(self.record.signature, "rendered_function")
        FunctionReprMock.assert_called_with(MyClass.my_method)

        self.record.obj = MyClass.my_prop
        self.assertEqual(
            self.record.signature, "rendered_function\n\nrendered_function"
        )

        self.record.obj = MyClass
        self.record.is_class = True
        self.assertEqual(self.record.signature, "rendered_class")
        ClassReprMock.assert_called_with(MyClass)
