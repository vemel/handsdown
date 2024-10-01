# AttributeRecord

Wrapper for an `ast.Assign` node of a module or class attribute.

[Handsdown API Index](../../../README.md#handsdown-api-index) / [Handsdown](../../index.md#handsdown) / [AST Parser](../index.md#ast-parser) / [Node Records](./index.md#node-records) / AttributeRecord

> Auto-generated documentation for [handsdown.ast_parser.node_records.attribute_record](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/attribute_record.py) module.

## AttributeRecord

[Show source in attribute_record.py:12](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/attribute_record.py#L12)

Wrapper for an `ast.Assign` node of a module or class attribute.

#### Arguments

- `node` - AST node.

#### Signature

```python
class AttributeRecord(NodeRecord):
    def __init__(self, node: Union[ast.Assign, ast.AnnAssign]) -> None:
        ...
```

#### See also

- [NodeRecord](./node_record.md#noderecord)

### AttributeRecord().append_to

[Show source in attribute_record.py:69](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/attribute_record.py#L69)

Append AttributeRecord to NodeRecord.

#### Signature

```python
def append_to(self, node_record: NodeRecord) -> None:
    ...
```

#### See also

- [NodeRecord](./node_record.md#noderecord)

### AttributeRecord().related_names

[Show source in attribute_record.py:32](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/attribute_record.py#L32)

Set of related names.

#### Signature

```python
@property
def related_names(self) -> Set[str]:
    ...
```

### AttributeRecord().render

[Show source in attribute_record.py:55](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/attribute_record.py#L55)

Render attribute with docstring.

#### Signature

```python
def render(self) -> str:
    ...
```
