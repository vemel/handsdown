"""
Markdown file builder.
"""
from __future__ import annotations

import re
from types import TracebackType
from typing import Text, Optional, List, Tuple, Type
from pathlib import Path

from handsdown.indent_trimmer import IndentTrimmer
from handsdown.path_finder import PathFinder


__all__ = ["MDDocument"]


class MDDocument:
    """
    Markdown file builder.

    Can be used as a context manager, on exit context is written to `path`.

    Examples::

        md_doc = MDDocument(path=Path('output.md'))
        md_doc.append('## New section')
        md_doc.append('some content')
        md_doc.title = 'My doc'
        md_doc.ensure_toc_exists()
        md_doc.write()

        # output is indented for readability
        Path('output.md').read_text()
        '''# My doc

        - [My doc](#my-doc)
          - [New section](#new-section)

        ## New section

        some content
        '''

        with MDDocument(path=Path('output.md')) as md_document:
            md_document.title = 'My doc'
            md_doc.append_title('New section', level=2)
            md_doc.append('New line')

    Arguments:
        path -- Path to store document.
    """

    _anchor_re = re.compile(r"[^a-z0-9_-]+")
    _escape_title_re = re.compile(r"(_+\S+_+)$")
    _section_separator = "\n\n"

    def __init__(self, path: Path) -> None:
        self._sections: List[Text] = []
        self._content = ""
        self._title = ""
        self._subtitle = ""
        self._toc_section = ""
        self._path = path
        self._path_finder = PathFinder(self._path.parent)

    def __enter__(self) -> MDDocument:
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        if exc_type:
            raise exc_type
        return self.write()

    def read(self) -> None:
        """
        Read and parse content from `path`.
        """
        self._content = self._path.read_text()
        self._title = ""
        self._toc_section = ""
        title, content = self.extract_title(self._content)
        if title:
            self._title = title

        sections = content.split(self._section_separator)
        self._sections = []
        for section in sections:
            section = IndentTrimmer.trim_empty_lines(section)
            if not section:
                continue
            if self.is_toc(section) and not self._toc_section:
                self._toc_section = section
                if self._sections:
                    self._subtitle = self._section_separator.join(self._sections)
                    self._sections = []
                continue

            self._sections.append(section)

    def ensure_toc_exists(self) -> None:
        """
        Check if ToC exists in the document or create one.
        """
        if not self._toc_section:
            self._toc_section = self.generate_toc_section()

    @classmethod
    def get_anchor(cls, title: Text) -> Text:
        """
        Convert title to a GitHub-friendly anchor link.

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

    @classmethod
    def render_link(cls, title: Text, link: Text) -> Text:
        """
        Render Markdown link wih escaped title.

        Examples::

            MDDocument.render_link('my title', 'doc.md#test')
            '[my title](doc.md#test)'

            MDDocument.render_link('MyClass.__init__', 'my.md')
            '[MyClass.__init__](doc.md#my.md)'

        Arguments:
            title -- Link text.
            link -- Link target.

        Returns:
            A string with Markdown link.
        """
        return f"[{title}]({link})"

    def render_doc_link(
        self, title: Text, anchor: Text = "", target_path: Optional[Path] = None
    ) -> Text:
        """
        Render Markdown link to a local MD document, use relative path as a link.

        Examples::

            md_doc = MDDocument(path='/root/parent/doc.md')
            MDDocument.render_doc_link('my title', anchor='my-anchor', target_path=Path('/root/parent/doc.md')
            '[my title](#my-anchor)'

            MDDocument.render_doc_link('my title', target_path=Path('/root/parent/other.md'))
            '[my title](other.md)'

            MDDocument.render_doc_link('my title', anchor='my-anchor', target_path=Path('doc.md'))
            '[my title](doc.md#my-anchor)'

            MDDocument.render_doc_link('my title', anchor='my-anchor')
            '[my title](#my-anchor)'

        Arguments:
            title -- Link text.
            anchor -- Unescaped or escaped anchor tag.
            target_path -- Target MDDocument path.

        Returns:
            A string with Markdown link.
        """
        link = ""
        if anchor:
            link = f"#{anchor}"
        if target_path and target_path != self._path:
            link_path = self._path_finder.relative(target_path)
            link = f"{link_path}{link}"

        return self.render_link(title, link)

    def _build_content(self) -> Text:
        sections = []
        if self._title:
            sections.append(f"# {self._title}")
        if self._subtitle:
            sections.append(self._subtitle)
        if self._toc_section:
            sections.append(self._toc_section)

        sections.extend(self._sections)
        return self._section_separator.join(sections) + "\n"

    def write(self) -> None:
        """
        Write MD content to `path`.
        """
        content = self._build_content()
        self._path_finder.mkdir()
        self._path.write_text(content)

    @property
    def title(self) -> Text:
        """
        `MDDocument` title or an empty string.
        """
        return self._title

    @title.setter
    def title(self, title: Text) -> None:
        self._title = title
        self._content = self._build_content()

    @property
    def subtitle(self) -> Text:
        """
        `MDDocument` subtitle or an empty string.
        """
        return self._subtitle

    @subtitle.setter
    def subtitle(self, subtitle: Text) -> None:
        self._subtitle = subtitle
        self._content = self._build_content()

    @property
    def toc_section(self) -> Text:
        """
        Document Tree of Contents section or an empty line.
        """
        return self._toc_section

    @toc_section.setter
    def toc_section(self, toc_section: Text) -> None:
        self._toc_section = toc_section

    @property
    def sections(self) -> List[Text]:
        """
        All non-special `sections` of the document.
        """
        return self._sections

    @property
    def path(self) -> Path:
        """
        Output path of the document.
        """
        return self._path

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

    def append_title(self, title: Text, level: int) -> None:
        """
        Append `title` of a given `level` to the document.
        Handle trimming and sectioning the content and update
        `title` and `toc_section` fields.

        Arguments:
            title -- Title to add.
            level -- Title level, number of `#` symbols.
        """
        section = f'{"#" * level} {self._escape_title(title)}'
        self._sections.append(section)
        self._content = self._build_content()

    def generate_toc_section(self, max_depth: int = 3) -> Text:
        """
        Generate Table of Contents MD content.

        Arguments:
            max_depth -- Add headers to ToC only up to this level.

        Returns:
            A string with ToC.
        """
        toc_lines = []

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
            link = self.render_doc_link(title, anchor=self.get_anchor(title))
            toc_lines.append(f'{"  " * (header_level- 1)}- {link}')

        return "\n".join(toc_lines)

    @staticmethod
    def extract_title(content: Text) -> Tuple[Text, Text]:
        """
        Extract title from the first line of content.
        If title is present -  return a title and a remnaing content.
        if not - return an empty title and untouched content.

        Examples::

            MDDocument.extract_title('# Title\\ncontent')
            ('Title', 'content')

            MDDocument.extract_title('no title\\ncontent')
            ('', 'no title\\ncontent')

        Returns:
            A tuple fo title and remaining content.
        """
        title = ""
        if content.startswith("# "):
            if "\n" not in content:
                content = f"{content}\n"

            title_line, content = content.split("\n", 1)
            title = title_line.split(" ", 1)[-1]

        return title, content

    @classmethod
    def _escape_title(cls, title: Text) -> Text:
        for match in cls._escape_title_re.findall(title):
            title = title.replace(match, match.replace("_", "\\_"))
        return title
