# Utils

> Auto-generated documentation for [utils](../utils.py) module..

Handful utils that do not deserve a separate module.

- [Index](README.md#modules) / Utils
  - [OSEnvironMock](#osenvironmock)
  - [get_title_from_path_part](#get_title_from_path_part)

## OSEnvironMock

[🔍 find in source code](../utils.py#L7)

```python
class OSEnvironMock()
```

Mock for `os.environ` that returns `env` string isntead of undefined variables.

## get_title_from_path_part

[🔍 find in source code](../utils.py#L23)

```python
def get_title_from_path_part(path_part: Text) -> Text
```

Convert `pathlib.Path` part to a human-readable title.
Replace underscores with spaces and capitalize result.

#### Returns

A human-readable title as a string.

#### Examples

```python
get_title_from_path_part("my_path.py")
"My Path Py"

get_title_from_path_part("my_title")
"My Title"

get_title_from_path_part("__init__.py")
"Init Py"
```

#### Arguments

- `path_part` - Part of filename path.
