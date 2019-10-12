# Handsdown: Loader

- [Handsdown: Loader](#handsdown-loader)
  - [Loader](#loader)
    - [Loader.get_module_objects](#loaderget_module_objects)
    - [Loader.get_object_docstring](#loaderget_object_docstring)
    - [Loader.get_object_signature](#loaderget_object_signature)
    - [Loader.get_source_line_number](#loaderget_source_line_number)
    - [Loader.import_module](#loaderimport_module)

> Auto-generated documentation for [handsdown.loader](../handsdown/loader.py) module.

## Loader

[🔍 find in source code](../handsdown/loader.py#L12)

```python
class Loader(*args, **kwargs)
```
A utility class that is responsible for working with python source code.

### Loader.get_module_objects

[🔍 find in source code](../handsdown/loader.py#L92)

```python
def get_module_objects(import_string: str) -> Generator[Tuple[str, Any, int], NoneType, NoneType]
```
Yield (`name`, `object`, `level`) for every object in a module. `name` is object name.
`object` - object iteslf. `level` - deepness of the object. Maximum `level` is 1.

#### Arguments

- `import_string` - Module import string.

#### Returns

A generator that yields tuples of (`name`, `object`, `level`).

### Loader.get_object_docstring

[🔍 find in source code](../handsdown/loader.py#L34)

```python
def get_object_docstring(obj: Any) -> str
```
Get trimmed object docstring or an empty string.

#### Arguments

- `obj` - Object to inspect.

#### Returns

A string with object docsting.

### Loader.get_object_signature

[🔍 find in source code](../handsdown/loader.py#L17)

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

[🔍 find in source code](../handsdown/loader.py#L142)

```python
def get_source_line_number(obj: Any) -> int
```
Get line number in source file where `obj` is declared.

- `obj` - Object to inspect.

#### Returns

A line number.

### Loader.import_module

[🔍 find in source code](../handsdown/loader.py#L47)

```python
def import_module(import_string: str) -> Any
```
Path os.environ to avoid failing on undefined variables.

#### Arguments

- `import_string` - Module import string.

#### Returns

Imported module object.
