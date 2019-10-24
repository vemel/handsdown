# ImportRecord

> Auto-generated documentation for [handsdown.ast_parser.node_records.import_record](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/import_record.py) module.

- [Handsdown](../../../README.md#-handsdown---python-documentation-generator) / [Modules](../../../MODULES.md#modules) / [Handsdown](../../index.md#handsdown) / [Ast Parser](../index.md#ast-parser) / [Node Records](index.md#node-records) / ImportRecord
    - [ImportRecord](#importrecord)
        - [ImportRecord().get_import_string](#importrecordget_import_string)
        - [ImportRecord().match](#importrecordmatch)

## ImportRecord

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/import_record.py#L10)

```python
class ImportRecord(NodeRecord):
    def __init__(node: ast.alias, alias: ASTImport) -> None:
```

#### See also

- [ASTImport](../type_defs.md#astimport)
- [NodeRecord](node_record.md#noderecord)

### ImportRecord().get_import_string

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/import_record.py#L23)

```python
def get_import_string() -> Text:
```

### ImportRecord().match

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/import_record.py#L46)

```python
def match(string: Text) -> Optional[Text]:
```
