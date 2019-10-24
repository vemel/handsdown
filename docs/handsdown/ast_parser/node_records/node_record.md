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

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/node_record.py#L16)

```python
class NodeRecord(object):
    def __init__(node: ast.AST) -> None:
```

### NodeRecord().get_documented_attribute_strings

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/node_record.py#L238)

```python
def get_documented_attribute_strings() -> List[Text]:
```

### NodeRecord().get_related_import_strings

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/node_record.py#L213)

```python
def get_related_import_strings(module_record: ModuleRecord) -> Set[Text]:
```

#### See also

- [ModuleRecord](module_record.md#modulerecord)

### NodeRecord().is_line_fit

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/node_record.py#L205)

```python
def is_line_fit(line: int, indent: Text) -> bool:
```

### NodeRecord().iter_children

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/node_record.py#L73)

```python
def iter_children() -> Generator[NodeRecord, None, None]:
```

### NodeRecord().line_number

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/node_record.py#L48)

```python
@property
def line_number() -> int:
```

### NodeRecord().line_number

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/node_record.py#L58)

```python
@line_number.setter
def line_number(value: int) -> None:
```

### NodeRecord().parse

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/node_record.py#L87)

```python
def parse() -> None:
```

### NodeRecord().related_names

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/node_record.py#L77)

```python
@property
def related_names() -> Set[Text]:
```

### NodeRecord().render

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/node_record.py#L154)

```python
def render(indent: bool = 0, allow_multiline: int = False) -> Text:
```

### NodeRecord().render_indent

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/node_record.py#L209)

```python
def render_indent(indent: int) -> Text:
```
