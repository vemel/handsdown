# Sentinel

> Auto-generated documentation for [handsdown.utils.sentinel](https://github.com/vemel/handsdown/blob/master/handsdown/utils/sentinel.py) module.

Sentinel value than can be used as a placeholder.

- [Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / [Utils](index.md#utils) / Sentinel
    - [Sentinel](#sentinel)

## Sentinel

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/utils/sentinel.py#L7)

```python
class Sentinel():
    def __init__(name: Text = 'DEFAULT') -> None:
```

Sentinel value than can be used as a placeholder.
Doc generation friendly.

#### Examples

```python
NOT_SET = Sentinel('NOT_SET')

def check_value(name=NOT_SET):
    if name is NOT_SET:
        return 'This is a NOT_SET value'

    return 'This is something else'

repr(NOT_SET) # 'NOT_SET'
```

#### Arguments

- `name` - String used as a representation of the object.
