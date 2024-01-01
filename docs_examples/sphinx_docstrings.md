# Sphinx docstrings examples

[Handsdown Index](./README.md#handsdown-index) /
Sphinx docstrings examples

> Auto-generated documentation for [sphinx_docstrings](../examples/sphinx_docstrings.py) module.

- [Sphinx docstrings examples](#sphinx-docstrings-examples)
  - [RSTExample](#rstexample)
    - [RSTExample.directives_test](#rstexampledirectives_test)
    - [RSTExample.reference](#rstexamplereference)
    - [RSTExample.version_directives_test](#rstexampleversion_directives_test)

## RSTExample

[Show source in sphinx_docstrings.py:10](../examples/sphinx_docstrings.py#L10)

#### Signature

```python
class RSTExample:
    ...
```

### RSTExample.directives_test

[Show source in sphinx_docstrings.py:33](../examples/sphinx_docstrings.py#L33)

Test for some random Sphinx directives


```ruby
def sum_eq_n?(arr, n)
    return true if arr.empty? && n == 0
    arr.product(arr).reject { |a,b| a == b }.any? { |a,b| a + b == n }
end
```

#### Notes

short note


```python
(a + b)^2 = a^2 + 2ab + b^2

(a - b)^2 = a^2 - 2ab + b^2
```

#### See also

modules :py:mod:`zipfile`, :py:mod:`tarfile`

#### Signature

```python
@staticmethod
def directives_test():
    ...
```

### RSTExample.reference

[Show source in sphinx_docstrings.py:11](../examples/sphinx_docstrings.py#L11)

This is a reference for ``Sphinx-style RST-style`` docstrings. Check `source` code
to see how it works.

Code example

```python
data = {
    'key': 'value',
}

print(data)
```

#### Arguments

- `my_param` - Parameter example
- `typed_param` *int* - Typed parameter example

#### Returns

Type: *str*
Return statement

#### Raises

- `ValueError` -  Raises example

#### Signature

```python
@staticmethod
def reference():
    ...
```

### RSTExample.version_directives_test

[Show source in sphinx_docstrings.py:57](../examples/sphinx_docstrings.py#L57)

Test for Version-related directives

#### Notes

Added in version 2.5
    The *spam* parameter.


Changed in version 2.7
    Mandatory *spam* parameter.


Deprecated in version 3.1
    Use :func:`spam` instead.

#### Signature

```python
@staticmethod
def version_directives_test():
    ...
```