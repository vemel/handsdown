# Generator

> Auto-generated documentation for [handsdown.generator](../../handsdown/generator.py) module.

- [Index](../README.md#handsdown-index) / [Handsdown](index.md#handsdown) / [Generator](#generator) / Generator
  - [Generator](#generator)
    - [Generator()._render_docstring](#generator_render_docstring)
    - [Generator().cleanup_old_docs](#generatorcleanup_old_docs)
    - [Generator().generate_doc](#generatorgenerate_doc)
    - [Generator().generate_docs](#generatorgenerate_docs)
    - [Generator().generate_index](#generatorgenerate_index)
  - [GeneratorError](#generatorerror)

## Generator

[🔍 find in source code](../../handsdown/generator.py#l21)

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
- `raise_errors` - Raise [LoaderError](loader.md#loadererror) instead of silencing in.
- `ignore_unknown_errors` - Continue on any error.

- `LOGGER_NAME` - Name of logger: `handsdown`
- `INDEX_NAME` - Docs index filename: `README.md`
- `INDEX_TITLE` - Docs index title: `Index`
- `INDEX_MODULES_NAME` - Modules ToC name in index: `Modules`

#### See also

- [BaseDocstringProcessor](processors/base.md#basedocstringprocessor)
- [Loader](loader.md#loader)

### Generator()._render_docstring

[🔍 find in source code](../../handsdown/generator.py#l355)

```python
def _render_docstring(
    module_record: Union[handsdown.module_record.ModuleRecord, handsdown.module_record.ModuleObjectRecord],
    md_document: handsdown.md_document.MDDocument,
    signature: Union[str, NoneType] = None,
) -> Union[str, NoneType]
```

Get object docstring and convert it to a valid markdown using
`[BaseDocstringProcessor](processors/base.md#basedocstringprocessor)`.

#### Arguments

- `source_path` - Path to object source file.
- `module_object` - Object to inspect.
- `signature` - Object signature if exists.

#### Returns

A module docstring with valid markdown.

#### See also

- [ModuleRecord](module_record.md#modulerecord)
- [MDDocument](md_document.md#mddocument)

### Generator().cleanup_old_docs

[🔍 find in source code](../../handsdown/generator.py#l109)

```python
def cleanup_old_docs() -> None
```

Remove old docs generated for this module.

### Generator().generate_doc

[🔍 find in source code](../../handsdown/generator.py#l140)

```python
def generate_doc(source_path: pathlib.Path) -> None
```

Generate one module doc at once.

#### Arguments

- `source_path` - Path to source file.

#### Raises

- [GeneratorError](#generatorerror) - If `source_path` not found in current repo.

### Generator().generate_docs

[🔍 find in source code](../../handsdown/generator.py#l238)

```python
def generate_docs() -> None
```

Generate all doc files at once.

### Generator().generate_index

[🔍 find in source code](../../handsdown/generator.py#l253)

```python
def generate_index() -> None
```

Generate `<output>/README.md` file with title from `<root>/README.md` and `Modules`
section that contains a Tree of all modules in the project.

## GeneratorError

[🔍 find in source code](../../handsdown/generator.py#l15)

```python
class GeneratorError(*args, **kwargs)
```

Main error for [Generator](#generator)