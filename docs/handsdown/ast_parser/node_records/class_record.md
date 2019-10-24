# ClassRecord

> Auto-generated documentation for [handsdown.ast_parser.node_records.class_record](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/class_record.py) module.

- [Handsdown](../../../README.md#-handsdown---python-documentation-generator) / [Modules](../../../MODULES.md#modules) / [Handsdown](../../index.md#handsdown) / [Ast Parser](../index.md#ast-parser) / [Node Records](index.md#node-records) / ClassRecord
  - [ClassRecord](#classrecord)
    - [ClassRecord().get_public_methods](#classrecordget_public_methods)
    - [ClassRecord().iter_records](#classrecorditer_records)
    - [ClassRecord().related_names](#classrecordrelated_names)

## ClassRecord

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/class_record.py#L14)

```python
class ClassRecord(NodeRecord):
    def __init__(node: ast.ClassDef) -> None:
```

### ClassRecord().get_public_methods

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/class_record.py#L49)

```python
def get_public_methods() -> List[FunctionRecord]:
```

### ClassRecord().iter_records

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/class_record.py#L44)

```python
def iter_records() -> Generator[NodeRecord, None, None]:
```

### ClassRecord().related_names

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/class_record.py#L29)

```python
@property
def related_names() -> Set[Text]:
```
