# CLI Parser

- [CLI Parser](#cli-parser)
  - [abs_path](#abs_path)
  - [get_cli_parser](#get_cli_parser)

> Auto-generated documentation for [Handsdown](./README.md#modules) / `Cli Parser` module ([cli_parser.py](../handsdown/cli_parser.py))

## abs_path

[🔍 find in source code](../handsdown/cli_parser.py#L9)

```python
def abs_path(path: str) -> pathlib.Path
```

Make path absolute.

#### Arguments

path - A path to check.

#### Returns

An absolute path.

## get_cli_parser

[🔍 find in source code](../handsdown/cli_parser.py#L22)

```python
def get_cli_parser() -> argparse.ArgumentParser
```

Get CLI arguments parser.

#### Returns

An `argparse.ArgumentParser` instance.
