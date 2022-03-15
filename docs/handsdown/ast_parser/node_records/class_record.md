# ClassRecord

> Auto-generated documentation for [handsdown.ast_parser.node_records.class_record](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/class_record.py) module.

Wrapper for an `ast.ClassDef` node.

- [Handsdown](../../../README.md#-handsdown---python-documentation-generator) / [Modules](../../../MODULES.md#modules) / [Handsdown](../../index.md#handsdown) / [AST Parser](../index.md#ast-parser) / [Node Records](index.md#node-records) / ClassRecord
    - [ClassRecord](#classrecord)
        - [ClassRecord().find_record](#classrecordfind_record)
        - [ClassRecord().get_public_methods](#classrecordget_public_methods)
        - [ClassRecord().iter_records](#classrecorditer_records)
        - [ClassRecord().related_names](#classrecordrelated_names)

## ClassRecord

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/class_record.py#L17)

```python
class ClassRecord(NodeRecord):
    def __init__(node: ast.ClassDef) -> None:
```

Wrapper for an `ast.ClassDef` node.

#### Arguments

- `node` - AST node.

#### See also

- [NodeRecord](node_record.md#noderecord)

### ClassRecord().find_record

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/class_record.py#L36)

```python
def find_record(name: str) -> Optional[NodeRecord]:
```

Find child method or attribute record.

#### Arguments

- `name` - Record name to lookup.

#### Returns

Itself or None.

### ClassRecord().get_public_methods

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/class_record.py#L89)

```python
def get_public_methods() -> List[FunctionRecord]:
```

Get Class public methods.

Skips methods with names starting with `_` and magic methods  `__` if
they have no docstring. Method `__init__` is always skipped.

#### Returns

A list of child records.

### ClassRecord().iter_records

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/class_record.py#L76)

```python
def iter_records() -> Iterator[NodeRecord]:
```

Iterate over Class public methods.

#### Yields

A child record.

### ClassRecord().related_names

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/class_record.py#L59)

```python
@property
def related_names() -> Set[str]:
```

Set of related names.
