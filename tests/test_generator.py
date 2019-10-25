# pylint: disable=missing-docstring
import unittest
from unittest.mock import patch, MagicMock
from pathlib import Path

from handsdown.generator import Generator


class TestGenerator(unittest.TestCase):
    @patch("handsdown.generator.Loader")
    @patch("handsdown.generator.ModuleRecordList")
    @patch("handsdown.generator.MDDocument")
    @patch("handsdown.generator.PathFinder")
    def test_init(
        self, PathFinderMock, MDDocumentMock, ModuleRecordListMock, LoaderMock
    ):
        source_path_mock = MagicMock()
        generator = Generator(
            project_name="test",
            input_path=Path("/input"),
            output_path=Path("/output"),
            source_paths=[source_path_mock],
        )
        self.assertIsInstance(generator, Generator)
        LoaderMock.assert_called_with(
            output_path=Path("/output"), root_path=Path("/input")
        )
        ModuleRecordListMock.assert_called_with()
        ModuleRecordListMock().add.assert_called_with(LoaderMock().get_module_record())
        PathFinderMock.assert_called_with(Path("/output"))
        MDDocumentMock.assert_called_with(Path("/output/MODULES.md"))

    @patch("handsdown.generator.Loader")
    @patch("handsdown.generator.ModuleRecordList")
    @patch("handsdown.generator.MDDocument")
    @patch("handsdown.generator.PathFinder")
    def test_generate_docs(
        self, PathFinderMock, MDDocumentMock, ModuleRecordListMock, LoaderMock
    ):
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
        module_record_mock.import_string = "my.import.string"
        ModuleRecordListMock().__iter__ = MagicMock(
            return_value=iter([module_record_mock])
        )

        generator.generate_docs()

        LoaderMock.assert_called_with(
            output_path=Path("/output"), root_path=Path("/input")
        )
        PathFinderMock.assert_called_with(Path("/output"))

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
