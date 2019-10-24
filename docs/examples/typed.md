# Typed

> Auto-generated documentation for [examples.typed](https://github.com/vemel/handsdown/blob/master/examples/typed.py) module.

- [Handsdown](../README.md#-handsdown---python-documentation-generator) / [Modules](../MODULES.md#modules) / [Examples](index.md#examples) / Typed
    - [MyValue](#myvalue)
    - [Typed](#typed)
        - [Typed.classmethod](#typedclassmethod)
    - [func](#func)

## MyValue

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/examples/typed.py#L4)

```python
class MyValue():
```

## Typed

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/examples/typed.py#L8)

```python
class Typed():
    def __init__(
        _value: Union[List[Text], Text, MyValue] = MyValue(
            {
                'key1': 'value1',
                'key2': 'value2',
                'key3': 'value3',
                'key4': 'value4',
                'key5': 'value5',
                'key6': 'value6',
            },
        ),
        _name: Text = 'default',
    ) -> Dict[Text, MyValue]:
```

### Typed.classmethod

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/examples/typed.py#L26)

```python
@classmethod
def classmethod(_my_value: MyValue, *_args: Text, **_kwargs: Any) -> None:
```

#### See also

- [MyValue](#myvalue)

## func

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/examples/typed.py#L31)

```python
def func(
    _list: Tuple[List[Text], ...],
    _my_value_cls: Type[MyValue] = MyValue,
    **_kwargs: None,
) -> Any:
```

#### See also

- [MyValue](#myvalue)
