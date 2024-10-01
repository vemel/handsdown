# SectionBlock

`Section` block.

[Handsdown API Index](../../README.md#handsdown-api-index) / [Handsdown](../index.md#handsdown) / [Processors](./index.md#processors) / SectionBlock

> Auto-generated documentation for [handsdown.processors.section_block](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_block.py) module.

## SectionBlock

[Show source in section_block.py:9](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_block.py#L9)

`Section` block.

#### Arguments

- `lines` - List of lines.

#### Signature

```python
class SectionBlock:
    def __init__(self, lines: Iterable[str]) -> None:
        ...
```

### SectionBlock().render

[Show source in section_block.py:20](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_block.py#L20)

Render trimmed block lines.

#### Returns

Block lines as a text.

#### Signature

```python
def render(self) -> str:
    ...
```
