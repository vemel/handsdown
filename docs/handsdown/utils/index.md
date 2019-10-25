# Utils

> Auto-generated documentation for [handsdown.utils](https://github.com/vemel/handsdown/blob/master/handsdown/utils/__init__.py) module.

Handful utils that do not deserve a separate module.

- [Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / Utils
    - [extract_md_title](#extract_md_title)
    - [make_title](#make_title)
    - [render_asset](#render_asset)
    - [split_import_string](#split_import_string)
    - Modules
        - [Logger](logger.md#logger)

## extract_md_title

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/utils/__init__.py#L54)

```python
def extract_md_title(content: Text) -> Tuple[Text, Text]:
```

Extract title from the first line of content.
If title is present -  return a title and a remnaing content.
if not - return an empty title and untouched content.

#### Examples

```python
extract_md_title('# Title\ncontent')
('Title', 'content')

extract_md_title('no title\ncontent')
('', 'no title\ncontent')
```

#### Returns

A tuple fo title and remaining content.

## make_title

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/utils/__init__.py#L11)

```python
def make_title(path_part: Text) -> Text:
```

Convert `pathlib.Path` part or any other string to a human-readable title.
Replace underscores with spaces and capitalize result.

#### Examples

```python
make_title("my_path.py")
"My Path Py"

make_title("my_title")
"My Title"

make_title("__init__.py")
"Init Py"
```

#### Arguments

- `path_part` - Part of filename path.

#### Returns

A human-readable title as a string.

## render_asset

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/utils/__init__.py#L39)

```python
def render_asset(
    name: Dict[Text, Text],
    target_path: Path,
    format_dict: Text,
) -> None:
```

Render `assets/<name>` file to `target_path`.

#### Arguments

- `name` - Asset file name.
- `target_path` - Path of output file.
- `format_dict` - Format asset with values from the dict before writing.

## split_import_string

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/utils/__init__.py#L83)

```python
def split_import_string(import_string: Text) -> List[Text]:
```

Split import string by dots.

#### Examples

```python
split_import_string('my_module.new_class.NewClass')
['my_module', 'new_class', 'NewClass']
```

#### Arguments

- `import_string` - Python import string.

#### Returns

A list of import string parts.
