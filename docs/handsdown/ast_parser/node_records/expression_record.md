# ExpressionRecord

> Auto-generated documentation for [handsdown.ast_parser.node_records.expression_record](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/expression_record.py) module.

Wrapper for an `ast.expr` node.

- [Handsdown](../../../README.md#-handsdown---python-documentation-generator) / [Modules](../../../MODULES.md#modules) / [Handsdown](../../index.md#handsdown) / [AST Parser.](../index.md#ast-parser) / [Node Records](index.md#node-records) / ExpressionRecord
    - [ExpressionRecord](#expressionrecord)
        - [ExpressionRecord().related_names](#expressionrecordrelated_names)

## ExpressionRecord

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/expression_record.py#L13)

```python
class ExpressionRecord(NodeRecord):
    def __init__(node: ast.AST) -> None:
```

Wrapper for an `ast.expr` node.

#### Arguments

- `node` - AST node.

#### See also

- [NodeRecord](node_record.md#noderecord)

### ExpressionRecord().related_names

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/expression_record.py#L28)

```python
@property
def related_names() -> Set[str]:
```

Set of related names.
