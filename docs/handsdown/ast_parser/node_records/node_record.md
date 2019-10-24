# NodeRecord

> Auto-generated documentation for [handsdown.ast_parser.node_records.node_record](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/node_record.py) module.

- [Handsdown](../../../README.md#-handsdown---python-documentation-generator) / [Modules](../../../MODULES.md#modules) / [Handsdown](../../index.md#handsdown) / [Ast Parser](../index.md#ast-parser) / [Node Records](index.md#node-records) / NodeRecord
  - [NodeRecord](#noderecord)
    - [NodeRecord().get_documented_attribute_strings](#noderecordget_documented_attribute_strings)
    - [NodeRecord().get_related_import_strings](#noderecordget_related_import_strings)
    - [NodeRecord().is_line_fit](#noderecordis_line_fit)
    - [NodeRecord().iter_children](#noderecorditer_children)
    - [NodeRecord().line_number](#noderecordline_number)
    - [NodeRecord().line_number](#noderecordline_number)
    - [NodeRecord().parse](#noderecordparse)
    - [NodeRecord().related_names](#noderecordrelated_names)
    - [NodeRecord().render](#noderecordrender)
    - [NodeRecord().render_indent](#noderecordrender_indent)

## NodeRecord

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/node_record.py#L16)

```python
class NodeRecord(object):
    def __init__(node: ast.AST) -> None:
```

### NodeRecord().get_documented_attribute_strings

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/node_record.py#L221)

```python
def get_documented_attribute_strings() -> List[Text]:
```

### NodeRecord().get_related_import_strings

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/node_record.py#L197)

```python
def get_related_import_strings(module_record: ModuleRecord) -> Set[Text]:
```

### NodeRecord().is_line_fit

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/node_record.py#L189)

```python
def is_line_fit(line: int, indent: Text) -> bool:
```

### NodeRecord().iter_children

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/node_record.py#L77)

```python
def iter_children() -> Generator[NodeRecord, None, None]:
```

### NodeRecord().line_number

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/node_record.py#L45)

```python
@property
def line_number() -> int:
```

### NodeRecord().line_number

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/node_record.py#L54)

```python
@line_number.setter
def line_number(value: int) -> None:
```

### NodeRecord().parse

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/node_record.py#L91)

```python
def parse() -> None:
```

### NodeRecord().related_names

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/node_record.py#L81)

```python
@property
def related_names() -> Set[Text]:
```

### NodeRecord().render

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/node_record.py#L148)

```python
def render(indent: int = 0) -> Text:
```

### NodeRecord().render_indent

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/node_record.py#L193)

```python
def render_indent(indent: int) -> Text:
```
