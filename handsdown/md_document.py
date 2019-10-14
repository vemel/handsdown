import re
from typing import Text, Optional, List
from pathlib import Path

from handsdown.indent_trimmer import IndentTrimmer


class MDDocument:
    """
    MD file wrapper. Controls docuemnt title and Table of Contents.

    Examples:

        ```python
        md_doc = MDDocument('hello')
        md_doc.append('## New section')
        md_doc.append('some content')
        md_doc.title = 'My doc'
        md_doc.ensure_toc_exists()
        md_doc.write(Path('output.md'))

        Path('output.md').read_text()
        # # My doc
        #
        # - [My doc](#my-doc)
        #   - [New section](#new-section)
        #
        # ## New section
        #
        # some content
        #
        ```

    Arguments:
        content -- Initial MD content.
    """

    _anchor_re = re.compile(r"[^a-z0-9_-]+")
    _section_separator = "\n\n"

    def __init__(self, content: Text = "") -> None:
        self._sections: List[Text] = []
        self._content = ""
        self.title: Optional[Text] = None
        self.toc_section: Optional[Text] = None
        if content:
            self.append(content)

    def _parse_content(self) -> None:
        content = self._content
        self.title = None
        self.toc_section = None
        if content.startswith("# "):
            title_line, content = content.split("\n", 1)
            self.title = title_line.split(" ", 1)[1]

        sections = content.split(self._section_separator)
        self._sections = []
        for section_index, section in enumerate(sections):
            section = IndentTrimmer.trim_empty_lines(section)
            if not section:
                continue
            if self.is_toc(section) and not self.toc_section and section_index < 2:
                self.toc_section = section
                continue

            self._sections.append(section)

    def ensure_toc_exists(self) -> None:
        """
        Check if ToC exists in the document or create one.
        """
        if not self.toc_section:
            self.toc_section = self.generate_toc_section()

    @classmethod
    def get_anchor_link(cls, title: Text) -> Text:
        """
        Convert title to Github-compatible anchor link.

        Returns:
            A test of anchor link.
        """
        title = title.lower().replace(" ", "-")
        result = cls._anchor_re.sub("", title)
        return result

    @staticmethod
    def is_toc(section: Text) -> bool:
        """
        Check if the section is Tree of Contents.

        Returns:
            True the section is ToC.
        """
        lines = section.split("\n")
        if len(lines) < 2:
            return False
        for line in lines:
            if "- [" not in line:
                return False

        return True

    def _render_link(self, title: Text, md_name: Optional[Text] = None) -> Text:
        anchor = self.get_anchor_link(title)
        if md_name:
            return f"[{title}](./{md_name}#{anchor})"

        return f"[{title}](#{anchor})"

    def _build_content(self) -> Text:
        sections = []
        if self.title:
            sections.append(f"# {self.title}")
        if self.toc_section:
            sections.append(self.toc_section)

        sections.extend(self._sections)
        return self._section_separator.join(sections) + "\n"

    def write(self, path: Path) -> None:
        """
        Write MD content to `path`.

        Arguments:
            path -- Output path.
        """
        content = self._build_content()
        path.write_text(content)

    def append(self, content: Text) -> None:
        """
        Append `content` to the document.
        Handle trimming and sectioning the content and update
        `title` and `toc_section` fields.

        Arguments:
            content -- Text to add.
        """
        for section in content.split(self._section_separator):
            section = IndentTrimmer.trim_empty_lines(section)
            if section:
                self._sections.append(section)

        self._content = self._build_content()
        self._parse_content()

    def generate_toc_section(self, max_depth: int = 3) -> Text:
        """
        Generate Table of Contents MD content.

        Arguments:
            max_depth -- Add headers to ToC only up to this level.

        Returns:
            A string with ToC.
        """
        toc_lines = []
        if self.title:
            toc_lines.append(f"- {self._render_link(self.title)}")

        in_codeblock = False
        for line in self._content.split("\n"):
            line = line.strip()
            if line.count("```") > 1:
                continue

            if line.startswith("```"):
                in_codeblock = not in_codeblock

            if in_codeblock:
                continue

            if not line.startswith("#"):
                continue

            header_symbols = line.split(" ")[0]
            if header_symbols.replace("#", ""):
                continue

            header_level = len(header_symbols)
            if header_level > max_depth:
                continue

            title = line.split(" ", 1)[-1].strip()
            link = self._render_link(title)
            toc_lines.append(f'{"  " * (header_level- 1)}- {link}')

        return "\n".join(toc_lines)
