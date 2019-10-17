# Smart

> Auto-generated documentation for [handsdown.processors.smart](../../../handsdown/processors/smart.py) module..

    Docstring processor that selects a `DocstringProcessor` based on a docstring content:

- [Index](../../README.md#modules) / [Handsdown](../index.md#handsdown) / [Processors](index.md#processors) / Smart
  - [SmartDocstringProcessor](#smartdocstringprocessor)
    - [SmartDocstringProcessor().build_sections](#smartdocstringprocessorbuild_sections)

- [PEP257DocstringProcessor](pep257.md#pep257docstringprocessor)
- [RSTDocstringProcessor](rst.md#rstdocstringprocessor)

## SmartDocstringProcessor

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/processors/smart.py#L16)

```python
class SmartDocstringProcessor()
```

Docstring processor that selects a `DocstringProcessor` based on a docstring content.

### SmartDocstringProcessor().build_sections

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/processors/smart.py#L29)

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
