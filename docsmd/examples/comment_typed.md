# PEP 484 - comment-based type annotations examples

[Handsdown API Index](../README.md#handsdown-api-index) /
[Examples](./index.md#examples) /
PEP 484 - comment-based type annotations examples

> Auto-generated documentation for [examples.comment_typed](https://github.com/vemel/handsdown/blob/main/examples/comment_typed.py) module.

## MyValue

[Show source in comment_typed.py:11](https://github.com/vemel/handsdown/blob/main/examples/comment_typed.py#L11)

#### Signature

```python
class MyValue:
    def __init__(self, *args, **kwargs) -> None:
        ...
```



## Typed

[Show source in comment_typed.py:17](https://github.com/vemel/handsdown/blob/main/examples/comment_typed.py#L17)

#### Attributes

- `two` - comment here: `2`


#### Signature

```python
class Typed:
    def __init__(
        self,
        my_bool: bool = one & ~two == "three" and not -4,
        my_lambda=lambda x, y, *args, **kwargs,: x + y,
        my_set: Set = {1, 2, [3, 4], {5: 6}, (7, 8)},
        _value: Union[List[str], str, MyValue] = MyValue(
            "asd", *args, kwarg=123, **extras
        ),
        _name: str = "default",
    ) -> None:
        ...
```

#### See also

- [MyValue](#myvalue)

### Typed.classmethod

[Show source in comment_typed.py:36](https://github.com/vemel/handsdown/blob/main/examples/comment_typed.py#L36)

#### Signature

```python
@classmethod
def classmethod(cls, _my_value: MyValue, *_args: str, **_kwargs: Any) -> Typed:
    ...
```

#### See also

- [MyValue](#myvalue)



## func

[Show source in comment_typed.py:42](https://github.com/vemel/handsdown/blob/main/examples/comment_typed.py#L42)

#### Signature

```python
def func(
    _list: Tuple[List[str], ...], _my_value_cls: Type[MyValue] = MyValue, **_kwargs: None
) -> Any:
    ...
```

#### See also

- [MyValue](#myvalue)



## func_any

[Show source in comment_typed.py:47](https://github.com/vemel/handsdown/blob/main/examples/comment_typed.py#L47)

#### Signature

```python
def func_any(
    _list: Tuple[List[str], ...], _my_value_cls: Any = MyValue, **_kwargs: None
) -> Any:
    ...
```

#### See also

- [MyValue](#myvalue)



