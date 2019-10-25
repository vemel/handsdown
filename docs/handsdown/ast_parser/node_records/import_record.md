# ImportRecord

> Auto-generated documentation for [handsdown.ast_parser.node_records.import_record](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/import_record.py) module.

Wrapper for an `ast.Import` and `ast.ImportFrom` nodes.

- [Handsdown](../../../README.md#-handsdown---python-documentation-generator) / [Modules](../../../MODULES.md#modules) / [Handsdown](../../index.md#handsdown) / [Ast Parser](../index.md#ast-parser) / [Node Records](index.md#node-records) / ImportRecord
    - [ImportRecord](#importrecord)
        - [ImportRecord().get_import_string](#importrecordget_import_string)
        - [ImportRecord().match](#importrecordmatch)

## ImportRecord

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/import_record.py#L13)

```python
class ImportRecord(NodeRecord):
    def __init__(node: ast.alias, alias: ASTImport) -> None:
```

Wrapper for an `ast.Import` and `ast.ImportFrom` nodes.

#### Arguments

- `node` - AST node.
- `alias` - AST node with import alias.

#### See also

- [ASTImport](../type_defs.md#astimport)
- [NodeRecord](node_record.md#noderecord)

### ImportRecord().get_import_string

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/import_record.py#L34)

```python
def get_import_string() -> Text:
```

Get import string from a node.

#### Returns

An absolute import string.

### ImportRecord().match

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/import_record.py#L63)

```python
def match(name: Text) -> Optional[Text]:
```

Check if `name` matches or stats with a local name.

#### Examples

```python
import_node = ast.parse('from my_module import Name as LocalName')
import_record = ImportRecord(import_node)

import_record.match('LocalName')
True

import_record.match('LocalName.child')
True

import_record.match('OtherName')
False

import_record.match('LocalNameOther')
False
```

#### Returns

True if name is imported object itself on one of his children.
