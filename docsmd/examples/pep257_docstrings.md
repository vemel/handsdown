# PEP 257 - PEP 257 and Google docstrings examples

[Handsdown API Index](../README.md#handsdown-api-index) /
[Examples](./index.md#examples) /
PEP 257 - PEP 257 and Google docstrings examples

> Auto-generated documentation for [examples.pep257_docstrings](https://github.com/vemel/handsdown/blob/main/examples/pep257_docstrings.py) module.

## ClassExample

[Show source in pep257_docstrings.py:10](https://github.com/vemel/handsdown/blob/main/examples/pep257_docstrings.py#L10)

PEP257-style class example

#### Attributes

- `attr1` - Description of `attr1`.
- `attr2` - Description of `attr2`.

```python
Example of a code block
```

You can use `~~~` to start a block as well

~~~
MD block example inside a tilde block

```python
This is not a codeblock, test inside tildes rendered as it is
```
~~~

#### Signature

```python
class ClassExample:
    ...
```

### ClassExample().method_example

[Show source in pep257_docstrings.py:33](https://github.com/vemel/handsdown/blob/main/examples/pep257_docstrings.py#L33)

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

#### Signature

```python
def method_example(self, text: str = "hello") -> int:
    ...
```



## function_example

[Show source in pep257_docstrings.py:66](https://github.com/vemel/handsdown/blob/main/examples/pep257_docstrings.py#L66)

Form a complex number.

#### Arguments

- `real` - the real part (default 0.0)
- `imag` - the imaginary part (default 0.0)

#### Signature

```python
def function_example(real=0.0, imag=0.0):
    ...
```



