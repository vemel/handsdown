"""
Utils for markdown rendering.
"""
from typing import Iterable, List, Type, TypeVar

_R = TypeVar("_R", bound="TableOfContents")


class Header:
    """
    Markdown header.

    Arguments:
        title -- Header title
        level -- Header level, 1-6
    """

    def __init__(self, title: str, level: int) -> None:
        self.title: str = title
        self.level: int = level

    @staticmethod
    def get_anchor_link(text: str) -> str:
        """
        Convert header to markdown anchor link.
        """
        return text.strip().replace(" ", "-").replace(".", "").lower()

    @property
    def anchor(self) -> str:
        """
        Anchor link for title.
        """
        return self.get_anchor_link(self.title)

    def render(self) -> str:
        """
        Render menu item to string.
        """
        indent = "  " * (self.level - 1)
        return f"{indent}- [{self.title}](#{self.anchor})"


class TableOfContents:
    """
    MarkDown Table of Contents.

    Arguments:
        headers -- List of headers
    """

    def __init__(self, headers: Iterable[Header]) -> None:
        self.headers: List[Header] = list(headers)

    @classmethod
    def parse(cls: Type[_R], text: str) -> _R:
        """
        Parse table of Contents for MarkDown text.

        Arguments:
            text -- MarkDown text.
        """
        headers: List[Header] = []
        in_codeblock = False
        for line in text.splitlines():
            if line.startswith("```"):
                in_codeblock = not in_codeblock
            if in_codeblock:
                continue
            if not line.startswith("#"):
                continue

            level, title = line.split(" ", 1)
            headers.append(Header(title.strip(), len(level)))

        return cls(headers)

    def render(self, max_level: int = 3) -> str:
        """
        Render ToC to string.
        """
        result: List[str] = []
        for header in self.headers:
            if header.level > max_level:
                continue
            result.append(header.render())
        return "\n".join(result)


def insert_md_toc(text: str, depth: int = 3) -> str:
    """
    Insert Table of Contents before the first second-level header.
    """
    toc = TableOfContents.parse(text)
    toc_lines = toc.render(depth).splitlines()
    lines = text.splitlines()
    result: List[str] = []
    inserted = False
    for line in lines:
        if not inserted and line.startswith("## "):
            result.extend(toc_lines)
            result.append("")
            inserted = True

        result.append(line)

    if not inserted:
        result.extend(toc_lines)
        result.append("")

    return "\n".join(result)
