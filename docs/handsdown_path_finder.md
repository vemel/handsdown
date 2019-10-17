# PathFinder

> Auto-generated documentation for [handsdown.path_finder](../handsdown/path_finder.py) module.

- [Handsdown](README.md#handsdown) / [Handsdown](handsdown_index.md#handsdown) / PathFinder
  - [PathFinder](#pathfinder)
    - [PathFinder().exclude](#pathfinderexclude)
    - [PathFinder().include](#pathfinderinclude)
    - [PathFinder().list](#pathfinderlist)
    - [PathFinder().relative](#pathfinderrelative)

## PathFinder

[🔍 find in source code](../handsdown/path_finder.py#l12)

```python
class PathFinder(root: pathlib.Path)
```

Find matching paths inside `root` path.

#### Examples

```python
path_finder = PathFinder(root=Path.cwd())
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

### PathFinder().exclude

[🔍 find in source code](../handsdown/path_finder.py#l66)

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

- [PathFinder](.#pathfinder)

### PathFinder().include

[🔍 find in source code](../handsdown/path_finder.py#l46)

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

- [PathFinder](.#pathfinder)

### PathFinder().list

[🔍 find in source code](../handsdown/path_finder.py#l108)

```python
def list(glob_expr: str) -> List[pathlib.Path]
```

Return all matching paths as a list.

#### Returns

A list of all matched paths.

### PathFinder().relative

[🔍 find in source code](../handsdown/path_finder.py#l126)

```python
def relative(target: pathlib.Path) -> pathlib.Path
```

Find a relative path from `root` to `target`.
`target` should be an absolute path.

#### Arguments

- `target` - Target path.

#### Returns

A relative path to `target`.

#### Raises

- `ValueError` - if `target` is not absolute.
