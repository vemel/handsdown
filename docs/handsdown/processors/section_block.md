# SectionBlock

[Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / [Processors](index.md#processors) / SectionBlock

> Auto-generated documentation for [handsdown.processors.section_block](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_block.py) module.

- [SectionBlock](#sectionblock)

## SectionBlock

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_block.py#L9)

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

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_block.py#L20)

Render trimmed block lines.

#### Returns

Block lines as a text.

#### Signature

```python
def render(self) -> str:
    ...
```


