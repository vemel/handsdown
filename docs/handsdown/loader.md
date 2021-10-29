# Loader

> Auto-generated documentation for [handsdown.loader](https://github.com/vemel/handsdown/blob/master/handsdown/loader.py) module.

Loader for python source code.

- [Handsdown](../README.md#-handsdown---python-documentation-generator) / [Modules](../MODULES.md#modules) / [Handsdown](index.md#handsdown) / Loader
    - [Loader](#loader)
        - [Loader().get_import_string](#loaderget_import_string)
        - [Loader().get_module_record](#loaderget_module_record)
        - [Loader().get_output_path](#loaderget_output_path)
        - [Loader.parse_module_record](#loaderparse_module_record)
    - [LoaderError](#loadererror)

## Loader

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/loader.py#L21)

```python
class Loader():
    def __init__(root_path: Path, output_path: Path) -> None:
```

Loader for python source code.

#### Examples

```python
loader = Loader(Path('path/to/my_module/'))
my_module_utils = loader.import_module('my_module.utils')
```

#### Arguments

- `root_path` - Root path of the project.
- `output_path` - Docs output path.

### Loader().get_import_string

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/loader.py#L122)

```python
def get_import_string(source_path: Path) -> str:
```

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

### Loader().get_module_record

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/loader.py#L61)

```python
def get_module_record(source_path: Path) -> Optional[ModuleRecord]:
```

Build `ModuleRecord` for given `source_path`.

#### Arguments

- `source_path` - Absolute path to source file.

#### Returns

A new `ModuleRecord` instance or None if there is ntohing to import.

#### Raises

- `LoaderError` - If python source cannot be loaded.

### Loader().get_output_path

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/loader.py#L41)

```python
def get_output_path(source_path: Path) -> Path:
```

Get output MD document path based on `source_path`.

#### Arguments

- `source_path` - Path to source code file.

#### Returns

A path to the output `.md` file even if it does not exist yet.

### Loader.parse_module_record

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/loader.py#L107)

```python
@staticmethod
def parse_module_record(module_record: ModuleRecord) -> None:
```

Parse `ModuleRecord` children and fully load a tree for it.

#### Raises

- `LoaderError` - If python source cannot be parsed.

#### See also

- [ModuleRecord](ast_parser/node_records/module_record.md#modulerecord)

## LoaderError

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/loader.py#L15)

```python
class LoaderError(Exception):
```

Main error for [Loader](#loader) class.
