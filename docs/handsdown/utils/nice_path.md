# NicePath

[Handsdown API Index](../../README.md#handsdown-api-index) /
[Handsdown](../index.md#handsdown) /
[Utils](./index.md#utils) /
NicePath

> Auto-generated documentation for [handsdown.utils.nice_path](https://github.com/vemel/handsdown/blob/main/handsdown/utils/nice_path.py) module.

## NicePath

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/nice_path.py#L11)

Path that represents it as relative to workdir.

#### Signature

```python
class NicePath(type(Path())):
    ...
```

### NicePath().rmtree

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/nice_path.py#L63)

Remove directory and all its contents.

#### Signature

```python
def rmtree(self, ignore_errors: bool = True) -> None:
    ...
```

### NicePath().walk

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/nice_path.py#L33)

Walk files except for `exclude`.

#### Yields

Existing Path.

#### Signature

```python
def walk(
    self: _R, exclude: Iterable[Path] = tuple(), glob_pattern: str = "**/*"
) -> Iterator[_R]:
    ...
```

### NicePath().write_changed

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/nice_path.py#L52)

Write content to file if it's changed.

#### Signature

```python
def write_changed(self, content: str, encoding: str) -> bool:
    ...
```



