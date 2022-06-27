# Base Docstring Processor

[🙌 Handsdown - Python documentation generator](../../README.md#-handsdown---python-documentation-generator) /
[Modules](../../MODULES.md#modules) /
[Handsdown](../index.md#handsdown) /
[Processors](index.md#processors) /
Base Docstring Processor

> Auto-generated documentation for [handsdown.processors.base](https://github.com/vemel/handsdown/blob/main/handsdown/processors/base.py) module.

- [Base Docstring Processor](#base-docstring-processor)
  - [BaseDocstringProcessor](#basedocstringprocessor)
    - [BaseDocstringProcessor().build_sections](#basedocstringprocessor()build_sections)

## BaseDocstringProcessor

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/processors/base.py#L28)

Base docstring processor. All docstring processors are based on top of it.

#### Attributes

- `line_re_map` - Mapping of line regexp to format string for it
- `section_name_map` - Mapping of Section search key to Section title
- `replace_map` - Mapping of string to replace to replacer

#### Signature

```python
class BaseDocstringProcessor:
    def __init__(self) -> None:
        ...
```

### BaseDocstringProcessor().build_sections

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/processors/base.py#L66)

Parse docstring and split it to sections with arrays of strings.

#### Arguments

- `content` - Object docstring.

#### Returns

A dictionary where key is a section name and value is a list of string sof this
section.

#### Signature

```python
def build_sections(self, content: str) -> SectionMap:
    ...
```

#### See also

- [SectionMap](section_map.md#sectionmap)


