# Main

> Auto-generated documentation for [handsdown.main](https://github.com/vemel/handsdown/blob/master/handsdown/main.py) module.

Main CLI entrypoint for `handsdown`

- [Handsdown](../README.md#-handsdown---python-documentation-generator) / [Modules](../MODULES.md#modules) / [Handsdown](index.md#handsdown) / Main
  - [create_external_configs](#create_external_configs)
  - [get_logger](#get_logger)
  - [main](#main)

#### Attributes

- `EXCLUDE_EXPRS` - Path glob expressions to always exclude.
    By default `build/*`, `tests/*`, `test/*`, `*/__pycache__/*`, `.*/*` are excluded.
- `SOURCES_GLOB` - Glob expr to lokkup python source files: `**/*.py`

## create_external_configs

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/main.py#L52)

```python
def create_external_configs(namespace: argparse.Namespace) -> None:
```

Create `GitHub Pages` and `Read the Docs` configuration files.

## get_logger

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/main.py#L27)

```python
def get_logger(level: int) -> logging.Logger:
```

Get stdout stream logger.

#### Arguments

- `level` - Desired logging level.

#### Returns

A `logging.Logger` instance.

## main

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/main.py#L80)

```python
def main() -> None:
```

Main entrypoint for CLI.
