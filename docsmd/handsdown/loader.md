# Loader

[Handsdown API Index](../README.md#handsdown-api-index) /
[Handsdown](./index.md#handsdown) /
Loader

> Auto-generated documentation for [handsdown.loader](https://github.com/vemel/handsdown/blob/main/handsdown/loader.py) module.

## Loader

[Show source in loader.py:17](https://github.com/vemel/handsdown/blob/main/handsdown/loader.py#L17)

Loader for python source code.

#### Examples

```python
loader = Loader(Path('path/to/my_module/'))
my_module_utils = loader.import_module('my_module.utils')
```

#### Arguments

- `root_path` - Root path of the project.
- `output_path` - Docs output path.
- `encoding` - File encoding.

#### Signature

```python
class Loader:
    def __init__(
        self, root_path: Path, output_path: Path, encoding: str = ENCODING
    ) -> None:
        ...
```

#### See also

- [ENCODING](./constants.md#encoding)

### Loader().get_import_string

[Show source in loader.py:124](https://github.com/vemel/handsdown/blob/main/handsdown/loader.py#L124)

Get Python import string for a source `source_path` relative to `root_path`.

#### Examples

```python
loader = Loader(root_path=Path("/root"), ...)
loader.get_import_string('/root/my_module/test.py')
'my_module.test'

loader.get_import_string('/root/my_module/__init__.py')
'my_module'
```

#### Arguments

- `source_path` - Path to a source file.

#### Returns

A Python import string.

#### Signature

```python
def get_import_string(self, source_path: Path) -> str:
    ...
```

### Loader().get_module_record

[Show source in loader.py:59](https://github.com/vemel/handsdown/blob/main/handsdown/loader.py#L59)

Build `ModuleRecord` for given `source_path`.

#### Arguments

- `source_path` - Absolute path to source file.

#### Returns

A new `ModuleRecord` instance or None if there is ntohing to import.

#### Raises

- `LoaderError` - If python source cannot be loaded.

#### Signature

```python
def get_module_record(self, source_path: Path) -> Optional[ModuleRecord]:
    ...
```

### Loader.parse_module_record

[Show source in loader.py:109](https://github.com/vemel/handsdown/blob/main/handsdown/loader.py#L109)

Parse `ModuleRecord` children and fully load a tree for it.

#### Raises

- `LoaderError` - If python source cannot be parsed.

#### Signature

```python
@staticmethod
def parse_module_record(module_record: ModuleRecord) -> None:
    ...
```

#### See also

- [ModuleRecord](ast_parser/node_records/module_record.md#modulerecord)



