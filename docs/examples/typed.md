# PEP 484 - type annotations examples

> Auto-generated documentation for [examples.typed](https://github.com/vemel/handsdown/blob/main/examples/typed.py) module.

- [Handsdown](../README.md#-handsdown---python-documentation-generator) / [Modules](../MODULES.md#modules) / [Examples](index.md#examples) / PEP 484 - type annotations examples
    - [Links](#links)
    - [MyValue](#myvalue)
    - [Typed](#typed)
        - [Typed().async_method](#typedasync_method)
        - [Typed.classmethod](#typedclassmethod)
    - [func](#func)
    - [my_deco](#my_deco)

## Links

[PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/)

## MyValue

[[find in source code]](https://github.com/vemel/handsdown/blob/main/examples/typed.py#L12)

```python
class MyValue():
```

## Typed

[[find in source code]](https://github.com/vemel/handsdown/blob/main/examples/typed.py#L16)

```python
class Typed():
    def __init__(
        _value: Union[List[str], str, MyValue] = MyValue(
            {
                'key1': 'value1',
                'key2': 'value2',
                'key3': 'value3',
                'key4': 'value4',
                'key5': 'value5',
                'key6': 'value6',
            },
        ),
        _name: str = 'default',
    ) -> Dict[str, MyValue]:
```

#### See also

- [MyValue](#myvalue)

### Typed().async_method

[[find in source code]](https://github.com/vemel/handsdown/blob/main/examples/typed.py#L38)

```python
async def async_method(_value: str) -> str:
```

### Typed.classmethod

[[find in source code]](https://github.com/vemel/handsdown/blob/main/examples/typed.py#L34)

```python
@classmethod
def classmethod(_my_value: MyValue, *_args: str, **_kwargs: Any) -> None:
```

#### See also

- [MyValue](#myvalue)

## func

[[find in source code]](https://github.com/vemel/handsdown/blob/main/examples/typed.py#L46)

```python
@my_deco(key='value')
def func(
    _list: Tuple[List[str], ...],
    _my_value_cls: Type[MyValue] = MyValue,
    **_kwargs: None,
) -> Optional[MyValue]:
```

#### See also

- [MyValue](#myvalue)

## my_deco

[[find in source code]](https://github.com/vemel/handsdown/blob/main/examples/typed.py#L42)

```python
def my_deco(key):
```
