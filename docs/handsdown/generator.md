# Generator

> Auto-generated documentation for [handsdown.generator](https://github.com/vemel/handsdown/blob/main/handsdown/generator.py) module.

Main handsdown documentation generator.

- [Handsdown](../README.md#-handsdown---python-documentation-generator) / [Modules](../MODULES.md#modules) / [Handsdown](index.md#handsdown) / Generator
    - [Generator](#generator)
        - [Generator().cleanup_old_docs](#generatorcleanup_old_docs)
        - [Generator().generate_doc](#generatorgenerate_doc)
        - [Generator().generate_docs](#generatorgenerate_docs)
        - [Generator().generate_index](#generatorgenerate_index)
        - [Generator().generate_modules](#generatorgenerate_modules)
    - [GeneratorError](#generatorerror)

## Generator

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/generator.py#L31)

```python
class Generator():
    def __init__(
        input_path: Path,
        output_path: Path,
        source_paths: Iterable[Path],
        project_name: Optional[str] = None,
        docstring_processor: Optional[BaseDocstringProcessor] = None,
        loader: Optional[Loader] = None,
        raise_errors: bool = False,
        source_code_url: Optional[str] = None,
        source_code_path: Optional[Path] = None,
        toc_depth: int = 1,
        encoding: str = ENCODING,
    ) -> None:
```

Main documentation generator.

#### Arguments

- `project_name` - Name of the project.
- `input_path` - Path to repo to generate docs.
- `output_path` - Path to folder with auto-generated docs to output.
- `source_paths` - List of paths to source files for generation.
- `docstring_processor` - Docstring converter to Markdown.
- `loader` - Loader for python modules.
- `raise_errors` - Raise `LoaderError` instead of silencing in.
- `source_code_url` - URL to source files to use instead of relative paths,
    useful for [GitHub Pages](https://pages.github.com/).
- `source_code_path` - Path to local source code
- `toc_depth` - Maximum depth of child modules ToC
- `encoding` - File encoding

#### Attributes

- `LOGGER_NAME` - Name of logger: `'handsdown'`
- `INDEX_NAME` - Docs index filename: `'README.md'`
- `INDEX_TITLE` - Docs index title: `'Index'`
- `MODULES_NAME` - Docs modules filename: `'MODULES.md'`
- `MODULES_TITLE` - Docs modules title: `'Modules'`

#### See also

- [ENCODING](settings.md#encoding)

### Generator().cleanup_old_docs

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/generator.py#L155)

```python
def cleanup_old_docs() -> None:
```

Remove old docs generated for this module.

### Generator().generate_doc

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/generator.py#L189)

```python
def generate_doc(source_path: Path) -> None:
```

Generate one module doc at once.

#### Arguments

- `source_path` - Path to source file.

#### Raises

- `GeneratorError` - If `source_path` not found in current repo.

### Generator().generate_docs

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/generator.py#L314)

```python
def generate_docs() -> None:
```

Generate all doc files at once.

### Generator().generate_index

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/generator.py#L328)

```python
def generate_index() -> None:
```

Generate `<output>/README.md` file with title from `<root>/README.md`.

Also `Modules` section that contains a Tree of all modules in the project.

### Generator().generate_modules

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/generator.py#L354)

```python
def generate_modules() -> None:
```

Generate `<output>/README.md` file.

Title from `<root>/README.md` and `Modules`
section that contains a Tree of all modules in the project.

## GeneratorError

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/generator.py#L25)

```python
class GeneratorError(Exception):
```

Main error for [Generator](#generator).
