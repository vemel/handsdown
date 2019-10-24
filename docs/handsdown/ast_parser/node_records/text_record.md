# TextRecord

> Auto-generated documentation for [handsdown.ast_parser.node_records.text_record](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/text_record.py) module.

- [Handsdown](../../../README.md#-handsdown---python-documentation-generator) / [Modules](../../../MODULES.md#modules) / [Handsdown](../../index.md#handsdown) / [Ast Parser](../index.md#ast-parser) / [Node Records](index.md#node-records) / TextRecord
  - [TextRecord](#textrecord)
    - [TextRecord().related_names](#textrecordrelated_names)

## TextRecord

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/text_record.py#L11)

```python
class TextRecord(ExpressionRecord):
    def __init__(node: Text, text: ast.AST) -> None:
```

### TextRecord().related_names

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/text_record.py#L20)

```python
@property
def related_names() -> Set[Text]:
```
