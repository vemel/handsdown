# Utils

[🙌 Handsdown - Python documentation generator](../../README.md#-handsdown---python-documentation-generator) /
[Modules](../../MODULES.md#modules) /
[Handsdown](../index.md#handsdown) /
Utils

> Auto-generated documentation for [handsdown.utils](https://github.com/vemel/handsdown/blob/main/handsdown/utils/__init__.py) module.

- [Utils](#utils)
  - [extract_md_title](#extract_md_title)
  - [make_title](#make_title)
  - [render_asset](#render_asset)

## extract_md_title

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/__init__.py#L69)

Extract title from the first line of content.If title is present - return a title and a remnaing content.
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

#### Signature

```python
def extract_md_title(content: str) -> Tuple[str, str]:
    ...
```



## make_title

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/__init__.py#L12)

Convert `pathlib.Path` part or any other string to a human-readable title.Replace underscores with spaces and capitalize result.

#### Examples

```python
make_title(Path("my_module/my_path.py").stem)
"My Path"

make_title("my_title")
"My Title"

make_title("__init__.py")
"Init Py"

make_title(Path("my_module/__main__.py").stem)
"Module"
```

#### Arguments

- `file_stem` - Stem from path.

#### Returns

A human-readable title as a string.

#### Signature

```python
def make_title(file_stem: str) -> str:
    ...
```



## render_asset

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/__init__.py#L53)

Render `assets/<name>` file to `target_path`.

#### Arguments

- `name` - Asset file name.
- `target_path` - Path of output file.
- `format_dict` - Format asset with values from the dict before writing.
- `encoding` - File encoding.

#### Signature

```python
def render_asset(
    name: str, target_path: Path, format_dict: Dict[str, str], encoding: str
) -> None:
    ...
```


