# Handsdown: Path finder

- [Handsdown: Path finder](#handsdown-path-finder)
  - [PathFinder](#pathfinder)
    - [PathFinder().exclude](#pathfinderexclude)
    - [PathFinder().include](#pathfinderinclude)
    - [PathFinder().list](#pathfinderlist)

> Auto-generated documentation for [handsdown.path_finder](../handsdown/path_finder.py) module.

## PathFinder

[🔍 find in source code](../handsdown/path_finder.py#L9)

```python
class PathFinder(root: pathlib.Path, glob_expr: str) -> None
```

Find matching paths inside `root` path.

#### Examples

```python
path_finder = PathFinder(root=Path.cwd(), glob_expr='*.txt')
path_finder.list() # ['my_new.txt', 'my.txt', 'new.txt']
path_finder.include('my*').list() # ['my_new.txt', 'my.txt']
path_finder.exclude('*new*').list() # ['my.txt']
```

#### Arguments

- `root` - Path to root folder.
- `glob_expr` - `glob` expression to lookup in `root`

### PathFinder().exclude

[🔍 find in source code](../handsdown/path_finder.py#L61)

```python
def exclude(*fn_exrps: str) -> handsdown.path_finder.PathFinder
```

Find matching paths inside `root` path.

#### Examples

```python
path_finder = PathFinder(root=Path.cwd(), glob_expr='*.txt')
path_finder.list() # ['my_new.txt', 'my.txt', 'new.txt']
path_finder.include('my*').list() # ['my_new.txt', 'my.txt']
path_finder.exclude('*new*').list() # ['my.txt']
```

#### Arguments

- `root` - Path to root folder.
- `glob_expr` - `glob` expression to lookup in `root`

#### See also

- [PathFinder](#pathfinder)

### PathFinder().include

[🔍 find in source code](../handsdown/path_finder.py#L41)

```python
def include(*fn_exrps: str) -> handsdown.path_finder.PathFinder
```

Find matching paths inside `root` path.

#### Examples

```python
path_finder = PathFinder(root=Path.cwd(), glob_expr='*.txt')
path_finder.list() # ['my_new.txt', 'my.txt', 'new.txt']
path_finder.include('my*').list() # ['my_new.txt', 'my.txt']
path_finder.exclude('*new*').list() # ['my.txt']
```

#### Arguments

- `root` - Path to root folder.
- `glob_expr` - `glob` expression to lookup in `root`

#### See also

- [PathFinder](#pathfinder)

### PathFinder().list

[🔍 find in source code](../handsdown/path_finder.py#L119)

```python
def list() -> List[pathlib.Path]
```

Find matching paths inside `root` path.

#### Examples

```python
path_finder = PathFinder(root=Path.cwd(), glob_expr='*.txt')
path_finder.list() # ['my_new.txt', 'my.txt', 'new.txt']
path_finder.include('my*').list() # ['my_new.txt', 'my.txt']
path_finder.exclude('*new*').list() # ['my.txt']
```

#### Arguments

- `root` - Path to root folder.
- `glob_expr` - `glob` expression to lookup in `root`
