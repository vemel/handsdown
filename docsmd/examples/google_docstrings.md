# Google docstrings examples

[Handsdown API Index](../README.md#handsdown-api-index) / [Examples](./index.md#examples) / Google docstrings examples

> Auto-generated documentation for [examples.google_docstrings](https://github.com/vemel/handsdown/blob/main/examples/google_docstrings.py) module.

## ClassExample

[Show source in google_docstrings.py:13](https://github.com/vemel/handsdown/blob/main/examples/google_docstrings.py#L13)

Google-style class example

#### Attributes

- `attr1` *str* - Description of `attr1`.
- `attr2` *:obj:`int`, optional* - Description of `attr2`.

#### Signature

```python
class ClassExample:
    ...
```

### ClassExample().method_example

[Show source in google_docstrings.py:22](https://github.com/vemel/handsdown/blob/main/examples/google_docstrings.py#L22)

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

#### Signature

```python
def method_example(self, text: str = "hello") -> int:
    ...
```



## function_example

[Show source in google_docstrings.py:56](https://github.com/vemel/handsdown/blob/main/examples/google_docstrings.py#L56)

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

#### Signature

```python
def function_example(arg1, arg2, arg3=None):
    ...
```



## function_with_pep484_type_annotations

[Show source in google_docstrings.py:87](https://github.com/vemel/handsdown/blob/main/examples/google_docstrings.py#L87)

Example function with PEP 484 type annotations.

#### Arguments

- `param1` - The first parameter.
- `param2` - The second parameter.

#### Returns

The return value. True for success, False otherwise.

#### Signature

```python
def function_with_pep484_type_annotations(param1: int, param2: str) -> bool:
    ...
```
