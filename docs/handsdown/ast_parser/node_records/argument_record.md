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
        default: Optional[ast.expr] = None,
        type_hint: Optional[ast.expr] = None,
        prefix: Text = '',
    ) -> None:
```

Wrapper for an `ast.arg` node.

#### Arguments

- `node` - AST node.

#### See also

- [NodeRecord](node_record.md#noderecord)

### ArgumentRecord().related_names

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/argument_record.py#L41)

```python
@property
def related_names() -> Set[Text]:
```
