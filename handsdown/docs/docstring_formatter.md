# DocstringFormatter

> Auto-generated documentation for [docstring_formatter](../docstring_formatter.py) module..

Translator of docstrings to Markdown format.

- [Index](README.md#modules) / DocstringFormatter
  - [DocstringFormatter](#docstringformatter)
    - [DocstringFormatter().render](#docstringformatterrender)

## DocstringFormatter

[🔍 find in source code](../docstring_formatter.py#L14)

```python
class DocstringFormatter(docstring: Text) -> None
```

Translator of docstrings to Markdown format.

#### Arguments

- `docstring` - Raw docstring.

### DocstringFormatter().render

[🔍 find in source code](../docstring_formatter.py#L63)

```python
def render() -> Text
```

Get Markdown-friendly docstring.

#### Returns

A cleaned up docstring.
