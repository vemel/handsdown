# SectionMap

[Handsdown API Index](../../README.md#handsdown-api-index) /
[Handsdown](../index.md#handsdown) /
[Processors](./index.md#processors) /
SectionMap

> Auto-generated documentation for [handsdown.processors.section_map](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_map.py) module.

- [SectionMap](#sectionmap)
  - [SectionMap](#sectionmap-1)
    - [SectionMap().__iter__](#sectionmap()__iter__)
    - [SectionMap().add_block](#sectionmap()add_block)
    - [SectionMap().add_line](#sectionmap()add_line)
    - [SectionMap().add_line_indent](#sectionmap()add_line_indent)
    - [SectionMap().trim_block](#sectionmap()trim_block)

## SectionMap

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_map.py#L11)

Dict-based storage for parsed `Section` list.Used for `handsdown.processors.base.BaseDocstringProcessor`.Key is a `Section` title.
Value is a related `Section` instance.

#### Signature

```python
class SectionMap:
    def __init__(self) -> None:
        ...
```

### SectionMap().__iter__

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_map.py#L95)

Iterate over existing `Section` objects.

#### Yields

`Section` objects in order of appearance.

#### Signature

```python
def __iter__(self) -> Iterator[Section]:
    ...
```

### SectionMap().add_block

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_map.py#L65)

Add new `SectionBlock` to section `section_name`.If `Section` does not exist - it is not created.

#### Arguments

- `section_name` - Target section title

#### Signature

```python
def add_block(self, section_name: str) -> None:
    ...
```

### SectionMap().add_line

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_map.py#L42)

Add new `line` to the last `SectionBlock` of section `section_name`.If line and section are empty - section is not created.

#### Arguments

- `section_name` - Target section title
- `line` - Line to add

#### Signature

```python
def add_line(self, section_name: str, line: str) -> None:
    ...
```

### SectionMap().add_line_indent

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_map.py#L26)

Add line respecting indent of the current section block.

#### Arguments

- `section_name` - Target section title
- `line` - Line to add

#### Signature

```python
def add_line_indent(self, section_name: str, line: str) -> None:
    ...
```

### SectionMap().trim_block

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_map.py#L79)

Delete last empty lines from the last `SectionBlock`.If `Section` does not exist - it is not created.

#### Arguments

- `section_name` - Target section title.

#### Signature

```python
def trim_block(self, section_name: str) -> None:
    ...
```


