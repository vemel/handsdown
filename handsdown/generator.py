"""
Main handsdown documentation generator.
"""
import re
from pathlib import Path
from typing import Iterable, List, Optional

from handsdown.ast_parser.module_record_list import ModuleRecordList
from handsdown.ast_parser.node_records.attribute_record import AttributeRecord
from handsdown.ast_parser.node_records.module_record import ModuleRecord
from handsdown.ast_parser.node_records.node_record import NodeRecord
from handsdown.jinja_manager import JinjaManager
from handsdown.loader import Loader, LoaderError
from handsdown.md_document import MDDocument
from handsdown.processors.base import BaseDocstringProcessor
from handsdown.processors.smart import SmartDocstringProcessor
from handsdown.settings import ENCODING
from handsdown.utils import make_title
from handsdown.utils.import_string import ImportString
from handsdown.utils.logger import get_logger
from handsdown.utils.markdown import insert_md_toc
from handsdown.utils.nice_path import NicePath
from handsdown.utils.path_finder import PathFinder


class GeneratorError(Exception):
    """
    Main error for `Generator`.
    """


class Generator:
    """
    Main documentation generator.

    Arguments:
        project_name -- Name of the project.
        input_path -- Path to repo to generate docs.
        output_path -- Path to folder with auto-generated docs to output.
        source_paths -- List of paths to source files for generation.
        docstring_processor -- Docstring converter to Markdown.
        loader -- Loader for python modules.
        raise_errors -- Raise `LoaderError` instead of silencing in.
        source_code_url -- URL to source files to use instead of relative paths,
            useful for [GitHub Pages](https://pages.github.com/).
        source_code_path -- Path to local source code
        toc_depth -- Maximum depth of child modules ToC
        encoding -- File encoding
    """

    # Name of logger
    LOGGER_NAME = "handsdown"

    # Docs index filename
    INDEX_NAME = "README.md"

    # Docs index title
    INDEX_TITLE = "Index"

    # Docs modules filename
    MODULES_NAME = "MODULES.md"

    # Docs modules title
    MODULES_TITLE = "Modules"

    _short_link_re = re.compile(r"`+[A-Za-z]\S+`+")

    def __init__(
        self,
        input_path: Path,
        output_path: Path,
        source_paths: Iterable[Path],
        project_name: Optional[str] = None,
        docstring_processor: Optional[BaseDocstringProcessor] = None,
        loader: Optional[Loader] = None,
        raise_errors: bool = False,
        source_code_url: Optional[str] = None,
        source_code_path: Optional[Path] = None,
        toc_depth: int = 1,
        encoding: str = ENCODING,
    ) -> None:
        self._logger = get_logger()
        self._root_path = input_path
        self._output_path = output_path
        self._project_name = project_name or make_title(input_path.name)
        self._root_path_finder = PathFinder(self._root_path)
        self._source_code_url = source_code_url
        self._source_code_path: Path = source_code_path or Path()
        self._toc_depth = toc_depth
        self._raise_errors = raise_errors
        self._encoding = encoding
        self._jinja_manager = JinjaManager()

        # create output folder if it does not exist
        if not self._output_path.exists():
            self._logger.info(f"Creating folder {self._output_path.as_posix()}")
            PathFinder(self._output_path).mkdir()

        self._loader = loader or Loader(
            root_path=self._root_path,
            output_path=self._output_path,
            encoding=self._encoding,
        )
        self._docstring_processor = docstring_processor or SmartDocstringProcessor()

        self._source_paths = sorted(source_paths)
        self._logger.debug(f"Generating source map for {len(self._source_paths)} source files")
        self.module_records = self._build_module_record_list()
        self._logger.debug("Source map generated")

        package_names = self.module_records.get_package_names()
        package_names_re_expr = "|".join(package_names)
        self._docstring_links_re = re.compile(rf"`+(?:{package_names_re_expr})\.\S+`+")
        self._prepare_index()

    def _prepare_index(self) -> None:
        self.md_index = MDDocument(self._output_path / self.INDEX_NAME, encoding=self._encoding)
        self.md_modules = MDDocument(self._output_path / self.MODULES_NAME, encoding=self._encoding)

        # copy `README.md` content from root dir if it exists
        readme_path = self._root_path / "README.md"
        if readme_path.exists():
            self.md_index.read(readme_path)

        if not self.md_index.title:
            self.md_index.title = f"{self._project_name} {self.INDEX_TITLE}"

        # copy `MODULES.md` content from root dir if it exists
        modules_path = self._root_path / "MODULES.md"
        if modules_path.exists():
            self.md_modules.read(modules_path)

        if not self.md_modules.title:
            self.md_modules.title = f"{self._project_name} {self.MODULES_TITLE}"

    def _build_module_record_list(self) -> ModuleRecordList:
        module_record_list = ModuleRecordList()
        for source_path in self._source_paths:
            module_record = None
            try:
                module_record = self._loader.get_module_record(source_path)
            except LoaderError as e:
                if self._raise_errors:
                    raise

                self._logger.warning(f"Skipping: {e}")
                continue
            if module_record:
                if not module_record.title:
                    module_record.title = make_title(module_record.name)
                module_record_list.add(module_record)

        return module_record_list

    def cleanup_old_docs(self) -> None:
        """
        Remove old docs generated for this module.
        """
        self._logger.debug("Removing orphaned docs")
        preserve_paths = {i.output_path for i in self.module_records}
        orphaned_dirs = []
        preserve_paths.add(self.md_index.path)
        preserve_paths.add(self.md_modules.path)

        for doc_path in PathFinder(self._output_path).glob("**/*.md"):
            if doc_path in preserve_paths:
                continue

            file_content = doc_path.read_text()
            is_autogenerated = "> Auto-generated documentation" in file_content
            if not is_autogenerated:
                continue

            self._logger.info(f"Deleting orphaned doc file {NicePath(doc_path)}")
            doc_path.unlink()

            # remove parent directory if it is empty
            children = list(doc_path.parent.iterdir())
            if not children:
                orphaned_dirs.append(doc_path.parent)

        for orphaned_dir in orphaned_dirs:
            self._logger.info(f"Deleting orphaned directory {NicePath(orphaned_dir)}")
            orphaned_dir.rmdir()

    def generate_doc(self, source_path: Path) -> None:
        """
        Generate one module doc at once.

        Arguments:
            source_path -- Path to source file.

        Raises:
            GeneratorError -- If `source_path` not found in current repo.
        """
        for module_record in self.module_records:
            if module_record.source_path != source_path:
                continue

            md_document = MDDocument(module_record.output_path, encoding=self._encoding)
            self._generate_doc(module_record, md_document)

            return

        raise GeneratorError(f"Record not found for {NicePath(source_path)}")

    def _get_source_code_url(self, module_record: ModuleRecord, md_document: MDDocument) -> str:
        if not self._source_code_url:
            relative_path = md_document.path_finder.relative(module_record.source_path)
            return (self._source_code_path / relative_path).as_posix()

        relative_path_str = self._root_path_finder.relative(module_record.source_path).as_posix()
        return f"{self._source_code_url}{relative_path_str}"

    def _generate_doc(self, module_record: ModuleRecord, md_document: MDDocument) -> None:
        self._logger.debug(
            f"Generating doc {NicePath(md_document.path)} for {NicePath(module_record.source_path)}"
        )
        try:
            self._loader.parse_module_record(module_record)
        except LoaderError as e:
            if self._raise_errors:
                raise

            self._logger.warning(f"Skipping: {e}")
            return

        md_document.source_code_url = self._get_source_code_url(module_record, md_document)

        content = self._jinja_manager.render(
            template_path=Path("mkdocs") / "module.md.jinja2",
            module_record=module_record,
            md_document=md_document,
            docstring_processor=self._docstring_processor,
            generator=self,
        )
        content = insert_md_toc(content, self._toc_depth)
        if NicePath(md_document.path).write_changed(content, encoding=self._encoding):
            self._logger.info(
                f"Updated doc {NicePath(md_document.path)} for"
                f" {NicePath(module_record.source_path)}"
            )

    def generate_docs(self) -> None:
        """
        Generate all doc files at once.
        """
        self._logger.debug(
            f"Generating docs for {self._project_name} to {NicePath(self._output_path)}"
        )

        for module_record in self.module_records:
            md_document = MDDocument(module_record.output_path, encoding=self._encoding)
            self._generate_doc(module_record, md_document)

    def generate_index(self) -> None:
        """
        Generate `<output>/README.md` file with title from `<root>/README.md`.

        Also `Modules` section that contains a Tree of all modules in the project.
        """
        self._logger.debug(f"Generating {NicePath(self.md_index.path)}")
        with self.md_index as md_index:
            if not md_index.title:
                md_index.title = f"{self._project_name} {self.INDEX_TITLE}"

            autogenerated_marker = "> Auto-generated documentation index."
            modules_link = md_index.render_md_doc_link(self.md_modules, title=self.MODULES_TITLE)
            modules_section = (
                f"Full {self._project_name} project documentation can be found in {modules_link}"
            )
            subtitle_parts = [autogenerated_marker]
            if md_index.subtitle:
                subtitle_parts.append(md_index.subtitle)
            subtitle_parts.append(modules_section)
            md_index.subtitle = "\n\n".join(subtitle_parts)

            md_index.add_toc_if_not_exists()
            md_modules_link = md_index.render_md_doc_link(self.md_modules)
            md_index.toc_section = f"{md_index.toc_section}\n  - {md_modules_link}"

    def generate_modules(self) -> None:
        """
        Generate `<output>/README.md` file.

        Title from `<root>/README.md` and `Modules`
        section that contains a Tree of all modules in the project.
        """
        self._logger.debug(f"Generating {NicePath(self.md_modules.path)}")
        with self.md_modules as md_modules:
            if not md_modules.title:
                md_modules.title = f"{self._project_name} {self.MODULES_TITLE}"

            autogenerated_marker = "> Auto-generated documentation modules index."
            subtitle_parts = [autogenerated_marker]
            if md_modules.subtitle:
                subtitle_parts.append(md_modules.subtitle)

            modules_link = md_modules.render_md_doc_link(self.md_index, title=self._project_name)
            subtitle_parts.append(f"Full list of {modules_link} project modules.")
            md_modules.subtitle = "\n\n".join(subtitle_parts)

            modules_toc_lines = self._build_modules_toc_lines(
                import_string=ImportString(""),
                max_depth=10,
                md_document=md_modules,
                start_level=1,
            )

            md_doc_link = md_modules.render_md_doc_link(self.md_index)
            modules_toc_lines.insert(0, md_modules.get_toc_line(md_doc_link, level=0))

            md_modules.toc_section = "\n".join(modules_toc_lines)

    def _replace_links(
        self,
        module_record: ModuleRecord,
        record: NodeRecord,
        md_document: MDDocument,
        docstring: str,
    ) -> str:
        parent_import_string = None
        if not record.import_string.is_top_level():
            parent_import_string = record.import_string.parent

        for match in self._short_link_re.findall(docstring):
            related_record_name = match.replace("`", "")
            related_import_string = None
            related_record = None
            target_path = md_document.path

            # find record in parent
            if parent_import_string:
                related_import_string = parent_import_string + related_record_name
                if related_import_string != record.import_string:
                    related_record = module_record.find_record(related_import_string)

            # find record in module
            if not related_record:
                related_import_string = module_record.import_string + related_record_name
                related_record = module_record.find_record(related_import_string)

            # find record globally
            if not related_record:
                related_import_string = ImportString(related_record_name)
                related_module_record = self.module_records.find_module_record(
                    related_import_string
                )
                if related_module_record:
                    related_record = related_module_record.find_record(related_import_string)
                    target_path = related_module_record.output_path

            if not related_record:
                continue

            if related_record.import_string.startswith(record.import_string):
                continue

            title = related_record.title
            anchor = md_document.get_anchor(related_record.title)
            if isinstance(related_record, AttributeRecord):
                parent_related_record = module_record.find_record(
                    related_record.import_string.parent
                )
                if parent_related_record:
                    anchor = md_document.get_anchor(parent_related_record.title)

            link = md_document.render_doc_link(title, anchor=anchor, target_path=target_path)
            docstring = docstring.replace(match, link)
            self._logger.debug(f"Adding local link '{title}' to '{record.title}'")
        return docstring

    def get_see_also_links(
        self,
        record: NodeRecord,
        module_record: ModuleRecord,
        md_document: MDDocument,
    ) -> List[str]:
        """
        Get links to other modules that are referenced in the docstring.
        """

        related_import_strings = module_record.get_related_import_strings(record)
        links = set()
        for import_string in related_import_strings:
            related_module_record = self.module_records.find_module_record(import_string)
            if not related_module_record:
                continue

            related_record = related_module_record.find_record(import_string)
            if not related_record:
                continue

            if related_record is record:
                continue

            title = related_record.title
            link = md_document.render_doc_link(
                title,
                target_path=related_module_record.output_path,
                anchor=md_document.get_anchor(title),
            )
            links.add(link)

        return sorted(links)

    def _build_modules_toc_lines(
        self, import_string: ImportString, max_depth: int, md_document: MDDocument, start_level: int
    ) -> List[str]:
        lines: List[str] = []
        parts = import_string.parts

        last_import_string_parts: List[str] = []
        for module_record in self.module_records:
            if module_record.import_string == import_string:
                continue

            if import_string and not module_record.import_string.startswith(import_string):
                continue

            import_string_parts = module_record.import_string.parts
            if len(import_string_parts) > len(parts) + max_depth:
                continue

            for index, import_string_part in enumerate(import_string_parts[:-1]):
                if index < len(parts):
                    continue

                if (
                    len(last_import_string_parts) > index
                    and last_import_string_parts[index] == import_string_parts[index]
                ):
                    continue

                title = make_title(import_string_part)
                toc_line = md_document.get_toc_line(title, level=index - len(parts) + start_level)
                lines.append(toc_line)

            last_import_string_parts = import_string_parts
            link = md_document.render_doc_link(
                title=module_record.title,
                target_path=module_record.output_path,
                anchor=md_document.get_anchor(module_record.title),
            )
            toc_line = md_document.get_toc_line(
                link, level=len(import_string_parts) - len(parts) - 1 + start_level
            )
            lines.append(toc_line)
        return lines
