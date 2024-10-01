# SectionMap

Module for splitting docstring into `Section` groups.

[Handsdown API Index](../../README.md#handsdown-api-index) / [Handsdown](../index.md#handsdown) / [Processors](./index.md#processors) / SectionMap

> Auto-generated documentation for [handsdown.processors.section_map](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_map.py) module.

## SectionMap

[Show source in section_map.py:11](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_map.py#L11)

Dict-based storage for parsed `Section` list.

Used for [BaseDocstringProcessor](./base.md#basedocstringprocessor).

Key is a `Section` title.
Value is a related `Section` instance.

#### Signature

```python
class SectionMap:
    def __init__(self) -> None:
        ...
```

### SectionMap().__iter__

[Show source in section_map.py:95](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_map.py#L95)

Iterate over existing `Section` objects.

#### Yields

`Section` objects in order of appearance.

#### Signature

```python
def __iter__(self) -> Iterator[Section]:
    ...
```

#### See also

- [Section](./section.md#section)

### SectionMap().add_block

[Show source in section_map.py:65](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_map.py#L65)

Add new `SectionBlock` to section `section_name`.

If `Section` does not exist - it is not created.

#### Arguments

- `section_name` - Target section title

#### Signature

```python
def add_block(self, section_name: str) -> None:
    ...
```

### SectionMap().add_line

[Show source in section_map.py:42](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_map.py#L42)

Add new `line` to the last `SectionBlock` of section `section_name`.

If line and section are empty - section is not created.

#### Arguments

- `section_name` - Target section title
- `line` - Line to add

#### Signature

```python
def add_line(self, section_name: str, line: str) -> None:
    ...
```

### SectionMap().add_line_indent

[Show source in section_map.py:26](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_map.py#L26)

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

[Show source in section_map.py:79](https://github.com/vemel/handsdown/blob/main/handsdown/processors/section_map.py#L79)

Delete last empty lines from the last `SectionBlock`.

If `Section` does not exist - it is not created.

#### Arguments

- `section_name` - Target section title.

#### Signature

```python
def trim_block(self, section_name: str) -> None:
    ...
```
