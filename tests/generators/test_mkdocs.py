import shutil
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import MagicMock, patch

import pytest

from handsdown.generators.base import GeneratorError
from handsdown.generators.rtd import RTDGenerator
from handsdown.utils.import_string import ImportString


class TestGenerator:
    input_path: Path
    output_path: Path

    @pytest.fixture(autouse=True)
    def _tmp_path(self):
        self.input_path = Path("/input")
        self.output_path = Path(TemporaryDirectory().name)
        self.output_path.mkdir(exist_ok=True, parents=True)
        yield
        shutil.rmtree(self.output_path, ignore_errors=True)

    @patch("handsdown.generators.base.Loader")
    @patch("handsdown.generators.base.ModuleRecordList")
    @patch("handsdown.generators.base.MDDocument")
    @patch("handsdown.generators.base.PathFinder")
    def test_init(self, PathFinderMock, MDDocumentMock, ModuleRecordListMock, LoaderMock):
        source_path_mock = MagicMock()
        generator = RTDGenerator(
            project_name="test",
            input_path=self.input_path,
            output_path=self.output_path,
            source_paths=[source_path_mock],
        )
        assert isinstance(generator, RTDGenerator)
        LoaderMock.assert_called_with(
            output_path=self.output_path, root_path=self.input_path, encoding="utf-8"
        )
        ModuleRecordListMock.assert_called_with()
        ModuleRecordListMock().add.assert_called_with(LoaderMock().get_module_record())
        PathFinderMock.assert_called()
        MDDocumentMock.assert_called_with(self.output_path / "README.md", encoding="utf-8")

    @patch("handsdown.generators.base.Loader")
    @patch("handsdown.generators.base.ModuleRecordList")
    @patch("handsdown.generators.base.MDDocument")
    @patch("handsdown.generators.base.PathFinder")
    def test_generate_docs(self, PathFinderMock, MDDocumentMock, ModuleRecordListMock, LoaderMock):
        source_path_mock = MagicMock()
        generator = RTDGenerator(
            project_name="test",
            input_path=self.input_path,
            output_path=self.output_path,
            source_paths=[self.input_path / "source.py"],
        )

        MDDocumentMock().render_doc_link.return_value = "doc_link"
        MDDocumentMock().path_finder.relative.return_value = Path("test")
        MDDocumentMock().path = self.output_path / "test.md"

        module_record_mock = MagicMock()
        module_record_mock.title = "Title"
        module_record_mock.docstring = "Docstring"
        module_record_mock.source_path = self.input_path / "source.py"
        module_record_mock.import_string = ImportString("my.import.string")
        ModuleRecordListMock().__iter__ = MagicMock(return_value=iter([module_record_mock]))

        generator.generate_docs()

        LoaderMock.assert_called_with(
            output_path=self.output_path, root_path=self.input_path, encoding="utf-8"
        )
        PathFinderMock.assert_called()

    @patch("handsdown.generators.base.Loader")
    @patch("handsdown.generators.base.ModuleRecordList")
    @patch("handsdown.generators.base.MDDocument")
    @patch("handsdown.generators.base.PathFinder")
    def test_generate_doc(self, PathFinderMock, MDDocumentMock, ModuleRecordListMock, LoaderMock):
        source_path_mock = MagicMock()
        generator = RTDGenerator(
            project_name="test",
            input_path=self.input_path,
            output_path=self.output_path,
            source_paths=[source_path_mock],
            raise_errors=True,
        )

        MDDocumentMock().render_doc_link.return_value = "doc_link"
        MDDocumentMock().path_finder.relative.return_value = Path("test")
        MDDocumentMock().path = self.output_path / "test.md"

        module_record_mock = MagicMock()
        module_record_mock.title = "Title"
        module_record_mock.docstring = "Docstring"
        module_record_mock.source_path = self.input_path / "source.py"
        module_record_mock.import_string = ImportString("my.import.string")

        module_record_mock2 = MagicMock()
        module_record_mock2.title = "Title"
        module_record_mock2.docstring = "Docstring"
        module_record_mock2.source_path = self.input_path / "source2.py"
        module_record_mock2.import_string = ImportString("my.import.string2")

        ModuleRecordListMock().__iter__ = MagicMock(
            return_value=iter([module_record_mock, module_record_mock2])
        )

        generator.generate_doc(self.input_path / "source2.py")

        LoaderMock.assert_called_with(
            output_path=self.output_path, root_path=self.input_path, encoding="utf-8"
        )
        PathFinderMock.assert_called()

        ModuleRecordListMock().__iter__ = MagicMock(return_value=iter([module_record_mock]))
        with pytest.raises(GeneratorError):
            generator.generate_doc(self.input_path / "source2.py")

        LoaderMock().parse_module_record.side_effect = ValueError("loader_error")
        ModuleRecordListMock().__iter__ = MagicMock(return_value=iter([module_record_mock2]))
        with pytest.raises(ValueError):
            generator.generate_doc(self.input_path / "source2.py")

    def test_cleanup_old_docs(self):
        (self.output_path / "auto.md").write_text("> Auto-generated documentation")
        (self.output_path / "manual.md").write_text("other file")
        generator = RTDGenerator(
            project_name="test",
            input_path=self.input_path,
            output_path=self.output_path,
            source_paths=[],
        )
        generator.cleanup_old_docs()
        assert list(self.output_path.glob("*")) == [self.output_path / "manual.md"]
