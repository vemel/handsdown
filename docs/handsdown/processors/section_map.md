# SectionMap

> Auto-generated documentation for [handsdown.processors.section_map](../../../handsdown/processors/section_map.py) module.

- [Index](../../README.md#modules) / [Handsdown](../index.md#handsdown) / [Processors](index.md#processors) / SectionMap
  - [Section](#section)
    - [Section().render](#sectionrender)
  - [SectionBlock](#sectionblock)
    - [SectionBlock().render](#sectionblockrender)
  - [SectionMap](#sectionmap)
    - [SectionMap().sections](#sectionmapsections)
    - [SectionMap().add_block](#sectionmapadd_block)
    - [SectionMap().add_line](#sectionmapadd_line)
    - [SectionMap().trim_block](#sectionmaptrim_block)

## Section

[🔍 find in source code](../../../handsdown/processors/section_map.py#L31)

```python
class Section(title: str, blocks: List[handsdown.processors.section_map.SectionBlock])
```

Dataclass representing a section in a [SectionMap](#sectionmap).

#### Attributes

- `title` - Section title.
- `blocks` - List of line blocks.

### Section().render

[🔍 find in source code](../../../handsdown/processors/section_map.py#L43)

```python
def render() -> str
```

Render section content as a text.

#### Returns

Section lines as a text.

## SectionBlock

[🔍 find in source code](../../../handsdown/processors/section_map.py#L9)

```python
class SectionBlock(lines: List[str])
```

Dataclass representing a [Section](#section) block.

#### Attributes

- `lines` - List of lines.

### SectionBlock().render

[🔍 find in source code](../../../handsdown/processors/section_map.py#L19)

```python
def render() -> str
```

Render trimmed block lines.

#### Returns

Block lines as a text.

## SectionMap

[🔍 find in source code](../../../handsdown/processors/section_map.py#L56)

```python
class SectionMap(*args, **kwargs)
```

Dict-based storage for parsed [Section](#section) list for
`handsdown.processors.base.BaseProcessor`

Key is a [Section](#section) title.
Value is a related [Section](#section) instance.

### SectionMap().sections

[🔍 find in source code](../../../handsdown/processors/section_map.py#L56)

```python
#property getter
def sections() -> Generator[handsdown.processors.section_map.Section, NoneType, NoneType]
```

List [Section](#section) objects.

#### Yields

[Section](#section) objects in order of appearance.

#### See also

- [Section](#section)

### SectionMap().add_block

[🔍 find in source code](../../../handsdown/processors/section_map.py#L86)

```python
def add_block(section_name: str) -> None
```

Add new [SectionBlock](#sectionblock) to section `section_name`.

#### Arguments

- `section_name` - Target section title

### SectionMap().add_line

[🔍 find in source code](../../../handsdown/processors/section_map.py#L65)

```python
def add_line(section_name: str, line: str) -> None
```

Add new `line` to the last [SectionBlock](#sectionblock) of section `section_name`.
If line and section are empty - section is not created.

#### Arguments

- `section_name` - Target section title
- `line` - Line to add

### SectionMap().trim_block

[🔍 find in source code](../../../handsdown/processors/section_map.py#L98)

```python
def trim_block(section_name: str) -> None
```

Delete last empty lines from the last [SectionBlock](#sectionblock).

#### Arguments

section_name - Target section title.
