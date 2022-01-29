# pylint: disable=missing-docstring
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from handsdown.generator import Generator, GeneratorError
from handsdown.utils.import_string import ImportString


class TestGenerator(unittest.TestCase):
    @patch("handsdown.generator.Loader")
    @patch("handsdown.generator.ModuleRecordList")
    @patch("handsdown.generator.MDDocument")
    @patch("handsdown.generator.PathFinder")
    def test_init(self, PathFinderMock, MDDocumentMock, ModuleRecordListMock, LoaderMock):
        source_path_mock = MagicMock()
        generator = Generator(
            project_name="test",
            input_path=Path("/input"),
            output_path=Path("/output"),
            source_paths=[source_path_mock],
        )
        self.assertIsInstance(generator, Generator)
        LoaderMock.assert_called_with(
            output_path=Path("/output"), root_path=Path("/input"), encoding="utf-8"
        )
        ModuleRecordListMock.assert_called_with()
        ModuleRecordListMock().add.assert_called_with(LoaderMock().get_module_record())
        PathFinderMock.assert_called_with(Path("/output"))
        MDDocumentMock.assert_called_with(Path("/output/MODULES.md"), encoding="utf-8")

    @patch("handsdown.generator.Loader")
    @patch("handsdown.generator.ModuleRecordList")
    @patch("handsdown.generator.MDDocument")
    @patch("handsdown.generator.PathFinder")
    def test_generate_docs(self, PathFinderMock, MDDocumentMock, ModuleRecordListMock, LoaderMock):
        source_path_mock = MagicMock()
        generator = Generator(
            project_name="test",
            input_path=Path("/input"),
            output_path=Path("/output"),
            source_paths=[source_path_mock],
        )

        MDDocumentMock().render_md_doc_link.return_value = "md_doc_link"
        MDDocumentMock().render_doc_link.return_value = "doc_link"

        module_record_mock = MagicMock()
        module_record_mock.title = "Title"
        module_record_mock.docstring = "Docstring"
        module_record_mock.import_string = ImportString("my.import.string")
        ModuleRecordListMock().__iter__ = MagicMock(return_value=iter([module_record_mock]))

        generator.generate_docs()

        LoaderMock.assert_called_with(
            output_path=Path("/output"), root_path=Path("/input"), encoding="utf-8"
        )
        PathFinderMock.assert_called_with(Path("/output"))

    @patch("handsdown.generator.Loader")
    @patch("handsdown.generator.ModuleRecordList")
    @patch("handsdown.generator.MDDocument")
    @patch("handsdown.generator.PathFinder")
    def test_generate_doc(self, PathFinderMock, MDDocumentMock, ModuleRecordListMock, LoaderMock):
        source_path_mock = MagicMock()
        generator = Generator(
            project_name="test",
            input_path=Path("/input"),
            output_path=Path("/output"),
            source_paths=[source_path_mock],
            raise_errors=True,
        )

        MDDocumentMock().render_md_doc_link.return_value = "md_doc_link"
        MDDocumentMock().render_doc_link.return_value = "doc_link"

        module_record_mock = MagicMock()
        module_record_mock.title = "Title"
        module_record_mock.docstring = "Docstring"
        module_record_mock.source_path = Path("/input/source.py")
        module_record_mock.import_string = ImportString("my.import.string")

        module_record_mock2 = MagicMock()
        module_record_mock2.title = "Title"
        module_record_mock2.docstring = "Docstring"
        module_record_mock2.source_path = Path("/input/source2.py")
        module_record_mock2.import_string = ImportString("my.import.string2")

        ModuleRecordListMock().__iter__ = MagicMock(
            return_value=iter([module_record_mock, module_record_mock2])
        )

        generator.generate_doc(Path("/input/source2.py"))

        LoaderMock.assert_called_with(
            output_path=Path("/output"), root_path=Path("/input"), encoding="utf-8"
        )
        PathFinderMock.assert_called_with(Path("/output"))

        ModuleRecordListMock().__iter__ = MagicMock(return_value=iter([module_record_mock]))
        with self.assertRaises(GeneratorError):
            generator.generate_doc(Path("/input/source2.py"))

        LoaderMock().parse_module_record.side_effect = ValueError("loader_error")
        ModuleRecordListMock().__iter__ = MagicMock(return_value=iter([module_record_mock2]))
        with self.assertRaises(ValueError):
            generator.generate_doc(Path("/input/source2.py"))

    @patch("handsdown.generator.Loader")
    @patch("handsdown.generator.ModuleRecordList")
    @patch("handsdown.generator.MDDocument")
    @patch("handsdown.generator.PathFinder")
    def test_cleanup_old_docs(
        self, PathFinderMock, _MDDocumentMock, _ModuleRecordListMock, _LoaderMock
    ):
        doc_path_mock = MagicMock()
        doc_path_mock.read_text.return_value = "> Auto-generated documentation"
        other_path_mock = MagicMock()
        other_path_mock.read_text.return_value = "other file"
        PathFinderMock().glob.return_value = [doc_path_mock, other_path_mock]
        generator = Generator(
            project_name="test",
            input_path=Path("/input"),
            output_path=Path("/output"),
            source_paths=[],
        )
        generator.cleanup_old_docs()
        PathFinderMock.assert_called_with(Path("/output"))
        PathFinderMock().glob.assert_called_with("**/*.md")
        doc_path_mock.unlink.assert_called_with()
