# PEP 287 - reStructuredText docstrings examples

[🙌 Handsdown - Python documentation generator](../README.md#-handsdown---python-documentation-generator) /
[Modules](../MODULES.md#modules) /
[Examples](index.md#examples) /
PEP 287 - reStructuredText docstrings examples

> Auto-generated documentation for [examples.rst_docstrings](https://github.com/vemel/handsdown/blob/main/examples/rst_docstrings.py) module.

- [PEP 287 - reStructuredText docstrings examples](#pep-287---restructuredtext-docstrings-examples)
  - [RSTExample](#rstexample)
    - [RSTExample.reference](#rstexamplereference)

## RSTExample

[find in source code](https://github.com/vemel/handsdown/blob/main/examples/rst_docstrings.py#L10)

#### Signature

```python
class RSTExample:
    ...
```

### RSTExample.reference

[find in source code](https://github.com/vemel/handsdown/blob/main/examples/rst_docstrings.py#L11)

This is a reference for ``RST-style`` docstrings. Check `source` code
to see how it works.

#### Arguments

- `my_param` - Parameter example
- `typed_param` *int* - Typed parameter example

#### Returns

Type: *str*
Return statement

#### Raises

- `ValueError` -  Raises exampleCode example```python
data = {
    'key': 'value',
}

print(data)
```

#### Signature

```python
@staticmethod
def reference():
    ...
```

### RSTExample.replace_test

[find in source code](https://github.com/vemel/handsdown/blob/main/examples/rst_docstrings.py#L40)

Check if all attribute `attributes`, ``data`` and exception `Exception` in
class ``RSTExample`` and class `RSTExample` look good.

#### Signature

```python
@staticmethod
def replace_test():
    ...
```

### RSTExample.rtype_test

[find in source code](https://github.com/vemel/handsdown/blob/main/examples/rst_docstrings.py#L31)

`:rtype:` test.

#### Returns

Return statement
Type: *bool*

#### Signature

```python
@staticmethod
def rtype_test():
    ...
```


