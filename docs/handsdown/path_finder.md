# PathFinder

> Auto-generated documentation for [handsdown.path_finder](../../handsdown/path_finder.py) module.

- [Index](../README.md#handsdown-index) / [Handsdown](index.md#handsdown) / [PathFinder](#pathfinder) / PathFinder
  - [PathFinder](#pathfinder)
    - [PathFinder().exclude](#pathfinderexclude)
    - [PathFinder().glob](#pathfinderglob)
    - [PathFinder().include](#pathfinderinclude)
    - [PathFinder().mkdir](#pathfindermkdir)
    - [PathFinder().relative](#pathfinderrelative)
  - [PathFinderError](#pathfindererror)

## PathFinder

[🔍 find in source code](../../handsdown/path_finder.py#l18)

```python
class PathFinder(root: pathlib.Path)
```

Find matching paths inside `root` path.

#### Examples

```python
path_finder = PathFinder(Path.cwd())
path_finder.list()
['my_new.txt', 'my.txt', 'new.txt']

path_finder.include('my*').list('*.txt')
['my_new.txt', 'my.txt']

path_finder.exclude('*new*').list('*.txt')
['my.txt']
```

#### Arguments

- `root` - Path to root folder.
- `glob_expr` - `glob` expression to lookup in `root`

#### Raises

- [PathFinderError](#pathfindererror) - If `root` is not absolute or not a directory.

### PathFinder().exclude

[🔍 find in source code](../../handsdown/path_finder.py#l80)

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

[🔍 find in source code](../../handsdown/path_finder.py#l122)

```python
def glob(glob_expr: str) -> Generator[pathlib.Path, NoneType, NoneType]
```

Find all matching `Path` objects respecting `include` and
`exclude` patterns.

#### Yields

Matching `Path` objects.

### PathFinder().include

[🔍 find in source code](../../handsdown/path_finder.py#l60)

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

[🔍 find in source code](../../handsdown/path_finder.py#l166)

```python
def mkdir(force=False)
```

Create directories up to `root` if they do not exist.

#### Arguments

- `force` - Delete existing parent if it is not a directory.

#### Raises

- [PathFinderError](#pathfindererror) - If any existing parent is not a directory and not in `safe` mode.

### PathFinder().relative

[🔍 find in source code](../../handsdown/path_finder.py#l139)

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

[🔍 find in source code](../../handsdown/path_finder.py#l12)

```python
class PathFinderError(*args, **kwargs)
```

Main error for [PathFinder](#pathfinder).
