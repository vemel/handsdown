# Google docstrings examples

> Auto-generated documentation for [examples.google_docstrings](../../examples/google_docstrings.py) module.

- [Index](../README.md#modules) / [Examples](index.md#examples) / Google docstrings examples
  - [Links](#links)
  - [ClassExample](#classexample)
    - [ClassExample().method_example](#classexamplemethod_example)
  - [function_example](#function_example)
  - [function_with_pep484_type_annotations](#function_with_pep484_type_annotations)

## Links

[Google Python Style Guide](http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)

## ClassExample

[🔍 find in source code](../../examples/google_docstrings.py#L11)

```python
class ClassExample(*args, **kwargs)
```

Google-style class example

#### Attributes

- `attr1` *str* - Description of `attr1`.
- `attr2` *:obj:`int`, optional* - Description of `attr2`.

### ClassExample().method_example

[🔍 find in source code](../../examples/google_docstrings.py#L20)

```python
def method_example(text: str = 'hello') -> int
```

Summary line.

Extended description of method.

#### Examples

Examples should be written in doctest format, and should illustrate how
to use the function

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

- `text` *str, optional* - Description of arg1
- `*args` *str* - Description of args
- `**kwargs` *str* - Description of kwargs

#### Returns

- `int` - Description of return value

## function_example

[🔍 find in source code](../../examples/google_docstrings.py#L54)

```python
def function_example(arg1, arg2, arg3=None)
```

Summary line.

Extended description of function.
You can use this function like

```python
result = function_example(
    {
        'key': 'value',
    },
    None,
)

print result
```

#### Arguments

- `arg1` *int* - Description of arg1
- `arg2` *str* - Description of arg2
- `arg3` *str, optional* - Description of arg3

#### Returns

- `bool` - Description of return value

#### Raises

- `AttributeError` - The ``Raises`` section is a list of all exceptions
    that are relevant to the interface.
- `ValueError` - If `param2` is equal to `param1`.

## function_with_pep484_type_annotations

[🔍 find in source code](../../examples/google_docstrings.py#L85)

```python
def function_with_pep484_type_annotations(param1: int, param2: str) -> bool
```

Example function with PEP 484 type annotations.

#### Arguments

- `param1` - The first parameter.
- `param2` - The second parameter.

#### Returns

The return value. True for success, False otherwise.
