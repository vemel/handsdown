# Cli Parser

[Handsdown API Index](../README.md#handsdown-api-index) /
[Handsdown](./index.md#handsdown) /
Cli Parser

> Auto-generated documentation for [handsdown.cli_parser](https://github.com/vemel/handsdown/blob/main/handsdown/cli_parser.py) module.

## CLINamespace

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/cli_parser.py#L18)

Main CLI Namespace.

#### Signature

```python
class CLINamespace:
    ...
```

### CLINamespace().get_source_code_url

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/cli_parser.py#L41)

Get URL to source code.

#### Returns

URL as a string.

#### Signature

```python
def get_source_code_url(self) -> str:
    ...
```



## abs_path

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/cli_parser.py#L90)

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

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/cli_parser.py#L103)

Validate directory `path_str` and make it absolute.

#### Arguments

- `path_str` - A path to check.

#### Returns

An absolute path.

#### Raises

- `argparse.ArgumentTypeError` - If path is not a directory.

#### Signature

```python
def dir_abs_path(path_str: str) -> NicePath:
    ...
```

#### See also

- [NicePath](utils/nice_path.md#nicepath)



## existing_dir_abs_path

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/cli_parser.py#L122)

Validate existing directory `path_str` and make it absolute.

#### Arguments

- `path_str` - A path to check.

#### Returns

An absolute path.

#### Raises

- `argparse.ArgumentTypeError` - If path does not exist or is not a directory.

#### Signature

```python
def existing_dir_abs_path(path_str: str) -> NicePath:
    ...
```

#### See also

- [NicePath](utils/nice_path.md#nicepath)



## git_repo

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/cli_parser.py#L62)

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

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/cli_parser.py#L154)

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



## parse_theme

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/cli_parser.py#L143)

Cast theme name to `Theme`.

#### Signature

```python
def parse_theme(name: str) -> Theme:
    ...
```

#### See also

- [Theme](./constants.md#theme)



