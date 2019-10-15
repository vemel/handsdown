import re
import logging
from pathlib import Path
from typing import Iterable, Text, List, Optional, Union

from handsdown.loader import Loader, LoaderError
from handsdown.processors.smart import SmartDocstringProcessor
from handsdown.processors.base import BaseDocstringProcessor
from handsdown.module_record import ModuleRecord, ModuleObjectRecord, ModuleRecordList
from handsdown.md_document import MDDocument
from handsdown.utils import get_title_from_path_part


class GeneratorError(Exception):
    """
    Main error for `Generator`
    """


class Generator:
    """
    Main handsdown doc generator.

    Arguments:
        input_path -- Path to repo to generate docs.
        output_path -- Path to folder with auto-generated docs to output.
        source_paths -- List of paths to source files for generation.
        logger -- Logger instance.
        docstring_processor -- Docstring converter to Markdown.
        loader -- Loader for python modules.
        raise_errors -- Raise Loader errors instead of silencing them.

    Arguments:
        LOGGER_NAME -- Name of logger: `handsdown`
        INDEX_NAME -- Docs index filename: `README.md`
        INDEX_MODULES_NAME -- Modules ToC name in index: `Modules`

    Raises:
        GeneratorError -- If input/output paths are invalid.
    """

    LOGGER_NAME = "handsdown"
    INDEX_NAME = "README.md"
    MODULES_NAME = "Modules"

    def __init__(
        self,
        input_path: Path,
        output_path: Path,
        source_paths: Iterable[Path],
        logger: Optional[logging.Logger] = None,
        docstring_processor: Optional[BaseDocstringProcessor] = None,
        loader: Optional[Loader] = None,
        raise_errors: bool = False,
    ) -> None:
        self._logger = logger or logging.Logger(self.LOGGER_NAME)
        self._root_path = input_path
        self._output_path = output_path
        self._project_name = get_title_from_path_part(input_path.name)
        self._index_path = Path(self._output_path, self.INDEX_NAME)

        try:
            output_relative_path = self._output_path.relative_to(self._root_path)
        except ValueError as e:
            raise GeneratorError(f"Output path should be inside input path: {e}")

        # relative path from output to source root folder
        # used while creating links to source
        root_relative_path = Path()
        for part in output_relative_path.parts:
            root_relative_path = root_relative_path / ".."
        self._root_relative_path = root_relative_path

        # create output folder if it does not exist
        if not self._output_path.exists():
            self._logger.info(f"Creating folder {self._output_path}")
            self._output_path.mkdir(parents=True)

        self._raise_errors = raise_errors
        self._loader = loader or Loader(root_path=self._root_path, logger=self._logger)
        self._docstring_processor = docstring_processor or SmartDocstringProcessor()

        self._source_paths = sorted(source_paths)
        self._module_records = self._build_module_record_list()

        package_names = self._module_records.get_package_names()
        self._docstring_links_re = re.compile(f'`(?:{"|".join(package_names)})\\.\\S+`')
        self._signature_links_re = re.compile(
            f'[ \\[]((?:{"|".join(package_names)})\\.[^() :,]+)'
        )

    def _build_module_record_list(self) -> ModuleRecordList:
        result = ModuleRecordList()
        for source_path in self._source_paths:
            try:
                module_record = self._loader.get_module_record(source_path)
            except LoaderError as e:
                if self._raise_errors:
                    raise

                self._logger.warning(
                    f"Skipping {source_path.relative_to(self._root_path)} due to import error: {e}"
                )

            if module_record:
                result.add(module_record)

        return result

    def cleanup_old_docs(self) -> None:
        """
        Remove old docs generated for this module.
        """
        self._logger.debug(f"Removing orphaned docs")
        preserve_file_names = self._module_records.get_output_file_names()
        for doc_path in self._output_path.glob("*.md"):
            if doc_path.name == self.INDEX_NAME:
                continue

            md_name = doc_path.name
            if md_name in preserve_file_names:
                continue

            file_content = doc_path.read_text()
            is_autogenerated = "Auto-generated documentation" in file_content
            if is_autogenerated:
                self._logger.info(f"Deleting orphaned doc file {md_name}")
                doc_path.unlink()

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

            self._generate_doc(module_record)
            self.replace_links(self._output_path / module_record.output_file_name)
            self._replace_local_links(module_record)
            return

        raise GeneratorError(f"Record not found for {source_path.name}")

    def _generate_doc(self, module_record: ModuleRecord) -> None:
        md_name = module_record.output_file_name
        target_file = self._output_path / md_name
        relative_doc_path = target_file.relative_to(self._root_path)
        relative_file_path = module_record.source_path.relative_to(self._root_path)
        self._logger.debug(
            f"Generating doc {relative_doc_path} for {relative_file_path}"
        )

        docstring = self._get_formatted_docstring(module_record)
        content_lines = self._generate_module_doc_lines(module_record)

        md_doc = MDDocument()
        source_link = MDDocument.render_link(
            f"{module_record.import_string}",
            f"{self._root_relative_path / relative_file_path}",
        )
        md_doc.append(f"> Auto-generated documentation for {source_link} module")

        if docstring:
            # set MD and module record title if it is found in docstring
            title, docstring = md_doc.extract_title(docstring)
            if title:
                module_record.title = title
                md_doc.title = title

            md_doc.append(docstring)
        md_doc.append("\n".join(content_lines))

        if not md_doc.title:
            md_doc.title = module_record.title

        md_doc.ensure_toc_exists()

        modules_toc_lines = self._build_modules_toc_lines(
            module_record.import_string, max_depth=3
        )

        toc_lines = md_doc.toc_section.split("\n")
        breadscrumbs = self._build_breadcrumbs_string(module_record)
        toc_lines[0] = f"- {breadscrumbs}"
        if modules_toc_lines:
            toc_lines.append(f"  - {self.MODULES_NAME}")
            for line in modules_toc_lines:
                toc_lines.append(f"    {line}")

        md_doc.toc_section = "\n".join(toc_lines)

        md_doc.write(self._output_path / md_name)

    def _build_breadcrumbs_string(self, module_record: ModuleRecord) -> Text:
        breadcrumbs: List[Text] = []

        import_string_parts = module_record.get_import_string_parts()
        parent_import_parts: List[Text] = []
        for part in import_string_parts[:-1]:
            parent_import_parts.append(part)
            parent_import = ".".join(parent_import_parts)
            parend_module_record = self._module_records.find_object(parent_import)
            if not parend_module_record:
                breadcrumbs.append(f"`{get_title_from_path_part(part)}`")
                continue

            breadcrumbs.append(
                MDDocument.render_doc_link(
                    parend_module_record.title,
                    md_name=parend_module_record.output_file_name,
                )
            )

        breadcrumbs.append(module_record.title)
        breadcrumbs.insert(
            0, MDDocument.render_doc_link(self._project_name, md_name=self.INDEX_NAME)
        )

        return " / ".join(breadcrumbs)

    def generate_docs(self) -> None:
        """
        Generate all doc files at once.
        """
        self._logger.debug(
            f"Generating docs for {self._root_path.name} to {self._output_path.relative_to(self._root_path.parent)}"
        )

        for module_record in self._module_records:
            self._generate_doc(module_record)
            output_file_path = self._output_path / module_record.output_file_name
            self._replace_local_links(module_record)
            self.replace_links(output_file_path)

    def generate_index(self) -> None:
        """
        Generate `README.md` file with title from `<root>/README.md` and `Modules` section that
        contains a Tree of all modules in the project.
        """
        self._logger.debug(
            f"Generating {self._index_path.relative_to(self._root_path)}"
        )
        self._generate_index()

    def _replace_local_links(self, module_record: ModuleRecord) -> None:
        output_file_name = self._output_path / module_record.output_file_name
        content = output_file_name.read_text()
        file_changed = False
        for obj in module_record.objects:
            search_str = f"`{obj.title}`"
            if search_str in content:
                title = obj.title
                link = MDDocument.render_doc_link(title, anchor=title)
                content = content.replace(search_str, link)
                self._logger.debug(f'Adding local link "{title}" to {output_file_name}')
                file_changed = True

        if file_changed:
            output_file_name.write_text(content)

    def replace_links(self, file_path: Path) -> None:
        """
        Replace all import strings with Markdown links. Only import strings that present in this
        package are replaced, so not dead linsk should be generated.

        ```python
        my_md = Path('doc.md')
        my_md.write_text('I love `' + 'handsdown.indent_trimmer.IndentTrimmer.trim_lines` function!')
        handsdown.replace_links(my_md)

        my_md.read_text()
        # 'I love [IndentTrimmer.trim_lines](./handsdown_indent_trimmer.md#indenttrimmertrim_lines) function!'
        ```

        Arguments:
            file_path -- Path to MD document file.
        """
        content = file_path.read_text()
        file_changed = False
        for match in re.findall(self._docstring_links_re, content):
            module_name = match.replace("`", "")
            module_object_record = self._module_records.find_object(module_name)
            if module_object_record is None:
                continue

            md_name = module_object_record.output_file_name
            if md_name == file_path.name:
                continue

            title = module_object_record.title
            link = MDDocument.render_doc_link(title, anchor=title, md_name=md_name)
            content = content.replace(match, link)
            self._logger.debug(f'Adding link "{title}" to {file_path.name}')
            file_changed = True

        if file_changed:
            file_path.write_text(content)

    def _generate_module_doc_lines(self, module_record: ModuleRecord) -> List[Text]:
        lines = []
        for module_object_record in module_record.objects:
            lines.append(
                f'{"#" * (module_object_record.level + 2)} {module_object_record.title}\n'
            )

            source_path = module_object_record.source_path
            relative_path = source_path.relative_to(self._root_path)
            lines.append(
                f"[🔍 find in source code]({self._root_relative_path}/{relative_path}"
                f"#L{module_object_record.source_line_number})\n"
            )

            signature = self._loader.get_object_signature(module_object_record.object)

            if signature:
                lines.append(f"```python\n{signature}\n```\n")

            formatted_docstring = self._get_formatted_docstring(
                module_record=module_object_record, signature=signature
            )
            if formatted_docstring:
                lines.extend(formatted_docstring.split("\n"))
                lines.append("")

        return lines

    def _get_formatted_docstring(
        self,
        module_record: Union[ModuleRecord, ModuleObjectRecord],
        signature: Optional[Text] = None,
    ) -> Optional[Text]:
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
        output_file_name = module_record.output_file_name
        docstring = module_record.docstring
        if not docstring:
            return None

        section_map = self._docstring_processor.build_sections(docstring)
        if signature:
            related_objects = self._get_objects_from_signature(signature)
            for related_object in related_objects:
                if related_object is module_record:
                    continue

                md_name = ""
                if related_object.output_file_name != output_file_name:
                    md_name = related_object.output_file_name

                title = related_object.title
                link = MDDocument.render_doc_link(title, anchor=title, md_name=md_name)
                section_map.add_line("See also", f"- {link}")
                self._logger.debug(
                    f'Adding link "{title}" to {self._output_path / output_file_name} "See also" section'
                )

        formatted_docstring = section_map.render(header_level=4)
        return formatted_docstring.strip("\n")

    def _get_objects_from_signature(self, signature: Text) -> List[ModuleObjectRecord]:
        result: List[ModuleObjectRecord] = []
        for match in re.findall(self._signature_links_re, signature):
            module_object_record = self._module_records.find_object(match)
            if not module_object_record or module_object_record in result:
                continue

            result.append(module_object_record)

        return result

    def _generate_index(self) -> None:
        """
        Generate new `<output>/README.md`. Copy content from `README.md` and add ToC.
        """
        md_doc = MDDocument()
        readme_path = Path(self._root_path / "README.md")
        if readme_path.exists():
            title, _ = MDDocument.extract_title(readme_path.read_text())
            if title:
                md_doc.title = title

        md_doc.append(f"> Auto-generated `{self._project_name}` documentation index.")
        md_doc.ensure_toc_exists()

        modules_toc_lines = self._build_modules_toc_lines("", max_depth=10)
        if modules_toc_lines:
            toc_lines = md_doc.toc_section.split("\n")
            for line in modules_toc_lines:
                toc_lines.append(f"  {line}")

            md_doc.toc_section = "\n".join(toc_lines)

        md_doc.write(self._output_path / self.INDEX_NAME)

    def _build_modules_toc_lines(
        self, import_string: Text, max_depth: int
    ) -> List[Text]:
        lines: List[Text] = []
        parts: List[Text] = []
        if import_string:
            parts = import_string.split(".")

        last_import_string_parts: List[Text] = []
        for module_record in self._module_records:
            if module_record.import_string == import_string:
                continue

            if not module_record.import_string.startswith(import_string):
                continue

            if len(module_record.import_string.split(".")) > len(parts) + max_depth:
                continue

            md_name = module_record.output_file_name
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
                lines.append(f"{indent}- {title_part}")

            last_import_string_parts = import_string_parts
            indent = "  " * (len(title_parts) - len(parts) - 1)
            lines.append(f"{indent}- [{title_parts[-1]}](./{md_name})")
        return lines
