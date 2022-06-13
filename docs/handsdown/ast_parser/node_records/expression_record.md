# ExpressionRecord

[Handsdown](../../../README.md#-handsdown---python-documentation-generator) / [Modules](../../../MODULES.md#modules) / [Handsdown](../../index.md#handsdown) / [AST Parser](../index.md#ast-parser) / [Node Records](index.md#node-records) / ExpressionRecord

> Auto-generated documentation for [handsdown.ast_parser.node_records.expression_record](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/expression_record.py) module.

- [ExpressionRecord](#expressionrecord)

## ExpressionRecord

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/expression_record.py#L13)

Wrapper for an `ast.expr` node.

#### Arguments

- `node` - AST node.

#### Signature

```python
class ExpressionRecord(NodeRecord):
    def __init__(self, node: ast.AST) -> None:
        ...
```

#### See also
- [NodeRecord](node_record.md#noderecord)

### ExpressionRecord().related_names

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/expression_record.py#L28)

Set of related names.

#### Signature

```python
@property
def related_names(self) -> Set[str]:
    ...
```

### ExpressionRecord().render_str

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/expression_record.py#L54)

Render expression to a string.

#### Signature

```python
def render_str(self) -> str:
    ...
```


