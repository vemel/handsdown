"""
Main handsdown documentation generator.
"""
import re
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

from handsdown.ast_parser.module_record_list import ModuleRecordList
from handsdown.ast_parser.node_records.attribute_record import AttributeRecord
from handsdown.ast_parser.node_records.module_record import ModuleRecord
from handsdown.ast_parser.node_records.node_record import NodeRecord
from handsdown.constants import ENCODING
from handsdown.exceptions import GeneratorError, LoaderError
from handsdown.jinja_manager import JinjaManager
from handsdown.loader import Loader
from handsdown.md_document import MDDocument
from handsdown.processors.base import BaseDocstringProcessor
from handsdown.processors.smart import SmartDocstringProcessor
from handsdown.utils.import_string import ImportString
from handsdown.utils.logger import get_logger
from handsdown.utils.markdown import insert_md_toc
from handsdown.utils.nice_path import NicePath
from handsdown.utils.path_finder import PathFinder
from handsdown.utils.strings import make_title


class BaseGenerator:
    """
    Base documentation generator.

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

    # Index filename
    INDEX_NAME = "README.md"

    # Index title
    INDEX_TITLE = "Index"

    _short_link_re = re.compile(r"`+[A-Za-z]\S+`+")

    common_templates_path = NicePath("common")
    templates_path = NicePath("mkdocs")
    index_template_path = common_templates_path / "index.md.jinja2"
    module_template_path = templates_path / "module.md.jinja2"

    # Whether to add ToC to generated module docs
    insert_toc = False

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
        self._output_path = NicePath(output_path)
        self._project_name = project_name or make_title(input_path.name)
        self._root_path_finder = PathFinder(self._root_path)
        self._source_code_url = source_code_url
        self._source_code_path = NicePath(source_code_path or Path())
        self._toc_depth = toc_depth
        self._raise_errors = raise_errors
        self._encoding = encoding
        self._jinja_manager = JinjaManager()
        self._md_document_map: Dict[NicePath, MDDocument] = {}

        # create output folder if it does not exist
        if not self._output_path.exists():
            self._logger.info(f"Creating folder {self._output_path}")
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

        # copy `HANDSDOWN.md` content from root dir if it exists
        index_template_path = self._root_path / "HANDSDOWN.md"
        if index_template_path.exists():
            self.md_index.read(index_template_path)

        if not self.md_index.title:
            self.md_index.title = f"{self._project_name} {self.INDEX_TITLE}"

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
        preserve_paths = {self.get_md_document(i).path for i in self.module_records}
        orphaned_dirs = []
        preserve_paths.add(self.md_index.path)

        for doc_path in PathFinder(self._output_path).glob("**/*.md"):
            if doc_path in preserve_paths:
                continue

            file_content = doc_path.read_text()
            is_autogenerated = "> Auto-generated documentation" in file_content
            if not is_autogenerated:
                continue

            self._logger.info(f"Deleting orphaned doc file {doc_path}")
            doc_path.unlink()

            # remove parent directory if it is empty
            children = list(doc_path.parent.iterdir())
            if not children:
                orphaned_dirs.append(doc_path.parent)

        for orphaned_dir in orphaned_dirs:
            self._logger.info(f"Deleting orphaned directory {orphaned_dir}")
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

            self._generate_doc(module_record)

            return

        raise GeneratorError(f"Record not found for {source_path}")

    def _get_source_code_url(self, module_record: ModuleRecord, md_document: MDDocument) -> str:
        if not self._source_code_url:
            relative_path = md_document.path_finder.relative(module_record.source_path)
            return (self._source_code_path / relative_path).as_posix()

        relative_path_str = self._root_path_finder.relative(module_record.source_path).as_posix()
        return f"{self._source_code_url}{relative_path_str}"

    def get_md_document(self, module_record: ModuleRecord) -> MDDocument:
        """
        Get or create MDDocument for module record.
        """
        if module_record.source_path not in self._md_document_map:
            self._md_document_map[module_record.source_path] = MDDocument(
                self._loader._get_output_path(module_record.source_path), encoding=self._encoding
            )
        return self._md_document_map[module_record.source_path]

    def _generate_doc(self, module_record: ModuleRecord) -> None:
        md_document = self.get_md_document(module_record)
        self._logger.debug(f"Generating doc {md_document.path} for {module_record.source_path}")
        try:
            self._loader.parse_module_record(module_record)
        except LoaderError as e:
            if self._raise_errors:
                raise

            self._logger.warning(f"Skipping: {e}")
            return

        md_document.source_code_url = self._get_source_code_url(module_record, md_document)

        content = self._jinja_manager.render(
            template_path=self.module_template_path,
            module_record=module_record,
            md_document=md_document,
            docstring_processor=self._docstring_processor,
            generator=self,
        )
        if self.insert_toc:
            content = insert_md_toc(content, self._toc_depth)
        if NicePath(md_document.path).write_changed(content, encoding=self._encoding):
            self._logger.info(f"Updated doc {md_document.path} for {module_record.source_path}")

    def generate_docs(self) -> None:
        """
        Generate all doc files at once.
        """
        self._logger.debug(f"Generating docs for {self._project_name} to {self._output_path}")

        for module_record in self.module_records:
            self._generate_doc(module_record)

    def generate_index(self) -> None:
        """
        Generate `<output>/README.md` file.

        Contains a Tree of all modules in the project.
        """
        self._logger.debug(f"Generating {self.md_index.path}")
        md_document = self.md_index
        content = self._jinja_manager.render(
            template_path=self.index_template_path,
            md_document=md_document,
            generator=self,
            project_name=self._project_name,
            source_code_url=self._get_main_source_code_url(),
        )
        if md_document.path.write_changed(content, encoding=self._encoding):
            self._logger.info(f"Updated index {md_document.path}")

    def replace_links(
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
                    related_md_document = self.get_md_document(related_module_record)
                    target_path = related_md_document.path

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
            related_md_document = self.get_md_document(related_module_record)
            link = md_document.render_doc_link(
                title,
                target_path=related_md_document.path,
                anchor=md_document.get_anchor(title),
            )
            links.add(link)

        return sorted(links)

    def get_external_configs_templates(self) -> Tuple[Tuple[NicePath, NicePath], ...]:
        """
        Get a tuple with pairs of template path to project path
        """
        return (
            (
                self.common_templates_path / "gh_pages_config.yml.jinja2",
                self._output_path / "_config.yml",
            ),
            (self.templates_path / "mkdocs.yml.jinja2", self._output_path.parent / "mkdocs.yml"),
            (
                self.templates_path / "readthedocs.yml.jinja2",
                self._output_path.parent / ".readthedocs.yml",
            ),
        )

    def _get_output_path_str(self) -> str:
        result = str(self._output_path.relative_to(self._root_path))
        if result.startswith("./"):
            result = result[2:]
        return result

    def _get_main_source_code_url(self) -> str:
        result = self._source_code_url or ""
        if "/blob/" in result:
            result = result.split("/blob/")[0]
        return result

    def generate_external_configs(self) -> None:
        configs = self.get_external_configs_templates()
        for template_path, output_path in configs:
            content = self._jinja_manager.render(
                template_path=template_path,
                project_name=self._project_name,
                source_code_url=self._get_main_source_code_url(),
                output_path=self._get_output_path_str(),
            )
            if output_path.write_changed(content, encoding=self._encoding):
                self._logger.info(f"Updated config {output_path}")

    def get_children_module_records(self, parent: ModuleRecord) -> List[ModuleRecord]:
        """
        Get all module records that are children of this module.
        """
        result = []
        for module_record in self.module_records:
            if module_record.import_string.is_top_level():
                continue
            if module_record.import_string.parent != parent.import_string:
                continue

            result.append(module_record)

        return result
