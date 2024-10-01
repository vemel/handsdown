# TextRecord

Wrapper for a text-only `ast.expr` node.

[Handsdown API Index](../../../README.md#handsdown-api-index) / [Handsdown](../../index.md#handsdown) / [AST Parser](../index.md#ast-parser) / [Node Records](./index.md#node-records) / TextRecord

> Auto-generated documentation for [handsdown.ast_parser.node_records.text_record](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/text_record.py) module.

## TextRecord

[Show source in text_record.py:12](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/text_record.py#L12)

Wrapper for a text-only `ast.expr` node.

#### Arguments

- `node` - Related AST node.
- `text` - Text to represent it.

#### Signature

```python
class TextRecord(ExpressionRecord):
    def __init__(self, node: ast.AST, text: str) -> None:
        ...
```

#### See also

- [ExpressionRecord](./expression_record.md#expressionrecord)

### TextRecord().related_names

[Show source in text_record.py:28](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/text_record.py#L28)

A list of fake `ast.Name.id` records inside the node.

#### Examples

```python
TextRecord(ast_node, 'Union[str, MyClass]').related_names
{'Union', 'str', 'MyClass'}
```

#### Returns

A set of related names.

#### Signature

```python
@property
def related_names(self) -> Set[str]:
    ...
```
