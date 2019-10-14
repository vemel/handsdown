# Handsdown: Cli parser

- [Handsdown: Cli parser](#handsdown-cli-parser)
- [CLI Parser](#cli-parser)
  - [abs_path](#abs_path)
  - [abs_path_list](#abs_path_list)
  - [get_cli_parser](#get_cli_parser)

> Auto-generated documentation for [handsdown.cli_parser](../handsdown/cli_parser.py) module.

# CLI Parser

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

## abs_path_list

[🔍 find in source code](../handsdown/cli_parser.py#L22)

```python
def abs_path_list(paths: Iterable[str]) -> List[pathlib.Path]
```

Make path absolute.

#### Arguments

path - A path to check.

#### Returns

An absolute path.

## get_cli_parser

[🔍 find in source code](../handsdown/cli_parser.py#L39)

```python
def get_cli_parser() -> argparse.ArgumentParser
```

Get CLI arguments parser.

#### Returns

An `argparse.ArgumentParser` instance.
