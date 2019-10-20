# Utils

> Auto-generated documentation for [handsdown.utils](https://github.com/vemel/handsdown/blob/master/handsdown/utils.py) module.

Handful utils that do not deserve a separate module.

- [Handsdown](../README.md#-handsdown---python-documentation-generator) / [Modules](../MODULES.md#modules) / [Handsdown](index.md#handsdown) / Utils
  - [OSEnvironMock](#osenvironmock)
  - [TypeCheckingMock](#typecheckingmock)
  - [get_title_from_path_part](#get_title_from_path_part)
  - [render_asset](#render_asset)

## OSEnvironMock

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/utils.py#L14)

```python
class OSEnvironMock():
```

Mock for `os.environ` that returns `env` string instead of undefined variables.

## TypeCheckingMock

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/utils.py#L30)

```python
class TypeCheckingMock(target_file_path: Path) -> None:
```

Helper to turn on or off `TYPE_CHECKING` to avoid sircular imports.

Returns `True` for usage from the `target_file_path`.

#### Examples

```python
import_string = fet_import_string_from_path(file_path)
with patch("typing.TYPE_CHECKING", TypeCheckingMock(file_path)):
    module = importlib.import_module(import_string)
```

#### Arguments

- `target_file_path` - Source path where `typing.TYPE_CHECKING` should be `True`

## get_title_from_path_part

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/utils.py#L68)

```python
def get_title_from_path_part(path_part: Text) -> Text:
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

## render_asset

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/utils.py#L96)

```python
def render_asset(
    name: Text,
    target_path: Path,
    format_dict: Dict[Text, Text],
) -> None:
```

Render `assets/<name>` file to `target_path`.

#### Arguments

- `name` - Asset file name.
- `target_path` - Path of output file.
- `format_dict` - Format asset with values from the dict before writing.
