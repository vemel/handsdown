# Base

> Auto-generated documentation for [handsdown.processors.base](https://github.com/vemel/handsdown/blob/master/handsdown/processors/base.py) module.

Base class for all docstring processors:

- [Index](../../README.md#modules) / [Handsdown](../index.md#handsdown) / [Processors](index.md#processors) / Base
  - [BaseDocstringProcessor](#basedocstringprocessor)
    - [BaseDocstringProcessor().build_sections](#basedocstringprocessorbuild_sections)

- [PEP257DocstringProcessor](pep257.md#pep257docstringprocessor)
- [RSTDocstringProcessor](rst.md#rstdocstringprocessor)
- [SmartDocstringProcessor](smart.md#smartdocstringprocessor)

## BaseDocstringProcessor

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/processors/base.py#L15)

```python
class BaseDocstringProcessor() -> None
```

Base docstring processor. All docstring processors are based on top of it.

#### Attributes

- `line_re_map` - Mapping of line regexp to format string for it
- `section_name_map` - Mapping of Section search key to Section title
- `replace_map` - Mapping of string to replace to replacer

### BaseDocstringProcessor().build_sections

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/processors/base.py#L49)

```python
def build_sections(content: Text) -> SectionMap
```

Parse docstring and split it to sections with arrays of strings.

#### Arguments

content - Object docstring.

#### Returns

A dictionary where key is a section name and value is a list of string sof this
section.
