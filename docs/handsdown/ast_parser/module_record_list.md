# ModuleRecordList

> Auto-generated documentation for [handsdown.ast_parser.module_record_list](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/module_record_list.py) module.

Aggregation of `ModuleRecord` objects.

- [Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / [AST Parser.](index.md#ast-parser) / ModuleRecordList
    - [ModuleRecordList](#modulerecordlist)
        - [ModuleRecordList().\_\_iter\_\_](#modulerecordlist__iter__)
        - [ModuleRecordList().add](#modulerecordlistadd)
        - [ModuleRecordList().find_module_record](#modulerecordlistfind_module_record)
        - [ModuleRecordList().get_package_names](#modulerecordlistget_package_names)

## ModuleRecordList

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/module_record_list.py#L11)

```python
class ModuleRecordList():
    def __init__() -> None:
```

Aggregation of `ModuleRecord` objects.

### ModuleRecordList().\_\_iter\_\_

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/module_record_list.py#L62)

```python
def __iter__() -> Iterator[ModuleRecord]:
```

Iterate over all added `ModuleRecord` entries.

#### Yields

`ModuleRecord` entries.

### ModuleRecordList().add

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/module_record_list.py#L52)

```python
def add(module_record: ModuleRecord) -> None:
```

Add new `ModuleRecord`.

#### Arguments

- `module_record` - A new `ModuleRecord`

#### See also

- [ModuleRecord](node_records/module_record.md#modulerecord)

### ModuleRecordList().find_module_record

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/module_record_list.py#L21)

```python
def find_module_record(import_string: ImportString) -> Optional[ModuleRecord]:
```

Find `ModuleRecord` by it's import string.

#### Arguments

- `import_string` - Object import string.

#### Returns

Found `NodeRecord` instance or None.

#### See also

- [ImportString](../utils/import_string.md#importstring)

### ModuleRecordList().get_package_names

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/module_record_list.py#L43)

```python
def get_package_names() -> Set[str]:
```

Get top level import strings.

#### Returns

A set of top level imports as strings.
