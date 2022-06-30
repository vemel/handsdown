# ArgumentRecord

[Handsdown API Index](../../../README.md#handsdown-api-index) /
[Handsdown](../../index.md#handsdown) /
[AST Parser](../index.md#ast-parser) /
[Node Records](./index.md#node-records) /
ArgumentRecord

> Auto-generated documentation for [handsdown.ast_parser.node_records.argument_record](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/argument_record.py) module.

## ArgumentRecord

[Show source in argument_record.py:13](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/argument_record.py#L13)

Wrapper for an `ast.arg` node.

#### Arguments

- `node` - AST node.
- `name` - Argument name.
- `type_hint` - Argument type hint.
- `prefix` - Prefix for arguemnt name, used for starargs.

#### Signature

```python
class ArgumentRecord(NodeRecord):
    def __init__(
        self,
        node: ast.arg,
        name: str,
        type_hint: Optional[ast.expr] = None,
        prefix: str = "",
    ) -> None:
        ...
```

#### See also

- [NodeRecord](./node_record.md#noderecord)

### ArgumentRecord().default

[Show source in argument_record.py:39](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/argument_record.py#L39)

Default value of the argument.

#### Returns

Default exression or None.

#### Signature

```python
@property
def default(self) -> Optional[ExpressionRecord]:
    ...
```

### ArgumentRecord().related_names

[Show source in argument_record.py:71](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/argument_record.py#L71)

Set of related names.

#### Signature

```python
@property
def related_names(self) -> Set[str]:
    ...
```

### ArgumentRecord().required

[Show source in argument_record.py:49](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/argument_record.py#L49)

Whether the argument is required.

#### Returns

True if required, False otherwise.

#### Signature

```python
@property
def required(self) -> bool:
    ...
```

### ArgumentRecord().set_default

[Show source in argument_record.py:59](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/argument_record.py#L59)

Set default expression from test or `ast.AST` node.

#### Arguments

- `node` - Text or AST node.

#### Signature

```python
def set_default(self, node: Node) -> None:
    ...
```

#### See also

- [Node](../type_defs.md#node)



