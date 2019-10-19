# CLI Parser

> Auto-generated documentation for [cli_parser](../cli_parser.py) module.

- [Index](README.md#modules) / CLI Parser
  - [abs_path](#abs_path)
  - [dir_abs_path](#dir_abs_path)
  - [existing_dir_abs_path](#existing_dir_abs_path)
  - [get_cli_parser](#get_cli_parser)
  - [git_repo](#git_repo)

## abs_path

[🔍 find in source code](../cli_parser.py#L36)

```python
def abs_path(path_str: Text) -> Path
```

Validate `path_str` and make it absolute.

#### Returns

An absolute path.

#### Arguments

path - A path to check.

## dir_abs_path

[🔍 find in source code](../cli_parser.py#L50)

```python
def dir_abs_path(path_str: Text) -> Path
```

Validate directory `path_str` and make it absolute.

#### Returns

An absolute path.

#### Arguments

path - A path to check.

#### Raises

- `argparse.ArgumentTypeError` - If path is not a directory.

## existing_dir_abs_path

[🔍 find in source code](../cli_parser.py#L70)

```python
def existing_dir_abs_path(path_str: Text) -> Path
```

Validate existing directory `path_str` and make it absolute.

#### Returns

An absolute path.

#### Arguments

path - A path to check.

#### Raises

- `argparse.ArgumentTypeError` - If path does not exist or is not a directory.

## get_cli_parser

[🔍 find in source code](../cli_parser.py#L92)

```python
def get_cli_parser() -> argparse.ArgumentParser
```

Get CLI arguments parser.

#### Returns

An `argparse.ArgumentParser` instance.

## git_repo

[🔍 find in source code](../cli_parser.py#L15)

```python
def git_repo(git_repo_url: Text) -> Text
```

Validate `git_repo_url` to be a GitHub repo and converts SSH urls to HTTPS.

#### Returns

A GitHub URL.

#### Arguments

git_repo_url - GitHub URL or `remote.origin.url`
