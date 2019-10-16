# SectionMap

> Auto-generated documentation for [handsdown.processors.section_map](../handsdown/processors/section_map.py) module.

- [Handsdown](./README.md#handsdown) / [Handsdown](./handsdown_index.md#handsdown) / [Processors](./handsdown_processors_index.md#processors) / SectionMap
  - [Section](#section)
  - [SectionBlock](#sectionblock)
  - [SectionMap](#sectionmap)
    - [SectionMap().add_block](#sectionmapadd_block)
    - [SectionMap().add_line](#sectionmapadd_line)
    - [SectionMap().render](#sectionmaprender)
    - [SectionMap().trim_block](#sectionmaptrim_block)

## Section

[🔍 find in source code](../handsdown/processors/section_map.py#L20)

```python
class Section(title: str, blocks: List[handsdown.processors.section_map.SectionBlock])
```

Dataclass representing a section in a [SectionMap](#sectionmap).

#### Attributes

- `title` - Section title.
- `blocks` - List of line blocks.

## SectionBlock

[🔍 find in source code](../handsdown/processors/section_map.py#L8)

```python
class SectionBlock(lines: List[str])
```

Dataclass representing a [Section](#section) block.

#### Attributes

- `lines` - List of lines.

## SectionMap

[🔍 find in source code](../handsdown/processors/section_map.py#L33)

```python
class SectionMap(*args, **kwargs)
```

Dict-based storage for parsed [Section](#section) list for
`handsdown.processors.base.BaseProcessor`

Key is a [Section](#section) title.
Value is a related [Section](#section) instance.

### SectionMap().add_block

[🔍 find in source code](../handsdown/processors/section_map.py#L63)

```python
def add_block(section_name: str) -> None
```

Add new [SectionBlock](#sectionblock) to section `section_name`.

#### Arguments

- `section_name` - Target section title

### SectionMap().add_line

[🔍 find in source code](../handsdown/processors/section_map.py#L42)

```python
def add_line(section_name: str, line: str) -> None
```

Add new `line` to the last [SectionBlock](#sectionblock) of section `section_name`.
If line and section are empty - section is not created.

#### Arguments

- `section_name` - Target section title
- `line` - Line to add

### SectionMap().render

[🔍 find in source code](../handsdown/processors/section_map.py#L89)

```python
def render(header_level: int) -> str
```

Render sections to a string.

#### Arguments

- `header_level` - Level of section title header.

#### Returns

A markdown string.

### SectionMap().trim_block

[🔍 find in source code](../handsdown/processors/section_map.py#L75)

```python
def trim_block(section_name: str) -> None
```

Delete last empty lines from the last [SectionBlock](#sectionblock).

#### Arguments

section_name - Target section title.
