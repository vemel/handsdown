# FunctionRecord

> Auto-generated documentation for [handsdown.ast_parser.node_records.function_record](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/function_record.py) module.

Wrapper for an `ast.FunctionDef` node.

- [Handsdown](../../../README.md#-handsdown---python-documentation-generator) / [Modules](../../../MODULES.md#modules) / [Handsdown](../../index.md#handsdown) / [Ast Parser](../index.md#ast-parser) / [Node Records](index.md#node-records) / FunctionRecord
    - [FunctionRecord](#functionrecord)
        - [FunctionRecord().parse_type_comments](#functionrecordparse_type_comments)
        - [FunctionRecord().related_names](#functionrecordrelated_names)

## FunctionRecord

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/function_record.py#L17)

```python
class FunctionRecord(NodeRecord):
    def __init__(node: bool, is_method: ast.FunctionDef) -> None:
```

Wrapper for an `ast.FunctionDef` node.

#### Arguments

- `node` - AST node.

#### See also

- [NodeRecord](node_record.md#noderecord)

### FunctionRecord().parse_type_comments

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/function_record.py#L100)

```python
def parse_type_comments(lines: List[Text]) -> None:
```

Extract comment type annotations from a function definiition lines.

Sets `arguemnts_record` to a new `TextRecord` for each found type annotaiton.
Also sets `return_type_hint` to a `TextRecord` if fucntion return type found.

### FunctionRecord().related_names

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/function_record.py#L45)

```python
@property
def related_names() -> Set[Text]:
```
