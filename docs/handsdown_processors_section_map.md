# SectionMap

- [Handsdown](./README.md) / [Handsdown](./handsdown_index.md) / [Processors](./handsdown_processors_index.md) / SectionMap
  - [SectionMap](#sectionmap)
    - [SectionMap().add_line](#sectionmapadd_line)
    - [SectionMap().render](#sectionmaprender)

> Auto-generated documentation for [handsdown.processors.section_map](../handsdown/processors/section_map.py) module

## SectionMap

[🔍 find in source code](../handsdown/processors/section_map.py#L6)

```python
class SectionMap(*args, **kwargs)
```

Storage for parsed section for `handsdown.processors.base.BaseProcessor`

### SectionMap().add_line

[🔍 find in source code](../handsdown/processors/section_map.py#L11)

```python
def add_line(section_name: str, line: str) -> None
```

Add new `line` to section `section_name`.
If line and section are empty - sections is not created.

#### Arguments

section_name - Target section title
line - Line to add

### SectionMap().render

[🔍 find in source code](../handsdown/processors/section_map.py#L26)

```python
def render(header_level: int) -> str
```

Render sections to a string.

#### Arguments

- `header_level` - Level of section title header.

#### Returns

A markdown string.
