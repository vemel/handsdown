# DocstringFormatter

> Auto-generated documentation for [handsdown.utils.docstring_formatter](https://github.com/vemel/handsdown/blob/main/handsdown/utils/docstring_formatter.py) module.

Translator of docstrings to Markdown format.

- [Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / [Utils](index.md#utils) / DocstringFormatter
    - [DocstringFormatter](#docstringformatter)
        - [DocstringFormatter().render](#docstringformatterrender)

## DocstringFormatter

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/utils/docstring_formatter.py#L9)

```python
class DocstringFormatter():
    def __init__(docstring: str) -> None:
```

Translator of docstrings to Markdown format.

#### Arguments

- `docstring` - Raw docstring.

### DocstringFormatter().render

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/utils/docstring_formatter.py#L57)

```python
def render() -> str:
```

Get Markdown-friendly docstring.

#### Returns

A cleaned up docstring.
