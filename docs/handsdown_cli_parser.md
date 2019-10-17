# CLI Parser

> Auto-generated documentation for [handsdown.cli_parser](../handsdown/cli_parser.py) module.

- [Handsdown](README.md#handsdown) / [Handsdown](handsdown_index.md#handsdown) / CLI Parser
  - [abs_path](#abs_path)
  - [get_cli_parser](#get_cli_parser)

## abs_path

[🔍 find in source code](../handsdown/cli_parser.py#l9)

```python
def abs_path(path: str) -> pathlib.Path
```

Make path absolute.

#### Arguments

path - A path to check.

#### Returns

An absolute path.

## get_cli_parser

[🔍 find in source code](../handsdown/cli_parser.py#l22)

```python
def get_cli_parser() -> argparse.ArgumentParser
```

Get CLI arguments parser.

#### Returns

An `argparse.ArgumentParser` instance.
