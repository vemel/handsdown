# Section

[Handsdown API Index](../../README.md#handsdown-api-index) /
[Handsdown](../index.md#handsdown) /
[Processors](./index.md#processors) /
Section

> Auto-generated documentation for [handsdown.processors.section](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section.py) module.

- [Section](#section)
  - [Section](#section-1)
    - [Section().render](#section()render)

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


