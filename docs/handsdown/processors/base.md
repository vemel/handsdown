# Base

> Auto-generated documentation for [handsdown.processors.base](../../../handsdown/processors/base.py) module.

- [Index](../../README.md#handsdown-index) / [Handsdown](../index.md#handsdown) / [Processors](index.md#processors) / [Base](#base) / Base
  - [BaseDocstringProcessor](#basedocstringprocessor)
    - [BaseDocstringProcessor().build_sections](#basedocstringprocessorbuild_sections)

## BaseDocstringProcessor

[🔍 find in source code](../../../handsdown/processors/base.py#L7)

```python
class BaseDocstringProcessor()
```

Base docstring processor. All docstring processors are based on top of it:

- `[PEP257DocstringProcessor](pep257.md#pep257docstringprocessor)`
- `[RSTDocstringProcessor](rst.md#rstdocstringprocessor)`
- `[SmartDocstringProcessor](smart.md#smartdocstringprocessor)`

### BaseDocstringProcessor().build_sections

[🔍 find in source code](../../../handsdown/processors/base.py#L38)

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
