# ClassRecord

[Handsdown](../../../README.md#-handsdown---python-documentation-generator) / [Modules](../../../MODULES.md#modules) / [Handsdown](../../index.md#handsdown) / [AST Parser](../index.md#ast-parser) / [Node Records](index.md#node-records) / ClassRecord

> Auto-generated documentation for [handsdown.ast_parser.node_records.class_record](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/class_record.py) module.

- [ClassRecord](#classrecord)

## ClassRecord

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/class_record.py#L17)

Wrapper for an `ast.ClassDef` node.

#### Arguments

- `node` - AST node.

#### Signature

```python
class ClassRecord(NodeRecord):
    def __init__(self, node: ast.ClassDef) -> None:
        ...
```

#### See also
- [NodeRecord](node_record.md#noderecord)

### ClassRecord().find_record

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/class_record.py#L35)

Find child method or attribute record.

#### Arguments

- `name` - Record name to lookup.

#### Returns

Itself or None.

#### Signature

```python
def find_record(self, name: str) -> Optional[NodeRecord]:
    ...
```

### ClassRecord().get_public_methods

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/class_record.py#L88)

Get Class public methods.Skips methods with names starting with `_` and magic methods  `__` if
they have no docstring. Method `__init__` is always skipped.

#### Returns

A list of child records.

#### Signature

```python
def get_public_methods(self) -> List[FunctionRecord]:
    ...
```

### ClassRecord().init_method

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/class_record.py#L155)

Get the `__init__` method.

#### Signature

```python
@property
def init_method(self) -> Optional[FunctionRecord]:
    ...
```

### ClassRecord().iter_records

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/class_record.py#L75)

Iterate over Class public methods.

#### Yields

A child record.

#### Signature

```python
def iter_records(self) -> Iterator[NodeRecord]:
    ...
```

### ClassRecord().related_names

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/class_record.py#L58)

Set of related names.

#### Signature

```python
@property
def related_names(self) -> Set[str]:
    ...
```


