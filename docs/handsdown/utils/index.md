# Utils

> Auto-generated documentation for [handsdown.utils](https://github.com/vemel/handsdown/blob/master/handsdown/utils/__init__.py) module.

Handful utils that do not deserve a separate module.

- [Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / Utils
  - [make_title](#make_title)
  - [render_asset](#render_asset)
  - Modules
    - [Logger](logger.md#logger)
    - [OSEnvironMock](os_environ_mock.md#osenvironmock)
    - [TypeCheckingMock](type_checking_mock.md#typecheckingmock)

## make_title

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/utils/__init__.py#L11)

```python
def make_title(path_part: Text) -> Text:
```

Convert `pathlib.Path` part or any other string to a human-readable title.
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

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/utils/__init__.py#L39)

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
