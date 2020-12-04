"""
Main handsdown documentation generator.
"""

from __future__ import unicode_literals

import re
from typing import TYPE_CHECKING, Iterable, List, Optional, Set

from handsdown.ast_parser.module_record_list import ModuleRecordList
from handsdown.ast_parser.node_records.attribute_record import AttributeRecord
from handsdown.loader import Loader, LoaderError
from handsdown.md_document import MDDocument
from handsdown.processors.smart import SmartDocstringProcessor
from handsdown.settings import FIND_IN_SOURCE_LABEL
from handsdown.utils import make_title
from handsdown.utils.import_string import ImportString
from handsdown.utils.logger import get_logger
from handsdown.utils.path_finder import PathFinder

if TYPE_CHECKING:  # pragma: no cover
    from pathlib import Path

    from handsdown.ast_parser.node_records.module_record import ModuleRecord
    from handsdown.ast_parser.node_records.node_record import NodeRecord
    from handsdown.processors.base import BaseDocstringProcessor


class GeneratorError(Exception):
    """
    Main error for `Generator`
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
        toc_depth -- Maximum depth of child modules ToC
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
        toc_depth: int = 1,
    ) -> None:
        self._logger = get_logger()
        self._root_path = input_path
        self._output_path = output_path
        self._project_name = project_name or make_title(input_path.name)
        self._root_path_finder = PathFinder(self._root_path)
        self._source_code_url = source_code_url
        self._toc_depth = toc_depth
        self._raise_errors = raise_errors

        # create output folder if it does not exist
        if not self._output_path.exists():
            self._logger.info("Creating folder {}".format(self._output_path))
            PathFinder(self._output_path).mkdir()

        self._loader = loader or Loader(root_path=self._root_path, output_path=self._output_path)
        self._docstring_processor = docstring_processor or SmartDocstringProcessor()

        self._source_paths = sorted(source_paths)
        self._error_output_paths: Set[Path] = set()
        self._logger.debug(
            "Generating source map for {} source files".format(len(self._source_paths))
        )
        self._module_records = self._build_module_record_list()
        self._logger.debug("Source map generated")

        package_names = self._module_records.get_package_names()
        package_names_re_expr = "|".join(package_names)
        self._docstring_links_re = re.compile(r"`+(?:{})\.\S+`+".format(package_names_re_expr))
        self._prepare_index()

    def _prepare_index(self) -> None:
        self.md_index = MDDocument(self._output_path / self.INDEX_NAME)
        self.md_modules = MDDocument(self._output_path / self.MODULES_NAME)

        # copy `README.md` content from root dir if it exists
        readme_path = self._root_path / "README.md"
        if readme_path.exists():
            self.md_index.read(readme_path)

        if not self.md_index.title:
            self.md_index.title = "{} {}".format(self._project_name, self.INDEX_TITLE)

        # copy `MODULES.md` content from root dir if it exists
        modules_path = self._root_path / "MODULES.md"
        if modules_path.exists():
            self.md_modules.read(modules_path)

        if not self.md_modules.title:
            self.md_modules.title = "{} {}".format(self._project_name, self.MODULES_TITLE)

    def _build_module_record_list(self) -> ModuleRecordList:
        module_record_list = ModuleRecordList()
        for source_path in self._source_paths:
            module_record = None
            try:
                module_record = self._loader.get_module_record(source_path)
            except LoaderError as e:
                if self._raise_errors:
                    raise

                self._logger.warning("Skipping: {}".format(e))
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
        preserve_paths = {self._loader.get_output_path(i.source_path) for i in self._module_records}
        orphaned_dirs = []
        preserve_paths.add(self.md_index.path)
        preserve_paths.add(self.md_modules.path)

        # skip error output paths
        # preserve_paths.update(self._error_output_paths)

        for doc_path in PathFinder(self._output_path).glob("**/*.md"):
            if doc_path in preserve_paths:
                continue

            file_content = doc_path.read_text()
            is_autogenerated = "> Auto-generated documentation" in file_content
            if not is_autogenerated:
                continue

            self._logger.info(
                "Deleting orphaned doc file {}".format(self._root_path_finder.relative(doc_path))
            )
            doc_path.unlink()

            # remove parent directory if it is empty
            children = list(doc_path.parent.iterdir())
            if not children:
                orphaned_dirs.append(doc_path.parent)

        for orphaned_dir in orphaned_dirs:
            self._logger.info(
                "Deleting orphaned directory {}".format(
                    self._root_path_finder.relative(orphaned_dir)
                )
            )
            orphaned_dir.rmdir()

    def generate_doc(self, source_path: Path) -> None:
        """
        Generate one module doc at once.

        Arguments:
            source_path -- Path to source file.

        Raises:
            GeneratorError -- If `source_path` not found in current repo.
        """
        for module_record in self._module_records:
            if module_record.source_path != source_path:
                continue

            output_path = self._loader.get_output_path(module_record.source_path)

            md_document = MDDocument(output_path)
            self._generate_doc(module_record, md_document)
            md_document.write()

            return

        raise GeneratorError("Record not found for {}".format(source_path.name))

    def _generate_doc(self, module_record: ModuleRecord, md_document: MDDocument) -> None:
        self._logger.debug(
            "Generating doc {} for {}".format(
                self._root_path_finder.relative(md_document.path),
                self._root_path_finder.relative(module_record.source_path),
            )
        )
        try:
            self._loader.parse_module_record(module_record)
        except LoaderError as e:
            if self._raise_errors:
                raise

            self._logger.warning("Skipping: {}".format(e))
            return

        source_link = md_document.render_doc_link(
            title=module_record.import_string.value,
            target_path=module_record.source_path,
        )
        if self._source_code_url:
            relative_path_str = self._root_path_finder.relative(
                module_record.source_path
            ).as_posix()
            source_link = md_document.render_link(
                title=module_record.import_string.value,
                link="{}{}".format(self._source_code_url, relative_path_str),
            )

        md_document.title = module_record.title

        self._render_docstring(
            module_record=module_record, record=module_record, md_document=md_document
        )

        autogenerated_marker = "> Auto-generated documentation for {} module.".format(source_link)
        if md_document.subtitle:
            md_document.subtitle = "{}\n\n{}".format(autogenerated_marker, md_document.subtitle)
        else:
            md_document.subtitle = autogenerated_marker

        self._generate_module_doc_lines(module_record, md_document)
        md_document.add_toc_if_not_exists()

        modules_toc_lines = self._build_modules_toc_lines(
            module_record.import_string,
            max_depth=self._toc_depth,
            md_document=md_document,
            start_level=2,
        )

        toc_lines = md_document.toc_section.split("\n")
        breadscrumbs = self._build_breadcrumbs_string(
            module_record=module_record, md_document=md_document
        )
        toc_lines[0] = md_document.get_toc_line(breadscrumbs, level=0)
        if modules_toc_lines:
            toc_line = md_document.get_toc_line(self.MODULES_TITLE, level=1)
            toc_lines.append(toc_line)
            for line in modules_toc_lines:
                toc_lines.append(line)

        md_document.toc_section = "\n".join(toc_lines)

    def _build_breadcrumbs_string(
        self,
        module_record: ModuleRecord,
        md_document: MDDocument,
    ) -> str:
        import_string_breadcrumbs: List[str] = []
        parent_import_strings = []
        import_string = module_record.import_string
        while not import_string.is_top_level():
            import_string = import_string.parent
            parent_import_strings.append(import_string)

        parent_import_strings.reverse()

        for parent_import_string in parent_import_strings:
            parent_module_record = self._module_records.find_module_record(parent_import_string)
            if not parent_module_record:
                import_string_breadcrumbs.append(
                    "`{}`".format(make_title(parent_import_string.parts[-1]))
                )
                continue

            output_path = self._loader.get_output_path(parent_module_record.source_path)
            import_string_breadcrumbs.append(
                md_document.render_doc_link(
                    parent_module_record.title,
                    target_path=output_path,
                    anchor=md_document.get_anchor(parent_module_record.title),
                )
            )

        breadcrumbs = (
            [
                md_document.render_md_doc_link(self.md_index, title=self._project_name),
                md_document.render_md_doc_link(self.md_modules, title=self.MODULES_TITLE),
            ]
            + import_string_breadcrumbs
            + [module_record.title]
        )

        return " / ".join(breadcrumbs)

    def generate_docs(self) -> None:
        """
        Generate all doc files at once.
        """
        self._logger.debug(
            "Generating docs for {} to {}".format(
                self._project_name, self._root_path_finder.relative(self._output_path)
            )
        )

        for module_record in self._module_records:
            output_path = self._loader.get_output_path(module_record.source_path)
            md_document = MDDocument(output_path)
            self._generate_doc(module_record, md_document)
            md_document.write()

    def generate_index(self) -> None:
        """
        Generate `<output>/README.md` file with title from `<root>/README.md` and `Modules`
        section that contains a Tree of all modules in the project.
        """
        self._logger.debug(
            "Generating {}".format(self._root_path_finder.relative(self.md_index.path))
        )
        with self.md_index as md_index:
            if not md_index.title:
                md_index.title = "{} {}".format(self._project_name, self.INDEX_TITLE)

            autogenerated_marker = "> Auto-generated documentation index."
            modules_section = "Full {} project documentation can be found in {}".format(
                self._project_name,
                md_index.render_md_doc_link(self.md_modules, title=self.MODULES_TITLE),
            )
            subtitle_parts = [autogenerated_marker]
            if md_index.subtitle:
                subtitle_parts.append(md_index.subtitle)
            subtitle_parts.append(modules_section)
            md_index.subtitle = "\n\n".join(subtitle_parts)

            md_index.add_toc_if_not_exists()
            md_index.toc_section = "{}\n  - {}".format(
                md_index.toc_section, md_index.render_md_doc_link(self.md_modules)
            )

    def generate_modules(self) -> None:
        """
        Generate `<output>/README.md` file with title from `<root>/README.md` and `Modules`
        section that contains a Tree of all modules in the project.
        """
        self._logger.debug(
            "Generating {}".format(self._root_path_finder.relative(self.md_modules.path))
        )
        with self.md_modules as md_modules:
            if not md_modules.title:
                md_modules.title = "{} {}".format(self._project_name, self.MODULES_TITLE)

            autogenerated_marker = "> Auto-generated documentation modules index."
            subtitle_parts = [autogenerated_marker]
            if md_modules.subtitle:
                subtitle_parts.append(md_modules.subtitle)

            subtitle_parts.append(
                "Full list of {} project modules.".format(
                    md_modules.render_md_doc_link(self.md_index, title=self._project_name)
                )
            )
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

    def _generate_module_doc_lines(
        self,
        module_record: ModuleRecord,
        md_document: MDDocument,
    ) -> None:
        for record in module_record.iter_records():
            if isinstance(record, AttributeRecord):
                continue

            header_level = 2
            if record.is_method:
                header_level = 3

            md_document.append_title(record.title, level=header_level)

            source_path = module_record.source_path
            source_line_number = record.line_number
            source_link = md_document.render_doc_link(
                title=FIND_IN_SOURCE_LABEL,
                target_path=source_path,
                anchor="L{}".format(source_line_number),
            )
            if self._source_code_url:
                relative_path_str = self._root_path_finder.relative(source_path).as_posix()
                source_link = md_document.render_link(
                    title=FIND_IN_SOURCE_LABEL,
                    link="{}{}#L{}".format(
                        self._source_code_url, relative_path_str, source_line_number
                    ),
                )

            md_document.append(source_link)

            signature = record.render(allow_multiline=True)
            md_document.append("```python\n{}\n```".format(signature))

            self._render_docstring(
                module_record=module_record, record=record, md_document=md_document
            )

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
                related_module_record = self._module_records.find_module_record(
                    related_import_string
                )
                if related_module_record:
                    related_record = related_module_record.find_record(related_import_string)
                    target_path = self._loader.get_output_path(related_module_record.source_path)

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
            self._logger.debug("Adding local link '{}' to '{}'".format(title, record.title))
        return docstring

    def _render_docstring(
        self,
        module_record: ModuleRecord,
        record: NodeRecord,
        md_document: MDDocument,
    ) -> None:
        """
        Get object docstring and convert it to a valid markdown using
        `handsdown.processors.base.BaseDocstringProcessor`.

        Arguments:
            module_record -- Parent ModuleRecord
            record -- Target NodeRecord
            md_document -- Output document.

        Returns:
            A module docstring with valid markdown.
        """
        docstring = record.docstring
        docstring = self._replace_links(module_record, record, md_document, docstring)

        section_map = self._docstring_processor.build_sections(docstring)

        for attrubute in record.get_documented_attribute_strings():
            section_map.add_line_indent("Attributes", "- {}".format(attrubute))

        related_import_strings = record.get_related_import_strings(module_record)
        links = []
        title = ""
        for import_string in related_import_strings:
            related_module_record = self._module_records.find_module_record(import_string)
            if not related_module_record:
                continue

            related_record = related_module_record.find_record(import_string)
            if not related_record:
                continue

            if related_record is record:
                continue

            title = related_record.title
            target_path = self._loader.get_output_path(related_module_record.source_path)
            link = md_document.render_doc_link(
                title, target_path=target_path, anchor=md_document.get_anchor(title)
            )
            links.append(link)

        links.sort()
        for link in links:
            section_map.add_line("See also", "- {}".format(link))
            self._logger.debug(
                "Adding link `{}` to `{}` `See also` section".format(title, record.title)
            )

        for section in section_map.sections:
            if section.title:
                md_document.append_title(section.title, level=4)
            for block in section.blocks:
                md_document.append(block.render())

    def _build_modules_toc_lines(
        self, import_string: ImportString, max_depth: int, md_document: MDDocument, start_level: int
    ) -> List[str]:
        lines: List[str] = []
        parts = import_string.parts

        last_import_string_parts: List[str] = []
        for module_record in self._module_records:
            output_path = self._loader.get_output_path(module_record.source_path)
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
                target_path=output_path,
                anchor=md_document.get_anchor(module_record.title),
            )
            toc_line = md_document.get_toc_line(
                link, level=len(import_string_parts) - len(parts) - 1 + start_level
            )
            lines.append(toc_line)
        return lines
