# NodeRecord

> Auto-generated documentation for [handsdown.ast_parser.node_record](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_record.py) module.

- [Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / [Ast Parser](index.md#ast-parser) / NodeRecord
  - [NodeRecord](#noderecord)
    - [NodeRecord().get_related_import_strings](#noderecordget_related_import_strings)
    - [NodeRecord().is_line_fit](#noderecordis_line_fit)
    - [NodeRecord().iter_children](#noderecorditer_children)
    - [NodeRecord().parse](#noderecordparse)
    - [NodeRecord().related_names](#noderecordrelated_names)
    - [NodeRecord().render](#noderecordrender)
    - [NodeRecord().render_indent](#noderecordrender_indent)

## NodeRecord

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_record.py#L15)

```python
class NodeRecord(object):
    def __init__(node: Union[ast.AST, Text]) -> None:
```

### NodeRecord().get_related_import_strings

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_record.py#L331)

```python
def get_related_import_strings(module_record: ModuleRecord) -> Set[Text]:
```

### NodeRecord().is_line_fit

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_record.py#L323)

```python
def is_line_fit(line: int, indent: Text) -> bool:
```

### NodeRecord().iter_children

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_record.py#L65)

```python
def iter_children() -> Generator[NodeRecord, None, None]:
```

### NodeRecord().parse

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_record.py#L79)

```python
def parse() -> None:
```

### NodeRecord().related_names

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_record.py#L69)

```python
@property
def related_names() -> Set[Text]:
```

### NodeRecord().render

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_record.py#L136)

```python
def render(indent: int = 0) -> Text:
```

### NodeRecord().render_indent

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_record.py#L327)

```python
def render_indent(indent: int) -> Text:
```