# ArgumentRecord

> Auto-generated documentation for [handsdown.ast_parser.node_records.argument_record](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/argument_record.py) module.

Wrapper for an `ast.arg` node.

- [Handsdown](../../../README.md#-handsdown---python-documentation-generator) / [Modules](../../../MODULES.md#modules) / [Handsdown](../../index.md#handsdown) / [AST Parser](../index.md#ast-parser) / [Node Records](index.md#node-records) / ArgumentRecord
    - [ArgumentRecord](#argumentrecord)
        - [ArgumentRecord().related_names](#argumentrecordrelated_names)

## ArgumentRecord

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/argument_record.py#L14)

```python
class ArgumentRecord(NodeRecord):
    def __init__(
        node: ast.arg,
        name: Text,
        default: Optional[ExpressionRecord] = None,
        type_hint: Optional[ExpressionRecord] = None,
        prefix: Text = '',
    ) -> None:
```

Wrapper for an `ast.arg` node.

#### Arguments

- `node` - AST node.

#### See also

- [ExpressionRecord](expression_record.md#expressionrecord)
- [NodeRecord](node_record.md#noderecord)

### ArgumentRecord().related_names

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/argument_record.py#L37)

```python
@property
def related_names() -> Set[Text]:
```
