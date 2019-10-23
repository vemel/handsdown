# PathFinder

> Auto-generated documentation for [handsdown.path_finder](https://github.com/vemel/handsdown/blob/master/handsdown/path_finder.py) module.

Glob helper for matching paths inside `root` path with `.gitignore`-like
`include` and `exclude` patterns.

- [Handsdown](../README.md#-handsdown---python-documentation-generator) / [Modules](../MODULES.md#modules) / [Handsdown](index.md#handsdown) / PathFinder
  - [PathFinder](#pathfinder)
    - [PathFinder().exclude](#pathfinderexclude)
    - [PathFinder().glob](#pathfinderglob)
    - [PathFinder().include](#pathfinderinclude)
    - [PathFinder().mkdir](#pathfindermkdir)
    - [PathFinder().relative](#pathfinderrelative)
  - [PathFinderError](#pathfindererror)

## PathFinder

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/path_finder.py#L26)

```python
class PathFinder():
    def __init__(root: Path) -> None:
```

Glob helper for matching paths inside `root` path with `.gitignore`-like
`include` and `exclude` patterns.

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

- [PathFinderError](#pathfindererror) - If `root` is not absolute or not a directory.

### PathFinder().exclude

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/path_finder.py#L93)

```python
def exclude(*fn_exrps: Text) -> PathFinder:
```

Add `fnmatch` expression to black list.
If black list is empty - no black list filtration applied.
If expression does not have `*` or `.` characters, appends `/*` to it.

#### Arguments

- `fn_exrps` - One or more `fnmatch` expressions.

#### Returns

A copy of itself.

### PathFinder().glob

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/path_finder.py#L138)

```python
def glob(glob_expr: Text) -> Generator[Path, None, None]:
```

Find all matching `Path` objects respecting `include` and
`exclude` patterns.

#### Yields

Matching `Path` objects.

### PathFinder().include

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/path_finder.py#L72)

```python
def include(*fn_exrps: Text) -> PathFinder:
```

Add `fnmatch` expression to white list.
If white list is empty - no white list filtration applied.
If expression does not have `*` or `.` characters, appends `/*` to it.

#### Arguments

- `fn_exrps` - One or more `fnmatch` expressions.

#### Returns

A copy of itself.

### PathFinder().mkdir

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/path_finder.py#L187)

```python
def mkdir(force: bool = False) -> None:
```

Create directories up to `root` if they do not exist.

#### Arguments

- `force` - Delete existing parent if it is not a directory.

#### Raises

- [PathFinderError](#pathfindererror) - If any existing parent is not a directory and not in `safe` mode.

### PathFinder().relative

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/path_finder.py#L158)

```python
def relative(target: Path) -> Path:
```

Find a relative path from `root` to `target`.
`target` should be an absolute path.

#### Arguments

- `target` - Target path.

#### Returns

A relative path to `target`.

## PathFinderError

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/path_finder.py#L20)

```python
class PathFinderError(Exception):
```

Main error for [PathFinder](#pathfinder).
