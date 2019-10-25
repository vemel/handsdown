# AttributeRecord

> Auto-generated documentation for [handsdown.ast_parser.node_records.attribute_record](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/attribute_record.py) module.

Wrapper for an `ast.Assign` node of a module or class attribute.

- [Handsdown](../../../README.md#-handsdown---python-documentation-generator) / [Modules](../../../MODULES.md#modules) / [Handsdown](../../index.md#handsdown) / [AST Parser](../index.md#ast-parser) / [Node Records](index.md#node-records) / AttributeRecord
    - [AttributeRecord](#attributerecord)
        - [AttributeRecord().related_names](#attributerecordrelated_names)

## AttributeRecord

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/attribute_record.py#L15)

```python
class AttributeRecord(NodeRecord):
    def __init__(node: ast.Assign) -> None:
```

Wrapper for an `ast.Assign` node of a module or class attribute.

#### Arguments

- `node` - AST node.

#### See also

- [NodeRecord](node_record.md#noderecord)

### AttributeRecord().related_names

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/attribute_record.py#L35)

```python
@property
def related_names() -> Set[Text]:
```
