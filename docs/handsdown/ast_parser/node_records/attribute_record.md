# AttributeRecord

> Auto-generated documentation for [handsdown.ast_parser.node_records.attribute_record](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/attribute_record.py) module.

Wrapper for an `ast.Assign` node of a module or class attribute.

- [Handsdown](../../../README.md#-handsdown---python-documentation-generator) / [Modules](../../../MODULES.md#modules) / [Handsdown](../../index.md#handsdown) / [AST Parser](../index.md#ast-parser) / [Node Records](index.md#node-records) / AttributeRecord
    - [AttributeRecord](#attributerecord)
        - [AttributeRecord().append_to](#attributerecordappend_to)
        - [AttributeRecord().related_names](#attributerecordrelated_names)
        - [AttributeRecord().render](#attributerecordrender)

## AttributeRecord

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/attribute_record.py#L12)

```python
class AttributeRecord(NodeRecord):
    def __init__(node: ast.Assign) -> None:
```

Wrapper for an `ast.Assign` node of a module or class attribute.

#### Arguments

- `node` - AST node.

#### See also

- [NodeRecord](node_record.md#noderecord)

### AttributeRecord().append_to

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/attribute_record.py#L57)

```python
def append_to(node_record: NodeRecord) -> None:
```

Append AttributeRecord to NodeRecord.

#### See also

- [NodeRecord](node_record.md#noderecord)

### AttributeRecord().related_names

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/attribute_record.py#L29)

```python
@property
def related_names() -> Set[str]:
```

Set of related names.

### AttributeRecord().render

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/attribute_record.py#L51)

```python
def render(indent: int = 0, allow_multiline: bool = False) -> str:
```

Render attribute with docstring.
