# Handsdown: Processors: Base

- [Handsdown: Processors: Base](#handsdown-processors-base)
  - [BaseDocstringProcessor](#basedocstringprocessor)
    - [BaseDocstringProcessor().build_sections](#basedocstringprocessorbuild_sections)

> Auto-generated [Handsdown](./README.md#modules) documentation for [handsdown.processors.base](../handsdown/processors/base.py) module.

## BaseDocstringProcessor

[🔍 find in source code](../handsdown/processors/base.py#L8)

```python
class BaseDocstringProcessor()
```

Base docstring processor. All docstring processors are based on top of it:

- [PEP257DocstringProcessor](./handsdown_processors_pep257.md#pep257docstringprocessor)
- [RSTDocstringProcessor](./handsdown_processors_rst.md#rstdocstringprocessor)
- [SmartDocstringProcessor](./handsdown_processors_smart.md#smartdocstringprocessor)

### BaseDocstringProcessor().build_sections

[🔍 find in source code](../handsdown/processors/base.py#L23)

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

- [SectionMap](./handsdown_processors_section_map.md#sectionmap)
