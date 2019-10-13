# Handsdown: Loader

- [Handsdown: Loader](#handsdown-loader)
  - [LoaderError](#loadererror)
  - [Loader](#loader)
    - [Loader().get_module_objects](#loaderget_module_objects)
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

### Loader().get_module_objects

[🔍 find in source code](../handsdown/loader.py#L213)

```python
def get_module_objects(
    module: Any,
    file_path: str,
) -> Generator[Tuple[str, Any, int], NoneType, NoneType]
```
Yield (`name`, `object`, `level`) for every object in a module. `name` is object name.
`object` - object iteslf. `level` - deepness of the object. Maximum `level` is 1.

#### Arguments

- `module` - Module to inspect.
- `file_path` - Absolute path to source file.

#### Returns

A generator that yields tuples of (`name`, `object`, `level`).

### Loader.get_object_docstring

[🔍 find in source code](../handsdown/loader.py#L126)

```python
def get_object_docstring(obj: Any) -> str
```
Get trimmed object docstring or an empty string.

#### Arguments

- `obj` - Object to inspect.

#### Returns

A string with object docsting.

### Loader.get_object_signature

[🔍 find in source code](../handsdown/loader.py#L109)

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

[🔍 find in source code](../handsdown/loader.py#L267)

```python
def get_source_line_number(obj: Any) -> int
```
Get line number in source file where `obj` is declared.

- `obj` - Object to inspect.

#### Returns

A line number.

### Loader().import_module

[🔍 find in source code](../handsdown/loader.py#L150)

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
