# PathFinder

[Handsdown API Index](../../README.md#handsdown-api-index) /
[Handsdown](../index.md#handsdown) /
[Utils](./index.md#utils) /
PathFinder

> Auto-generated documentation for [handsdown.utils.path_finder](https://github.com/vemel/handsdown/blob/main/handsdown/utils/path_finder.py) module.

- [PathFinder](#pathfinder)
  - [PathFinder](#pathfinder-1)
    - [PathFinder().exclude](#pathfinder()exclude)
    - [PathFinder().glob](#pathfinder()glob)
    - [PathFinder().include](#pathfinder()include)
    - [PathFinder().mkdir](#pathfinder()mkdir)
    - [PathFinder().relative](#pathfinder()relative)

## PathFinder

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/path_finder.py#L19)

Glob helper for matching paths inside `root` path.

With `.gitignore`-like `include` and `exclude` patterns.

#### Examples

```python
path_finder = PathFinder(Path.cwd())
list(path_finder.glob('*.txt'))
['my_new.txt', 'my.txt', 'new.txt']

list(path_finder.include('my*').glob('*.txt'))
['my_new.txt', 'my.txt']

list(path_finder.exclude('*new*').glob('*.txt'))
['my.txt']
```

#### Arguments

- `root` - Path to root folder.
- `glob_expr` - `glob` expression to lookup in `root`

#### Raises

- `PathFinderError` - If `root` is not absolute or not a directory.

#### Signature

```python
class PathFinder:
    def __init__(self, root: Path) -> None:
        ...
```

### PathFinder().exclude

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/path_finder.py#L86)

Add `fnmatch` expression to black list.

If black list is empty - no black list filtration applied.
If expression does not have `*` or `.` characters, appends `/*` to it.

#### Arguments

- `fn_exrps` - One or more `fnmatch` expressions.

#### Returns

A copy of itself.

#### Signature

```python
def exclude(self: _R, *fn_exrps: str) -> _R:
    ...
```

### PathFinder().glob

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/path_finder.py#L129)

Find all matching `Path` objects respecting [PathFinder().include](#pathfinderinclude) and [PathFinder().exclude](#pathfinderexclude) patterns.

#### Yields

Matching `Path` objects.

#### Signature

```python
def glob(self, glob_expr: str) -> Iterator[NicePath]:
    ...
```

### PathFinder().include

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/path_finder.py#L65)

Add `fnmatch` expression to white list.

If white list is empty - no white list filtration applied.
If expression does not have `*` or `.` characters, appends `/*` to it.

#### Arguments

- `fn_exrps` - One or more `fnmatch` expressions.

#### Returns

A copy of itself.

#### Signature

```python
def include(self: _R, *fn_exrps: str) -> _R:
    ...
```

### PathFinder().mkdir

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/path_finder.py#L174)

Create directories up to `root` if they do not exist.

#### Arguments

- `force` - Delete existing parent if it is not a directory.

#### Raises

- `PathFinderError` - If any existing parent is not a directory and not in `force` mode.

#### Signature

```python
def mkdir(self, force: bool = False) -> None:
    ...
```

### PathFinder().relative

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/path_finder.py#L145)

Find a relative path from `root` to `target`.

`target` should be an absolute path.

#### Arguments

- `target` - Target path.

#### Returns

A relative path to `target`.

#### Signature

```python
def relative(self, target: Path) -> NicePath:
    ...
```

#### See also

- [NicePath](./nice_path.md#nicepath)


