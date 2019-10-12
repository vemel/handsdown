# Build: Lib: Handsdown: Handsdown

- [Build: Lib: Handsdown: Handsdown](#build-lib-handsdown-handsdown)
  - [Handsdown](#handsdown)
    - [Handsdown().cleanup_old_docs](#handsdowncleanup_old_docs)
    - [Handsdown().generate](#handsdowngenerate)
    - [Handsdown().generate_doc](#handsdowngenerate_doc)
    - [Handsdown().replace_links](#handsdownreplace_links)

> Auto-generated documentation for [build.lib.handsdown.handsdown](../build/lib/handsdown/handsdown.py) module.

## Handsdown

[🔍 find in source code](../build/lib/handsdown/handsdown.py#L13)

```python
class Handsdown(
    input_path: pathlib.Path,
    logger: Union[logging.Logger, NoneType] = None,
    docstring_processor: Union[handsdown.processors.base.BaseDocstringProcessor, NoneType] = None,
    loader: Union[handsdown.loader.Loader, NoneType] = None,
    output_path: Union[pathlib.Path, NoneType] = None,
)
```
Main doc generator.

#### Arguments

- `input_path` - Path to repo to generate docs.
- `logger` - Logger instance.
- `docstring_processor` - Docstring converter to Markdown.
- `loader` - Loader for python modules.
- `output_path` - Path to folder with auto-generated docs to output.

### Handsdown().cleanup_old_docs

[🔍 find in source code](../build/lib/handsdown/handsdown.py#L69)

```python
def cleanup_old_docs(preserve_paths: Iterable[pathlib.Path]) -> None
```
Remove old docs generated for this module.

#### Arguments

- `preserve_paths` - All doc files generated paths that should not be deleted.

### Handsdown().generate

[🔍 find in source code](../build/lib/handsdown/handsdown.py#L160)

```python
def generate() -> None
```
Generate all module docs at once.

### Handsdown().generate_doc

[🔍 find in source code](../build/lib/handsdown/handsdown.py#L109)

```python
def generate_doc(file_path: pathlib.Path) -> Union[pathlib.Path, NoneType]
```
Generate one module doc at once. If `file_path` has nothing to document - return `None`.

#### Arguments

- `file_path` - Path to source file.

#### Returns

A path to generated MD file or None.

### Handsdown().replace_links

[🔍 find in source code](../build/lib/handsdown/handsdown.py#L208)

```python
def replace_links(file_path: pathlib.Path) -> None
```
Replace all import strings with Markdown links. Only import strings that present in this
package are replaced, so not dead linsk should be generated.

```python
my_md = Path('doc.md')
my_md.write_text('I love `' + 'handsdown.indent_trimmer.IndentTrimmer.trim_lines` function!')
handsdown.replace_links(my_md)

my_md.read_text()
# 'I love [IndentTrimmer.trim_lines](./handsdown_indent_trimmer.md#indenttrimmertrim_lines) function!'
```

#### Arguments

- `file_path` - Path to MD document file.
