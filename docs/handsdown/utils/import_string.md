# ImportString

[🙌 Handsdown - Python documentation generator](../../README.md#-handsdown---python-documentation-generator) /
[Modules](../../MODULES.md#modules) /
[Handsdown](../index.md#handsdown) /
[Utils](index.md#utils) /
ImportString

> Auto-generated documentation for [handsdown.utils.import_string](https://github.com/vemel/handsdown/blob/main/handsdown/utils/import_string.py) module.

- [ImportString](#importstring)
  - [ImportString](#importstring-1)
    - [ImportString().__add__](#importstring()__add__)
    - [ImportString().__bool__](#importstring()__bool__)
    - [ImportString().__eq__](#importstring()__eq__)
    - [ImportString().__str__](#importstring()__str__)
    - [ImportString().get_parents](#importstring()get_parents)
    - [ImportString().is_top_level](#importstring()is_top_level)
    - [ImportString().parent](#importstring()parent)
    - [ImportString().parts](#importstring()parts)
    - [ImportString().startswith](#importstring()startswith)
  - [ImportStringError](#importstringerror)

## ImportString

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/import_string.py#L15)

Wrapper for python import strings.

#### Arguments

- `value` - Import string.

#### Signature

```python
class ImportString:
    def __init__(self, value: str) -> None:
        ...
```

### ImportString().__add__

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/import_string.py#L43)

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

A new `ImportString` instance.

#### Signature

```python
def __add__(self, other: str) -> "ImportString":
    ...
```

### ImportString().__bool__

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/import_string.py#L66)

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

#### Signature

```python
def __bool__(self) -> bool:
    ...
```

### ImportString().__eq__

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/import_string.py#L83)

Compare to another `ImportString` or a string.

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

#### Signature

```python
def __eq__(self, other: Any) -> bool:
    ...
```

### ImportString().__str__

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/import_string.py#L26)

Get string value.

#### Examples

```python
str(ImportString("my_module"))
"my_module"
```

#### Returns

Original import string.

#### Signature

```python
def __str__(self) -> str:
    ...
```

### ImportString().get_parents

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/import_string.py#L168)

Get all parents.

#### Returns

A list of `ImportString` instances.

#### Signature

```python
def get_parents(self: _R) -> List[_R]:
    ...
```

### ImportString().is_top_level

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/import_string.py#L136)

Check if import string has no parents.

#### Returns

True if it has no parents.

#### Signature

```python
def is_top_level(self) -> bool:
    ...
```

### ImportString().parent

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/import_string.py#L145)

Parent import string.

#### Returns

A new `ImportString` instance.

#### Signature

```python
@property
def parent(self: _R) -> _R:
    ...
```

### ImportString().parts

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/import_string.py#L118)

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

#### Signature

```python
@property
def parts(self) -> List[str]:
    ...
```

### ImportString().startswith

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/import_string.py#L159)

Check if it starts with `import_string`.

#### Returns

True if it is a child.

#### Signature

```python
def startswith(self, import_string: "ImportString") -> bool:
    ...
```



## ImportStringError

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/import_string.py#L9)

Main error for `ImportString`.

#### Signature

```python
class ImportStringError(Exception):
    ...
```


