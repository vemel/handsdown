# CLI Parser

> Auto-generated documentation for [handsdown.cli_parser](../../handsdown/cli_parser.py) module.

- [Index](../README.md#handsdown-index) / [Handsdown](index.md#handsdown) / [CLI Parser](#cli-parser) / CLI Parser
  - [abs_path](#abs_path)
  - [dir_abs_path](#dir_abs_path)
  - [existing_dir_abs_path](#existing_dir_abs_path)
  - [get_cli_parser](#get_cli_parser)
  - [git_repo](#git_repo)

## abs_path

[🔍 find in source code](../../handsdown/cli_parser.py#L32)

```python
def abs_path(path_str: str) -> pathlib.Path
```

Validate `path_str` and make it absolute.

#### Arguments

path - A path to check.

#### Returns

An absolute path.

## dir_abs_path

[🔍 find in source code](../../handsdown/cli_parser.py#L45)

```python
def dir_abs_path(path_str: str) -> pathlib.Path
```

Validate directory `path_str` and make it absolute.

#### Arguments

path - A path to check.

#### Returns

An absolute path.

#### Raises

- `argparse.ArgumentTypeError` - If path is not a directory.

## existing_dir_abs_path

[🔍 find in source code](../../handsdown/cli_parser.py#L64)

```python
def existing_dir_abs_path(path_str: str) -> pathlib.Path
```

Validate existing directory `path_str` and make it absolute.

#### Arguments

path - A path to check.

#### Returns

An absolute path.

#### Raises

- `argparse.ArgumentTypeError` - If path does not exist or is not a directory.

## get_cli_parser

[🔍 find in source code](../../handsdown/cli_parser.py#L85)

```python
def get_cli_parser() -> argparse.ArgumentParser
```

Get CLI arguments parser.

#### Returns

An `argparse.ArgumentParser` instance.

## git_repo

[🔍 find in source code](../../handsdown/cli_parser.py#L13)

```python
def git_repo(git_repo_url: str) -> str
```

Validate `git_repo_url` to be a Github repo and converts SSH urls to HTTPS.

#### Arguments

git_repo_url - Github URL or `remote.origin.url`

#### Returns

A Github URL.
