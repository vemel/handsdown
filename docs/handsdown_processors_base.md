# Handsdown: Processors: Base

- [Handsdown: Processors: Base](#handsdown-processors-base)
  - [BaseDocstringProcessor](#basedocstringprocessor)
    - [BaseDocstringProcessor().build_sections](#basedocstringprocessorbuild_sections)
    - [BaseDocstringProcessor().render_sections](#basedocstringprocessorrender_sections)

> Auto-generated documentation for [handsdown.processors.base](..//home/vlad/work/vemel/handsdown/handsdown/processors/base.py) module.

## BaseDocstringProcessor

[🔍 find in source code](../handsdown/processors/base.py#L9)

```python
class BaseDocstringProcessor() -> None
```

This class implements the preprocessor for PEP257 and Google style.

### BaseDocstringProcessor().build_sections

[🔍 find in source code](../handsdown/processors/base.py#L47)

```python
def build_sections(content: str) -> DefaultDict[str, List[str]]
```

Parse docstring and split it to sections with arrays of strings.

#### Arguments

content - Object docstring.

#### Returns

A dictionary where key is a section name and value is a list of string sof this
section.

### BaseDocstringProcessor().render_sections

[🔍 find in source code](../handsdown/processors/base.py#L74)

```python
def render_sections(sections: Dict[str, List[str]]) -> str
```

Render sections produced by `render_sections` to a string.

#### Arguments

sections - Built sections.

#### Returns

Markdown string.
