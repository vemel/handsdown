# ArgumentRecord

> Auto-generated documentation for [handsdown.ast_parser.node_records.argument_record](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/argument_record.py) module.

Wrapper for an `ast.arg` node.

- [Handsdown](../../../README.md#-handsdown---python-documentation-generator) / [Modules](../../../MODULES.md#modules) / [Handsdown](../../index.md#handsdown) / [AST Parser](../index.md#ast-parser) / [Node Records](index.md#node-records) / ArgumentRecord
    - [ArgumentRecord](#argumentrecord)
        - [ArgumentRecord().default](#argumentrecorddefault)
        - [ArgumentRecord().related_names](#argumentrecordrelated_names)
        - [ArgumentRecord().set_default](#argumentrecordset_default)

## ArgumentRecord

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/argument_record.py#L15)

```python
class ArgumentRecord(NodeRecord):
    def __init__(
        node: ast.arg,
        name: Text,
        type_hint: Optional[ast.expr] = None,
        prefix: Text = '',
    ) -> None:
```

Wrapper for an `ast.arg` node.

#### Arguments

- `node` - AST node.
- `name` - Argument name.
- `type_hint` - Argument type hint.
- `prefix` - Prefix for arguemnt name, used for starargs.

#### See also

- [NodeRecord](node_record.md#noderecord)

### ArgumentRecord().default

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/argument_record.py#L42)

```python
@property
def default() -> Optional[ExpressionRecord]:
```

Default value of the argument.

#### Returns

Default exression or None.

#### See also

- [ExpressionRecord](expression_record.md#expressionrecord)

### ArgumentRecord().related_names

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/argument_record.py#L66)

```python
@property
def related_names() -> Set[Text]:
```

### ArgumentRecord().set_default

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/argument_record.py#L53)

```python
def set_default(node: Node) -> None:
```

Set default expression from test or `ast.AST` node.

#### Arguments

- `node` - Text or AST node.

#### See also

- [Node](../type_defs.md#node)
