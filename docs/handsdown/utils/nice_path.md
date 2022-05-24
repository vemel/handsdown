# NicePath

> Auto-generated documentation for [handsdown.utils.nice_path](https://github.com/vemel/handsdown/blob/main/handsdown/utils/nice_path.py) module.

Path that represents it as relative to workdir.

- [Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / [Utils](index.md#utils) / NicePath
    - [NicePath](#nicepath)
        - [NicePath().walk](#nicepathwalk)

## NicePath

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/utils/nice_path.py#L11)

```python
class NicePath(Path):
```

Path that represents it as relative to workdir.

### NicePath().walk

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/utils/nice_path.py#L35)

```python
def walk(
    exclude: Iterable[Path] = tuple(),
    glob_pattern: str = '**/*',
) -> Iterator[_R]:
```

Walk files except for `exclude`.

#### Yields

Existing Path.
