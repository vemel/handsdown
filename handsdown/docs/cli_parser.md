# Cli parser

- [Cli parser](#cli-parser)
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
  - [abs_path](#abs_path)
  - [get_cli_parser](#get_cli_parser)

> Auto-generated documentation for [cli_parser](../cli_parser.py) module.

## Path

[🔍 find in source code](../cli_parser.py#L986)

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

[🔍 find in source code](../cli_parser.py#L1118)

```python
def absolute()
```
Return an absolute version of this path.  This function works
        even if the path doesn't point to anything.

        No normalization is done, i.e. all '.' and '..' will be kept along.
        Use resolve() to get the canonical path to a file.
        

### Path().chmod

[🔍 find in source code](../cli_parser.py#L1263)

```python
def chmod(mode)
```
Change the permissions of the path, like os.chmod().

### Path.cwd

[🔍 find in source code](../cli_parser.py#L1052)

```python
def cwd()
```
Return a new path pointing to the current working directory
        (as returned by os.getcwd()).
        

### Path().exists

[🔍 find in source code](../cli_parser.py#L1334)

```python
def exists()
```
Whether this path exists.

### Path().expanduser

[🔍 find in source code](../cli_parser.py#L1458)

```python
def expanduser()
```
Return a new path with expanded ~ and ~user constructs
       (as returned by os.path.expanduser)
       

### Path().glob

[🔍 find in source code](../cli_parser.py#L1091)

```python
def glob(pattern)
```
Iterate over this subtree and yield all existing files (of any
        kind, including directories) matching the given relative pattern.
        

### Path().group

[🔍 find in source code](../cli_parser.py#L1170)

```python
def group()
```
Return the group name of the file gid.

### Path.home

[🔍 find in source code](../cli_parser.py#L1059)

```python
def home()
```
Return a new path pointing to the user's home directory (as
        returned by os.path.expanduser('~')).
        

### Path().is_block_device

[🔍 find in source code](../cli_parser.py#L1406)

```python
def is_block_device()
```
Whether this path is a block device.

### Path().is_char_device

[🔍 find in source code](../cli_parser.py#L1419)

```python
def is_char_device()
```
Whether this path is a character device.

### Path().is_dir

[🔍 find in source code](../cli_parser.py#L1346)

```python
def is_dir()
```
Whether this path is a directory.

### Path().is_fifo

[🔍 find in source code](../cli_parser.py#L1432)

```python
def is_fifo()
```
Whether this path is a FIFO.

### Path().is_file

[🔍 find in source code](../cli_parser.py#L1359)

```python
def is_file()
```
Whether this path is a regular file (also True for symlinks pointing
to regular files).

### Path().is_mount

[🔍 find in source code](../cli_parser.py#L1373)

```python
def is_mount()
```
Check if this path is a POSIX mount point

### Path().is_socket

[🔍 find in source code](../cli_parser.py#L1445)

```python
def is_socket()
```
Whether this path is a socket.

### Path().is_symlink

[🔍 find in source code](../cli_parser.py#L1394)

```python
def is_symlink()
```
Whether this path is a symbolic link.

### Path().iterdir

[🔍 find in source code](../cli_parser.py#L1077)

```python
def iterdir()
```
Iterate over the files in this directory.  Does not yield any
        result for the special paths '.' and '..'.
        

### Path().lchmod

[🔍 find in source code](../cli_parser.py#L1271)

```python
def lchmod(mode)
```
Like chmod(), except if the path points to a symlink, the symlink's
permissions are changed, rather than its target's.

### Path().lstat

[🔍 find in source code](../cli_parser.py#L1297)

```python
def lstat()
```
Like stat(), except if the path points to a symlink, the symlink's
status information is returned, rather than its target's.

### Path().mkdir

[🔍 find in source code](../cli_parser.py#L1244)

```python
def mkdir(mode=511, parents=False, exist_ok=False)
```
Create a new directory at this given path.

### Path().open

[🔍 find in source code](../cli_parser.py#L1177)

```python
def open(mode='r', buffering=-1, encoding=None, errors=None, newline=None)
```
Open the file pointed by this path and return a file object, as
the built-in open() function does.

### Path().owner

[🔍 find in source code](../cli_parser.py#L1163)

```python
def owner()
```
Return the login name of the file owner.

### Path().read_bytes

[🔍 find in source code](../cli_parser.py#L1188)

```python
def read_bytes()
```
Open the file in bytes mode, read it, and close the file.

### Path().read_text

[🔍 find in source code](../cli_parser.py#L1195)

```python
def read_text(encoding=None, errors=None)
```
Open the file in text mode, read it, and close the file.

### Path().rename

[🔍 find in source code](../cli_parser.py#L1306)

```python
def rename(target)
```
Rename this path to the given path.

### Path().replace

[🔍 find in source code](../cli_parser.py#L1314)

```python
def replace(target)
```
Rename this path to the given path, clobbering the existing
destination if it exists.

### Path().resolve

[🔍 find in source code](../cli_parser.py#L1136)

```python
def resolve(strict=False)
```
Make the path absolute, resolving all symlinks on the way and also
normalizing it (for example turning slashes into backslashes under
Windows).

### Path().rglob

[🔍 find in source code](../cli_parser.py#L1105)

```python
def rglob(pattern)
```
Recursively yield all existing files (of any kind, including
        directories) matching the given relative pattern, anywhere in
        this subtree.
        

### Path().rmdir

[🔍 find in source code](../cli_parser.py#L1289)

```python
def rmdir()
```
Remove this directory.  The directory must be empty.

### Path().samefile

[🔍 find in source code](../cli_parser.py#L1066)

```python
def samefile(other_path)
```
Return whether other_path is the same or not as this file
        (as returned by os.path.samefile()).
        

### Path().stat

[🔍 find in source code](../cli_parser.py#L1156)

```python
def stat()
```
Return the result of the stat() system call on this path, like
os.stat() does.

### Path().symlink_to

[🔍 find in source code](../cli_parser.py#L1323)

```python
def symlink_to(target, target_is_directory=False)
```
Make this path a symlink pointing to the given path.
Note the order of arguments (self, target) is the reverse of os.symlink's.

### Path().touch

[🔍 find in source code](../cli_parser.py#L1221)

```python
def touch(mode=438, exist_ok=True)
```
Create this file with the given access mode, if it doesn't exist.

### Path().unlink

[🔍 find in source code](../cli_parser.py#L1280)

```python
def unlink()
```
Remove this file or link.
If the path is a directory, use rmdir() instead.

### Path().write_bytes

[🔍 find in source code](../cli_parser.py#L1202)

```python
def write_bytes(data)
```
Open the file in bytes mode, write to it, and close the file.

### Path().write_text

[🔍 find in source code](../cli_parser.py#L1211)

```python
def write_text(data, encoding=None, errors=None)
```
Open the file in text mode, write to it, and close the file.

## abs_path

[🔍 find in source code](../cli_parser.py#L6)

```python
def abs_path(path: str) -> pathlib.Path
```
Make path absolute.

#### Arguments

path - A path to check.

#### Returns

An absolute path.

## get_cli_parser

[🔍 find in source code](../cli_parser.py#L19)

```python
def get_cli_parser() -> argparse.ArgumentParser
```
Get CLI arguments parser.

#### Returns

An `argparse.ArgumentParser` instance.
