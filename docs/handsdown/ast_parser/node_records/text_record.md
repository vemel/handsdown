# TextRecord

> Auto-generated documentation for [handsdown.ast_parser.node_records.text_record](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/text_record.py) module.

Wrapper for a text-only `ast.expr` node.

- [Handsdown](../../../README.md#-handsdown---python-documentation-generator) / [Modules](../../../MODULES.md#modules) / [Handsdown](../../index.md#handsdown) / [AST Parser.](../index.md#ast-parser) / [Node Records](index.md#node-records) / TextRecord
    - [TextRecord](#textrecord)
        - [TextRecord().related_names](#textrecordrelated_names)

## TextRecord

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/text_record.py#L12)

```python
class TextRecord(ExpressionRecord):
    def __init__(node: ast.AST, text: str) -> None:
```

Wrapper for a text-only `ast.expr` node.

#### Arguments

- `node` - Related AST node.
- `text` - Text to represent it.

#### See also

- [ExpressionRecord](expression_record.md#expressionrecord)

### TextRecord().related_names

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/text_record.py#L28)

```python
@property
def related_names() -> Set[str]:
```

A list of fake `ast.Name.id` records inside the node.

#### Examples

```python
TextRecord(ast_node, 'Union[str, MyClass]').related_names
{'Union', 'str', 'MyClass'}
```

#### Returns

A set of related names.
