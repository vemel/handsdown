# Base

[Handsdown API Index](../../README.md#handsdown-api-index) /
[Handsdown](../index.md#handsdown) /
[Generators](./index.md#generators) /
Base

> Auto-generated documentation for [handsdown.generators.base](https://github.com/vemel/handsdown/blob/main/handsdown/generators/base.py) module.

- [Base](#base)
  - [BaseGenerator](#basegenerator)
    - [BaseGenerator().cleanup_old_docs](#basegenerator()cleanup_old_docs)
    - [BaseGenerator().generate_doc](#basegenerator()generate_doc)
    - [BaseGenerator().generate_docs](#basegenerator()generate_docs)
    - [BaseGenerator().generate_external_configs](#basegenerator()generate_external_configs)
    - [BaseGenerator().generate_index](#basegenerator()generate_index)
    - [BaseGenerator().get_md_document](#basegenerator()get_md_document)
    - [BaseGenerator().get_see_also_links](#basegenerator()get_see_also_links)
  - [GeneratorError](#generatorerror)

## BaseGenerator

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/generators/base.py#L32)

#### Attributes

- `INDEX_NAME` - Index filename: `'README.md'`

- `INDEX_TITLE` - Index title: `'Index'`


Base documentation generator.

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
class BaseGenerator:
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

- [ENCODING](../settings.md#encoding)

### BaseGenerator().cleanup_old_docs

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/generators/base.py#L140)

Remove old docs generated for this module.

#### Signature

```python
def cleanup_old_docs(self) -> None:
    ...
```

### BaseGenerator().generate_doc

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/generators/base.py#L170)

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

### BaseGenerator().generate_docs

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/generators/base.py#L233)

Generate all doc files at once.

#### Signature

```python
def generate_docs(self) -> None:
    ...
```

### BaseGenerator().generate_external_configs

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/generators/base.py#L353)

#### Signature

```python
def generate_external_configs(self, overwrite: bool) -> None:
    ...
```

### BaseGenerator().generate_index

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/generators/base.py#L242)

Generate `<output>/README.md` file.Contains a Tree of all modules in the project.

#### Signature

```python
def generate_index(self) -> None:
    ...
```

### BaseGenerator().get_md_document

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/generators/base.py#L198)

Get or create MDDocument for module record.

#### Signature

```python
def get_md_document(self, module_record: ModuleRecord) -> MDDocument:
    ...
```

#### See also

- [MDDocument](../md_document.md#mddocument)
- [ModuleRecord](../ast_parser/node_records/module_record.md#modulerecord)

### BaseGenerator().get_see_also_links

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/generators/base.py#L318)

Get links to other modules that are referenced in the docstring.

#### Signature

```python
def get_see_also_links(
    self, record: NodeRecord, module_record: ModuleRecord, md_document: MDDocument
) -> List[str]:
    ...
```

#### See also

- [MDDocument](../md_document.md#mddocument)
- [ModuleRecord](../ast_parser/node_records/module_record.md#modulerecord)
- [NodeRecord](../ast_parser/node_records/node_record.md#noderecord)



## GeneratorError

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/generators/base.py#L26)

Main error for `BaseGenerator`.

#### Signature

```python
class GeneratorError(Exception):
    ...
```


