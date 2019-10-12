# Build: Lib: Handsdown: Processors: Smart

- [Build: Lib: Handsdown: Processors: Smart](#build-lib-handsdown-processors-smart)
  - [SmartDocstringProcessor](#smartdocstringprocessor)
    - [SmartDocstringProcessor().build_sections](#smartdocstringprocessorbuild_sections)

> Auto-generated documentation for [build.lib.handsdown.processors.smart](../build/lib/handsdown/processors/smart.py) module.

## SmartDocstringProcessor

[🔍 find in source code](../build/lib/handsdown/processors/smart.py#L9)

```python
class SmartDocstringProcessor() -> None
```
This class implements the preprocessor for restructured text and google.

### SmartDocstringProcessor().build_sections

[🔍 find in source code](../build/lib/handsdown/processors/smart.py#L22)

```python
def build_sections(content: str) -> DefaultDict[str, List[str]]
```
Preprocessors a given section into it's components.
