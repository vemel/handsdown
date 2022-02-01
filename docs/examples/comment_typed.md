# PEP 484 - comment-based type annotations examples

> Auto-generated documentation for [examples.comment_typed](https://github.com/vemel/handsdown/blob/main/examples/comment_typed.py) module.

- [Handsdown](../README.md#-handsdown---python-documentation-generator) / [Modules](../MODULES.md#modules) / [Examples](index.md#examples) / PEP 484 - comment-based type annotations examples
    - [Links](#links)
    - [MyValue](#myvalue)
    - [Typed](#typed)
        - [Typed.classmethod](#typedclassmethod)
    - [func](#func)
    - [func_any](#func_any)

## Links

[PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/)

## MyValue

[[find in source code]](https://github.com/vemel/handsdown/blob/main/examples/comment_typed.py#L12)

```python
class MyValue():
    def __init__(*args, **kwargs) -> None:
```

## Typed

[[find in source code]](https://github.com/vemel/handsdown/blob/main/examples/comment_typed.py#L18)

```python
class Typed():
    def __init__(
        my_bool: bool = one & ~two == 'three' and not -4,
        my_lambda=lambda x, y, *args, **kwargs: x + y,
        my_set: Set = {1, 2, [3, 4], {5: 6}, (7, 8)},
        _value: Union[List[str], str, MyValue] = MyValue('asd', *args, kwarg=123, **extras),
        _name: str = 'default',
    ) -> None:
```

#### Attributes

- `two` - comment here: `2`

#### See also

- [MyValue](#myvalue)

### Typed.classmethod

[[find in source code]](https://github.com/vemel/handsdown/blob/main/examples/comment_typed.py#L37)

```python
@classmethod
def classmethod(_my_value: MyValue, *_args: str, **_kwargs: Any) -> Typed:
```

#### See also

- [MyValue](#myvalue)

## func

[[find in source code]](https://github.com/vemel/handsdown/blob/main/examples/comment_typed.py#L43)

```python
def func(
    _list: Tuple[List[str], ...],
    _my_value_cls: Type[MyValue] = MyValue,
    **_kwargs: None,
) -> Any:
```

#### See also

- [MyValue](#myvalue)

## func_any

[[find in source code]](https://github.com/vemel/handsdown/blob/main/examples/comment_typed.py#L48)

```python
def func_any(
    _list: Tuple[List[str], ...],
    _my_value_cls: Any = MyValue,
    **_kwargs: None,
) -> Any:
```

#### See also

- [MyValue](#myvalue)
