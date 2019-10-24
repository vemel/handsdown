# ExpressionRecord

> Auto-generated documentation for [handsdown.ast_parser.node_records.expression_record](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/expression_record.py) module.

- [Handsdown](../../../README.md#-handsdown---python-documentation-generator) / [Modules](../../../MODULES.md#modules) / [Handsdown](../../index.md#handsdown) / [Ast Parser](../index.md#ast-parser) / [Node Records](index.md#node-records) / ExpressionRecord
  - [ExpressionRecord](#expressionrecord)
    - [ExpressionRecord().related_names](#expressionrecordrelated_names)

## ExpressionRecord

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/expression_record.py#L12)

```python
class ExpressionRecord(NodeRecord):
    def __init__(node: ast.AST) -> None:
```

### ExpressionRecord().related_names

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/expression_record.py#L21)

```python
@property
def related_names() -> Set[Text]:
```
