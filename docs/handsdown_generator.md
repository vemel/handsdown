# Handsdown: Generator

- [Handsdown: Generator](#handsdown-generator)
  - [GeneratorError](#generatorerror)
  - [Generator](#generator)
    - [Generator().cleanup_old_docs](#generatorcleanup_old_docs)
    - [Generator().generate](#generatorgenerate)
    - [Generator().replace_links](#generatorreplace_links)

> Auto-generated documentation for [/.home.vlad.work.vemel.handsdown.handsdown.generator](..//home/vlad/work/vemel/handsdown/handsdown/generator.py) module.

## GeneratorError

[🔍 find in source code](../handsdown/generator.py#L13)

```python
class GeneratorError(*args, **kwargs)
```
## Generator

[🔍 find in source code](../handsdown/generator.py#L17)

```python
class Generator(
    input_path: pathlib.Path,
    source_paths: Iterable[pathlib.Path],
    logger: Union[logging.Logger, NoneType] = None,
    docstring_processor: Union[handsdown.processors.base.BaseDocstringProcessor, NoneType] = None,
    loader: Union[handsdown.loader.Loader, NoneType] = None,
    output_path: Union[pathlib.Path, NoneType] = None,
    raise_import_errors: bool = False,
)
```
Main doc generator.

#### Arguments

- `input_path` - Path to repo to generate docs.
- `logger` - Logger instance.
- `docstring_processor` - Docstring converter to Markdown.
- `loader` - Loader for python modules.
- `output_path` - Path to folder with auto-generated docs to output.

#### See also

- [BaseDocstringProcessor](./handsdown_processors_base.md#basedocstringprocessor)
- [Loader](./handsdown_loader.md#loader)

### Generator().cleanup_old_docs

[🔍 find in source code](../handsdown/generator.py#L82)

```python
def cleanup_old_docs() -> None
```
Remove old docs generated for this module.

#### Arguments

- `preserve_paths` - All doc files generated paths that should not be deleted.

### Generator().generate

[🔍 find in source code](../handsdown/generator.py#L139)

```python
def generate() -> None
```
Generate all module docs at once.

### Generator().replace_links

[🔍 find in source code](../handsdown/generator.py#L173)

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
