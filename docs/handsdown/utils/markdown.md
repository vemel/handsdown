# Markdown

[Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / [Utils](index.md#utils) / Markdown

> Auto-generated documentation for [handsdown.utils.markdown](https://github.com/vemel/handsdown/blob/main/handsdown/utils/markdown.py) module.

- [Markdown](#markdown)
  - [Header](#header)
    - [Header().render](#header()render)
  - [TableOfContents](#tableofcontents)
    - [TableOfContents.parse](#tableofcontentsparse)
    - [TableOfContents().render](#tableofcontents()render)
  - [insert_md_toc](#insert_md_toc)

## Header

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/markdown.py#L9)

Markdown header.

#### Arguments

- `title` - Header title
- `level` - Header level, 1-6
- `anchor` - Anchor link

#### Signature

```python
class Header:
    def __init__(self, title: str, level: int, anchor: str) -> None:
        ...
```

### Header().render

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/markdown.py#L24)

Render menu item to string.

#### Signature

```python
def render(self) -> str:
    ...
```



## TableOfContents

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/markdown.py#L32)

MarkDown Table of Contents.

#### Arguments

- `headers` - List of headers

#### Signature

```python
class TableOfContents:
    def __init__(self, headers: Iterable[Header]) -> None:
        ...
```

### TableOfContents.parse

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/markdown.py#L43)

Parse table of Contents for MarkDown text.

#### Arguments

- `text` - MarkDown text.

#### Signature

```python
@classmethod
def parse(cls: Type[_R], text: str) -> _R:
    ...
```

### TableOfContents().render

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/markdown.py#L71)

Render ToC to string.

#### Signature

```python
def render(self, max_level: int = 3) -> str:
    ...
```



## insert_md_toc

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/markdown.py#L87)

Insert Table of Contents before the first second-level header.

#### Signature

```python
def insert_md_toc(text: str, depth: int = 3) -> str:
    ...
```


