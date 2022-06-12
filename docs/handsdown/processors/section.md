# Section

> Auto-generated documentation for [handsdown.processors.section](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section.py) module.

Section in a `SectionMap`.

- [Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / [Processors](index.md#processors) / Section
    - [Section](#section)
        - [Section().render](#sectionrender)

## Section

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section.py#L9)

```python
class Section():
    def __init__(title: str, blocks: Iterable[SectionBlock]) -> None:
```

Section in a `SectionMap`.

#### Arguments

- `title` - Section title.
- `blocks` - List of line blocks.

### Section().render

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section.py#L22)

```python
def render() -> str:
```

Render all Section block lines.

#### Returns

Section lines as a text.
