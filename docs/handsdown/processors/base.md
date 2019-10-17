# Base

> Auto-generated documentation for [handsdown.processors.base](../../../handsdown/processors/base.py) module.

- [Index](../../README.md#modules) / [Handsdown](../index.md#handsdown) / [Processors](index.md#processors) / Base
  - [BaseDocstringProcessor](#basedocstringprocessor)
    - [BaseDocstringProcessor().build_sections](#basedocstringprocessorbuild_sections)

Base class for all docstring processors:

- [PEP257DocstringProcessor](pep257.md#pep257docstringprocessor)
- [RSTDocstringProcessor](rst.md#rstdocstringprocessor)
- [SmartDocstringProcessor](smart.md#smartdocstringprocessor)

## BaseDocstringProcessor

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/processors/base.py#L15)

```python
class BaseDocstringProcessor()
```

Base docstring processor. All docstring processors are based on top of it.

### BaseDocstringProcessor().build_sections

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/processors/base.py#L42)

```python
def build_sections(content: str) -> handsdown.processors.section_map.SectionMap
```

Parse docstring and split it to sections with arrays of strings.

#### Arguments

content - Object docstring.

#### Returns

A dictionary where key is a section name and value is a list of string sof this
section.

#### See also

- [SectionMap](section_map.md#sectionmap)
