# Handsdown: Loader

- [Handsdown: Loader](#handsdown-loader)
  - [LoaderError](#loadererror)
  - [Loader](#loader)
    - [Loader.get_object_docstring](#loaderget_object_docstring)
    - [Loader.get_object_signature](#loaderget_object_signature)
    - [Loader.get_source_line_number](#loaderget_source_line_number)
    - [Loader().import_module](#loaderimport_module)

> Auto-generated documentation for [/.home.vlad.work.vemel.handsdown.handsdown.loader](..//home/vlad/work/vemel/handsdown/handsdown/loader.py) module.

## LoaderError

[🔍 find in source code](../handsdown/loader.py#L17)

```python
class LoaderError(*args, **kwargs)
```
## Loader

[🔍 find in source code](../handsdown/loader.py#L21)

```python
class Loader(root_path: pathlib.Path) -> None
```
Loader for python source code.

#### Examples


```python
loader = Loader(Path('path/to/my_module/'))
my_module_utils = loader.import_module('my_module.utils')
```

#### Arguments

- `import_paths` - List of import paths for `import_module` lookup.

### Loader.get_object_docstring

[🔍 find in source code](../handsdown/loader.py#L124)

```python
def get_object_docstring(obj: Any) -> str
```
Get trimmed object docstring or an empty string.

#### Arguments

- `obj` - Object to inspect.

#### Returns

A string with object docsting.

### Loader.get_object_signature

[🔍 find in source code](../handsdown/loader.py#L107)

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

[🔍 find in source code](../handsdown/loader.py#L280)

```python
def get_source_line_number(obj: Any) -> int
```
Get line number in source file where `obj` is declared.

- `obj` - Object to inspect.

#### Returns

A line number.

### Loader().import_module

[🔍 find in source code](../handsdown/loader.py#L148)

```python
def import_module(file_path: pathlib.Path) -> Any
```
Import module using `import_paths` list. Clean up path afterwards.
Patch `os.environ` to avoid failing on undefined variables.
Set `typing.TYPE_CHECKING` to `True` while importing.

#### Arguments

- `file_path` - Abslute path to source file.

#### Returns

Imported module object.
