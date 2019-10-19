# PathFinder

> Auto-generated documentation for [path_finder](../path_finder.py) module..

Glob helper for matching paths inside `root` path with `.gitignore`-like
`include` and `exclude` patterns.

- [Index](README.md#modules) / PathFinder
  - [PathFinder](#pathfinder)
    - [PathFinder().exclude](#pathfinderexclude)
    - [PathFinder().glob](#pathfinderglob)
    - [PathFinder().include](#pathfinderinclude)
    - [PathFinder().mkdir](#pathfindermkdir)
    - [PathFinder().relative](#pathfinderrelative)
  - [PathFinderError](#pathfindererror)

## PathFinder

[🔍 find in source code](../path_finder.py#L25)

```python
class PathFinder(root: Path) -> None
```

Glob helper for matching paths inside `root` path with `.gitignore`-like
`include` and `exclude` patterns.

#### Raises

- [PathFinderError](#pathfindererror) - If `root` is not absolute or not a directory.

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

### PathFinder().exclude

[🔍 find in source code](../path_finder.py#L92)

```python
def exclude(fn_exrps: Text) -> PathFinder
```

Add `fnmatch` expression to black list.
If black list is empty - no black list filtration applied.
If expression does not have `*` or `.` characters, appends `/*` to it.

#### Returns

A copy of itself.

#### Arguments

- `fn_exrps` - One or more `fnmatch` expressions.

### PathFinder().glob

[🔍 find in source code](../path_finder.py#L137)

```python
def glob(glob_expr: Text) -> Generator[Path, None, None]
```

Find all matching `Path` objects respecting `include` and
`exclude` patterns.

#### Yields

Matching `Path` objects.

### PathFinder().include

[🔍 find in source code](../path_finder.py#L71)

```python
def include(fn_exrps: Text) -> PathFinder
```

Add `fnmatch` expression to white list.
If white list is empty - no white list filtration applied.
If expression does not have `*` or `.` characters, appends `/*` to it.

#### Returns

A copy of itself.

#### Arguments

- `fn_exrps` - One or more `fnmatch` expressions.

### PathFinder().mkdir

[🔍 find in source code](../path_finder.py#L184)

```python
def mkdir(force: bool = False) -> None
```

Create directories up to `root` if they do not exist.

#### Arguments

- `force` - Delete existing parent if it is not a directory.

#### Raises

- [PathFinderError](#pathfindererror) - If any existing parent is not a directory and not in `safe` mode.

### PathFinder().relative

[🔍 find in source code](../path_finder.py#L155)

```python
def relative(target: Path) -> Path
```

Find a relative path from `root` to `target`.
`target` should be an absolute path.

#### Returns

A relative path to `target`.

#### Arguments

- `target` - Target path.

## PathFinderError

[🔍 find in source code](../path_finder.py#L19)

```python
class PathFinderError()
```

Main error for [PathFinder](#pathfinder).
