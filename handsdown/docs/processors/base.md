# Base

> Auto-generated documentation for [processors.base](../../processors/base.py) module..

Base class for all docstring processors:

- [Index](../README.md#modules) / [Processors](index.md#processors) / Base
  - [BaseDocstringProcessor](#basedocstringprocessor)
    - [BaseDocstringProcessor().build_sections](#basedocstringprocessorbuild_sections)

- `handsdown.processors.pep257.PEP257DocstringProcessor`
- `handsdown.processors.rst.RSTDocstringProcessor`
- `handsdown.processors.smart.SmartDocstringProcessor`

## BaseDocstringProcessor

[🔍 find in source code](../../processors/base.py#L16)

```python
class BaseDocstringProcessor() -> None
```

Base docstring processor. All docstring processors are based on top of it.

#### Attributes

- `line_re_map` - Mapping of line regexp to format string for it
- `section_name_map` - Mapping of Section search key to Section title
- `replace_map` - Mapping of string to replace to replacer

### BaseDocstringProcessor().build_sections

[🔍 find in source code](../../processors/base.py#L50)

```python
def build_sections(content: Text) -> SectionMap
```

Parse docstring and split it to sections with arrays of strings.

#### Returns

A dictionary where key is a section name and value is a list of string sof this
section.

#### Arguments

content - Object docstring.
