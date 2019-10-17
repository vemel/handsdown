# PathFinder

> Auto-generated documentation for [handsdown.path_finder](../../handsdown/path_finder.py) module..

Glob helper for matching paths inside `root` path with `.gitignore`-like
`include` and `exclude` patterns.

- [Index](../README.md#modules) / [Handsdown](index.md#handsdown) / PathFinder
  - [PathFinder](#pathfinder)
    - [PathFinder().exclude](#pathfinderexclude)
    - [PathFinder().glob](#pathfinderglob)
    - [PathFinder().include](#pathfinderinclude)
    - [PathFinder().mkdir](#pathfindermkdir)
    - [PathFinder().relative](#pathfinderrelative)
  - [PathFinderError](#pathfindererror)

## PathFinder

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/path_finder.py#L23)

```python
class PathFinder(root: pathlib.Path)
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

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/path_finder.py#L89)

```python
def exclude(*fn_exrps: str) -> handsdown.path_finder.PathFinder
```

Add `fnmatch` expression to black list.
If black list is empty - no black list filtration applied.
If expression does not have `*` or `.` characters, appends `/*` to it.

#### Arguments

fn_exrps - One or more `fnmatch` expressions.

#### Returns

A copy of itself.

#### See also

- [PathFinder](#pathfinder)

### PathFinder().glob

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/path_finder.py#L131)

```python
def glob(glob_expr: str) -> Generator[pathlib.Path, NoneType, NoneType]
```

Find all matching `Path` objects respecting `include` and
`exclude` patterns.

#### Yields

Matching `Path` objects.

### PathFinder().include

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/path_finder.py#L69)

```python
def include(*fn_exrps: str) -> handsdown.path_finder.PathFinder
```

Add `fnmatch` expression to white list.
If white list is empty - no white list filtration applied.
If expression does not have `*` or `.` characters, appends `/*` to it.

#### Arguments

fn_exrps - One or more `fnmatch` expressions.

#### Returns

A copy of itself.

#### See also

- [PathFinder](#pathfinder)

### PathFinder().mkdir

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/path_finder.py#L176)

```python
def mkdir(force: bool = False) -> None
```

Create directories up to `root` if they do not exist.

#### Arguments

- `force` - Delete existing parent if it is not a directory.

#### Raises

- [PathFinderError](#pathfindererror) - If any existing parent is not a directory and not in `safe` mode.

### PathFinder().relative

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/path_finder.py#L148)

```python
def relative(target: pathlib.Path) -> pathlib.Path
```

Find a relative path from `root` to `target`.
`target` should be an absolute path.

#### Arguments

- `target` - Target path.

#### Returns

A relative path to `target`.

## PathFinderError

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/path_finder.py#L17)

```python
class PathFinderError(*args, **kwargs)
```

Main error for [PathFinder](#pathfinder).
