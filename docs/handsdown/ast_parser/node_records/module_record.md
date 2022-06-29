# ModuleRecord

[Handsdown API Index](../../../README.md#handsdown-api-index) /
[Handsdown](../../index.md#handsdown) /
[AST Parser](../index.md#ast-parser) /
[Node Records](./index.md#node-records) /
ModuleRecord

> Auto-generated documentation for [handsdown.ast_parser.node_records.module_record](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/module_record.py) module.

## ModuleRecord

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/module_record.py#L21)

Wrapper for an `ast.Module` node with corresponding node info.

Responsible for parsing Python source as well.

#### Arguments

- `node` - Result of `ast.parse`.

#### Signature

```python
class ModuleRecord(NodeRecord):
    def __init__(self, node: ast.Module) -> None:
        ...
```

#### See also

- [NodeRecord](./node_record.md#noderecord)

### ModuleRecord().build_children

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/module_record.py#L137)

Collect full information about Module child records.

Used only when doc for this ModuleRecord is building.

#### Signature

```python
def build_children(self) -> None:
    ...
```

### ModuleRecord.create_from_source

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/module_record.py#L45)

Create new [ModuleRecord](#modulerecord) from path.

#### Arguments

- `source_path` - Path to a Python source file.
- `import_string` - File absolute import string.
- `encoding` - File encoding.

#### Returns

New [ModuleRecord](#modulerecord) instance.

#### Signature

```python
@classmethod
def create_from_source(
    cls, source_path: Path, import_string: ImportString, encoding: str = ENCODING
) -> "ModuleRecord":
    ...
```

#### See also

- [ENCODING](../../constants.md#encoding)
- [ImportString](../../utils/import_string.md#importstring)

### ModuleRecord().find_record

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/module_record.py#L73)

Find child in the Module by an absolute or relative import string.

#### Attributes

- `import_string` - record import string.

#### Returns

Found child record on None.

#### Signature

```python
def find_record(self, import_string: ImportString) -> Optional[NodeRecord]:
    ...
```

#### See also

- [ImportString](../../utils/import_string.md#importstring)

### ModuleRecord().get_related_import_strings

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/module_record.py#L251)

Get a set of `related_names` found in module class, function, method and attribute records.

#### Returns

A set of absolute import strings found.

#### Signature

```python
def get_related_import_strings(self, node_record: NodeRecord) -> Set[ImportString]:
    ...
```

#### See also

- [NodeRecord](./node_record.md#noderecord)

### ModuleRecord().is_init

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/module_record.py#L281)

Check if this module is the __init__.py file.

#### Returns

True if this module is the __init__.py file.

#### Signature

```python
def is_init(self) -> bool:
    ...
```

### ModuleRecord().iter_records

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/module_record.py#L92)

Iterate over Module class, method and fucntion records.

#### Yields

A child record.

#### Signature

```python
def iter_records(self) -> Iterator[NodeRecord]:
    ...
```



