# Section

Section in a `SectionMap`.

[Handsdown API Index](../../README.md#handsdown-api-index) / [Handsdown](../index.md#handsdown) / [Processors](./index.md#processors) / Section

> Auto-generated documentation for [handsdown.processors.section](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section.py) module.

## Section

[Show source in section.py:9](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section.py#L9)

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

#### See also

- [SectionBlock](./section_block.md#sectionblock)

### Section().iterate_blocks

[Show source in section.py:35](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section.py#L35)

Iterate over all non-empty Section block lines.

#### Returns

Section block lines.

#### Signature

```python
def iterate_blocks(self) -> Iterable[SectionBlock]:
    ...
```

#### See also

- [SectionBlock](./section_block.md#sectionblock)

### Section().render

[Show source in section.py:22](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section.py#L22)

Render all Section block lines.

#### Returns

Section lines as a text.

#### Signature

```python
def render(self) -> str:
    ...
```
