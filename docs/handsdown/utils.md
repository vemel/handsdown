# Utils

> Auto-generated documentation for [handsdown.utils](https://github.com/vemel/handsdown/blob/master/handsdown/utils.py) module..

Handful utils that do not deserve a separate module.

- [Index](../README.md#modules) / [Handsdown](index.md#handsdown) / Utils
  - [OSEnvironMock](#osenvironmock)
  - [get_title_from_path_part](#get_title_from_path_part)

## OSEnvironMock

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/utils.py#L8)

```python
class OSEnvironMock(*args, **kwargs)
```

Mock for `os.environ` that returns `env` string isntead of undefined variables.

## get_title_from_path_part

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/utils.py#L17)

```python
def get_title_from_path_part(path_part: str) -> str
```

Convert `pathlib.Path` part to a human-readable title.
Replace underscores with spaces and capitalize result.

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

#### Returns

A human-readable title as a string.
