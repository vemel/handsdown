# Generator

- [Generator](#generator)
  - [Generator](#generator)
    - [Generator()._generate_index](#generator_generate_index)
    - [Generator()._get_formatted_docstring](#generator_get_formatted_docstring)
    - [Generator().cleanup_old_docs](#generatorcleanup_old_docs)
    - [Generator().generate_doc](#generatorgenerate_doc)
    - [Generator().generate_docs](#generatorgenerate_docs)
    - [Generator().generate_index](#generatorgenerate_index)
    - [Generator().replace_links](#generatorreplace_links)
  - [GeneratorError](#generatorerror)

> Auto-generated documentation for [Handsdown](./README.md) / [Generator](#generator) module ([generator.py](../handsdown/generator.py))

## Generator

[🔍 find in source code](../handsdown/generator.py#L20)

```python
class Generator(
    input_path: pathlib.Path,
    output_path: pathlib.Path,
    source_paths: Iterable[pathlib.Path],
    logger: Union[logging.Logger, NoneType] = None,
    docstring_processor: Union[handsdown.processors.base.BaseDocstringProcessor, NoneType] = None,
    loader: Union[handsdown.loader.Loader, NoneType] = None,
    raise_errors: bool = False,
)
```

Main handsdown doc generator.

#### Arguments

- `input_path` - Path to repo to generate docs.
- `output_path` - Path to folder with auto-generated docs to output.
- `source_paths` - List of paths to source files for generation.
- `logger` - Logger instance.
- `docstring_processor` - Docstring converter to Markdown.
- `loader` - Loader for python modules.
- `raise_errors` - Raise Loader errors instead of silencing them.

- `LOGGER_NAME` - Name of logger: `handsdown`
- `INDEX_NAME` - Docs index filename: `README.md`
- `INDEX_MODULES_NAME` - Modules ToC name in index: `Modules`

#### Raises

- [GeneratorError](#generatorerror) - If input/output paths are invalid.

#### See also

- [BaseDocstringProcessor](./handsdown_processors_base.md#basedocstringprocessor)
- [Loader](./handsdown_loader.md#loader)

### Generator()._generate_index

[🔍 find in source code](../handsdown/generator.py#L376)

```python
def _generate_index() -> None
```

Generate new `<output>/README.md`. Copy content from `README.md` and add ToC.

### Generator()._get_formatted_docstring

[🔍 find in source code](../handsdown/generator.py#L322)

```python
def _get_formatted_docstring(
    module_record: Union[handsdown.module_record.ModuleRecord, handsdown.module_record.ModuleObjectRecord],
    signature: Union[str, NoneType] = None,
) -> Union[str, NoneType]
```

Get object docstring and convert it to a valid markdown using
[BaseDocstringProcessor](./handsdown_processors_base.md#basedocstringprocessor).

#### Arguments

- `source_path` - Path to object source file.
- `module_object` - Object to inspect.
- `signature` - Object signature if exists.

#### Returns

A module docstring with valid markdown.

#### See also

- [ModuleRecord](./handsdown_module_record.md#modulerecord)

### Generator().cleanup_old_docs

[🔍 find in source code](../handsdown/generator.py#L110)

```python
def cleanup_old_docs() -> None
```

Remove old docs generated for this module.

### Generator().generate_doc

[🔍 find in source code](../handsdown/generator.py#L130)

```python
def generate_doc(source_path: pathlib.Path) -> None
```

Generate one module doc at once.

#### Arguments

- `source_path` - Path to source file.

#### Raises

- [GeneratorError](#generatorerror) - If `source_path` not found in current repo.

### Generator().generate_docs

[🔍 find in source code](../handsdown/generator.py#L216)

```python
def generate_docs() -> None
```

Generate all doc files at once.

### Generator().generate_index

[🔍 find in source code](../handsdown/generator.py#L230)

```python
def generate_index() -> None
```

Generate `README.md` file with title from `<root>/README.md` and `Modules` section that
contains a Tree of all modules in the project.

### Generator().replace_links

[🔍 find in source code](../handsdown/generator.py#L256)

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

## GeneratorError

[🔍 find in source code](../handsdown/generator.py#L14)

```python
class GeneratorError(*args, **kwargs)
```

Main error for [Generator](#generator)
