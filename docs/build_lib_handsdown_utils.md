# Build: Lib: Handsdown: Utils

- [Build: Lib: Handsdown: Utils](#build-lib-handsdown-utils)
  - [OSEnvironMock](#osenvironmock)
  - [get_anchor_link](#get_anchor_link)
  - [generate_toc_lines](#generate_toc_lines)

> Auto-generated documentation for [build.lib.handsdown.utils](../build/lib/handsdown/utils.py) module.

## OSEnvironMock

[🔍 find in source code](../build/lib/handsdown/utils.py#L10)

```python
class OSEnvironMock(*args, **kwargs)
```
## get_anchor_link

[🔍 find in source code](../build/lib/handsdown/utils.py#L15)

```python
def get_anchor_link(title: str) -> str
```
Convert title to Github-compatible anchor link.

#### Returns

A test of anchor link.

## generate_toc_lines

[🔍 find in source code](../build/lib/handsdown/utils.py#L27)

```python
def generate_toc_lines(content: str, max_depth: int = 3) -> List[str]
```
Generate Table of Contents for markdown text.

#### Arguments

- `content` - Markdown string.
- `max_depth` - Add headers to ToC only up to this level.

#### Returns

A list of ToC lines.
