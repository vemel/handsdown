# NicePath

[Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / [Utils](index.md#utils) / NicePath

> Auto-generated documentation for [handsdown.utils.nice_path](https://github.com/vemel/handsdown/blob/main/handsdown/utils/nice_path.py) module.

- [NicePath](#nicepath)

## NicePath

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/nice_path.py#L10)

Path that represents it as relative to workdir.

#### Signature

```python
class NicePath(type(Path())):
    ...
```

### NicePath().write_changed

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/nice_path.py#L32)

Write content to file if it's changed.

#### Signature

```python
def write_changed(self, content: str, encoding: str) -> bool:
    ...
```


