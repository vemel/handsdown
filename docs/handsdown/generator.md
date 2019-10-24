# Generator

> Auto-generated documentation for [handsdown.generator](https://github.com/vemel/handsdown/blob/master/handsdown/generator.py) module.

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

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/generator.py#L33)

```python
class Generator():
    def __init__(
        input_path: Path,
        output_path: Path,
        source_paths: Iterable[Path],
        docstring_processor: Optional[BaseDocstringProcessor] = None,
        loader: Optional[Loader] = None,
        raise_errors: bool = False,
        source_code_url: Optional[Text] = None,
        toc_depth: int = 3,
    ) -> None:
```

Main handsdown documentation generator.

#### Arguments

- `input_path` - Path to repo to generate docs.
- `output_path` - Path to folder with auto-generated docs to output.
- `source_paths` - List of paths to source files for generation.
- `docstring_processor` - Docstring converter to Markdown.
- `loader` - Loader for python modules.
- `raise_errors` - Raise `LoaderError` instead of silencing in.
- `source_code_url` - URL to source files to use instead of relative paths,
    useful for [GitHub Pages](https://pages.github.com/).
- `toc_depth` - Maximum depth of child modules ToC

#### Attributes

- `INDEX_NAME` - Docs index filename: `'README.md'`
- `INDEX_TITLE` - Docs index title: `'Index'`
- `LOGGER_NAME` - Name of logger: `'handsdown'`
- `MODULES_NAME` - Docs modules filename: `'MODULES.md'`
- `MODULES_TITLE` - Docs modules title: `'Modules'`

#### See also

- [BaseDocstringProcessor](processors/base.md#basedocstringprocessor)
- [Loader](loader.md#loader)

### Generator().cleanup_old_docs

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/generator.py#L153)

```python
def cleanup_old_docs() -> None:
```

Remove old docs generated for this module.

### Generator().generate_doc

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/generator.py#L194)

```python
def generate_doc(source_path: Path) -> None:
```

Generate one module doc at once.

#### Arguments

- `source_path` - Path to source file.

#### Raises

- [GeneratorError](#generatorerror) - If `source_path` not found in current repo.

### Generator().generate_docs

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/generator.py#L325)

```python
def generate_docs() -> None:
```

Generate all doc files at once.

### Generator().generate_index

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/generator.py#L343)

```python
def generate_index() -> None:
```

Generate `<output>/README.md` file with title from `<root>/README.md` and `Modules`
section that contains a Tree of all modules in the project.

### Generator().generate_modules

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/generator.py#L372)

```python
def generate_modules() -> None:
```

Generate `<output>/README.md` file with title from `<root>/README.md` and `Modules`
section that contains a Tree of all modules in the project.

## GeneratorError

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/generator.py#L27)

```python
class GeneratorError(Exception):
```

Main error for [Generator](#generator)
