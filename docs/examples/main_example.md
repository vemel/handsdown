# Main Example

> Auto-generated documentation for [examples.main_example](https://github.com/vemel/handsdown/blob/master/examples/main_example.py) module.

This is a module docstring. It will appear in documentation.

- [Handsdown](../README.md#-handsdown---python-documentation-generator) / [Modules](../MODULES.md#modules) / [Examples](index.md#examples) / Main Example
    - [Notes](#notes)
    - [MyClass](#myclass)
        - [MyClass().\_\_bool\_\_](#myclass__bool__)
        - [MyClass.do_something](#myclassdo_something)
    - [hello](#hello)

## Notes

You can use Markdown here to make it nicer. Also, in any docstring you
can put a global object import string in backticks, like `other_module.OtherClass`,
and it will be transformed to a link.

#### Attributes

- `MODULE_NAME` - This is a comment-style documented global variable, so it is added to `main_example` module attributes with this comment as a documentation for it: `'My Module'`

## MyClass

[[find in source code]](https://github.com/vemel/handsdown/blob/master/examples/main_example.py#L50)

```python
class MyClass(BaseClass):
```

MyClass documentation here.

#### Notes

This time we use RST docstrings format.

#### Attributes

- `STUFF_COUNT` - This is a comment-style documented class attribute, so it is added to `main_example.MyClass` attributes with this comment as a documentation for it.: `3`

### MyClass().\_\_bool\_\_

[[find in source code]](https://github.com/vemel/handsdown/blob/master/examples/main_example.py#L88)

```python
def __bool__() -> bool:
```

Magic methods are added to docs only if they have docstrings.

#### Returns

True if [STUFF_COUNT](#myclass) is not zero

### MyClass.do_something

[[find in source code]](https://github.com/vemel/handsdown/blob/master/examples/main_example.py#L61)

```python
@classmethod
def do_something(stuff: StuffCallable) -> bool:
```

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

## hello

[[find in source code]](https://github.com/vemel/handsdown/blob/master/examples/main_example.py#L23)

```python
def hello(name: Text) -> Text:
```

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
