# ModuleRecord

> Auto-generated documentation for [handsdown.ast_parser.node_records.module_record](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/module_record.py) module.

Wrapper for an `ast.Module` node with corresponding node info.

- [Handsdown](../../../README.md#-handsdown---python-documentation-generator) / [Modules](../../../MODULES.md#modules) / [Handsdown](../../index.md#handsdown) / [AST Parser](../index.md#ast-parser) / [Node Records](index.md#node-records) / ModuleRecord
    - [ModuleRecord](#modulerecord)
        - [ModuleRecord().build_children](#modulerecordbuild_children)
        - [ModuleRecord.create_from_source](#modulerecordcreate_from_source)
        - [ModuleRecord().find_record](#modulerecordfind_record)
        - [ModuleRecord().get_related_import_strings](#modulerecordget_related_import_strings)
        - [ModuleRecord().iter_records](#modulerecorditer_records)

## ModuleRecord

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/module_record.py#L20)

```python
class ModuleRecord(NodeRecord):
    def __init__(node: ast.Module) -> None:
```

Wrapper for an `ast.Module` node with corresponding node info.

Responsible for parsing Python source as well.

#### Arguments

- `node` - Result of `ast.parse`.

#### See also

- [NodeRecord](node_record.md#noderecord)

### ModuleRecord().build_children

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/module_record.py#L151)

```python
def build_children() -> None:
```

Collect full information about Module child records.

Used only when doc for this ModuleRecord is building.

### ModuleRecord.create_from_source

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/module_record.py#L44)

```python
@classmethod
def create_from_source(
    source_path: Path,
    import_string: ImportString,
    encoding: str = ENCODING,
) -> 'ModuleRecord':
```

Create new [ModuleRecord](#modulerecord) from path.

#### Arguments

- `source_path` - Path to a Python source file.
- `import_string` - File absolute import string.
- `encoding` - File encoding.

#### Returns

New [ModuleRecord](#modulerecord) instance.

#### See also

- [ENCODING](../../settings.md#encoding)
- [ImportString](../../utils/import_string.md#importstring)

### ModuleRecord().find_record

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/module_record.py#L72)

```python
def find_record(import_string: ImportString) -> Optional[NodeRecord]:
```

Find child in the Module by an absolute or relative import string.

#### Attributes

- `import_string` - record import string.

#### Returns

Found child record on None.

#### See also

- [ImportString](../../utils/import_string.md#importstring)

### ModuleRecord().get_related_import_strings

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/module_record.py#L265)

```python
def get_related_import_strings(node_record: NodeRecord) -> Set[ImportString]:
```

Get a set of `related_names` found in module class, function, method and attribute records.

#### Returns

A set of absolute import strings found.

#### See also

- [NodeRecord](node_record.md#noderecord)

### ModuleRecord().iter_records

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/module_record.py#L91)

```python
def iter_records() -> Iterator[NodeRecord]:
```

Iterate over Module class, method and fucntion records.

#### Yields

A child record.
