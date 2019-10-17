# Loader

> Auto-generated documentation for [handsdown.loader](../handsdown/loader.py) module.

- [Handsdown](./README.md#handsdown) / [Handsdown](./handsdown_index.md#handsdown) / Loader
  - [Loader](#loader)
    - [Loader()._discover_module_objects](#loader_discover_module_objects)
    - [Loader()._get_object_docstring](#loader_get_object_docstring)
    - [Loader()._setup_django](#loader_setup_django)
    - [Loader().get_module_record](#loaderget_module_record)
    - [Loader.get_object_signature](#loaderget_object_signature)
    - [Loader.get_source_line_number](#loaderget_source_line_number)
    - [Loader().import_module](#loaderimport_module)
    - [Loader().setup](#loadersetup)
  - [LoaderError](#loadererror)

## Loader

[🔍 find in source code](../handsdown/loader.py#L24)

```python
class Loader(root_path: pathlib.Path, logger: logging.Logger)
```

Loader for python source code.

#### Examples

```python
loader = Loader(Path('path/to/my_module/'))
my_module_utils = loader.import_module('my_module.utils')
```

#### Arguments

- `import_paths` - List of import paths for `import_module` lookup.

### Loader()._discover_module_objects

[🔍 find in source code](../handsdown/loader.py#L326)

```python
def _discover_module_objects(
    module_record: handsdown.module_record.ModuleRecord,
) -> Generator[handsdown.module_record.ModuleObjectRecord, NoneType, NoneType]
```

Get [ModuleObjectRecord](./handsdown_module_record.md#moduleobjectrecord) for every object in a module.

#### Arguments

- `module_record` - [ModuleRecord](./handsdown_module_record.md#modulerecord) instance.

#### Returns

A generator that yields [ModuleObjectRecord](./handsdown_module_record.md#moduleobjectrecord) instances.

#### See also

- [ModuleRecord](./handsdown_module_record.md#modulerecord)
- [ModuleObjectRecord](./handsdown_module_record.md#moduleobjectrecord)

### Loader()._get_object_docstring

[🔍 find in source code](../handsdown/loader.py#L206)

```python
def _get_object_docstring(obj: Any) -> str
```

Get trimmed object docstring or an empty string.

#### Arguments

- `obj` - Object to inspect.

#### Returns

A string with object docsting.

### Loader()._setup_django

[🔍 find in source code](../handsdown/loader.py#L152)

```python
def _setup_django() -> None
```

Initialize Django apps in order to safely import Django models.
Patches applied during apps initialization:

- Patch `os.environ` to avoid failing on undefined variables.
- Patch `sys.path` to add current repo to it.
- Patch `logging.config.dictConfig`.

### Loader().get_module_record

[🔍 find in source code](../handsdown/loader.py#L81)

```python
def get_module_record(
    source_path: pathlib.Path,
) -> Union[handsdown.module_record.ModuleRecord, NoneType]
```

Build [ModuleRecord](./handsdown_module_record.md#modulerecord) for given `source_path`.

#### Arguments

- `source_path` - Absolute path to source file.

#### Returns

A new [ModuleRecord](./handsdown_module_record.md#modulerecord) instance or None if there is ntohing to import.

#### Raises

- [LoaderError](#loadererror) - If module or any of it's objects cannot be imported.

#### See also

- [ModuleRecord](./handsdown_module_record.md#modulerecord)

### Loader.get_object_signature

[🔍 find in source code](../handsdown/loader.py#L177)

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

[🔍 find in source code](../handsdown/loader.py#L456)

```python
def get_source_line_number(obj: Any) -> int
```

Get line number in source file where `obj` is declared.

- `obj` - Object to inspect.

#### Returns

A line number as an integer, starting for 1.

### Loader().import_module

[🔍 find in source code](../handsdown/loader.py#L243)

```python
def import_module(file_path: pathlib.Path) -> Any
```

Import module using `import_paths` list. Clean up all patches afterwards.

- Patch `sys.path` to add current repo to it.
- Patch `os.environ` to avoid failing on undefined variables.
- Patch `typing.TYPE_CHECKING` to `True`.
- Patch `logging.Logger`.
- Patch `logging.config.dictConfig`.

#### Arguments

- `file_path` - Abslute path to source file.

#### Returns

Imported module object.

### Loader().setup

[🔍 find in source code](../handsdown/loader.py#L52)

```python
def setup() -> None
```

Setup local frameworks if needed.

Frameworks supported:
- `Django` (if `DJANGO_SETTINGS_MODULE` env variable is defined)

## LoaderError

[🔍 find in source code](../handsdown/loader.py#L18)

```python
class LoaderError(*args, **kwargs)
```

Main error for [Loader](#loader) class.
