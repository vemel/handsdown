# Smart

> Auto-generated documentation for [processors.smart](../../processors/smart.py) module..

Docstring processor that selects a `DocstringProcessor` based on a docstring content:

- [Index](../README.md#modules) / [Processors](index.md#processors) / Smart
  - [SmartDocstringProcessor](#smartdocstringprocessor)
    - [SmartDocstringProcessor().build_sections](#smartdocstringprocessorbuild_sections)

- `handsdown.processors.pep257.PEP257DocstringProcessor`
- `handsdown.processors.rst.RSTDocstringProcessor`

## SmartDocstringProcessor

[🔍 find in source code](../../processors/smart.py#L18)

```python
class SmartDocstringProcessor() -> None
```

Docstring processor that selects a `DocstringProcessor` based on a docstring content.

### SmartDocstringProcessor().build_sections

[🔍 find in source code](../../processors/smart.py#L33)

```python
def build_sections(content: Text) -> SectionMap
```

Parse docstring and split it to sections with arrays of strings.

#### Returns

A dictionary where key is a section name and value is a list of string sof this
section.

#### Arguments

content - Object docstring.
