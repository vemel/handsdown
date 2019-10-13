# Handsdown: Generator

- [Handsdown: Generator](#handsdown-generator)
  - [GeneratorError](#generatorerror)
  - [Generator](#generator)
    - [Generator().cleanup_old_docs](#generatorcleanup_old_docs)
    - [Generator().generate](#generatorgenerate)
    - [Generator().replace_links](#generatorreplace_links)

> Auto-generated documentation for [handsdown.generator](../handsdown/generator.py) module.

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

Main doc generator.

#### Arguments

- `input_path` - Path to repo to generate docs.
- `logger` - Logger instance.
- `docstring_processor` - Docstring converter to Markdown.
- `loader` - Loader for python modules.
- `output_path` - Path to folder with auto-generated docs to output.

### Generator().generate

[🔍 find in source code](../handsdown/generator.py#L133)

```python
def generate() -> None
```

Main doc generator.

#### Arguments

- `input_path` - Path to repo to generate docs.
- `logger` - Logger instance.
- `docstring_processor` - Docstring converter to Markdown.
- `loader` - Loader for python modules.
- `output_path` - Path to folder with auto-generated docs to output.

### Generator().replace_links

[🔍 find in source code](../handsdown/generator.py#L185)

```python
def replace_links(file_path: pathlib.Path) -> None
```

Main doc generator.

#### Arguments

- `input_path` - Path to repo to generate docs.
- `logger` - Logger instance.
- `docstring_processor` - Docstring converter to Markdown.
- `loader` - Loader for python modules.
- `output_path` - Path to folder with auto-generated docs to output.
