# Comment Typed

> Auto-generated documentation for [examples.comment_typed](https://github.com/vemel/handsdown/blob/master/examples/comment_typed.py) module.

- [Handsdown](../README.md#-handsdown---python-documentation-generator) / [Modules](../MODULES.md#modules) / [Examples](index.md#examples) / Comment Typed
  - [MyValue](#myvalue)
  - [Typed](#typed)
    - [Typed.classmethod](#typedclassmethod)
  - [func](#func)
  - [func_any](#func_any)

## MyValue

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/examples/comment_typed.py#L4)

```python
class MyValue():
```

## Typed

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/examples/comment_typed.py#L8)

```python
class Typed():
    def __init__(
        my_bool=one & ~two == 'three' and not -4,
        my_lambda=lambda x, y, *args, **kwargs: x + y,
        my_set={1, 2, [3, 4], {5: 6}, (7, 8)},
        _value=MyValue('asd', *args, kwarg=123, **extras),
        _name: Text = 'default',
    ) -> Dict[Text, MyValue]:
```

#### Attributes

- `two` - comment here: `2`

#### See also

- [Typed](#typed)

### Typed.classmethod

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/examples/comment_typed.py#L29)

```python
@classmethod
def classmethod(_my_value: Any, *_args: Text, **_kwargs: MyValue) -> Typed:
```

#### See also

- [Typed.classmethod](#typedclassmethod)

## func

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/examples/comment_typed.py#L35)

```python
def func(
    _list: None,
    _my_value_cls: Type[MyValue] = MyValue,
    **_kwargs: Tuple[List[Text], ...],
) -> Any:
```

#### See also

- [func](#func)

## func_any

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/examples/comment_typed.py#L40)

```python
def func_any(
    _list: None,
    _my_value_cls: Any = MyValue,
    **_kwargs: Tuple[List[Text], ...],
) -> Any:
```

#### See also

- [func_any](#func_any)
