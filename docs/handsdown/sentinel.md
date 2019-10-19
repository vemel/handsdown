# Sentinel

> Auto-generated documentation for [handsdown.sentinel](https://github.com/vemel/handsdown/blob/master/handsdown/sentinel.py) module.

- [Index](../README.md#modules) / [Handsdown](index.md#handsdown) / Sentinel
  - [Sentinel](#sentinel)

## Sentinel

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/sentinel.py#L4)

```python
class Sentinel(name: Text = 'DEFAULT') -> None
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
