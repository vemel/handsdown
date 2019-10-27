"""
Loader for python source code.
"""

from typing import Optional, Text, TYPE_CHECKING

from handsdown.ast_parser.node_records.module_record import ModuleRecord
from handsdown.utils import extract_md_title
from handsdown.utils.path_finder import PathFinder
from handsdown.utils.logger import get_logger
from handsdown.utils.import_string import ImportString

if TYPE_CHECKING:  # pragma: no cover
    import logging
    from pathlib import Path


class LoaderError(Exception):
    """
    Main error for `Loader` class.
    """


class Loader:
    """
    Loader for python source code.

    Examples::

        loader = Loader(Path('path/to/my_module/'))
        my_module_utils = loader.import_module('my_module.utils')

    Arguments:
        root_path -- Root path of the project.
        output_path -- Docs output path.
    """

    def __init__(self, root_path, output_path):
        # type: (Path, Path) -> None
        self._logger = get_logger()
        self._root_path = root_path
        self._root_path_finder = PathFinder(self._root_path)
        self._output_path = output_path

    def get_output_path(self, source_path):
        # type: (Path) -> Path
        """
        Get output MD document path based on `source_path`.

        Arguments:
            source_path -- Path to source code file.

        Returns:
            A path to the output `.md` file even if it does not exist yet.
        """
        relative_source_path = self._root_path_finder.relative(source_path)
        if relative_source_path.stem == "__init__":
            relative_source_path = relative_source_path.parent / "index"
        if relative_source_path.stem == "__main__":
            relative_source_path = relative_source_path.parent / "module"

        file_name = "{}.md".format(relative_source_path.stem)
        relative_output_path = relative_source_path.parent / file_name
        return self._output_path / relative_output_path

    def get_module_record(self, source_path):
        # type: (Path) -> Optional[ModuleRecord]
        """
        Build `ModuleRecord` for given `source_path`.

        Arguments:
            source_path -- Absolute path to source file.

        Returns:
            A new `ModuleRecord` instance or None if there is ntohing to import.

        Raises:
            LoaderError -- If python source cannot be loaded.
        """
        if not (source_path.parent / "__init__.py").exists():
            return None

        if source_path.name == "__init__.py" and source_path.parent == self._root_path:
            return None

        import_string = self.get_import_string(source_path)
        docstring_parts = []

        try:
            module_record = ModuleRecord(source_path, ImportString(import_string))
            module_record.build_children()
        except Exception as e:
            raise LoaderError(
                "{} while loading {}: {}".format(e.__class__.__name__, source_path, e)
            )

        if module_record.docstring:
            docstring_parts.append(module_record.docstring)

        if source_path.name == "__init__.py":
            readme_md_path = source_path.parent / "README.md"
            if readme_md_path.exists():
                docstring_parts.append(readme_md_path.read_text())

        docstring = "\n\n".join(docstring_parts)
        title, docstring = extract_md_title(docstring)
        if title:
            module_record.title = title
        module_record.docstring = docstring

        return module_record

    @staticmethod
    def parse_module_record(module_record):
        # type: (ModuleRecord) -> None
        """
        Parse `ModuleRecord` children and fully load a tree for it.

        Raises:
            LoaderError -- If python source cannot be parsed.
        """
        try:
            module_record.parse()
        except Exception as e:
            raise LoaderError(
                "{} while parsing {}: {}".format(
                    e.__class__.__name__, module_record.source_path, e
                )
            )

    def get_import_string(self, source_path):
        # type: (Path) -> Text
        """
        Get Python import string for a source `source_path` relative to `root_path`.

        Examples::

            loader = Loader(root_path=Path("/root"), ...)
            loader.get_import_string('/root/my_module/test.py')
            'my_module.test'

            loader.get_import_string('/root/my_module/__init__.py')
            'my_module'

        Arguments:
            source_path -- Path to a source file.

        Returns:
            A Python import string.
        """
        relative_path = source_path.relative_to(self._root_path)
        name_parts = []
        for part in relative_path.parts:
            stem = part.split(".")[0]
            if stem == "__init__":
                continue
            name_parts.append(stem)

        return ".".join(name_parts)
