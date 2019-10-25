# PEP 257 - PEP 257 and Google docstrings examples

> Auto-generated documentation for [examples.pep257_docstrings](https://github.com/vemel/handsdown/blob/master/examples/pep257_docstrings.py) module.

- [Handsdown](../README.md#-handsdown---python-documentation-generator) / [Modules](../MODULES.md#modules) / [Examples](index.md#examples) / PEP 257 - PEP 257 and Google docstrings examples
    - [Links](#links)
    - [ClassExample](#classexample)
        - [ClassExample().method_example](#classexamplemethod_example)
    - [function_example](#function_example)

## Links

[PEP 257 - Docstring Conventions](https://www.python.org/dev/peps/pep-0287/)

## ClassExample

[[find in source code]](https://github.com/vemel/handsdown/blob/master/examples/pep257_docstrings.py#L12)

```python
class ClassExample():
```

PEP257-style class example

#### Attributes

- `attr1` - Description of `attr1`.
- `attr2` - Description of `attr2`.

### ClassExample().method_example

[[find in source code]](https://github.com/vemel/handsdown/blob/master/examples/pep257_docstrings.py#L21)

```python
def method_example(text: Text = 'hello') -> int:
```

Summary line.

Extended description of method.

#### Examples

Examples should be written in doctest format, and should illustrate how
to use the function.

```python
>>> print([i for i in
... example_generator(2)])
[
    'one',
    'two',
]
```

```python
>>> setup_env()
>>> func_call(
...     first_name='test',
...     last_name='test',
... )
```

#### Arguments

- `text` - Description of arg1
- `*args` - Description of args
- `**kwargs` - Description of kwargs

#### Returns

Description of return value

## function_example

[[find in source code]](https://github.com/vemel/handsdown/blob/master/examples/pep257_docstrings.py#L54)

```python
def function_example(real=0.0, imag=0.0):
```

Form a complex number.

#### Arguments

- `real` - the real part (default 0.0)
- `imag` - the imaginary part (default 0.0)
