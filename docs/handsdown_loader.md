# Handsdown: Loader

- [Handsdown: Loader](#handsdown-loader)
  - [LoaderError](#loadererror)
  - [Loader](#loader)
    - [Loader().get_module_record](#loaderget_module_record)
    - [Loader().get_object_docstring](#loaderget_object_docstring)
    - [Loader.get_object_signature](#loaderget_object_signature)
    - [Loader.get_source_line_number](#loaderget_source_line_number)
    - [Loader().import_module](#loaderimport_module)

> Auto-generated documentation for [handsdown.loader](../handsdown/loader.py) module.

## LoaderError

[🔍 find in source code](../handsdown/loader.py#L18)

```python
class LoaderError(*args, **kwargs)
```

## Loader

[🔍 find in source code](../handsdown/loader.py#L22)

```python
class Loader(root_path: pathlib.Path, logger: logging.Logger) -> None
```

Loader for python source code.

#### Examples

```python
loader = Loader(Path('path/to/my_module/'))
my_module_utils = loader.import_module('my_module.utils')
```

#### Arguments

- `import_paths` - List of import paths for `import_module` lookup.

### Loader().get_module_record

[🔍 find in source code](../handsdown/loader.py#L66)

```python
def get_module_record(
    source_path: pathlib.Path,
) -> Union[handsdown.module_record.ModuleRecord, NoneType]
```

Build `ModuleRecord` for given `source_path`.

#### Arguments

- `source_path` - Absolute path to source file.

#### Returns

A new `ModuleRecord` instance or None if there is ntohing to import.

#### Raises

- [LoaderError](#loadererror) - If module or any of it's objects cannot be imported.

#### See also

- [ModuleRecord](./handsdown_module_record.md#modulerecord)

### Loader().get_object_docstring

[🔍 find in source code](../handsdown/loader.py#L138)

```python
def get_object_docstring(obj: Any) -> str
```

Get trimmed object docstring or an empty string.

#### Arguments

- `obj` - Object to inspect.

#### Returns

A string with object docsting.

### Loader.get_object_signature

[🔍 find in source code](../handsdown/loader.py#L121)

```python
def get_object_signature(obj: Any) -> Union[str, NoneType]
```

Get class, method or function signature. If object is not callable -
returns None.

#### Arguments

- `obj` - Object to inspect.

#### Returns

A string with object signature or None.

### Loader.get_source_line_number

[🔍 find in source code](../handsdown/loader.py#L311)

```python
def get_source_line_number(obj: Any) -> int
```

Get line number in source file where `obj` is declared.

- `obj` - Object to inspect.

#### Returns

A line number as an integer, starting for 1.

### Loader().import_module

[🔍 find in source code](../handsdown/loader.py#L179)

```python
def import_module(file_path: pathlib.Path) -> Any
```

Import module using `import_paths` list. Clean up all patches afterwards.

- Patch `sys.path` to add current repo to it.
- Patch `os.environ` to avoid failing on undefined variables.
- Patch `typing.TYPE_CHECKING` to `True`.

#### Arguments

- `file_path` - Abslute path to source file.

#### Returns

Imported module object.
