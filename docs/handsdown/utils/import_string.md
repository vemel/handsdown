# ImportString

[Handsdown API Index](../../README.md#handsdown-api-index) /
[Handsdown](../index.md#handsdown) /
[Utils](./index.md#utils) /
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
    - [ImportString().length](#importstring()length)
    - [ImportString().name](#importstring()name)
    - [ImportString().parent](#importstring()parent)
    - [ImportString().parts](#importstring()parts)
    - [ImportString().startswith](#importstring()startswith)

## ImportString

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/import_string.py#L11)

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

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/import_string.py#L39)

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

#### Signature

```python
def __add__(self, other: str) -> "ImportString":
    ...
```

### ImportString().__bool__

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/import_string.py#L62)

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

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/import_string.py#L79)

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

#### Signature

```python
def __eq__(self, other: Any) -> bool:
    ...
```

### ImportString().__str__

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/import_string.py#L22)

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

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/import_string.py#L164)

Get all parents.

#### Returns

A list of [ImportString](#importstring) instances.

#### Signature

```python
def get_parents(self: _R) -> List[_R]:
    ...
```

### ImportString().is_top_level

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/import_string.py#L132)

Check if import string has no parents.

#### Returns

True if it has no parents.

#### Signature

```python
def is_top_level(self) -> bool:
    ...
```

### ImportString().length

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/import_string.py#L183)

Length of import string parts.

#### Returns

Length of import string.

#### Signature

```python
@property
def length(self) -> int:
    ...
```

### ImportString().name

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/import_string.py#L193)

Last part of the import string.

#### Signature

```python
@property
def name(self) -> str:
    ...
```

### ImportString().parent

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/import_string.py#L141)

Parent import string.

#### Returns

A new [ImportString](#importstring) instance.

#### Signature

```python
@property
def parent(self: _R) -> _R:
    ...
```

### ImportString().parts

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/import_string.py#L114)

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

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/import_string.py#L155)

Check if it starts with `import_string`.

#### Returns

True if it is a child.

#### Signature

```python
def startswith(self: _R, import_string: _R) -> bool:
    ...
```


