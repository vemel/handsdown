# FunctionRecord

[Handsdown API Index](../../../README.md#handsdown-api-index) /
[Handsdown](../../index.md#handsdown) /
[AST Parser](../index.md#ast-parser) /
[Node Records](./index.md#node-records) /
FunctionRecord

> Auto-generated documentation for [handsdown.ast_parser.node_records.function_record](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/function_record.py) module.

## FunctionRecord

[Show source in function_record.py:16](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/function_record.py#L16)

Wrapper for an `ast.FunctionDef` and `ast.AsyncFunctionDef` node.

#### Arguments

- `node` - AST node.

#### Signature

```python
class FunctionRecord(NodeRecord):
    def __init__(self, node: ASTFunctionDef, is_method: bool) -> None:
        ...
```

#### See also

- [ASTFunctionDef](../type_defs.md#astfunctiondef)
- [NodeRecord](./node_record.md#noderecord)

### FunctionRecord().is_init

[Show source in function_record.py:140](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/function_record.py#L140)

Returns True if function is an __init__ method.

#### Signature

```python
def is_init(self) -> bool:
    ...
```

### FunctionRecord().parse_type_comments

[Show source in function_record.py:97](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/function_record.py#L97)

Extract comment type annotations from a function definiition lines.

Sets `arguments_record` to a new `TextRecord` for each found type annotaiton.
Also sets `return_type_hint` to a `TextRecord` if function return type found.

#### Signature

```python
def parse_type_comments(self, lines: Iterable[str]) -> None:
    ...
```

### FunctionRecord().related_names

[Show source in function_record.py:40](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/function_record.py#L40)

Set of related names.

#### Signature

```python
@property
def related_names(self) -> Set[str]:
    ...
```
