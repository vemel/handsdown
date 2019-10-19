# Comment Typed

> Auto-generated documentation for [examples.comment_typed](https://github.com/vemel/handsdown/blob/master/examples/comment_typed.py) module.

- [Index](../README.md#modules) / [Examples](index.md#examples) / Comment Typed
  - [MyValue](#myvalue)
  - [Typed](#typed)
    - [Typed.classmethod](#typedclassmethod)
  - [func](#func)
  - [func_any](#func_any)

## MyValue

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/examples/comment_typed.py#L4)

```python
class MyValue(args, kwargs)
```

## Typed

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/examples/comment_typed.py#L8)

```python
class Typed(
    _value: Union[List[Text], Text, MyValue] = <examples.comment_typed.MyValue object>,
    _name: Text = 'default',
) -> Dict[Text, MyValue]
```

#### See also

- [MyValue](#myvalue)

### Typed.classmethod

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/examples/comment_typed.py#L17)

```python
def classmethod(_my_value: MyValue, _args: Text, _kwargs: Any) -> Typed
```

#### See also

- [MyValue](#myvalue)

## func

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/examples/comment_typed.py#L23)

```python
def func(
    _list: Tuple[List[Text], ...],
    _my_value_cls: Type[MyValue],
    _kwargs: None = <class 'examples.comment_typed.MyValue'>,
) -> Any
```

#### See also

- [MyValue](#myvalue)

## func_any

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/examples/comment_typed.py#L28)

```python
def func_any(
    _list: Tuple[List[Text], ...],
    _my_value_cls: Any,
    _kwargs: None = <class 'examples.comment_typed.MyValue'>,
) -> Any
```

#### See also

- [MyValue](#myvalue)
