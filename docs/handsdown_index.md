# Handsdown

- [Handsdown](#handsdown)
  - [Generator](#generator)
    - [Generator().cleanup_old_docs](#generatorcleanup_old_docs)
    - [Generator().generate](#generatorgenerate)
    - [Generator().replace_links](#generatorreplace_links)
  - [PathFinder](#pathfinder)
    - [PathFinder().exclude](#pathfinderexclude)
    - [PathFinder().include](#pathfinderinclude)
    - [PathFinder().list](#pathfinderlist)
  - [LoaderError](#loadererror)

> Auto-generated documentation for [handsdown](../handsdown/__init__.py) module.


## Generator

[🔍 find in source code](../handsdown/__init__.py#L17)

```python
class Generator(
    input_path: pathlib.Path,
    source_paths: Iterable[pathlib.Path],
    logger: Union[logging.Logger, NoneType] = None,
    docstring_processor: Union[handsdown.processors.base.BaseDocstringProcessor, NoneType] = None,
    loader: Union[handsdown.loader.Loader, NoneType] = None,
    output_path: Union[pathlib.Path, NoneType] = None,
    raise_import_errors: bool = False,
)
```

Main doc generator.

#### Arguments

- `input_path` - Path to repo to generate docs.
- `logger` - Logger instance.
- `docstring_processor` - Docstring converter to Markdown.
- `loader` - Loader for python modules.
- `output_path` - Path to folder with auto-generated docs to output.

#### See also

- [BaseDocstringProcessor](./handsdown_processors_base.md#basedocstringprocessor)
- [Loader](./handsdown_loader.md#loader)

### Generator().cleanup_old_docs

[🔍 find in source code](../handsdown/__init__.py#L82)

```python
def cleanup_old_docs() -> None
```

Main doc generator.

#### Arguments

- `input_path` - Path to repo to generate docs.
- `logger` - Logger instance.
- `docstring_processor` - Docstring converter to Markdown.
- `loader` - Loader for python modules.
- `output_path` - Path to folder with auto-generated docs to output.

### Generator().generate

[🔍 find in source code](../handsdown/__init__.py#L133)

```python
def generate() -> None
```

Main doc generator.

#### Arguments

- `input_path` - Path to repo to generate docs.
- `logger` - Logger instance.
- `docstring_processor` - Docstring converter to Markdown.
- `loader` - Loader for python modules.
- `output_path` - Path to folder with auto-generated docs to output.

### Generator().replace_links

[🔍 find in source code](../handsdown/__init__.py#L172)

```python
def replace_links(file_path: pathlib.Path) -> None
```

Main doc generator.

#### Arguments

- `input_path` - Path to repo to generate docs.
- `logger` - Logger instance.
- `docstring_processor` - Docstring converter to Markdown.
- `loader` - Loader for python modules.
- `output_path` - Path to folder with auto-generated docs to output.

## PathFinder

[🔍 find in source code](../handsdown/__init__.py#L9)

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

[🔍 find in source code](../handsdown/__init__.py#L61)

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

- [PathFinder](./handsdown_path_finder.md#pathfinder)

### PathFinder().include

[🔍 find in source code](../handsdown/__init__.py#L41)

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

- [PathFinder](./handsdown_path_finder.md#pathfinder)

### PathFinder().list

[🔍 find in source code](../handsdown/__init__.py#L119)

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

## LoaderError

[🔍 find in source code](../handsdown/__init__.py#L18)

```python
class LoaderError(*args, **kwargs)
```

Main error for `Loader` class.
