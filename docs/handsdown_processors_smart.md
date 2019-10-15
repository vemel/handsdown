# Smart

- [Handsdown](./README.md) / [Handsdown](./handsdown_index.md) / [Processors](./handsdown_processors_index.md) / Smart
  - [SmartDocstringProcessor](#smartdocstringprocessor)
    - [SmartDocstringProcessor().build_sections](#smartdocstringprocessorbuild_sections)

> Auto-generated documentation for [handsdown.processors.smart](../handsdown/processors/smart.py) module

## SmartDocstringProcessor

[🔍 find in source code](../handsdown/processors/smart.py#L9)

```python
class SmartDocstringProcessor()
```

Docstring processor that checks docstring and uses on of processors

- [PEP257DocstringProcessor](./handsdown_processors_pep257.md#pep257docstringprocessor)
- [RSTDocstringProcessor](./handsdown_processors_rst.md#rstdocstringprocessor)

### SmartDocstringProcessor().build_sections

[🔍 find in source code](../handsdown/processors/smart.py#L25)

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
