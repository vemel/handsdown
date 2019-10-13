# Handsdown: Generator

- [Handsdown: Generator](#handsdown-generator)
  - [Generator](#generator)
    - [Generator()._generate_doc](#generator_generate_doc)
    - [Generator()._generate_index_md_content](#generator_generate_index_md_content)
    - [Generator()._get_formatted_docstring](#generator_get_formatted_docstring)
    - [Generator()._get_title_from_path](#generator_get_title_from_path)
    - [Generator().cleanup_old_docs](#generatorcleanup_old_docs)
    - [Generator().generate](#generatorgenerate)
    - [Generator().replace_links](#generatorreplace_links)

> Auto-generated documentation for [handsdown.generator](../handsdown/generator.py) module.

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

### Generator()._generate_doc

[🔍 find in source code](../handsdown/generator.py#L101)

```python
def _generate_doc(module_record: handsdown.module_record.ModuleRecord) -> None
```

Generate one module doc at once. If `file_path` has nothing to document - return `None`.

#### Arguments

- `file_path` - Path to source file.

#### Returns

A path to generated MD file or None.

#### See also

- [ModuleRecord](./handsdown_module_record.md#modulerecord)

### Generator()._generate_index_md_content

[🔍 find in source code](../handsdown/generator.py#L332)

```python
def _generate_index_md_content() -> str
```

Get new `index.md` file content. Copy content from `README.md` and add ToC.

#### Arguments

- `source_paths` - List of source paths to include to `Modules` section.

#### Returns

A string with new file content.

### Generator()._get_formatted_docstring

[🔍 find in source code](../handsdown/generator.py#L278)

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

### Generator()._get_title_from_path

[🔍 find in source code](../handsdown/generator.py#L395)

```python
def _get_title_from_path(path: pathlib.Path) -> str
```

Converts `pathlib.Path` to a human readable title.

#### Arguments

- `path` - Relative path to file or folder

#### Returns

Human readable title.

### Generator().cleanup_old_docs

[🔍 find in source code](../handsdown/generator.py#L82)

```python
def cleanup_old_docs() -> None
```

Remove old docs generated for this module.

#### Arguments

- `preserve_paths` - All doc files generated paths that should not be deleted.

### Generator().generate

[🔍 find in source code](../handsdown/generator.py#L133)

```python
def generate() -> None
```

Generate all module docs at once.

### Generator().replace_links

[🔍 find in source code](../handsdown/generator.py#L172)

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
