# ArgumentRecord

> Auto-generated documentation for [handsdown.ast_parser.argument_record](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/argument_record.py) module.

- [Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / [Ast Parser](index.md#ast-parser) / ArgumentRecord
  - [ArgumentRecord](#argumentrecord)
    - [ArgumentRecord().related_names](#argumentrecordrelated_names)

## ArgumentRecord

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/argument_record.py#L11)

```python
class ArgumentRecord(NodeRecord):
    def __init__(node: ast.arg) -> None:
```

### ArgumentRecord().related_names

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/argument_record.py#L49)

```python
@property
def related_names() -> Set[Text]:
```
