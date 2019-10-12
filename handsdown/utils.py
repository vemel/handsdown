import re

from collections import UserDict
from typing import Text, List


anchor_re = re.compile(r"[^a-z0-9_-]+")


class OSEnvironMock(UserDict):
    def __missing__(self, key):
        return "env"


def get_anchor_link(title: Text) -> Text:
    """
    Convert title to Github-compatible anchor link.

    Returns:
        A test of anchor link.
    """
    title = title.lower().replace(" ", "-")
    result = anchor_re.sub("", title)
    return result


def generate_toc_lines(content: Text, max_depth: int = 3) -> List[Text]:
    """
    Generate Table of Contents for markdown text.

    Arguments:
        content -- Markdown string.
        max_depth -- Add headers to ToC only up to this level.

    Returns:
        A list of ToC lines.
    """
    toc_lines = []
    in_codeblock = False
    for line in content.split("\n"):
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
        anchor = get_anchor_link(title)
        link = f"[{title}](#{anchor})"
        toc_lines.append(f'{"  " * (header_level- 1)}- {link}')

    return toc_lines
