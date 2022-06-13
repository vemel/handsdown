# Section

[Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / [Processors](index.md#processors) / Section

> Auto-generated documentation for [handsdown.processors.section](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section.py) module.

- [Section](#section)

## Section

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section.py#L9)

Section in a `SectionMap`.

#### Arguments

- `title` - Section title.
- `blocks` - List of line blocks.

#### Signature

```python
class Section:
    def __init__(self, title: str, blocks: Iterable[SectionBlock]) -> None:
        ...
```

### Section().render

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section.py#L22)

Render all Section block lines.

#### Returns

Section lines as a text.

#### Signature

```python
def render(self) -> str:
    ...
```


