# ClassRecord

> Auto-generated documentation for [handsdown.ast_parser.class_record](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/class_record.py) module.

- [Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / [Ast Parser](index.md#ast-parser) / ClassRecord
  - [ClassRecord](#classrecord)
    - [ClassRecord().get_public_methods](#classrecordget_public_methods)
    - [ClassRecord().iter_records](#classrecorditer_records)
    - [ClassRecord().related_names](#classrecordrelated_names)

## ClassRecord

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/class_record.py#L13)

```python
class ClassRecord(NodeRecord):
    def __init__(node: ast.ClassDef) -> None:
```

### ClassRecord().get_public_methods

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/class_record.py#L41)

```python
def get_public_methods() -> List[FunctionRecord]:
```

### ClassRecord().iter_records

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/class_record.py#L36)

```python
def iter_records() -> Generator[NodeRecord, None, None]:
```

### ClassRecord().related_names

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/class_record.py#L23)

```python
@property
def related_names() -> Set[Text]:
```
