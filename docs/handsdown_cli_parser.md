# CLI Parser

> Auto-generated documentation for [handsdown.cli_parser](../handsdown/cli_parser.py) module.

- [Handsdown](./README.md#handsdown) / [Handsdown](./handsdown_index.md#handsdown) / CLI Parser
  - [abs\_path](#abs_path)
  - [get\_cli\_parser](#get_cli_parser)

## abs\_path

[🔍 find in source code](../handsdown/cli_parser.py#L9)

```python
def abs_path(path: str) -> pathlib.Path
```

Make path absolute.

#### Arguments

path - A path to check.

#### Returns

An absolute path.

## get\_cli\_parser

[🔍 find in source code](../handsdown/cli_parser.py#L22)

```python
def get_cli_parser() -> argparse.ArgumentParser
```

Get CLI arguments parser.

#### Returns

An `argparse.ArgumentParser` instance.
