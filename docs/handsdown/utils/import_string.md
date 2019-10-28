# ImportString

> Auto-generated documentation for [handsdown.utils.import_string](https://github.com/vemel/handsdown/blob/master/handsdown/utils/import_string.py) module.

Wrapper for python import strings.

- [Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / [Utils](index.md#utils) / ImportString
    - [ImportString](#importstring)
        - [ImportString().\_\_add\_\_](#importstring__add__)
        - [ImportString().\_\_bool\_\_](#importstring__bool__)
        - [ImportString().\_\_eq\_\_](#importstring__eq__)
        - [ImportString().\_\_str\_\_](#importstring__str__)
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

### ImportString().\_\_add\_\_

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/utils/import_string.py#L44)

```python
def __add__(other: Text) -> ImportString:
```

Add new import part.

#### Examples

```python
ImportString("my_module") + "MyClass"
ImportString("my_module.MyClass")

ImportString("") + "MyClass"
ImportString("MyClass")
```

#### Arguments

- `other` - Import string part.

#### Returns

A new [ImportString](#importstring) instance.

### ImportString().\_\_bool\_\_

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/utils/import_string.py#L68)

```python
def __bool__() -> bool:
```

Check if not empty.

#### Examples

```python
bool(ImportString("my_module"))
True

bool(ImportString(""))
False
```

#### Returns

True if not empty.

### ImportString().\_\_eq\_\_

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/utils/import_string.py#L86)

```python
def __eq__(other: object) -> bool:
```

Compare to another [ImportString](#importstring) or a string.

#### Examples

```python
ImportString("my_module.MyClass") == ImportString("my_module.MyClass")
True

ImportString("my_module.MyClass") == ImportString("my_module.OtherClass")
False

ImportString("my_module.MyClass") == "my_module.MyClass"
True

ImportString("my_module.MyClass") == "my_module"
False

ImportString("my_module.MyClass") == b"my_module.MyClass"
False
```

#### Arguments

other - ImportString instance or a string.

#### Returns

True if import strings are equal.

### ImportString().\_\_str\_\_

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/utils/import_string.py#L25)

```python
def __str__() -> Text:
```

Get string value.

#### Examples

```python
str(ImportString("my_module"))
"my_module"
```

#### Returns

Original import string.

### ImportString().is_top_level

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/utils/import_string.py#L141)

```python
def is_top_level() -> bool:
```

Check if import string has no parents.

#### Returns

True if it has no parents.

### ImportString().parent

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/utils/import_string.py#L151)

```python
@property
def parent() -> ImportString:
```

Parent import string.

#### Returns

A new [ImportString](#importstring) instance.

### ImportString().parts

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/utils/import_string.py#L122)

```python
@property
def parts() -> List[Text]:
```

Parts of import string splitted by dots.

#### Examples

```python
ImportString("my_module.MyClass")
["my_module", "MyClass"]

ImportString("")
[]
```

#### Returns

A list of import string parts.

### ImportString().startswith

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/utils/import_string.py#L166)

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
