"""
Markdown file builder.
"""
import re
import traceback
from pathlib import Path
from types import TracebackType
from typing import List, Optional, Type, TypeVar

from handsdown.settings import ENCODING
from handsdown.utils import extract_md_title
from handsdown.utils.indent_trimmer import IndentTrimmer
from handsdown.utils.path_finder import PathFinder

__all__ = ["MDDocument"]


_MDDocument = TypeVar("_MDDocument", bound="MDDocument")


class MDDocument:
    """
    Markdown file builder.

    Can be used as a context manager, on exit context is written to `path`.

    Examples::

        md_doc = MDDocument(path=Path('output.md'))
        md_doc.append('## New section')
        md_doc.append('some content')
        md_doc.title = 'My doc'
        md_doc.add_toc_if_not_exists()
        md_doc.write()

        # output is indented for readability
        Path('output.md').read_text(encoding=self._encoding)
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

    # Indent in spaces for nested ToC lines
    TOC_INDENT = 4

    _anchor_re = re.compile(r"[^a-z0-9_-]+")
    _escape_title_re = re.compile(r"(_+\S+_+)$")
    _section_separator = "\n\n"

    def __init__(self, path: Path, encoding: str = ENCODING) -> None:
        self._sections: List[str] = []
        self._content = ""
        self._title = ""
        self._subtitle = ""
        self._toc_section = ""
        self._path = path
        self._path_finder = PathFinder(self._path.parent)
        self._encoding = encoding

    def __enter__(self) -> "MDDocument":
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        tb: Optional[TracebackType],
    ) -> None:
        if exc_value:
            traceback.print_tb(tb)
            raise exc_value
        return self.write()

    def read(self, source_path: Optional[Path] = None) -> None:
        """
        Read and parse content from `source_path`.

        Arguments:
            source_path -- Input file path. If not provided - `path` is used.
            encoding -- File encoding.
        """
        path = source_path or self._path
        self._content = path.read_text(encoding=self._encoding)
        self._title = ""
        self._toc_section = ""
        title, content = extract_md_title(self._content)
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

        # extract subtitle from the first section if it is not a title
        if not self._subtitle and self._sections and not self._sections[0].startswith("#"):
            self._subtitle = self._sections.pop(0)

    def add_toc_if_not_exists(self) -> None:
        """
        Check if ToC exists in the document or create one.
        """
        if not self._toc_section:
            self._toc_section = self.generate_toc_section()

    @classmethod
    def get_anchor(cls, title: str) -> str:
        """
        Convert title to a GitHub-friendly anchor link.

        Returns:
            A test of anchor link.
        """
        title = title.lower().replace(" ", "-")
        result = cls._anchor_re.sub("", title)
        return result

    @staticmethod
    def is_toc(section: str) -> bool:
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
    def render_link(cls, title: str, link: str) -> str:
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

    def render_md_doc_link(
        self: _MDDocument, target_md_document: _MDDocument, title: Optional[str] = None
    ) -> str:
        """
        Render Markdown link to `target_md_document` header path with a correct title.

        Arguments:
            target_md_document -- Target `MDDocument`.
            title -- Link text. If not provided `target_md_document.title` is used.

        Returns:
            A string with Markdown link.
        """
        return self.render_doc_link(
            title=title or target_md_document.title,
            anchor=self.get_anchor(target_md_document.title),
            target_path=target_md_document.path,
        )

    def render_doc_link(
        self, title: str, anchor: str = "", target_path: Optional[Path] = None
    ) -> str:
        """
        Render Markdown link to a local MD document, use relative path as a link.

        Examples::

            md_doc = MDDocument(path='/root/parent/doc.md')
            MDDocument.render_doc_link(
                'my title',
                anchor='my-anchor',
                target_path=Path('/root/parent/doc.md'
            )
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
            link = f"{link_path.as_posix()}{link}"

        return self.render_link(title, link)

    def _build_content(self) -> str:
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
        self._path.write_text(content, encoding=self._encoding)

    @property
    def title(self) -> str:
        """
        `MDDocument` title or an empty string.
        """
        return self._title

    @title.setter
    def title(self, title: str) -> None:
        self._title = title
        self._content = self._build_content()

    @property
    def subtitle(self) -> str:
        """
        `MDDocument` subtitle or an empty string.
        """
        return self._subtitle

    @subtitle.setter
    def subtitle(self, subtitle: str) -> None:
        self._subtitle = subtitle
        self._content = self._build_content()

    @property
    def toc_section(self) -> str:
        """
        Document Tree of Contents section or an empty line.
        """
        return self._toc_section

    @toc_section.setter
    def toc_section(self, toc_section: str) -> None:
        self._toc_section = toc_section
        self._content = self._build_content()

    @property
    def sections(self) -> List[str]:
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

    def append(self, content: str) -> None:
        """
        Append `content` to the document.

        Handle trimming and sectioning the content and update
        `title` and `toc_section` fields.

        Arguments:
            content -- Text to add.
        """
        content = IndentTrimmer.trim_empty_lines(content)
        if not content:
            return

        if not self.subtitle and not self.sections and not content.startswith("#"):
            self.subtitle = content
        else:
            self._sections.append(content)

        self._content = self._build_content()

    def append_title(self, title: str, level: int) -> None:
        """
        Append `title` of a given `level` to the document.

        Handle trimming and sectioning the content and update
        `title` and `toc_section` fields.

        Arguments:
            title -- Title to add.
            level -- Title level, number of `#` symbols.
        """
        section_level = "#" * level
        section = f"{section_level} {self._escape_title(title)}"
        self._sections.append(section)
        self._content = self._build_content()

    def generate_toc_section(self, max_depth: int = 3) -> str:
        """
        Generate Table of Contents MD content.

        Arguments:
            max_depth -- Add headers to ToC only up to this level.

        Returns:
            A string with ToC.
        """
        toc_lines = []
        if self.title:
            link = self.render_doc_link(self.title, anchor=self.get_anchor(self.title))
            toc_line = self.get_toc_line(link, level=0)
            toc_lines.append(toc_line)

        sections = [self.title, self.subtitle] + self.sections
        for section in sections:
            if not section.startswith("#"):
                continue

            if "\n" in section:
                continue

            if "# " not in section:
                continue

            section = section.rstrip()

            header_symbols, title = section.split(" ", 1)
            title = title.strip()
            if not title:
                continue

            if header_symbols.replace("#", ""):
                continue

            header_level = len(header_symbols)
            if header_level > max_depth:
                continue

            link = self.render_doc_link(title, anchor=self.get_anchor(title))
            toc_line = self.get_toc_line(link, level=header_level - 1)
            toc_lines.append(toc_line)

        return "\n".join(toc_lines)

    @classmethod
    def get_toc_line(cls, line: str, level: int = 0) -> str:
        """
        Get ToC `line` of given `level`.

        Arguments:
            line -- Line to prepare.
            level -- Line level, starts with `0`.

        Returns:
            Ready to insert ToC line.
        """
        indent = cls.TOC_INDENT * level
        return IndentTrimmer.indent_line(f"- {line}", indent)

    @classmethod
    def _escape_title(cls, title: str) -> str:
        for match in cls._escape_title_re.findall(title):
            title = title.replace(match, match.replace("_", "\\_"))
        return title
