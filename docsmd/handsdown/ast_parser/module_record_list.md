# ModuleRecordList

Aggregation of `ModuleRecord` objects.

[Handsdown API Index](../../README.md#handsdown-api-index) / [Handsdown](../index.md#handsdown) / [AST Parser](./index.md#ast-parser) / ModuleRecordList

> Auto-generated documentation for [handsdown.ast_parser.module_record_list](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/module_record_list.py) module.

## ModuleRecordList

[Show source in module_record_list.py:11](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/module_record_list.py#L11)

Aggregation of `ModuleRecord` objects.

#### Signature

```python
class ModuleRecordList:
    def __init__(self) -> None:
        ...
```

### ModuleRecordList().__iter__

[Show source in module_record_list.py:62](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/module_record_list.py#L62)

Iterate over all added `ModuleRecord` entries.

#### Yields

`ModuleRecord` entries.

#### Signature

```python
def __iter__(self) -> Iterator[ModuleRecord]:
    ...
```

#### See also

- [ModuleRecord](node_records/module_record.md#modulerecord)

### ModuleRecordList().add

[Show source in module_record_list.py:52](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/module_record_list.py#L52)

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

[Show source in module_record_list.py:21](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/module_record_list.py#L21)

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
- [ModuleRecord](node_records/module_record.md#modulerecord)

### ModuleRecordList().get_package_names

[Show source in module_record_list.py:43](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/module_record_list.py#L43)

Get top level import strings.

#### Returns

A set of top level imports as strings.

#### Signature

```python
def get_package_names(self) -> Set[str]:
    ...
```
