# CLI Parser

> Auto-generated documentation for [handsdown.cli_parser](../../handsdown/cli_parser.py) module.

- [Index](../README.md#handsdown-index) / [Handsdown](index.md#handsdown) / [CLI Parser](#cli-parser) / CLI Parser
  - [abs_path](#abs_path)
  - [dir_abs_path](#dir_abs_path)
  - [existing_dir_abs_path](#existing_dir_abs_path)
  - [get_cli_parser](#get_cli_parser)

## abs_path

[🔍 find in source code](../../handsdown/cli_parser.py#l9)

```python
def abs_path(path: str) -> pathlib.Path
```

Validate path and make it absolute.

#### Arguments

path - A path to check.

#### Returns

An absolute path.

## dir_abs_path

[🔍 find in source code](../../handsdown/cli_parser.py#l22)

```python
def dir_abs_path(path: str) -> pathlib.Path
```

Validate directory path and make it absolute.

#### Arguments

path - A path to check.

#### Returns

An absolute path.

#### Raises

- `argparse.ArgumentTypeError` - If path is not a directory.

## existing_dir_abs_path

[🔍 find in source code](../../handsdown/cli_parser.py#l41)

```python
def existing_dir_abs_path(path: str) -> pathlib.Path
```

Validate existing directory path and make it absolute.

#### Arguments

path - A path to check.

#### Returns

An absolute path.

#### Raises

- `argparse.ArgumentTypeError` - If path does not exist or is not a directory.

## get_cli_parser

[🔍 find in source code](../../handsdown/cli_parser.py#l62)

```python
def get_cli_parser() -> argparse.ArgumentParser
```

Get CLI arguments parser.

#### Returns

An `argparse.ArgumentParser` instance.
