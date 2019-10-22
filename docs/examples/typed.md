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
        _value: Union[(List[Text], Text, MyValue)] = MyValue(),
        _name: Text = 'default',
    ):
```

#### See also

- [Typed](#typed)

### Typed.classmethod

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/examples/typed.py#L16)

```python
@classmethod
def classmethod(_my_value: MyValue, *_args: Text, **_kwargs: Any):
```

#### See also

- [Typed.classmethod](#typedclassmethod)

## func

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/examples/typed.py#L21)

```python
def func(
    _list: Tuple[(List[Text], ...)],
    _my_value_cls: Type[MyValue] = MyValue,
    **_kwargs: None,
):
```

#### See also

- [func](#func)
