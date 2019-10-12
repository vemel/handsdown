# Generator

- [Generator](#generator)
  - [Path](#path)
    - [Path().absolute](#pathabsolute)
    - [Path().chmod](#pathchmod)
    - [Path.cwd](#pathcwd)
    - [Path().exists](#pathexists)
    - [Path().expanduser](#pathexpanduser)
    - [Path().glob](#pathglob)
    - [Path().group](#pathgroup)
    - [Path.home](#pathhome)
    - [Path().is_block_device](#pathis_block_device)
    - [Path().is_char_device](#pathis_char_device)
    - [Path().is_dir](#pathis_dir)
    - [Path().is_fifo](#pathis_fifo)
    - [Path().is_file](#pathis_file)
    - [Path().is_mount](#pathis_mount)
    - [Path().is_socket](#pathis_socket)
    - [Path().is_symlink](#pathis_symlink)
    - [Path().iterdir](#pathiterdir)
    - [Path().lchmod](#pathlchmod)
    - [Path().lstat](#pathlstat)
    - [Path().mkdir](#pathmkdir)
    - [Path().open](#pathopen)
    - [Path().owner](#pathowner)
    - [Path().read_bytes](#pathread_bytes)
    - [Path().read_text](#pathread_text)
    - [Path().rename](#pathrename)
    - [Path().replace](#pathreplace)
    - [Path().resolve](#pathresolve)
    - [Path().rglob](#pathrglob)
    - [Path().rmdir](#pathrmdir)
    - [Path().samefile](#pathsamefile)
    - [Path().stat](#pathstat)
    - [Path().symlink_to](#pathsymlink_to)
    - [Path().touch](#pathtouch)
    - [Path().unlink](#pathunlink)
    - [Path().write_bytes](#pathwrite_bytes)
    - [Path().write_text](#pathwrite_text)
  - [Loader](#loader)
    - [Loader().get_module_objects](#loaderget_module_objects)
    - [Loader.get_object_docstring](#loaderget_object_docstring)
    - [Loader.get_object_signature](#loaderget_object_signature)
    - [Loader.get_source_line_number](#loaderget_source_line_number)
    - [Loader().import_module](#loaderimport_module)
  - [LoaderError](#loadererror)
  - [SmartDocstringProcessor](#smartdocstringprocessor)
    - [SmartDocstringProcessor().build_sections](#smartdocstringprocessorbuild_sections)
  - [BaseDocstringProcessor](#basedocstringprocessor)
    - [BaseDocstringProcessor().build_sections](#basedocstringprocessorbuild_sections)
    - [BaseDocstringProcessor().render_sections](#basedocstringprocessorrender_sections)
  - [get_anchor_link](#get_anchor_link)
  - [generate_toc_lines](#generate_toc_lines)
  - [GeneratorError](#generatorerror)
  - [Generator](#generator)
    - [Generator().cleanup_old_docs](#generatorcleanup_old_docs)
    - [Generator().generate](#generatorgenerate)
    - [Generator().generate_doc](#generatorgenerate_doc)
    - [Generator().replace_links](#generatorreplace_links)

> Auto-generated documentation for [generator](../generator.py) module.

## Path

[🔍 find in source code](../generator.py#L986)

```python
class Path(*args, **kwargs)
```
PurePath subclass that can make system calls.

    Path represents a filesystem path but unlike PurePath, also offers
    methods to do system calls on path objects. Depending on your system,
    instantiating a Path will return either a PosixPath or a WindowsPath
    object. You can also instantiate a PosixPath or WindowsPath directly,
    but cannot instantiate a WindowsPath on a POSIX system or vice versa.
    

### Path().absolute

[🔍 find in source code](../generator.py#L1118)

```python
def absolute()
```
Return an absolute version of this path.  This function works
        even if the path doesn't point to anything.

        No normalization is done, i.e. all '.' and '..' will be kept along.
        Use resolve() to get the canonical path to a file.
        

### Path().chmod

[🔍 find in source code](../generator.py#L1263)

```python
def chmod(mode)
```
Change the permissions of the path, like os.chmod().

### Path.cwd

[🔍 find in source code](../generator.py#L1052)

```python
def cwd()
```
Return a new path pointing to the current working directory
        (as returned by os.getcwd()).
        

### Path().exists

[🔍 find in source code](../generator.py#L1334)

```python
def exists()
```
Whether this path exists.

### Path().expanduser

[🔍 find in source code](../generator.py#L1458)

```python
def expanduser()
```
Return a new path with expanded ~ and ~user constructs
       (as returned by os.path.expanduser)
       

### Path().glob

[🔍 find in source code](../generator.py#L1091)

```python
def glob(pattern)
```
Iterate over this subtree and yield all existing files (of any
        kind, including directories) matching the given relative pattern.
        

### Path().group

[🔍 find in source code](../generator.py#L1170)

```python
def group()
```
Return the group name of the file gid.

### Path.home

[🔍 find in source code](../generator.py#L1059)

```python
def home()
```
Return a new path pointing to the user's home directory (as
        returned by os.path.expanduser('~')).
        

### Path().is_block_device

[🔍 find in source code](../generator.py#L1406)

```python
def is_block_device()
```
Whether this path is a block device.

### Path().is_char_device

[🔍 find in source code](../generator.py#L1419)

```python
def is_char_device()
```
Whether this path is a character device.

### Path().is_dir

[🔍 find in source code](../generator.py#L1346)

```python
def is_dir()
```
Whether this path is a directory.

### Path().is_fifo

[🔍 find in source code](../generator.py#L1432)

```python
def is_fifo()
```
Whether this path is a FIFO.

### Path().is_file

[🔍 find in source code](../generator.py#L1359)

```python
def is_file()
```
Whether this path is a regular file (also True for symlinks pointing
to regular files).

### Path().is_mount

[🔍 find in source code](../generator.py#L1373)

```python
def is_mount()
```
Check if this path is a POSIX mount point

### Path().is_socket

[🔍 find in source code](../generator.py#L1445)

```python
def is_socket()
```
Whether this path is a socket.

### Path().is_symlink

[🔍 find in source code](../generator.py#L1394)

```python
def is_symlink()
```
Whether this path is a symbolic link.

### Path().iterdir

[🔍 find in source code](../generator.py#L1077)

```python
def iterdir()
```
Iterate over the files in this directory.  Does not yield any
        result for the special paths '.' and '..'.
        

### Path().lchmod

[🔍 find in source code](../generator.py#L1271)

```python
def lchmod(mode)
```
Like chmod(), except if the path points to a symlink, the symlink's
permissions are changed, rather than its target's.

### Path().lstat

[🔍 find in source code](../generator.py#L1297)

```python
def lstat()
```
Like stat(), except if the path points to a symlink, the symlink's
status information is returned, rather than its target's.

### Path().mkdir

[🔍 find in source code](../generator.py#L1244)

```python
def mkdir(mode=511, parents=False, exist_ok=False)
```
Create a new directory at this given path.

### Path().open

[🔍 find in source code](../generator.py#L1177)

```python
def open(mode='r', buffering=-1, encoding=None, errors=None, newline=None)
```
Open the file pointed by this path and return a file object, as
the built-in open() function does.

### Path().owner

[🔍 find in source code](../generator.py#L1163)

```python
def owner()
```
Return the login name of the file owner.

### Path().read_bytes

[🔍 find in source code](../generator.py#L1188)

```python
def read_bytes()
```
Open the file in bytes mode, read it, and close the file.

### Path().read_text

[🔍 find in source code](../generator.py#L1195)

```python
def read_text(encoding=None, errors=None)
```
Open the file in text mode, read it, and close the file.

### Path().rename

[🔍 find in source code](../generator.py#L1306)

```python
def rename(target)
```
Rename this path to the given path.

### Path().replace

[🔍 find in source code](../generator.py#L1314)

```python
def replace(target)
```
Rename this path to the given path, clobbering the existing
destination if it exists.

### Path().resolve

[🔍 find in source code](../generator.py#L1136)

```python
def resolve(strict=False)
```
Make the path absolute, resolving all symlinks on the way and also
normalizing it (for example turning slashes into backslashes under
Windows).

### Path().rglob

[🔍 find in source code](../generator.py#L1105)

```python
def rglob(pattern)
```
Recursively yield all existing files (of any kind, including
        directories) matching the given relative pattern, anywhere in
        this subtree.
        

### Path().rmdir

[🔍 find in source code](../generator.py#L1289)

```python
def rmdir()
```
Remove this directory.  The directory must be empty.

### Path().samefile

[🔍 find in source code](../generator.py#L1066)

```python
def samefile(other_path)
```
Return whether other_path is the same or not as this file
        (as returned by os.path.samefile()).
        

### Path().stat

[🔍 find in source code](../generator.py#L1156)

```python
def stat()
```
Return the result of the stat() system call on this path, like
os.stat() does.

### Path().symlink_to

[🔍 find in source code](../generator.py#L1323)

```python
def symlink_to(target, target_is_directory=False)
```
Make this path a symlink pointing to the given path.
Note the order of arguments (self, target) is the reverse of os.symlink's.

### Path().touch

[🔍 find in source code](../generator.py#L1221)

```python
def touch(mode=438, exist_ok=True)
```
Create this file with the given access mode, if it doesn't exist.

### Path().unlink

[🔍 find in source code](../generator.py#L1280)

```python
def unlink()
```
Remove this file or link.
If the path is a directory, use rmdir() instead.

### Path().write_bytes

[🔍 find in source code](../generator.py#L1202)

```python
def write_bytes(data)
```
Open the file in bytes mode, write to it, and close the file.

### Path().write_text

[🔍 find in source code](../generator.py#L1211)

```python
def write_text(data, encoding=None, errors=None)
```
Open the file in text mode, write to it, and close the file.

## Loader

[🔍 find in source code](../generator.py#L21)

```python
class Loader(import_paths: Iterable[pathlib.Path]) -> None
```
Loader for python source code.

#### Examples


```python
loader = Loader(['path/to/my_module/'])
my_module_utils = loader.import_module('my_module.utils')
```

#### Arguments

- `import_paths` - List of import paths for `import_module` lookup.

### Loader().get_module_objects

[🔍 find in source code](../generator.py#L136)

```python
def get_module_objects(import_string: str) -> Generator[Tuple[str, Any, int], NoneType, NoneType]
```
Yield (`name`, `object`, `level`) for every object in a module. `name` is object name.
`object` - object iteslf. `level` - deepness of the object. Maximum `level` is 1.

#### Arguments

- `import_string` - Module import string.

#### Returns

A generator that yields tuples of (`name`, `object`, `level`).

### Loader.get_object_docstring

[🔍 find in source code](../generator.py#L57)

```python
def get_object_docstring(obj: Any) -> str
```
Get trimmed object docstring or an empty string.

#### Arguments

- `obj` - Object to inspect.

#### Returns

A string with object docsting.

### Loader.get_object_signature

[🔍 find in source code](../generator.py#L40)

```python
def get_object_signature(obj: Any) -> Union[str, NoneType]
```
Get class, method or function signature. If object is not callable -
returns None.

#### Arguments

- `obj` - Object to inspect.

#### Returns

A string with object signature or None.

### Loader.get_source_line_number

[🔍 find in source code](../generator.py#L187)

```python
def get_source_line_number(obj: Any) -> int
```
Get line number in source file where `obj` is declared.

- `obj` - Object to inspect.

#### Returns

A line number.

### Loader().import_module

[🔍 find in source code](../generator.py#L70)

```python
def import_module(import_string: str) -> Any
```
Import module using `import_paths` list. Clean up path afterwards.
Patch `os.environ` to avoid failing on undefined variables.
Set `typing.TYPE_CHECKING` to `True` while importing.

#### Arguments

- `import_string` - Module import string.

#### Returns

Imported module object.

## LoaderError

[🔍 find in source code](../generator.py#L17)

```python
class LoaderError(*args, **kwargs)
```
## SmartDocstringProcessor

[🔍 find in source code](../generator.py#L9)

```python
class SmartDocstringProcessor() -> None
```
This class implements the preprocessor for restructured text and google.

### SmartDocstringProcessor().build_sections

[🔍 find in source code](../generator.py#L22)

```python
def build_sections(content: str) -> DefaultDict[str, List[str]]
```
Preprocessors a given section into it's components.

## BaseDocstringProcessor

[🔍 find in source code](../generator.py#L9)

```python
class BaseDocstringProcessor() -> None
```
This class implements the preprocessor for PEP257 and Google style.

### BaseDocstringProcessor().build_sections

[🔍 find in source code](../generator.py#L47)

```python
def build_sections(content: str) -> DefaultDict[str, List[str]]
```
Parse docstring and split it to sections with arrays of strings.

#### Arguments

content - Object docstring.

#### Returns

A dictionary where key is a section name and value is a list of string sof this
section.

### BaseDocstringProcessor().render_sections

[🔍 find in source code](../generator.py#L74)

```python
def render_sections(sections: Dict[str, List[str]]) -> str
```
Render sections produced by `render_sections` to a string.

#### Arguments

sections - Built sections.

#### Returns

Markdown string.

## get_anchor_link

[🔍 find in source code](../generator.py#L15)

```python
def get_anchor_link(title: str) -> str
```
Convert title to Github-compatible anchor link.

#### Returns

A test of anchor link.

## generate_toc_lines

[🔍 find in source code](../generator.py#L27)

```python
def generate_toc_lines(content: str, max_depth: int = 3) -> List[str]
```
Generate Table of Contents for markdown text.

#### Arguments

- `content` - Markdown string.
- `max_depth` - Add headers to ToC only up to this level.

#### Returns

A list of ToC lines.

## GeneratorError

[🔍 find in source code](../generator.py#L12)

```python
class GeneratorError(*args, **kwargs)
```
## Generator

[🔍 find in source code](../generator.py#L16)

```python
class Generator(
    input_path: pathlib.Path,
    source_paths: Iterable[pathlib.Path],
    logger: Union[logging.Logger, NoneType] = None,
    docstring_processor: Union[handsdown.processors.base.BaseDocstringProcessor, NoneType] = None,
    loader: Union[handsdown.loader.Loader, NoneType] = None,
    output_path: Union[pathlib.Path, NoneType] = None,
)
```
Main doc generator.

#### Arguments

- `input_path` - Path to repo to generate docs.
- `logger` - Logger instance.
- `docstring_processor` - Docstring converter to Markdown.
- `loader` - Loader for python modules.
- `output_path` - Path to folder with auto-generated docs to output.

### Generator().cleanup_old_docs

[🔍 find in source code](../generator.py#L62)

```python
def cleanup_old_docs(preserve_paths: Iterable[pathlib.Path]) -> None
```
Remove old docs generated for this module.

#### Arguments

- `preserve_paths` - All doc files generated paths that should not be deleted.

### Generator().generate

[🔍 find in source code](../generator.py#L167)

```python
def generate() -> None
```
Generate all module docs at once.

### Generator().generate_doc

[🔍 find in source code](../generator.py#L109)

```python
def generate_doc(file_path: pathlib.Path) -> Union[pathlib.Path, NoneType]
```
Generate one module doc at once. If `file_path` has nothing to document - return `None`.

#### Arguments

- `file_path` - Path to source file.

#### Returns

A path to generated MD file or None.

### Generator().replace_links

[🔍 find in source code](../generator.py#L209)

```python
def replace_links(file_path: pathlib.Path) -> None
```
Replace all import strings with Markdown links. Only import strings that present in this
package are replaced, so not dead linsk should be generated.

```python
my_md = Path('doc.md')
my_md.write_text('I love `' + 'handsdown.indent_trimmer.IndentTrimmer.trim_lines` function!')
handsdown.replace_links(my_md)

my_md.read_text()
# 'I love [IndentTrimmer.trim_lines](./handsdown_indent_trimmer.md#indenttrimmertrim_lines) function!'
```

#### Arguments

- `file_path` - Path to MD document file.
