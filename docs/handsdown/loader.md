# Loader

[Handsdown](../README.md#-handsdown---python-documentation-generator) / [Modules](../MODULES.md#modules) / [Handsdown](index.md#handsdown) / Loader

> Auto-generated documentation for [handsdown.loader](https://github.com/vemel/handsdown/blob/main/handsdown/loader.py) module.

- [Loader](#loader)

## Loader

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/loader.py#L22)

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
- [ENCODING](settings.md#encoding)

### Loader().get_import_string

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/loader.py#L129)

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

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/loader.py#L64)

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

### Loader().get_output_path

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/loader.py#L44)

Get output MD document path based on `source_path`.

#### Arguments

- `source_path` - Path to source code file.

#### Returns

A path to the output `.md` file even if it does not exist yet.

#### Signature

```python
def get_output_path(self, source_path: Path) -> Path:
    ...
```

### Loader.parse_module_record

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/loader.py#L114)

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



## LoaderError

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/loader.py#L16)

Main error for `Loader` class.

#### Signature

```python
class LoaderError(Exception):
    ...
```


