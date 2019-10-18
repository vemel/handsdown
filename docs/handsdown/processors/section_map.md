# SectionMap

> Auto-generated documentation for [handsdown.processors.section_map](https://github.com/vemel/handsdown/blob/master/handsdown/processors/section_map.py) module..

Module for splitting docstring into `Section` groups.

- [Index](../../README.md#modules) / [Handsdown](../index.md#handsdown) / [Processors](index.md#processors) / SectionMap
  - [Section](#section)
  - [SectionBlock](#sectionblock)
    - [SectionBlock().render](#sectionblockrender)
  - [SectionMap](#sectionmap)
    - [SectionMap().sections](#sectionmapsections)
    - [SectionMap().add_block](#sectionmapadd_block)
    - [SectionMap().add_line](#sectionmapadd_line)
    - [SectionMap().trim_block](#sectionmaptrim_block)

## Section

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/processors/section_map.py#L35)

```python
class Section(title: str, blocks: List[handsdown.processors.section_map.SectionBlock])
```

Dataclass representing a section in a [SectionMap](#sectionmap).

#### Attributes

- `title` - Section title.
- `blocks` - List of line blocks.

## SectionBlock

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/processors/section_map.py#L13)

```python
class SectionBlock(lines: List[str])
```

Dataclass representing a [Section](#section) block.

#### Attributes

- `lines` - List of lines.

### SectionBlock().render

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/processors/section_map.py#L23)

```python
def render() -> str
```

Render trimmed block lines.

#### Returns

Block lines as a text.

## SectionMap

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/processors/section_map.py#L48)

```python
class SectionMap(*args, **kwargs)
```

Dict-based storage for parsed [Section](#section) list for
`handsdown.processors.base.BaseProcessor`

Key is a [Section](#section) title.
Value is a related [Section](#section) instance.

### SectionMap().sections

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/processors/section_map.py#L48)

```python
#property getter
def sections() -> Generator[handsdown.processors.section_map.Section, NoneType, NoneType]
```

Iterate over existing [Section](#section) objects.

#### Yields

[Section](#section) objects in order of appearance.

#### See also

- [Section](#section)

### SectionMap().add_block

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/processors/section_map.py#L78)

```python
def add_block(section_name: str) -> None
```

Add new [SectionBlock](#sectionblock) to section `section_name`.
If [Section](#section) does not exist - it is not created.

#### Arguments

- `section_name` - Target section title

### SectionMap().add_line

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/processors/section_map.py#L57)

```python
def add_line(section_name: str, line: str) -> None
```

Add new `line` to the last [SectionBlock](#sectionblock) of section `section_name`.
If line and section are empty - section is not created.

#### Arguments

- `section_name` - Target section title
- `line` - Line to add

### SectionMap().trim_block

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/processors/section_map.py#L91)

```python
def trim_block(section_name: str) -> None
```

Delete last empty lines from the last [SectionBlock](#sectionblock).
If [Section](#section) does not exist - it is not created.

#### Arguments

section_name - Target section title.
