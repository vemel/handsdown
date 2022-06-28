# ImportRecord

[Handsdown API Index](../../../README.md#handsdown-api-index) /
[Handsdown](../../index.md#handsdown) /
[AST Parser](../index.md#ast-parser) /
[Node Records](./index.md#node-records) /
ImportRecord

> Auto-generated documentation for [handsdown.ast_parser.node_records.import_record](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/import_record.py) module.

- [ImportRecord](#importrecord)
  - [ImportRecord](#importrecord-1)
    - [ImportRecord().get_import_string](#importrecord()get_import_string)
    - [ImportRecord().match](#importrecord()match)

## ImportRecord

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/import_record.py#L12)

Wrapper for an `ast.Import` and `ast.ImportFrom` nodes.

#### Arguments

- `node` - AST node.
- `alias` - AST node with import alias.

#### Signature

```python
class ImportRecord(NodeRecord):
    def __init__(self, node: ASTImport, alias: ast.alias) -> None:
        ...
```

#### See also

- [ASTImport](../type_defs.md#astimport)
- [NodeRecord](./node_record.md#noderecord)

### ImportRecord().get_import_string

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/import_record.py#L32)

Get import string from a node.

#### Returns

An absolute import string.

#### Signature

```python
def get_import_string(self) -> ImportString:
    ...
```

#### See also

- [ImportString](../../utils/import_string.md#importstring)

### ImportRecord().match

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/import_record.py#L55)

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

#### Signature

```python
def match(self, name: str) -> Optional[ImportString]:
    ...
```


