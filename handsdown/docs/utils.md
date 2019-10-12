# Utils

- [Utils](#utils)
  - [UserDict](#userdict)
  - [OSEnvironMock](#osenvironmock)
  - [get_anchor_link](#get_anchor_link)
  - [generate_toc_lines](#generate_toc_lines)

> Auto-generated documentation for [utils](../utils.py) module.

## UserDict

[🔍 find in source code](../utils.py#L995)

```python
class UserDict(*args, **kwargs)
```
## OSEnvironMock

[🔍 find in source code](../utils.py#L10)

```python
class OSEnvironMock(*args, **kwargs)
```
## get_anchor_link

[🔍 find in source code](../utils.py#L15)

```python
def get_anchor_link(title: str) -> str
```
Convert title to Github-compatible anchor link.

#### Returns

A test of anchor link.

## generate_toc_lines

[🔍 find in source code](../utils.py#L27)

```python
def generate_toc_lines(content: str, max_depth: int = 3) -> List[str]
```
Generate Table of Contents for markdown text.

#### Arguments

- `content` - Markdown string.
- `max_depth` - Add headers to ToC only up to this level.

#### Returns

A list of ToC lines.
