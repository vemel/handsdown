# Smart

[Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / [Processors](index.md#processors) / Smart

> Auto-generated documentation for [handsdown.processors.smart](https://github.com/vemel/handsdown/blob/main/handsdown/processors/smart.py) module.

- [Smart](#smart)
  - [SmartDocstringProcessor](#smartdocstringprocessor)
    - [SmartDocstringProcessor().build_sections](#smartdocstringprocessor()build_sections)

## SmartDocstringProcessor

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/processors/smart.py#L15)

Docstring processor that selects a `DocstringProcessor` based on a docstring content.

#### Signature

```python
class SmartDocstringProcessor(BaseDocstringProcessor):
    def __init__(self) -> None:
        ...
```

#### See also

- [BaseDocstringProcessor](base.md#basedocstringprocessor)

### SmartDocstringProcessor().build_sections

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/processors/smart.py#L28)

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


