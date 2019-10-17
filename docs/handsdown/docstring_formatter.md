# DocstringFormatter

> Auto-generated documentation for [handsdown.docstring_formatter](../../handsdown/docstring_formatter.py) module.

- [Index](../README.md#handsdown-index) / [Handsdown](index.md#handsdown) / [DocstringFormatter](#docstringformatter) / DocstringFormatter
  - [DocstringFormatter](#docstringformatter)
    - [DocstringFormatter._cleanup](#docstringformatter_cleanup)
    - [DocstringFormatter().render](#docstringformatterrender)

## DocstringFormatter

[🔍 find in source code](../../handsdown/docstring_formatter.py#L9)

```python
class DocstringFormatter(docstring: str)
```

Clean up docstring to be compatible with Markdown format.

#### Arguments

- `docstring` - Raw docstring.

### DocstringFormatter._cleanup

[🔍 find in source code](../../handsdown/docstring_formatter.py#L23)

```python
def _cleanup(docstring: str) -> str
```

Fix multiline docstrings starting with no newline after quotes.

#### Arguments

- `docstring` - Raw docstring.

#### Returns

Aligned docstring.

### DocstringFormatter().render

[🔍 find in source code](../../handsdown/docstring_formatter.py#L55)

```python
def render() -> str
```

Get Markdown-friendly docstring.

#### Returns

A cleaned up docstring.
