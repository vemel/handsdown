# Sphinx docstrings examples

> Auto-generated documentation for [examples.sphinx_docstrings](https://github.com/vemel/handsdown/blob/main/examples/sphinx_docstrings.py) module.

- [Handsdown](../README.md#-handsdown---python-documentation-generator) / [Modules](../MODULES.md#modules) / [Examples](index.md#examples) / Sphinx docstrings examples
    - [Links](#links)
    - [RSTExample](#rstexample)
        - [RSTExample.directives_test](#rstexampledirectives_test)
        - [RSTExample.reference](#rstexamplereference)
        - [RSTExample.version_directives_test](#rstexampleversion_directives_test)

## Links

[reStructuredText Primer](http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)

## RSTExample

[[find in source code]](https://github.com/vemel/handsdown/blob/main/examples/sphinx_docstrings.py#L11)

```python
class RSTExample():
```

### RSTExample.directives_test

[[find in source code]](https://github.com/vemel/handsdown/blob/main/examples/sphinx_docstrings.py#L34)

```python
@staticmethod
def directives_test():
```

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

### RSTExample.reference

[[find in source code]](https://github.com/vemel/handsdown/blob/main/examples/sphinx_docstrings.py#L12)

```python
@staticmethod
def reference():
```

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

### RSTExample.version_directives_test

[[find in source code]](https://github.com/vemel/handsdown/blob/main/examples/sphinx_docstrings.py#L58)

```python
@staticmethod
def version_directives_test():
```

Test for Version-related directives

#### Notes

Added in version 2.5
    The *spam* parameter.

Changed in version 2.7
    Mandatory *spam* parameter.

Deprecated in version 3.1
    Use :func:`spam` instead.
