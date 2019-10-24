"""
Main handsdown documentation generator.
"""

from __future__ import unicode_literals

import re

from typing import Iterable, Text, List, Optional, Set, TYPE_CHECKING

from handsdown.loader import Loader, LoaderError
from handsdown.processors.smart import SmartDocstringProcessor
from handsdown.ast_parser.module_record_list import ModuleRecordList
from handsdown.md_document import MDDocument
from handsdown.utils import make_title, split_import_string
from handsdown.utils.logger import get_logger
from handsdown.path_finder import PathFinder
from handsdown.settings import FIND_IN_SOURCE_LABEL

if TYPE_CHECKING:  # pragma: no cover
    from handsdown.path_finder import Path
    from handsdown.processors.base import BaseDocstringProcessor
    from handsdown.ast_parser.node_records.node_record import NodeRecord
    from handsdown.ast_parser.node_records.module_record import ModuleRecord


class GeneratorError(Exception):
    """
    Main error for `Generator`
    """


class Generator:
    """
    Main handsdown documentation generator.

    Arguments:
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
        input_path,  # type: Path
        output_path,  # type: Path
        source_paths,  # type: Iterable[Path]
        docstring_processor=None,  # type: Optional[BaseDocstringProcessor]
        loader=None,  # type: Optional[Loader]
        raise_errors=False,  # type: bool
        source_code_url=None,  # type: Optional[Text]
        toc_depth=3,  # type: int
    ):
        # type: (...) -> None
        self._logger = get_logger()
        self._root_path = input_path
        self._output_path = output_path
        self._project_name = make_title(input_path.name)
        self._root_path_finder = PathFinder(self._root_path)
        self._source_code_url = source_code_url
        self._toc_depth = toc_depth
        self._raise_errors = raise_errors

        # create output folder if it does not exist
        if not self._output_path.exists():
            self._logger.info("Creating folder {}".format(self._output_path))
            PathFinder(self._output_path).mkdir()

        self._loader = loader or Loader(
            root_path=self._root_path, output_path=self._output_path
        )
        self._docstring_processor = docstring_processor or SmartDocstringProcessor()

        self._source_paths = sorted(source_paths)
        self._error_output_paths = set()  # type: Set[Path]
        self._module_records = self._build_module_record_list()

        package_names = self._module_records.get_package_names()
        package_names_re_expr = "|".join(package_names)
        self._docstring_links_re = re.compile(
            r"`+(?:{})\.\S+`+".format(package_names_re_expr)
        )
        self._prepare_index()

    def _prepare_index(self):
        # type: () -> None
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
            self.md_modules.title = "{} {}".format(
                self._project_name, self.MODULES_TITLE
            )

    def _build_module_record_list(self):
        # type: () -> ModuleRecordList
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
                module_record_list.add(module_record)

        return module_record_list

    def cleanup_old_docs(self):
        # type: () -> None
        """
        Remove old docs generated for this module.
        """
        self._logger.debug("Removing orphaned docs")
        preserve_paths = {
            self._loader.get_output_path(i.source_path) for i in self._module_records
        }
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
                "Deleting orphaned doc file {}".format(
                    self._root_path_finder.relative(doc_path)
                )
            )
            doc_path.unlink()

            # remove parent directory if it is empty
            children = list(doc_path.parent.iterdir())
            if not children:
                doc_path.parent.rmdir()

            else:
                self._logger.info(
                    "Deleting orphaned directory {}".format(
                        self._root_path_finder.relative(doc_path.parent)
                    )
                )

    def generate_doc(self, source_path):
        # type: (Path) -> None
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
            with MDDocument(output_path) as md_document:
                self._generate_doc(module_record, md_document)
                self._replace_short_links(module_record, md_document)
                self._replace_full_links(md_document)

            return

        raise GeneratorError("Record not found for {}".format(source_path.name))

    def _generate_doc(self, module_record, md_document):
        # type: (ModuleRecord, MDDocument) -> None
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
            title=module_record.import_string, target_path=module_record.source_path
        )
        if self._source_code_url:
            relative_path_str = self._root_path_finder.relative(
                module_record.source_path
            ).as_posix()
            source_link = md_document.render_link(
                title=module_record.import_string,
                link="{}{}".format(self._source_code_url, relative_path_str),
            )

        md_document.title = module_record.title

        self._render_docstring(
            module_record=module_record, record=module_record, md_document=md_document
        )

        autogenerated_marker = "> Auto-generated documentation for {} module.".format(
            source_link
        )
        if md_document.subtitle:
            md_document.subtitle = "{}\n\n{}".format(
                autogenerated_marker, md_document.subtitle
            )
        else:
            md_document.subtitle = autogenerated_marker

        self._generate_module_doc_lines(module_record, md_document)
        md_document.add_toc_if_not_exists()

        modules_toc_lines = self._build_modules_toc_lines(
            module_record.import_string,
            max_depth=self._toc_depth,
            md_document=md_document,
        )

        toc_lines = md_document.toc_section.split("\n")
        breadscrumbs = self._build_breadcrumbs_string(
            module_record=module_record, md_document=md_document
        )
        toc_lines[0] = "- {}".format(breadscrumbs)
        if modules_toc_lines:
            toc_lines.append("  - {}".format(self.MODULES_TITLE))
            for line in modules_toc_lines:
                toc_lines.append("    {}".format(line))

        md_document.toc_section = "\n".join(toc_lines)

    def _build_breadcrumbs_string(self, module_record, md_document):
        # type: (ModuleRecord, MDDocument) -> Text
        import_string_breadcrumbs = []  # type: List[Text]

        import_string_parts = split_import_string(module_record.import_string)
        parent_import_parts = []  # type: List[Text]
        for part in import_string_parts[:-1]:
            parent_import_parts.append(part)
            parent_import = ".".join(parent_import_parts)
            parent_module_record = self._module_records.find_module_record(
                parent_import
            )
            if not parent_module_record:
                import_string_breadcrumbs.append("`{}`".format(make_title(part)))
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
                md_document.render_md_doc_link(
                    self.md_modules, title=self.MODULES_TITLE
                ),
            ]
            + import_string_breadcrumbs
            + [module_record.title]
        )

        return " / ".join(breadcrumbs)

    def generate_docs(self):
        # type: () -> None
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
            with MDDocument(output_path) as md_document:
                self._generate_doc(module_record, md_document)
                self._replace_short_links(module_record, md_document)
                self._replace_full_links(md_document)

    def generate_index(self):
        # type: () -> None
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

    def generate_modules(self):
        # type: () -> None
        """
        Generate `<output>/README.md` file with title from `<root>/README.md` and `Modules`
        section that contains a Tree of all modules in the project.
        """
        self._logger.debug(
            "Generating {}".format(
                self._root_path_finder.relative(self.md_modules.path)
            )
        )
        with self.md_modules as md_modules:
            if not md_modules.title:
                md_modules.title = "{} {}".format(
                    self._project_name, self.MODULES_TITLE
                )

            autogenerated_marker = "> Auto-generated documentation modules index."
            subtitle_parts = [autogenerated_marker]
            if md_modules.subtitle:
                subtitle_parts.append(md_modules.subtitle)

            subtitle_parts.append(
                "Full list of {} project modules.".format(
                    md_modules.render_md_doc_link(
                        self.md_index, title=self._project_name
                    )
                )
            )
            md_modules.subtitle = "\n\n".join(subtitle_parts)

            modules_toc_lines = self._build_modules_toc_lines(
                import_string="", max_depth=10, md_document=md_modules
            )
            modules_toc_lines.insert(
                0, "- {}".format(md_modules.render_md_doc_link(self.md_index))
            )

            md_modules.toc_section = "\n".join(modules_toc_lines)

    def _replace_short_links(self, module_record, md_document):
        # type: (ModuleRecord, MDDocument) -> None
        records = [i[-1] for i in module_record.iter_records()]
        if not records:
            return

        sections = md_document.sections

        for index, section in enumerate(sections):
            for match in self._short_link_re.findall(section):
                import_string = match.replace("`", "")
                record = module_record.find_record(import_string)
                if not record:
                    continue

                title = record.title
                link = md_document.render_doc_link(
                    title, anchor=md_document.get_anchor(title)
                )
                section = section.replace(match, link)
                self._logger.debug(
                    "Adding local link '{}' to {}".format(
                        title, self._root_path_finder.relative(md_document.path)
                    )
                )
            sections[index] = section

    def _replace_full_links(self, md_document):
        # type: (MDDocument) -> None
        sections = md_document.sections

        for index, section in enumerate(sections):
            for match in re.findall(self._docstring_links_re, section):
                import_string = match.replace("`", "")
                module_record = self._module_records.find_module_record(import_string)
                if module_record is None:
                    continue

                node_record = module_record.find_record(import_string)
                if not node_record:
                    continue

                title = node_record.title
                output_path = self._loader.get_output_path(module_record.source_path)
                link = md_document.render_doc_link(
                    title, target_path=output_path, anchor=md_document.get_anchor(title)
                )
                section = section.replace(match, link)
                self._logger.debug(
                    "Adding link '{}' to {}".format(
                        title, self._root_path_finder.relative(md_document.path)
                    )
                )
            sections[index] = section

    def _generate_module_doc_lines(self, module_record, md_document):
        # type: (ModuleRecord, MDDocument) -> None
        for records in module_record.iter_records():
            record = records[-1]
            md_document.append_title(record.title, level=len(records))

            source_path = module_record.source_path
            source_line_number = record.line_number
            source_link = md_document.render_doc_link(
                title=FIND_IN_SOURCE_LABEL,
                target_path=source_path,
                anchor="L{}".format(source_line_number),
            )
            if self._source_code_url:
                relative_path_str = self._root_path_finder.relative(
                    source_path
                ).as_posix()
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

    def _render_docstring(self, module_record, record, md_document):
        # type: (ModuleRecord, NodeRecord, MDDocument) -> None
        """
        Get object docstring and convert it to a valid markdown using
        `handsdown.processors.base.BaseDocstringProcessor`.

        Arguments:
            source_path -- Path to object source file.
            module_object -- Object to inspect.
            signature -- Object signature if exists.

        Returns:
            A module docstring with valid markdown.
        """
        docstring = record.docstring
        section_map = self._docstring_processor.build_sections(docstring)

        for attrubute in record.get_documented_attribute_strings():
            section_map.add_line_indent("Attributes", "- {}".format(attrubute))

        for import_string in record.get_related_import_strings(module_record):
            related_module_record = self._module_records.find_module_record(
                import_string
            )
            if not related_module_record:
                continue

            related_record = related_module_record.find_record(import_string)
            if not related_record:
                continue

            if related_record is record:
                continue

            title = related_record.title
            output_path = self._loader.get_output_path(module_record.source_path)
            target_path = self._loader.get_output_path(
                related_module_record.source_path
            )
            link = md_document.render_doc_link(
                title, target_path=target_path, anchor=md_document.get_anchor(title)
            )
            section_map.add_line("See also", "- {}".format(link))
            self._logger.debug(
                "Adding link '{}' to {} 'See also' section".format(
                    title, self._root_path_finder.relative(output_path)
                )
            )

        for section in section_map.sections:
            if section.title:
                md_document.append_title(section.title, level=4)
            for block in section.blocks:
                md_document.append(block.render())

    def _build_modules_toc_lines(self, import_string, max_depth, md_document):
        # type: (Text, int, MDDocument) -> List[Text]
        lines = []  # type: List[Text]
        parts = []  # type: List[Text]
        if import_string:
            parts = import_string.split(".")

        last_import_string_parts = []  # type: List[Text]
        for module_record in self._module_records:
            output_path = self._loader.get_output_path(module_record.source_path)
            if module_record.import_string == import_string:
                continue

            if not module_record.import_string.startswith("{}.".format(import_string)):
                continue

            import_string_parts = split_import_string(module_record.import_string)
            if len(import_string_parts) > len(parts) + max_depth:
                continue

            title_parts = module_record.get_title_parts()
            for index, title_part in enumerate(title_parts[:-1]):
                if index < len(parts):
                    continue

                if (
                    len(last_import_string_parts) > index
                    and last_import_string_parts[index] == import_string_parts[index]
                ):
                    continue
                indent = "  " * (index - len(parts))
                lines.append("{}- {}".format(indent, title_part))

            last_import_string_parts = import_string_parts
            indent = "  " * (len(title_parts) - len(parts) - 1)
            link = md_document.render_doc_link(
                title=title_parts[-1],
                target_path=output_path,
                anchor=md_document.get_anchor(title_parts[-1]),
            )
            lines.append("{}- {}".format(indent, link))
        return lines
