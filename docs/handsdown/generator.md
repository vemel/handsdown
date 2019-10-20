# Generator

> Auto-generated documentation for [handsdown.generator](https://github.com/vemel/handsdown/blob/master/handsdown/generator.py) module.

Main handsdown documentation generator.

- [Index](../README.md#modules) / [Handsdown](index.md#handsdown) / Generator
  - [Generator](#generator)
    - [Generator().cleanup_old_docs](#generatorcleanup_old_docs)
    - [Generator().generate_doc](#generatorgenerate_doc)
    - [Generator().generate_docs](#generatorgenerate_docs)
    - [Generator().generate_index](#generatorgenerate_index)
  - [GeneratorError](#generatorerror)

## Generator

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/generator.py#L31)

```python
class Generator(
    input_path: Path,
    output_path: Path,
    source_paths: Iterable[Path],
    logger: Optional[logging.Logger] = None,
    docstring_processor: Optional[BaseDocstringProcessor] = None,
    loader: Optional[Loader] = None,
    raise_errors: bool = False,
    source_code_url: Optional[Text] = None,
    toc_depth: int = 3,
) -> None
```

Main handsdown documentation generator.

#### Arguments

- `input_path` - Path to repo to generate docs.
- `output_path` - Path to folder with auto-generated docs to output.
- `source_paths` - List of paths to source files for generation.
- `logger` - Logger instance.
- `docstring_processor` - Docstring converter to Markdown.
- `loader` - Loader for python modules.
- `raise_errors` - Raise [LoaderError](loader.md#loadererror) instead of silencing in.
- `ignore_unknown_errors` - Continue on any error.
- `source_code_url` - URL to source files to use instead of relative paths,
    useful for [GitHub Pages](https://pages.github.com/).
- `toc_depth` - Maximum depth of child modules ToC

#### Attributes

- `LOGGER_NAME` - Name of logger: `handsdown`
- `INDEX_NAME` - Docs index filename: `README.md`
- `INDEX_TITLE` - Docs index title: `Index`
- `MODULES_NAME` - Modules ToC name in index: `Modules`

#### See also

- [Loader](loader.md#loader)

### Generator().cleanup_old_docs

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/generator.py#L132)

```python
def cleanup_old_docs() -> None
```

Remove old docs generated for this module.

### Generator().generate_doc

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/generator.py#L174)

```python
def generate_doc(source_path: Path) -> None
```

Generate one module doc at once.

#### Arguments

- `source_path` - Path to source file.

#### Raises

- [GeneratorError](#generatorerror) - If `source_path` not found in current repo.

### Generator().generate_docs

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/generator.py#L288)

```python
def generate_docs() -> None
```

Generate all doc files at once.

### Generator().generate_index

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/generator.py#L305)

```python
def generate_index() -> None
```

Generate `<output>/README.md` file with title from `<root>/README.md` and `Modules`
section that contains a Tree of all modules in the project.

## GeneratorError

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/generator.py#L25)

```python
class GeneratorError()
```

Main error for [Generator](#generator)
