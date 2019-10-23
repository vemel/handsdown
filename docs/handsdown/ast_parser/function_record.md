# FunctionRecord

> Auto-generated documentation for [handsdown.ast_parser.function_record](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/function_record.py) module.

- [Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / [Ast Parser](index.md#ast-parser) / FunctionRecord
  - [FunctionRecord](#functionrecord)
    - [FunctionRecord().parse_type_comments](#functionrecordparse_type_comments)
    - [FunctionRecord().related_names](#functionrecordrelated_names)

## FunctionRecord

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/function_record.py#L10)

```python
class FunctionRecord(NodeRecord):
    def __init__(node: bool, is_method: ast.FunctionDef) -> None:
```

### FunctionRecord().parse_type_comments

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/function_record.py#L104)

```python
def parse_type_comments(lines: List[Text]) -> None:
```

### FunctionRecord().related_names

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/function_record.py#L26)

```python
@property
def related_names() -> Set[Text]:
```
