# SectionBlock

> Auto-generated documentation for [handsdown.processors.section_block](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_block.py) module.

`Section` block.

- [Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / [Processors](index.md#processors) / SectionBlock
    - [SectionBlock](#sectionblock)
        - [SectionBlock().render](#sectionblockrender)

## SectionBlock

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_block.py#L9)

```python
class SectionBlock():
    def __init__(lines: Iterable[str]) -> None:
```

`Section` block.

#### Arguments

- `lines` - List of lines.

### SectionBlock().render

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_block.py#L20)

```python
def render() -> str:
```

Render trimmed block lines.

#### Returns

Block lines as a text.
