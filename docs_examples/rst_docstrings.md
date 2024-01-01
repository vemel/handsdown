# PEP 287 - reStructuredText docstrings examples

[Handsdown Index](./README.md#handsdown-index) /
PEP 287 - reStructuredText docstrings examples

> Auto-generated documentation for [rst_docstrings](../examples/rst_docstrings.py) module.

- [PEP 287 - reStructuredText docstrings examples](#pep-287---restructuredtext-docstrings-examples)
  - [RSTExample](#rstexample)
    - [RSTExample.reference](#rstexamplereference)
    - [RSTExample.replace_test](#rstexamplereplace_test)
    - [RSTExample.rtype_test](#rstexamplertype_test)

## RSTExample

[Show source in rst_docstrings.py:10](../examples/rst_docstrings.py#L10)

#### Signature

```python
class RSTExample:
    ...
```

### RSTExample.reference

[Show source in rst_docstrings.py:11](../examples/rst_docstrings.py#L11)

This is a reference for ``RST-style`` docstrings. Check `source` code
to see how it works.

#### Arguments

- `my_param` - Parameter example
- `typed_param` *int* - Typed parameter example

#### Returns

Type: *str*
Return statement

#### Raises

- `ValueError` -  Raises example

Code example

```python
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

[Show source in rst_docstrings.py:40](../examples/rst_docstrings.py#L40)

Check if all attribute `attributes`, ``data`` and exception `Exception` in
class [RSTExample](#rstexample) and class [RSTExample](#rstexample) look good.

#### Signature

```python
@staticmethod
def replace_test():
    ...
```

### RSTExample.rtype_test

[Show source in rst_docstrings.py:31](../examples/rst_docstrings.py#L31)

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