# SectionMap

> Auto-generated documentation for [handsdown.processors.section_map](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_map.py) module.

Module for splitting docstring into `Section` groups.

- [Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / [Processors](index.md#processors) / SectionMap
    - [Section](#section)
        - [Section().render](#sectionrender)
    - [SectionBlock](#sectionblock)
        - [SectionBlock().render](#sectionblockrender)
    - [SectionMap](#sectionmap)
        - [SectionMap().add_block](#sectionmapadd_block)
        - [SectionMap().add_line](#sectionmapadd_line)
        - [SectionMap().add_line_indent](#sectionmapadd_line_indent)
        - [SectionMap().sections](#sectionmapsections)
        - [SectionMap().trim_block](#sectionmaptrim_block)

## Section

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_map.py#L31)

```python
class Section():
    def __init__(title: str, blocks: Iterable[SectionBlock]) -> None:
```

Dataclass representing a section in a [SectionMap](#sectionmap).

#### Arguments

- `title` - Section title.
- `blocks` - List of line blocks.

### Section().render

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_map.py#L44)

```python
def render() -> str:
```

Render all Section block lines.

#### Returns

Section lines as a text.

## SectionBlock

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_map.py#L9)

```python
class SectionBlock():
    def __init__(lines: Iterable[str]) -> None:
```

Dataclass representing a [Section](#section) block.

#### Arguments

- `lines` - List of lines.

### SectionBlock().render

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_map.py#L20)

```python
def render() -> str:
```

Render trimmed block lines.

#### Returns

Block lines as a text.

## SectionMap

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_map.py#L58)

```python
class SectionMap(dict):
    def __init__() -> None:
```

Dict-based storage for parsed [Section](#section) list.

Used for [BaseDocstringProcessor](base.md#basedocstringprocessor).

Key is a [Section](#section) title.
Value is a related [Section](#section) instance.

### SectionMap().add_block

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_map.py#L111)

```python
def add_block(section_name: str) -> None:
```

Add new [SectionBlock](#sectionblock) to section `section_name`.

If [Section](#section) does not exist - it is not created.

#### Arguments

- `section_name` - Target section title

### SectionMap().add_line

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_map.py#L88)

```python
def add_line(section_name: str, line: str) -> None:
```

Add new `line` to the last [SectionBlock](#sectionblock) of section `section_name`.

If line and section are empty - section is not created.

#### Arguments

- `section_name` - Target section title
- `line` - Line to add

### SectionMap().add_line_indent

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_map.py#L72)

```python
def add_line_indent(section_name: str, line: str) -> None:
```

Add line respecting indent of the current section block.

#### Arguments

- `section_name` - Target section title
- `line` - Line to add

### SectionMap().sections

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_map.py#L141)

```python
@property
def sections() -> Iterator[Section]:
```

Iterate over existing [Section](#section) objects.

#### Yields

[Section](#section) objects in order of appearance.

### SectionMap().trim_block

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_map.py#L125)

```python
def trim_block(section_name: str) -> None:
```

Delete last empty lines from the last [SectionBlock](#sectionblock).

If [Section](#section) does not exist - it is not created.

#### Arguments

- `section_name` - Target section title.
