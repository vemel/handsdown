# CLI Parser

> Auto-generated documentation for [handsdown.cli_parser](https://github.com/vemel/handsdown/blob/master/handsdown/cli_parser.py) module.

- [Handsdown](../README.md#-handsdown---python-documentation-generator) / [Modules](../MODULES.md#modules) / [Handsdown](index.md#handsdown) / CLI Parser
    - [abs_path](#abs_path)
    - [dir_abs_path](#dir_abs_path)
    - [existing_dir_abs_path](#existing_dir_abs_path)
    - [git_repo](#git_repo)
    - [parse_args](#parse_args)

## abs_path

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/cli_parser.py#L38)

```python
def abs_path(path_str: Text) -> Path:
```

Validate `path_str` and make it absolute.

#### Arguments

- `path_str` - A path to check.

#### Returns

An absolute path.

## dir_abs_path

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/cli_parser.py#L52)

```python
def dir_abs_path(path_str: Text) -> Path:
```

Validate directory `path_str` and make it absolute.

#### Arguments

- `path_str` - A path to check.

#### Returns

An absolute path.

#### Raises

- `argparse.ArgumentTypeError` - If path is not a directory.

## existing_dir_abs_path

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/cli_parser.py#L72)

```python
def existing_dir_abs_path(path_str: Text) -> Path:
```

Validate existing directory `path_str` and make it absolute.

#### Arguments

- `path_str` - A path to check.

#### Returns

An absolute path.

#### Raises

- `argparse.ArgumentTypeError` - If path does not exist or is not a directory.

## git_repo

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/cli_parser.py#L11)

```python
def git_repo(git_repo_url: Text) -> Text:
```

Validate `git_repo_url` to be a GitHub repo and converts SSH urls to HTTPS.

#### Arguments

- `git_repo_url` - GitHub URL or `remote.origin.url`

#### Returns

A GitHub URL.

## parse_args

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/cli_parser.py#L94)

```python
def parse_args(args: List[Text]) -> argparse.Namespace:
```

Get CLI arguments parser.

#### Returns

An `argparse.ArgumentParser` instance.
