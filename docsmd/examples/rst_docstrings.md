# PEP 287 - reStructuredText docstrings examples


## Links

[PEP 287 - reStructuredText Docstring Format](https://www.python.org/dev/peps/pep-0287/)

[Handsdown API Index](../README.md#handsdown-api-index) / [Examples](./index.md#examples) / PEP 287 - reStructuredText docstrings examples

> Auto-generated documentation for [examples.rst_docstrings](https://github.com/vemel/handsdown/blob/main/examples/rst_docstrings.py) module.

## RSTExample

[Show source in rst_docstrings.py:10](https://github.com/vemel/handsdown/blob/main/examples/rst_docstrings.py#L10)

#### Signature

```python
class RSTExample:
    ...
```

### RSTExample.reference

[Show source in rst_docstrings.py:11](https://github.com/vemel/handsdown/blob/main/examples/rst_docstrings.py#L11)

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

[Show source in rst_docstrings.py:40](https://github.com/vemel/handsdown/blob/main/examples/rst_docstrings.py#L40)

Check if all attribute `attributes`, ``data`` and exception `Exception` in
class [RSTExample](#rstexample) and class [RSTExample](#rstexample) look good.

#### Signature

```python
@staticmethod
def replace_test():
    ...
```

### RSTExample.rtype_test

[Show source in rst_docstrings.py:31](https://github.com/vemel/handsdown/blob/main/examples/rst_docstrings.py#L31)

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
