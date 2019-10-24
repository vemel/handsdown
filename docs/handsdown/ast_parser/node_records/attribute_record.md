# AttributeRecord

> Auto-generated documentation for [handsdown.ast_parser.node_records.attribute_record](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/attribute_record.py) module.

- [Handsdown](../../../README.md#-handsdown---python-documentation-generator) / [Modules](../../../MODULES.md#modules) / [Handsdown](../../index.md#handsdown) / [Ast Parser](../index.md#ast-parser) / [Node Records](index.md#node-records) / AttributeRecord
  - [AttributeRecord](#attributerecord)
    - [AttributeRecord().related_names](#attributerecordrelated_names)

## AttributeRecord

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/attribute_record.py#L11)

```python
class AttributeRecord(NodeRecord):
    def __init__(node: ast.Assign) -> None:
```

### AttributeRecord().related_names

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/attribute_record.py#L21)

```python
@property
def related_names() -> Set[Text]:
```
