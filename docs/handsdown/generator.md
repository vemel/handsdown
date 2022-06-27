# Generator

[🙌 Handsdown - Python documentation generator](../README.md#-handsdown---python-documentation-generator) /
[Modules](../MODULES.md#modules) /
[Handsdown](index.md#handsdown) /
Generator

> Auto-generated documentation for [handsdown.generator](https://github.com/vemel/handsdown/blob/main/handsdown/generator.py) module.

- [Generator](#generator)
  - [Generator](#generator-1)
    - [Generator().cleanup_old_docs](#generator()cleanup_old_docs)
    - [Generator().generate_doc](#generator()generate_doc)
    - [Generator().generate_docs](#generator()generate_docs)
    - [Generator().generate_index](#generator()generate_index)
    - [Generator().generate_modules](#generator()generate_modules)
    - [Generator().get_see_also_links](#generator()get_see_also_links)
  - [GeneratorError](#generatorerror)

## Generator

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/generator.py#L32)

#### Attributes

- `LOGGER_NAME` - Name of logger: `'handsdown'`

- `INDEX_NAME` - Docs index filename: `'README.md'`

- `INDEX_TITLE` - Docs index title: `'Index'`

- `MODULES_NAME` - Docs modules filename: `'MODULES.md'`

- `MODULES_TITLE` - Docs modules title: `'Modules'`


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

#### Signature

```python
class Generator:
    def __init__(
        self,
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
        ...
```

#### See also

- [ENCODING](settings.md#encoding)

### Generator().cleanup_old_docs

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/generator.py#L155)

Remove old docs generated for this module.

#### Signature

```python
def cleanup_old_docs(self) -> None:
    ...
```

### Generator().generate_doc

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/generator.py#L186)

Generate one module doc at once.

#### Arguments

- `source_path` - Path to source file.

#### Raises

- `GeneratorError` - If `source_path` not found in current repo.

#### Signature

```python
def generate_doc(self, source_path: Path) -> None:
    ...
```

### Generator().generate_docs

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/generator.py#L244)

Generate all doc files at once.

#### Signature

```python
def generate_docs(self) -> None:
    ...
```

### Generator().generate_index

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/generator.py#L256)

Generate `<output>/README.md` file with title from `<root>/README.md`.Also `Modules` section that contains a Tree of all modules in the project.

#### Signature

```python
def generate_index(self) -> None:
    ...
```

### Generator().generate_modules

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/generator.py#L282)

Generate `<output>/README.md` file.Title from `<root>/README.md` and `Modules`
section that contains a Tree of all modules in the project.

#### Signature

```python
def generate_modules(self) -> None:
    ...
```

### Generator().get_see_also_links

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/generator.py#L373)

Get links to other modules that are referenced in the docstring.

#### Signature

```python
def get_see_also_links(
    self, record: NodeRecord, module_record: ModuleRecord, md_document: MDDocument
) -> List[str]:
    ...
```

#### See also

- [MDDocument](md_document.md#mddocument)
- [ModuleRecord](ast_parser/node_records/module_record.md#modulerecord)
- [NodeRecord](ast_parser/node_records/node_record.md#noderecord)



## GeneratorError

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/generator.py#L26)

Main error for `Generator`.

#### Signature

```python
class GeneratorError(Exception):
    ...
```


