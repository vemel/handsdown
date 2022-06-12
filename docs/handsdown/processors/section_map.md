# SectionMap

> Auto-generated documentation for [handsdown.processors.section_map](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_map.py) module.

Module for splitting docstring into `Section` groups.

- [Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / [Processors](index.md#processors) / SectionMap
    - [SectionMap](#sectionmap)
        - [SectionMap().\_\_iter\_\_](#sectionmap__iter__)
        - [SectionMap().add_block](#sectionmapadd_block)
        - [SectionMap().add_line](#sectionmapadd_line)
        - [SectionMap().add_line_indent](#sectionmapadd_line_indent)
        - [SectionMap().trim_block](#sectionmaptrim_block)

## SectionMap

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_map.py#L11)

```python
class SectionMap():
    def __init__() -> None:
```

Dict-based storage for parsed `Section` list.

Used for [BaseDocstringProcessor](base.md#basedocstringprocessor).

Key is a `Section` title.
Value is a related `Section` instance.

### SectionMap().\_\_iter\_\_

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_map.py#L95)

```python
def __iter__() -> Iterator[Section]:
```

Iterate over existing `Section` objects.

#### Yields

`Section` objects in order of appearance.

### SectionMap().add_block

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_map.py#L65)

```python
def add_block(section_name: str) -> None:
```

Add new `SectionBlock` to section `section_name`.

If `Section` does not exist - it is not created.

#### Arguments

- `section_name` - Target section title

### SectionMap().add_line

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_map.py#L42)

```python
def add_line(section_name: str, line: str) -> None:
```

Add new `line` to the last `SectionBlock` of section `section_name`.

If line and section are empty - section is not created.

#### Arguments

- `section_name` - Target section title
- `line` - Line to add

### SectionMap().add_line_indent

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_map.py#L26)

```python
def add_line_indent(section_name: str, line: str) -> None:
```

Add line respecting indent of the current section block.

#### Arguments

- `section_name` - Target section title
- `line` - Line to add

### SectionMap().trim_block

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_map.py#L79)

```python
def trim_block(section_name: str) -> None:
```

Delete last empty lines from the last `SectionBlock`.

If `Section` does not exist - it is not created.

#### Arguments

- `section_name` - Target section title.
