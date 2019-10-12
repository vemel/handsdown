# Handsdown: Utils

- [Handsdown: Utils](#handsdown-utils)
  - [get_anchor_link](#get_anchor_link)
  - [generate_toc_lines](#generate_toc_lines)

> Auto-generated documentation for [handsdown.utils](../handsdown/utils.py) module.

## get_anchor_link

[🔍 find in source code](../handsdown/utils.py#L9)

```python
def get_anchor_link(title: str) -> str
```
Convert title to Github-compatible anchor link.

#### Returns

A test of anchor link.

## generate_toc_lines

[🔍 find in source code](../handsdown/utils.py#L21)

```python
def generate_toc_lines(content: str, max_depth: int = 3) -> List[str]
```
Generate Table of Contents for markdown text.

#### Arguments

- `content` - Markdown string.
- `max_depth` - Add headers to ToC only up to this level.

#### Returns

A list of ToC lines.
