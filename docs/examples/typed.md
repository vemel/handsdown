# PEP 484 - type annotations examples

[Handsdown](../README.md#-handsdown---python-documentation-generator) / [Modules](../MODULES.md#modules) / [Examples](index.md#examples) / PEP 484 - type annotations examples

> Auto-generated documentation for [examples.typed](https://github.com/vemel/handsdown/blob/main/examples/typed.py) module.

- [PEP 484 - type annotations examples](#pep-484---type-annotations-examples)

## MyValue

[find in source code](https://github.com/vemel/handsdown/blob/main/examples/typed.py#L11)

#### Signature

```python
class MyValue:
    ...
```



## Typed

[find in source code](https://github.com/vemel/handsdown/blob/main/examples/typed.py#L15)

#### Signature

```python
class Typed:
    def __init__(
        self,
        _value: Union[List[str], str, MyValue] = MyValue(
            {
                "key1": "value1",
                "key2": "value2",
                "key3": "value3",
                "key4": "value4",
                "key5": "value5",
                "key6": "value6",
            }
        ),
        _name: str = "default",
    ) -> Dict[str, MyValue]:
        ...
```

#### See also
- [MyValue](#myvalue)

### Typed().async_method

[find in source code](https://github.com/vemel/handsdown/blob/main/examples/typed.py#L37)

#### Signature

```python
async def async_method(self, _value: str) -> str:
    ...
```

### Typed.classmethod

[find in source code](https://github.com/vemel/handsdown/blob/main/examples/typed.py#L33)

#### Signature

```python
@classmethod
def classmethod(cls, _my_value: MyValue, *_args: str, **_kwargs: Any) -> None:
    ...
```

#### See also
- [MyValue](#myvalue)



## func

[find in source code](https://github.com/vemel/handsdown/blob/main/examples/typed.py#L45)

#### Signature

```python
@my_deco(key="value")
def func(
    _list: Tuple[List[str], ...], _my_value_cls: Type[MyValue] = MyValue, **_kwargs: None
) -> Optional[MyValue]:
    ...
```

#### See also
- [MyValue](#myvalue)



## my_deco

[find in source code](https://github.com/vemel/handsdown/blob/main/examples/typed.py#L41)

#### Signature

```python
def my_deco(key):
    ...
```


