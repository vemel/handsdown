# Cli Parser

> Auto-generated documentation for [handsdown.cli_parser](https://github.com/vemel/handsdown/blob/main/handsdown/cli_parser.py) module.

CLI Parser.

- [Handsdown](../README.md#-handsdown---python-documentation-generator) / [Modules](../MODULES.md#modules) / [Handsdown](index.md#handsdown) / Cli Parser
    - [CLINamespace](#clinamespace)
        - [CLINamespace().get_source_code_url](#clinamespaceget_source_code_url)
    - [abs_path](#abs_path)
    - [dir_abs_path](#dir_abs_path)
    - [existing_dir_abs_path](#existing_dir_abs_path)
    - [git_repo](#git_repo)
    - [parse_args](#parse_args)

## CLINamespace

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/cli_parser.py#L16)

```python
class CLINamespace():
    def __init__(
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
```

Main CLI Namespace.

### CLINamespace().get_source_code_url

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/cli_parser.py#L53)

```python
def get_source_code_url() -> str:
```

Get URL to source code.

#### Returns

URL as a string.

## abs_path

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/cli_parser.py#L102)

```python
def abs_path(path_str: str) -> Path:
```

Validate `path_str` and make it absolute.

#### Arguments

- `path_str` - A path to check.

#### Returns

An absolute path.

## dir_abs_path

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/cli_parser.py#L115)

```python
def dir_abs_path(path_str: str) -> Path:
```

Validate directory `path_str` and make it absolute.

#### Arguments

- `path_str` - A path to check.

#### Returns

An absolute path.

#### Raises

- `argparse.ArgumentTypeError` - If path is not a directory.

## existing_dir_abs_path

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/cli_parser.py#L134)

```python
def existing_dir_abs_path(path_str: str) -> Path:
```

Validate existing directory `path_str` and make it absolute.

#### Arguments

- `path_str` - A path to check.

#### Returns

An absolute path.

#### Raises

- `argparse.ArgumentTypeError` - If path does not exist or is not a directory.

## git_repo

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/cli_parser.py#L74)

```python
def git_repo(git_repo_url: str) -> str:
```

Validate `git_repo_url` to be a GitHub repo and converts SSH urls to HTTPS.

#### Arguments

- `git_repo_url` - GitHub URL or `remote.origin.url`

#### Returns

A GitHub URL.

## parse_args

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/cli_parser.py#L155)

```python
def parse_args(args: Iterable[str]) -> CLINamespace:
```

Get CLI arguments parser.

#### Returns

An `argparse.ArgumentParser` instance.

#### See also

- [CLINamespace](#clinamespace)
