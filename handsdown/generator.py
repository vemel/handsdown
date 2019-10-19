# -*- coding: utf-8 -*-
"""
Main handsdown documentation generator.
"""

from __future__ import unicode_literals

import re
import logging

from typing import Iterable, Text, List, Optional, Union, Set, TYPE_CHECKING

from handsdown.loader import Loader, LoaderError
from handsdown.processors.smart import SmartDocstringProcessor
from handsdown.module_record import ModuleRecordList
from handsdown.md_document import MDDocument
from handsdown.utils import get_title_from_path_part
from handsdown.path_finder import PathFinder, Path

if TYPE_CHECKING:
    from handsdown.processors.base import BaseDocstringProcessor
    from handsdown.module_record import ModuleRecord, ModuleObjectRecord


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
        logger -- Logger instance.
        docstring_processor -- Docstring converter to Markdown.
        loader -- Loader for python modules.
        raise_errors -- Raise `LoaderError` instead of silencing in.
        ignore_unknown_errors -- Continue on any error.
        source_code_url -- URL to source files to use instead of relative paths,
            useful for [GitHub Pages](https://pages.github.com/).
        toc_depth -- Maximum depth of child modules ToC

    Arguments:
        LOGGER_NAME -- Name of logger: `handsdown`
        INDEX_NAME -- Docs index filename: `README.md`
        INDEX_TITLE -- Docs index title: `Index`
        MODULES_NAME -- Modules ToC name in index: `Modules`
    """

    LOGGER_NAME = "handsdown"
    INDEX_NAME = "README.md"
    INDEX_TITLE = "Index"
    MODULES_NAME = "Modules"
    _short_link_re = re.compile(r"`+\S+`+")

    def __init__(
        self,
        input_path,  # type: Path
        output_path,  # type: Path
        source_paths,  # type: Iterable[Path]
        logger=None,  # type: Optional[logging.Logger]
        docstring_processor=None,  # type: Optional[BaseDocstringProcessor]
        loader=None,  # type: Optional[Loader]
        raise_errors=False,  # type: bool
        source_code_url=None,  # type: Optional[Text]
        toc_depth=3,  # type: int
    ):
        # type: (...) -> None
        self._logger = logger or logging.Logger(self.LOGGER_NAME)
        self._root_path = input_path
        self._output_path = output_path
        self._project_name = get_title_from_path_part(input_path.name)
        self._index_path = Path(self._output_path, self.INDEX_NAME)
        self._root_path_finder = PathFinder(self._root_path)
        self._source_code_url = source_code_url
        self._toc_depth = toc_depth

        # create output folder if it does not exist
        if not self._output_path.exists():
            self._logger.info("Creating folder {}".format(self._output_path))
            PathFinder(self._output_path).mkdir()

        self._raise_errors = raise_errors
        self._loader = loader or Loader(
            root_path=self._root_path,
            output_path=self._output_path,
            logger=self._logger,
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
        self._signature_links_re = re.compile(
            r"[ \[]((?:{})\.[^() :,]+)".format(package_names_re_expr)
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

                self._error_output_paths.add(self._loader.get_output_path(source_path))
                self._logger.warning(
                    "Skipping {} due to import error: {}".format(
                        self._root_path_finder.relative(source_path), e
                    )
                )

            if module_record:
                module_record_list.add(module_record)

        return module_record_list

    def cleanup_old_docs(self):
        # type: () -> None
        """
        Remove old docs generated for this module.
        """
        self._logger.debug("Removing orphaned docs")
        preserve_paths = {i.output_path for i in self._module_records}

        # skip error output paths
        # preserve_paths.update(self._error_output_paths)

        for doc_path in self._output_path.glob("**/*.md"):
            if doc_path == self._index_path:
                continue

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
            try:
                doc_path.parent.rmdir()
            except OSError:
                continue
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

            with MDDocument(module_record.output_path) as md_document:
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

        self._render_docstring(module_record=module_record, md_document=md_document)

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
        md_document.ensure_toc_exists()

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
            toc_lines.append("  - {}".format(self.MODULES_NAME))
            for line in modules_toc_lines:
                toc_lines.append("    {}".format(line))

        md_document.toc_section = "\n".join(toc_lines)

    def _build_breadcrumbs_string(self, module_record, md_document):
        # type: (ModuleRecord, MDDocument) -> Text
        breadcrumbs = []  # type: List[Text]

        import_string_parts = module_record.get_import_string_parts()
        parent_import_parts = []  # type: List[Text]
        for part in import_string_parts[:-1]:
            parent_import_parts.append(part)
            parent_import = ".".join(parent_import_parts)
            parend_module_record = self._module_records.find_object(parent_import)
            if not parend_module_record:
                breadcrumbs.append("`{}`".format(get_title_from_path_part(part)))
                continue

            breadcrumbs.append(
                md_document.render_doc_link(
                    parend_module_record.title,
                    target_path=parend_module_record.output_path,
                    anchor=md_document.get_anchor(parend_module_record.title),
                )
            )

        breadcrumbs.append(module_record.title)
        breadcrumbs.insert(
            0,
            md_document.render_doc_link(
                self.INDEX_TITLE,
                target_path=self._output_path / self.INDEX_NAME,
                anchor=md_document.get_anchor(self.MODULES_NAME),
            ),
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
            with MDDocument(module_record.output_path) as md_document:
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
            "Generating {}".format(self._root_path_finder.relative(self._index_path))
        )
        index_path = self._output_path / self.INDEX_NAME
        with MDDocument(index_path) as md_index:
            readme_path = self._root_path / "README.md"
            if readme_path.exists():
                index_path.write_text(readme_path.read_text())
                md_index.read()

            if not md_index.title:
                md_index.title = "{} {}".format(self._project_name, self.INDEX_TITLE)

            autogenerated_marker = "> Auto-generated documentation index."
            if md_index.subtitle:
                md_index.subtitle = "{}\n\n{}".format(
                    autogenerated_marker, md_index.subtitle
                )
            else:
                md_index.subtitle = autogenerated_marker

            md_index.append_title(self.MODULES_NAME, level=2)

            modules_toc_lines = self._build_modules_toc_lines(
                import_string="", max_depth=self._toc_depth, md_document=md_index
            )

            md_index.append("\n".join(modules_toc_lines))
            md_index.toc_section = md_index.generate_toc_section()

    def _replace_short_links(self, module_record, md_document):
        # type: (ModuleRecord, MDDocument) -> None
        if not module_record.objects:
            return

        sections = md_document.sections

        for index, section in enumerate(sections):
            for match in self._short_link_re.findall(section):
                import_string = match.replace("`", "")
                for module_object in module_record.objects:
                    if module_object.import_string != import_string:
                        continue

                    title = module_object.title
                    link = md_document.render_doc_link(
                        title,
                        target_path=module_object.output_path,
                        anchor=md_document.get_anchor(title),
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
                object_name = match.replace("`", "")
                module_object = self._module_records.find_object(object_name)
                if module_object is None:
                    continue

                title = module_object.title
                link = md_document.render_doc_link(
                    title,
                    target_path=module_object.output_path,
                    anchor=md_document.get_anchor(title),
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
        for module_object_record in module_record.objects:
            if module_object_record.is_related:
                continue

            md_document.append_title(
                module_object_record.title, level=module_object_record.level + 2
            )

            source_path = module_object_record.source_path
            source_line_number = module_object_record.source_line_number
            source_link = md_document.render_doc_link(
                title="🔍 find in source code",
                target_path=source_path,
                anchor="L{}".format(source_line_number),
            )
            if self._source_code_url:
                relative_path_str = self._root_path_finder.relative(
                    source_path
                ).as_posix()
                source_link = md_document.render_link(
                    title="🔍 find in source code",
                    link="{}{}#L{}".format(
                        self._source_code_url, relative_path_str, source_line_number
                    ),
                )

            md_document.append(source_link)

            signature = module_object_record.signature
            md_document.append("```python\n{}\n```".format(signature))

            self._render_docstring(
                module_record=module_object_record, md_document=md_document
            )

    def _render_docstring(self, module_record, md_document):
        # type: (Union[ModuleRecord, ModuleObjectRecord], MDDocument) -> None
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
        docstring = module_record.docstring
        title, docstring = md_document.extract_title(docstring)
        if title:
            module_record.title = title
            md_document.title = title

        section_map = self._docstring_processor.build_sections(docstring)
        reference_objects = module_record.get_reference_objects()
        for reference_object in reference_objects:
            title = reference_object.title
            link = md_document.render_doc_link(
                title,
                target_path=reference_object.output_path,
                anchor=md_document.get_anchor(title),
            )
            section_map.add_line("See also", "- {}".format(link))
            self._logger.debug(
                "Adding link '{}' to {} 'See also' section".format(
                    title, self._root_path_finder.relative(reference_object.output_path)
                )
            )

        for section in section_map.sections:
            if section.title:
                md_document.append_title(section.title, level=4)
            for block in section.blocks:
                md_document.append(block.render())

    def _get_objects_from_signature(self, signature):
        # type: (Text) -> List[ModuleObjectRecord]
        result = []  # type: List[ModuleObjectRecord]
        for match in re.findall(self._signature_links_re, signature):
            module_object_record = self._module_records.find_object(match)
            if not module_object_record or module_object_record in result:
                continue

            result.append(module_object_record)

        return result

    def _build_modules_toc_lines(self, import_string, max_depth, md_document):
        # type: (Text, int, MDDocument) -> List[Text]
        lines = []  # type: List[Text]
        parts = []  # type: List[Text]
        if import_string:
            parts = import_string.split(".")

        last_import_string_parts = []  # type: List[Text]
        for module_record in self._module_records:
            if module_record.import_string == import_string:
                continue

            if not module_record.import_string.startswith(import_string):
                continue

            if len(module_record.import_string.split(".")) > len(parts) + max_depth:
                continue

            title_parts = module_record.get_title_parts()
            import_string_parts = module_record.get_import_string_parts()
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
                target_path=module_record.output_path,
                anchor=md_document.get_anchor(title_parts[-1]),
            )
            lines.append("{}- {}".format(indent, link))
        return lines
