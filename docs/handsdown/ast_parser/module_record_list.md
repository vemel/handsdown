# ModuleRecordList

[Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / [AST Parser](index.md#ast-parser) / ModuleRecordList

> Auto-generated documentation for [handsdown.ast_parser.module_record_list](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/module_record_list.py) module.

- [ModuleRecordList](#modulerecordlist)
  - [ModuleRecordList](#modulerecordlist-1)
    - [ModuleRecordList().__iter__](#modulerecordlist()__iter__)
    - [ModuleRecordList().add](#modulerecordlist()add)
    - [ModuleRecordList().find_module_record](#modulerecordlist()find_module_record)
    - [ModuleRecordList().get_package_names](#modulerecordlist()get_package_names)

## ModuleRecordList

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/module_record_list.py#L11)

Aggregation of `ModuleRecord` objects.

#### Signature

```python
class ModuleRecordList:
    def __init__(self) -> None:
        ...
```

### ModuleRecordList().__iter__

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/module_record_list.py#L62)

Iterate over all added `ModuleRecord` entries.

#### Yields

`ModuleRecord` entries.

#### Signature

```python
def __iter__(self) -> Iterator[ModuleRecord]:
    ...
```

### ModuleRecordList().add

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/module_record_list.py#L52)

Add new `ModuleRecord`.

#### Arguments

- `module_record` - A new `ModuleRecord`

#### Signature

```python
def add(self, module_record: ModuleRecord) -> None:
    ...
```

#### See also

- [ModuleRecord](node_records/module_record.md#modulerecord)

### ModuleRecordList().find_module_record

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/module_record_list.py#L21)

Find `ModuleRecord` by it's import string.

#### Arguments

- `import_string` - Object import string.

#### Returns

Found `NodeRecord` instance or None.

#### Signature

```python
def find_module_record(self, import_string: ImportString) -> Optional[ModuleRecord]:
    ...
```

#### See also

- [ImportString](../utils/import_string.md#importstring)

### ModuleRecordList().get_package_names

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/module_record_list.py#L43)

Get top level import strings.

#### Returns

A set of top level imports as strings.

#### Signature

```python
def get_package_names(self) -> Set[str]:
    ...
```


