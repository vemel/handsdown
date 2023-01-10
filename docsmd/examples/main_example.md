# Main Example

[Handsdown API Index](../README.md#handsdown-api-index) /
[Examples](./index.md#examples) /
Main Example

> Auto-generated documentation for [examples.main_example](https://github.com/vemel/handsdown/blob/main/examples/main_example.py) module.

#### Attributes

- `MODULE_NAME` - This is a comment-style documented global variable, so it is added to
  `main_example` module attributes with this comment as a documentation for it: `'My Module'`


## MyClass

[Show source in main_example.py:54](https://github.com/vemel/handsdown/blob/main/examples/main_example.py#L54)

#### Attributes

- `STUFF_COUNT` - This is a comment-style documented class attribute, so it is added to
  `main_example.MyClass` attributes with this comment as a documentation for it.: `3`


MyClass documentation here.

#### Notes

This time we use RST docstrings format.

#### Signature

```python
class MyClass(BaseClass):
    ...
```

### MyClass().__bool__

[Show source in main_example.py:92](https://github.com/vemel/handsdown/blob/main/examples/main_example.py#L92)

Magic methods are added to docs only if they have docstrings.

#### Returns

True if [STUFF_COUNT](#myclass) is not zero

#### Signature

```python
def __bool__(self) -> bool:
    ...
```

### MyClass.do_something

[Show source in main_example.py:65](https://github.com/vemel/handsdown/blob/main/examples/main_example.py#L65)

This is a public method that uses comment-style type annotations. If decorators
or types from annotations are from your project, links to them will be added
to `See also` section. Since this function depends on [STUFF_COUNT](#myclass), we can add
it to a docstring in backticks and it will be transformed to a link.


```python
# usage example
def my_stuff(amount):
    return amount > 5

MyClass.do_something(my_stuff)  # False
```

#### Notes

Added in version 1.3

Deprecated in version 1.8

Changed in version 1.4
    All these directives are added to `Notes` section and formatted in Sphinx-style.

#### Arguments

- `stuff` - Function do execute.

#### Returns

`stuff` result.

#### Signature

```python
@classmethod
def do_something(cls, stuff: StuffCallable) -> bool:
    ...
```



## hello

[Show source in main_example.py:27](https://github.com/vemel/handsdown/blob/main/examples/main_example.py#L27)

This is module function and it is added to documentation even if it does
not have a docstring. Function signature will be also generated respecting
regular and comment-style type annotations. Let's use PEP 257 format here.

#### Examples

```python
# Google-style code block here, but we could use Markdown code block as well
>>> hello('John')
'Hello, John!'

>>> hello('')
'Hello!'
```

#### Arguments

- `name` - Name of the person to greet.

#### Returns

A greeting. No need to put types here if you use type annotations.

#### Signature

```python
def hello(name: str) -> str:
    ...
```
