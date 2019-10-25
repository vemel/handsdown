# ImportString

> Auto-generated documentation for [handsdown.utils.import_string](https://github.com/vemel/handsdown/blob/master/handsdown/utils/import_string.py) module.

Wrapper for python import strings.

- [Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / [Utils](index.md#utils) / ImportString
    - [ImportString](#importstring)
        - [ImportString().is_top_level](#importstringis_top_level)
        - [ImportString().parent](#importstringparent)
        - [ImportString().parts](#importstringparts)
        - [ImportString().startswith](#importstringstartswith)
    - [ImportStringError](#importstringerror)

## ImportString

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/utils/import_string.py#L13)

```python
class ImportString():
    def __init__(value: Text) -> None:
```

Wrapper for python import strings.

#### Arguments

- `value` - Import string.

### ImportString().is_top_level

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/utils/import_string.py#L55)

```python
def is_top_level() -> bool:
```

Check if import string has no parents.

#### Returns

True if it has no parents.

### ImportString().parent

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/utils/import_string.py#L65)

```python
@property
def parent() -> ImportString:
```

Parent import string.

#### Returns

A new `ImportString` instance.

### ImportString().parts

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/utils/import_string.py#L44)

```python
@property
def parts() -> List[Text]:
```

Parts of import string splitted by dots.

#### Returns

A list of import string parts.

### ImportString().startswith

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/utils/import_string.py#L80)

```python
def startswith(import_string: ImportString) -> bool:
```

Check if it starts with `import_string`.

#### Returns

True if it is a child.

## ImportStringError

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/utils/import_string.py#L7)

```python
class ImportStringError(Exception):
```

Main error for [ImportString](#importstring).
