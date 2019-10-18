# PEP 287 - reStructuredText docstrings examples

> Auto-generated documentation for [examples.rst_docstrings](https://github.com/vemel/handsdown/blob/master/examples/rst_docstrings.py) module.

- [Index](../README.md#modules) / [Examples](index.md#examples) / PEP 287 - reStructuredText docstrings examples
  - [Links](#links)
  - [RSTExample](#rstexample)
    - [RSTExample.reference](#rstexamplereference)
    - [RSTExample.replace_test](#rstexamplereplace_test)
    - [RSTExample.rtype_test](#rstexamplertype_test)

## Links

[PEP 287 - reStructuredText Docstring Format](https://www.python.org/dev/peps/pep-0287/)

## RSTExample

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/examples/rst_docstrings.py#L10)

```python
class RSTExample(args, kwargs)
```

### RSTExample.reference

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/examples/rst_docstrings.py#L11)

```python
def reference()
```

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

### RSTExample.replace_test

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/examples/rst_docstrings.py#L40)

```python
def replace_test()
```

Check if all attribute `attributes`, ``data`` and exception `Exception` in
class [RSTExample](#rstexample) and class [RSTExample](#rstexample) look good.

### RSTExample.rtype_test

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/examples/rst_docstrings.py#L31)

```python
def rtype_test()
```

`:rtype:` test.

#### Returns

Return statement
Type: *bool*
