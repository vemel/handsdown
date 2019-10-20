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
class MyValue()
```

## Typed

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/examples/typed.py#L8)

```python
class Typed(
    _value: Union[List[str], str, examples.typed.MyValue] = <examples.typed.MyValue object>,
    _name: str = 'default',
) -> Dict[str, examples.typed.MyValue]
```

#### See also

- [MyValue](#myvalue)

### Typed.classmethod

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/examples/typed.py#L16)

```python
@classmethod
def classmethod(_my_value: MyValue, _args: str, _kwargs: Any) -> None
```

#### See also

- [MyValue](#myvalue)

## func

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/examples/typed.py#L21)

```python
def func(
    _list: Tuple[List[str], ...],
    _my_value_cls: Type[examples.typed.MyValue],
    _kwargs: None = <class 'examples.typed.MyValue'>,
) -> Any
```

#### See also

- [MyValue](#myvalue)
