# Cli Parser

[Handsdown](../README.md#-handsdown---python-documentation-generator) / [Modules](../MODULES.md#modules) / [Handsdown](index.md#handsdown) / Cli Parser

> Auto-generated documentation for [handsdown.cli_parser](https://github.com/vemel/handsdown/blob/main/handsdown/cli_parser.py) module.

- [Cli Parser](#cli-parser)
  - [CLINamespace](#clinamespace)
    - [CLINamespace().get_source_code_url](#clinamespace()get_source_code_url)
  - [abs_path](#abs_path)
  - [dir_abs_path](#dir_abs_path)
  - [existing_dir_abs_path](#existing_dir_abs_path)
  - [git_repo](#git_repo)
  - [parse_args](#parse_args)

## CLINamespace

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/cli_parser.py#L16)

Main CLI Namespace.

#### Signature

```python
class CLINamespace:
    def __init__(
        self,
        panic: bool,
        input_path: Path,
        output_path: Path,
        toc_depth: int,
        log_level: int,
        include: Iterable[str],
        exclude: Iterable[str],
        source_code_url: str,
        source_code_path: Path,
        branch: str,
        project_name: str,
        files: Iterable[Path],
        cleanup: bool,
        encoding: str,
    ) -> None:
        ...
```

### CLINamespace().get_source_code_url

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/cli_parser.py#L53)

Get URL to source code.

#### Returns

URL as a string.

#### Signature

```python
def get_source_code_url(self) -> str:
    ...
```



## abs_path

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/cli_parser.py#L102)

Validate `path_str` and make it absolute.

#### Arguments

- `path_str` - A path to check.

#### Returns

An absolute path.

#### Signature

```python
def abs_path(path_str: str) -> Path:
    ...
```



## dir_abs_path

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/cli_parser.py#L115)

Validate directory `path_str` and make it absolute.

#### Arguments

- `path_str` - A path to check.

#### Returns

An absolute path.

#### Raises

- `argparse.ArgumentTypeError` - If path is not a directory.

#### Signature

```python
def dir_abs_path(path_str: str) -> Path:
    ...
```



## existing_dir_abs_path

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/cli_parser.py#L134)

Validate existing directory `path_str` and make it absolute.

#### Arguments

- `path_str` - A path to check.

#### Returns

An absolute path.

#### Raises

- `argparse.ArgumentTypeError` - If path does not exist or is not a directory.

#### Signature

```python
def existing_dir_abs_path(path_str: str) -> Path:
    ...
```



## git_repo

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/cli_parser.py#L74)

Validate `git_repo_url` to be a GitHub repo and converts SSH urls to HTTPS.

#### Arguments

- `git_repo_url` - GitHub URL or `remote.origin.url`

#### Returns

A GitHub URL.

#### Signature

```python
def git_repo(git_repo_url: str) -> str:
    ...
```



## parse_args

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/cli_parser.py#L155)

Get CLI arguments parser.

#### Returns

An `argparse.ArgumentParser` instance.

#### Signature

```python
def parse_args(args: Iterable[str]) -> CLINamespace:
    ...
```

#### See also

- [CLINamespace](#clinamespace)


