# Handsdown: Loader

- [Handsdown: Loader](#handsdown-loader)
  - [LoaderError](#loadererror)
  - [Loader](#loader)
    - [Loader().get_module_record](#loaderget_module_record)
    - [Loader.get_object_signature](#loaderget_object_signature)
    - [Loader.get_source_line_number](#loaderget_source_line_number)
    - [Loader().import_module](#loaderimport_module)

> Auto-generated documentation for [handsdown.loader](../handsdown/loader.py) module.

## LoaderError

[🔍 find in source code](../handsdown/loader.py#L18)

```python
class LoaderError(*args, **kwargs)
```

Main error for [Loader](#loader) class.

## Loader

[🔍 find in source code](../handsdown/loader.py#L24)

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

[🔍 find in source code](../handsdown/loader.py#L73)

```python
def get_module_record(
    source_path: pathlib.Path,
) -> Union[handsdown.module_record.ModuleRecord, NoneType]
```

Loader for python source code.

#### Examples

```python
loader = Loader(Path('path/to/my_module/'))
my_module_utils = loader.import_module('my_module.utils')
```

#### Arguments

- `import_paths` - List of import paths for `import_module` lookup.

#### See also

- [ModuleRecord](./handsdown_module_record.md#modulerecord)

### Loader.get_object_signature

[🔍 find in source code](../handsdown/loader.py#L132)

```python
def get_object_signature(obj: Any) -> Union[str, NoneType]
```

Loader for python source code.

#### Examples

```python
loader = Loader(Path('path/to/my_module/'))
my_module_utils = loader.import_module('my_module.utils')
```

#### Arguments

- `import_paths` - List of import paths for `import_module` lookup.

### Loader.get_source_line_number

[🔍 find in source code](../handsdown/loader.py#L321)

```python
def get_source_line_number(obj: Any) -> int
```

Loader for python source code.

#### Examples

```python
loader = Loader(Path('path/to/my_module/'))
my_module_utils = loader.import_module('my_module.utils')
```

#### Arguments

- `import_paths` - List of import paths for `import_module` lookup.

### Loader().import_module

[🔍 find in source code](../handsdown/loader.py#L190)

```python
def import_module(file_path: pathlib.Path) -> Any
```

Loader for python source code.

#### Examples

```python
loader = Loader(Path('path/to/my_module/'))
my_module_utils = loader.import_module('my_module.utils')
```

#### Arguments

- `import_paths` - List of import paths for `import_module` lookup.
