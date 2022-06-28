"""
Utils for markdown rendering.
"""
from typing import Dict, Iterable, List, Type, TypeVar

_R = TypeVar("_R", bound="TableOfContents")


class Header:
    """
    Markdown header.

    Arguments:
        title -- Header title
        level -- Header level, 1-6
        anchor -- Anchor link
    """

    def __init__(self, title: str, level: int, anchor: str) -> None:
        self.title: str = title
        self.level: int = level
        self.anchor: str = anchor

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
        title_counter: Dict[str, int] = {}
        for line in text.splitlines():
            if line.startswith("```"):
                in_codeblock = not in_codeblock
            if in_codeblock:
                continue
            if not line.startswith("#"):
                continue

            level, title = line.split(" ", 1)
            title = title.strip()
            title_counter[title] = title_counter.get(title, 0) + 1
            anchor_link = cls._get_anchor_link(title)
            if title_counter[title] > 1:
                anchor_link = f"{anchor_link}-{title_counter[title] - 1}"
            headers.append(Header(title, len(level), anchor_link))
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

    @staticmethod
    def _get_anchor_link(text: str) -> str:
        return text.strip().replace(" ", "-").replace(".", "").lower()


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
