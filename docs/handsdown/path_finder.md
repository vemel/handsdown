# PathFinder

> Auto-generated documentation for [handsdown.path_finder](https://github.com/vemel/handsdown/blob/master/handsdown/path_finder.py) module..

Glob helper for matching paths inside `root` path with `.gitignore`-like
`include` and `exclude` patterns.

- [Index](../README.md#modules) / [Handsdown](index.md#handsdown) / PathFinder
  - [Path](#path)
  - [PathFinder](#pathfinder)
    - [PathFinder().exclude](#pathfinderexclude)
    - [PathFinder().glob](#pathfinderglob)
    - [PathFinder().include](#pathfinderinclude)
    - [PathFinder().mkdir](#pathfindermkdir)
    - [PathFinder().relative](#pathfinderrelative)
  - [PathFinderError](#pathfindererror)

## Path

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/path_finder.py#L25)

```python
class Path()
```

Regular `pathlib.Path` or `pathlib2.Path`

## PathFinder

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/path_finder.py#L31)

```python
class PathFinder(root: Path) -> None
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

#### See also

- [Path](#path)

### PathFinder().exclude

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/path_finder.py#L98)

```python
def exclude(fn_exrps: Text) -> PathFinder
```

Add `fnmatch` expression to black list.
If black list is empty - no black list filtration applied.
If expression does not have `*` or `.` characters, appends `/*` to it.

#### Arguments

- `fn_exrps` - One or more `fnmatch` expressions.

#### Returns

A copy of itself.

### PathFinder().glob

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/path_finder.py#L143)

```python
def glob(glob_expr: Text) -> Generator[Path, None, None]
```

Find all matching [Path](#path) objects respecting `include` and
`exclude` patterns.

#### Yields

Matching [Path](#path) objects.

### PathFinder().include

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/path_finder.py#L77)

```python
def include(fn_exrps: Text) -> PathFinder
```

Add `fnmatch` expression to white list.
If white list is empty - no white list filtration applied.
If expression does not have `*` or `.` characters, appends `/*` to it.

#### Arguments

- `fn_exrps` - One or more `fnmatch` expressions.

#### Returns

A copy of itself.

### PathFinder().mkdir

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/path_finder.py#L190)

```python
def mkdir(force: bool = False) -> None
```

Create directories up to `root` if they do not exist.

#### Arguments

- `force` - Delete existing parent if it is not a directory.

#### Raises

- [PathFinderError](#pathfindererror) - If any existing parent is not a directory and not in `safe` mode.

### PathFinder().relative

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/path_finder.py#L161)

```python
def relative(target: Path) -> Path
```

Find a relative path from `root` to `target`.
`target` should be an absolute path.

#### Arguments

- `target` - Target path.

#### Returns

A relative path to `target`.

#### See also

- [Path](#path)

## PathFinderError

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/path_finder.py#L19)

```python
class PathFinderError()
```

Main error for [PathFinder](#pathfinder).
