# ModuleRecord

> Auto-generated documentation for [handsdown.ast_parser.node_records.module_record](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/module_record.py) module.

- [Handsdown](../../../README.md#-handsdown---python-documentation-generator) / [Modules](../../../MODULES.md#modules) / [Handsdown](../../index.md#handsdown) / [Ast Parser](../index.md#ast-parser) / [Node Records](index.md#node-records) / ModuleRecord
  - [ModuleRecord](#modulerecord)
    - [ModuleRecord().build_children](#modulerecordbuild_children)
    - [ModuleRecord().find_record](#modulerecordfind_record)
    - [ModuleRecord().get_title_parts](#modulerecordget_title_parts)
    - [ModuleRecord().iter_records](#modulerecorditer_records)
    - [ModuleRecord().related_names](#modulerecordrelated_names)

## ModuleRecord

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/module_record.py#L16)

```python
class ModuleRecord(NodeRecord):
    def __init__(
        source_path: Text,
        source_lines: List[Text],
        import_string: Path,
    ) -> None:
```

### ModuleRecord().build_children

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/module_record.py#L110)

```python
def build_children() -> None:
```

### ModuleRecord().find_record

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/module_record.py#L52)

```python
def find_record(import_string: Text) -> Optional[NodeRecord]:
```

### ModuleRecord().get_title_parts

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/module_record.py#L39)

```python
def get_title_parts() -> List[Text]:
```

### ModuleRecord().iter_records

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/module_record.py#L66)

```python
def iter_records() -> Generator[Tuple[NodeRecord, ...], None, None]:
```

### ModuleRecord().related_names

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/module_record.py#L34)

```python
@property
def related_names() -> Set[Text]:
```
