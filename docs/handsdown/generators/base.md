# Base

[Handsdown API Index](../../README.md#handsdown-api-index) /
[Handsdown](../index.md#handsdown) /
[Generators](./index.md#generators) /
Base

> Auto-generated documentation for [handsdown.generators.base](https://github.com/vemel/handsdown/blob/main/handsdown/generators/base.py) module.

## BaseGenerator

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/generators/base.py#L27)

#### Attributes

- `INDEX_NAME` - Index filename: `'README.md'`

- `INDEX_TITLE` - Index title: `'Index'`

- `insert_toc` - Whether to add ToC to generated module docs: `False`


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

- [ENCODING](../constants.md#encoding)

### BaseGenerator().cleanup_old_docs

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/generators/base.py#L141)

Remove old docs generated for this module.

#### Signature

```python
def cleanup_old_docs(self) -> None:
    ...
```

### BaseGenerator().generate_doc

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/generators/base.py#L171)

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

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/generators/base.py#L235)

Generate all doc files at once.

#### Signature

```python
def generate_docs(self) -> None:
    ...
```

### BaseGenerator().generate_external_configs

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/generators/base.py#L356)

#### Signature

```python
def generate_external_configs(self, overwrite: bool) -> None:
    ...
```

### BaseGenerator().generate_index

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/generators/base.py#L244)

Generate `<output>/README.md` file.

Contains a Tree of all modules in the project.

#### Signature

```python
def generate_index(self) -> None:
    ...
```

### BaseGenerator().get_children_module_records

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/generators/base.py#L379)

Get all module records that are children of this module.

#### Signature

```python
def get_children_module_records(self, parent: ModuleRecord) -> List[ModuleRecord]:
    ...
```

#### See also

- [ModuleRecord](../ast_parser/node_records/module_record.md#modulerecord)

### BaseGenerator().get_md_document

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/generators/base.py#L199)

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

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/generators/base.py#L321)

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

### BaseGenerator().replace_links

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/generators/base.py#L262)

#### Signature

```python
def replace_links(
    self,
    module_record: ModuleRecord,
    record: NodeRecord,
    md_document: MDDocument,
    docstring: str,
) -> str:
    ...
```

#### See also

- [MDDocument](../md_document.md#mddocument)
- [ModuleRecord](../ast_parser/node_records/module_record.md#modulerecord)
- [NodeRecord](../ast_parser/node_records/node_record.md#noderecord)



