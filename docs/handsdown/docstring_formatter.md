# DocstringFormatter

> Auto-generated documentation for [handsdown.docstring_formatter](../../handsdown/docstring_formatter.py) module.

- [Index](../README.md#modules) / [Handsdown](index.md#handsdown) / DocstringFormatter
  - [DocstringFormatter](#docstringformatter)
    - [DocstringFormatter().render](#docstringformatterrender)

## DocstringFormatter

[🔍 find in source code](../../handsdown/docstring_formatter.py#L9)

```python
class DocstringFormatter(docstring: str)
```

Clean up docstring to be compatible with Markdown format.

#### Arguments

- `docstring` - Raw docstring.

### DocstringFormatter().render

[🔍 find in source code](../../handsdown/docstring_formatter.py#L55)

```python
def render() -> str
```

Get Markdown-friendly docstring.

#### Returns

A cleaned up docstring.
