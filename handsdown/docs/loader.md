# Loader

- [Loader](#loader)
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
  - [patch](#patch)
  - [SignatureBuilder](#signaturebuilder)
    - [SignatureBuilder().build](#signaturebuilderbuild)
  - [IndentTrimmer](#indenttrimmer)
    - [IndentTrimmer.get_line_indent](#indenttrimmerget_line_indent)
    - [IndentTrimmer.trim_line](#indenttrimmertrim_line)
    - [IndentTrimmer.trim_lines](#indenttrimmertrim_lines)
    - [IndentTrimmer.trim_text](#indenttrimmertrim_text)
  - [OSEnvironMock](#osenvironmock)
  - [LoaderError](#loadererror)
  - [Loader](#loader)
    - [Loader().get_module_objects](#loaderget_module_objects)
    - [Loader.get_object_docstring](#loaderget_object_docstring)
    - [Loader.get_object_signature](#loaderget_object_signature)
    - [Loader.get_source_line_number](#loaderget_source_line_number)
    - [Loader().import_module](#loaderimport_module)

> Auto-generated documentation for [loader](../loader.py) module.

## Path

[🔍 find in source code](../loader.py#L986)

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

[🔍 find in source code](../loader.py#L1118)

```python
def absolute()
```
Return an absolute version of this path.  This function works
        even if the path doesn't point to anything.

        No normalization is done, i.e. all '.' and '..' will be kept along.
        Use resolve() to get the canonical path to a file.
        

### Path().chmod

[🔍 find in source code](../loader.py#L1263)

```python
def chmod(mode)
```
Change the permissions of the path, like os.chmod().

### Path.cwd

[🔍 find in source code](../loader.py#L1052)

```python
def cwd()
```
Return a new path pointing to the current working directory
        (as returned by os.getcwd()).
        

### Path().exists

[🔍 find in source code](../loader.py#L1334)

```python
def exists()
```
Whether this path exists.

### Path().expanduser

[🔍 find in source code](../loader.py#L1458)

```python
def expanduser()
```
Return a new path with expanded ~ and ~user constructs
       (as returned by os.path.expanduser)
       

### Path().glob

[🔍 find in source code](../loader.py#L1091)

```python
def glob(pattern)
```
Iterate over this subtree and yield all existing files (of any
        kind, including directories) matching the given relative pattern.
        

### Path().group

[🔍 find in source code](../loader.py#L1170)

```python
def group()
```
Return the group name of the file gid.

### Path.home

[🔍 find in source code](../loader.py#L1059)

```python
def home()
```
Return a new path pointing to the user's home directory (as
        returned by os.path.expanduser('~')).
        

### Path().is_block_device

[🔍 find in source code](../loader.py#L1406)

```python
def is_block_device()
```
Whether this path is a block device.

### Path().is_char_device

[🔍 find in source code](../loader.py#L1419)

```python
def is_char_device()
```
Whether this path is a character device.

### Path().is_dir

[🔍 find in source code](../loader.py#L1346)

```python
def is_dir()
```
Whether this path is a directory.

### Path().is_fifo

[🔍 find in source code](../loader.py#L1432)

```python
def is_fifo()
```
Whether this path is a FIFO.

### Path().is_file

[🔍 find in source code](../loader.py#L1359)

```python
def is_file()
```
Whether this path is a regular file (also True for symlinks pointing
to regular files).

### Path().is_mount

[🔍 find in source code](../loader.py#L1373)

```python
def is_mount()
```
Check if this path is a POSIX mount point

### Path().is_socket

[🔍 find in source code](../loader.py#L1445)

```python
def is_socket()
```
Whether this path is a socket.

### Path().is_symlink

[🔍 find in source code](../loader.py#L1394)

```python
def is_symlink()
```
Whether this path is a symbolic link.

### Path().iterdir

[🔍 find in source code](../loader.py#L1077)

```python
def iterdir()
```
Iterate over the files in this directory.  Does not yield any
        result for the special paths '.' and '..'.
        

### Path().lchmod

[🔍 find in source code](../loader.py#L1271)

```python
def lchmod(mode)
```
Like chmod(), except if the path points to a symlink, the symlink's
permissions are changed, rather than its target's.

### Path().lstat

[🔍 find in source code](../loader.py#L1297)

```python
def lstat()
```
Like stat(), except if the path points to a symlink, the symlink's
status information is returned, rather than its target's.

### Path().mkdir

[🔍 find in source code](../loader.py#L1244)

```python
def mkdir(mode=511, parents=False, exist_ok=False)
```
Create a new directory at this given path.

### Path().open

[🔍 find in source code](../loader.py#L1177)

```python
def open(mode='r', buffering=-1, encoding=None, errors=None, newline=None)
```
Open the file pointed by this path and return a file object, as
the built-in open() function does.

### Path().owner

[🔍 find in source code](../loader.py#L1163)

```python
def owner()
```
Return the login name of the file owner.

### Path().read_bytes

[🔍 find in source code](../loader.py#L1188)

```python
def read_bytes()
```
Open the file in bytes mode, read it, and close the file.

### Path().read_text

[🔍 find in source code](../loader.py#L1195)

```python
def read_text(encoding=None, errors=None)
```
Open the file in text mode, read it, and close the file.

### Path().rename

[🔍 find in source code](../loader.py#L1306)

```python
def rename(target)
```
Rename this path to the given path.

### Path().replace

[🔍 find in source code](../loader.py#L1314)

```python
def replace(target)
```
Rename this path to the given path, clobbering the existing
destination if it exists.

### Path().resolve

[🔍 find in source code](../loader.py#L1136)

```python
def resolve(strict=False)
```
Make the path absolute, resolving all symlinks on the way and also
normalizing it (for example turning slashes into backslashes under
Windows).

### Path().rglob

[🔍 find in source code](../loader.py#L1105)

```python
def rglob(pattern)
```
Recursively yield all existing files (of any kind, including
        directories) matching the given relative pattern, anywhere in
        this subtree.
        

### Path().rmdir

[🔍 find in source code](../loader.py#L1289)

```python
def rmdir()
```
Remove this directory.  The directory must be empty.

### Path().samefile

[🔍 find in source code](../loader.py#L1066)

```python
def samefile(other_path)
```
Return whether other_path is the same or not as this file
        (as returned by os.path.samefile()).
        

### Path().stat

[🔍 find in source code](../loader.py#L1156)

```python
def stat()
```
Return the result of the stat() system call on this path, like
os.stat() does.

### Path().symlink_to

[🔍 find in source code](../loader.py#L1323)

```python
def symlink_to(target, target_is_directory=False)
```
Make this path a symlink pointing to the given path.
Note the order of arguments (self, target) is the reverse of os.symlink's.

### Path().touch

[🔍 find in source code](../loader.py#L1221)

```python
def touch(mode=438, exist_ok=True)
```
Create this file with the given access mode, if it doesn't exist.

### Path().unlink

[🔍 find in source code](../loader.py#L1280)

```python
def unlink()
```
Remove this file or link.
If the path is a directory, use rmdir() instead.

### Path().write_bytes

[🔍 find in source code](../loader.py#L1202)

```python
def write_bytes(data)
```
Open the file in bytes mode, write to it, and close the file.

### Path().write_text

[🔍 find in source code](../loader.py#L1211)

```python
def write_text(data, encoding=None, errors=None)
```
Open the file in text mode, write to it, and close the file.

## patch

[🔍 find in source code](../loader.py#L1500)

```python
def patch(
    target,
    new=sentinel.DEFAULT,
    spec=None,
    create=False,
    spec_set=None,
    autospec=None,
    new_callable=None,
    **kwargs,
)
```
`patch` acts as a function decorator, class decorator or a context
manager. Inside the body of the function or with statement, the `target`
is patched with a `new` object. When the function/with statement exits
the patch is undone.

If `new` is omitted, then the target is replaced with a
`MagicMock`. If `patch` is used as a decorator and `new` is
omitted, the created mock is passed in as an extra argument to the
decorated function. If `patch` is used as a context manager the created
mock is returned by the context manager.

`target` should be a string in the form `'package.module.ClassName'`. The
`target` is imported and the specified object replaced with the `new`
object, so the `target` must be importable from the environment you are
calling `patch` from. The target is imported when the decorated function
is executed, not at decoration time.

The `spec` and `spec_set` keyword arguments are passed to the `MagicMock`
if patch is creating one for you.

In addition you can pass `spec=True` or `spec_set=True`, which causes
patch to pass in the object being mocked as the spec/spec_set object.

`new_callable` allows you to specify a different class, or callable object,
that will be called to create the `new` object. By default `MagicMock` is
used.

A more powerful form of `spec` is `autospec`. If you set `autospec=True`
then the mock will be created with a spec from the object being replaced.
All attributes of the mock will also have the spec of the corresponding
attribute of the object being replaced. Methods and functions being
mocked will have their arguments checked and will raise a `TypeError` if
they are called with the wrong signature. For mocks replacing a class,
their return value (the 'instance') will have the same spec as the class.

Instead of `autospec=True` you can pass `autospec=some_object` to use an
arbitrary object as the spec instead of the one being replaced.

By default `patch` will fail to replace attributes that don't exist. If
you pass in `create=True`, and the attribute doesn't exist, patch will
create the attribute for you when the patched function is called, and
delete it again afterwards. This is useful for writing tests against
attributes that your production code creates at runtime. It is off by
default because it can be dangerous. With it switched on you can write
passing tests against APIs that don't actually exist!

Patch can be used as a `TestCase` class decorator. It works by
decorating each test method in the class. This reduces the boilerplate
code when your test methods share a common patchings set. `patch` finds
tests by looking for method names that start with `patch.TEST_PREFIX`.
By default this is `test`, which matches the way `unittest` finds tests.
You can specify an alternative prefix by setting `patch.TEST_PREFIX`.

Patch can be used as a context manager, with the with statement. Here the
patching applies to the indented block after the with statement. If you
use "as" then the patched object will be bound to the name after the
"as"; very useful if `patch` is creating a mock object for you.

`patch` takes arbitrary keyword arguments. These will be passed to
the `Mock` (or `new_callable`) on construction.

`patch.dict(...)`, `patch.multiple(...)` and `patch.object(...)` are
available for alternate use-cases.

## SignatureBuilder

[🔍 find in source code](../loader.py#L78)

```python
class SignatureBuilder(obj: Any)
```
Renderer for object signature. Support lazy type annotations and tries
to beautify result by splitting lines.

#### Arguments

- `obj` - Object to inspect.

### SignatureBuilder().build

[🔍 find in source code](../loader.py#L134)

```python
def build() -> str
```
Render signature to string.

#### Returns

A string with functions signature.

## IndentTrimmer

[🔍 find in source code](../loader.py#L4)

```python
class IndentTrimmer(*args, **kwargs)
```
Utility class for removing indentation for sections and lines.

### IndentTrimmer.get_line_indent

[🔍 find in source code](../loader.py#L87)

```python
def get_line_indent(line: str) -> int
```
Get indent length of the line.

#### Examples


```python
IndentTrimmer.get_line_indent('   test') # 3
IndentTrimmer.get_line_indent('test') # 0
```

#### Arguments

- `line` - Line of text.

#### Returns

A number of indentation characters in a beginning of the line.

### IndentTrimmer.trim_line

[🔍 find in source code](../loader.py#L63)

```python
def trim_line(line: str, indent: int) -> str
```
Trim indent from line if it is empty.

#### Examples


```python
IndentTrimmer.trim_line('     test', 2) # '   test'
IndentTrimmer.trim_line('     test', 6) # 'test'
IndentTrimmer.trim_line('     test', 1) # '    test'
```

#### Arguments

- `line` - A line of text.

#### Returns

A line with removed indent.

### IndentTrimmer.trim_lines

[🔍 find in source code](../loader.py#L30)

```python
def trim_lines(lines: Iterable[str]) -> List[str]
```
Trim minimum indent from each line of text.

#### Examples


```python
IndentTrimmer.trim_lines([
    '  asd',
    ' asd',
    '   asd',
)
# [
#     ' asd',
#     'asd',
#     '  asd',
# ]
```

#### Arguments

- `lines` - List of lines.

#### Returns

A list of lines with trimmed indent.

### IndentTrimmer.trim_text

[🔍 find in source code](../loader.py#L9)

```python
def trim_text(text: str) -> str
```
Trim minimum indent from each line of text.

#### Examples


```python
IndentTrimmer.trim_text('  asd\n asd\n   asd\n')
# ' asd\nasd\n  asd\n'
```

#### Arguments

- `text` - Multiline text.

#### Returns

A text with trimmed indent.

## OSEnvironMock

[🔍 find in source code](../loader.py#L10)

```python
class OSEnvironMock(*args, **kwargs)
```
## LoaderError

[🔍 find in source code](../loader.py#L17)

```python
class LoaderError(*args, **kwargs)
```
## Loader

[🔍 find in source code](../loader.py#L21)

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

[🔍 find in source code](../loader.py#L136)

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

[🔍 find in source code](../loader.py#L57)

```python
def get_object_docstring(obj: Any) -> str
```
Get trimmed object docstring or an empty string.

#### Arguments

- `obj` - Object to inspect.

#### Returns

A string with object docsting.

### Loader.get_object_signature

[🔍 find in source code](../loader.py#L40)

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

[🔍 find in source code](../loader.py#L187)

```python
def get_source_line_number(obj: Any) -> int
```
Get line number in source file where `obj` is declared.

- `obj` - Object to inspect.

#### Returns

A line number.

### Loader().import_module

[🔍 find in source code](../loader.py#L70)

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
