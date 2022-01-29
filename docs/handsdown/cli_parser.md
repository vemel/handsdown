# Cli Parser

> Auto-generated documentation for [handsdown.cli_parser](https://github.com/vemel/handsdown/blob/master/handsdown/cli_parser.py) module.

CLI Parser.

- [Handsdown](../README.md#-handsdown---python-documentation-generator) / [Modules](../MODULES.md#modules) / [Handsdown](index.md#handsdown) / Cli Parser
    - [CLINamespace](#clinamespace)
    - [abs_path](#abs_path)
    - [dir_abs_path](#dir_abs_path)
    - [existing_dir_abs_path](#existing_dir_abs_path)
    - [git_repo](#git_repo)
    - [parse_args](#parse_args)

## CLINamespace

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/cli_parser.py#L15)

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
        branch: str,
        project_name: str,
        files: Iterable[Path],
        cleanup: bool,
        encoding: str,
    ) -> None:
```

Main CLI Namespace.

## abs_path

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/cli_parser.py#L79)

```python
def abs_path(path_str: str) -> Path:
```

Validate `path_str` and make it absolute.

#### Arguments

- `path_str` - A path to check.

#### Returns

An absolute path.

## dir_abs_path

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/cli_parser.py#L92)

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

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/cli_parser.py#L111)

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

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/cli_parser.py#L51)

```python
def git_repo(git_repo_url: str) -> str:
```

Validate `git_repo_url` to be a GitHub repo and converts SSH urls to HTTPS.

#### Arguments

- `git_repo_url` - GitHub URL or `remote.origin.url`

#### Returns

A GitHub URL.

## parse_args

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/cli_parser.py#L132)

```python
def parse_args(args: Iterable[str]) -> CLINamespace:
```

Get CLI arguments parser.

#### Returns

An `argparse.ArgumentParser` instance.

#### See also

- [CLINamespace](#clinamespace)
