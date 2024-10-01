# Cli Parser

CLI Parser.

[Handsdown API Index](../README.md#handsdown-api-index) / [Handsdown](./index.md#handsdown) / Cli Parser

> Auto-generated documentation for [handsdown.cli_parser](https://github.com/vemel/handsdown/blob/main/handsdown/cli_parser.py) module.

## CLINamespace

[Show source in cli_parser.py:22](https://github.com/vemel/handsdown/blob/main/handsdown/cli_parser.py#L22)

Main CLI Namespace.

#### Signature

```python
class CLINamespace:
    ...
```

### CLINamespace().get_source_code_url

[Show source in cli_parser.py:44](https://github.com/vemel/handsdown/blob/main/handsdown/cli_parser.py#L44)

Get URL to source code.

#### Returns

URL as a string.

#### Signature

```python
def get_source_code_url(self) -> str:
    ...
```



## abs_path

[Show source in cli_parser.py:93](https://github.com/vemel/handsdown/blob/main/handsdown/cli_parser.py#L93)

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

[Show source in cli_parser.py:106](https://github.com/vemel/handsdown/blob/main/handsdown/cli_parser.py#L106)

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

[Show source in cli_parser.py:125](https://github.com/vemel/handsdown/blob/main/handsdown/cli_parser.py#L125)

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

[Show source in cli_parser.py:65](https://github.com/vemel/handsdown/blob/main/handsdown/cli_parser.py#L65)

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

[Show source in cli_parser.py:164](https://github.com/vemel/handsdown/blob/main/handsdown/cli_parser.py#L164)

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

[Show source in cli_parser.py:146](https://github.com/vemel/handsdown/blob/main/handsdown/cli_parser.py#L146)

Cast theme name to `Theme`.

#### Signature

```python
def parse_theme(name: str) -> Theme:
    ...
```

#### See also

- [Theme](./constants.md#theme)
