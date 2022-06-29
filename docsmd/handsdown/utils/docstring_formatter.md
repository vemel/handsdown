# DocstringFormatter

[Handsdown API Index](../../README.md#handsdown-api-index) /
[Handsdown](../index.md#handsdown) /
[Utils](./index.md#utils) /
DocstringFormatter

> Auto-generated documentation for [handsdown.utils.docstring_formatter](https://github.com/vemel/handsdown/blob/main/handsdown/utils/docstring_formatter.py) module.

## DocstringFormatter

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/docstring_formatter.py#L9)

Translator of docstrings to Markdown format.

#### Arguments

- `docstring` - Raw docstring.

#### Signature

```python
class DocstringFormatter:
    def __init__(self, docstring: str) -> None:
        ...
```

### DocstringFormatter().render

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/docstring_formatter.py#L57)

Get Markdown-friendly docstring.

#### Returns

A cleaned up docstring.

#### Signature

```python
def render(self) -> str:
    ...
```


