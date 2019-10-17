# Main

> Auto-generated documentation for [handsdown.main](../handsdown/main.py) module.

- [Handsdown](README.md#handsdown) / [Handsdown](handsdown_index.md#handsdown) / Main
  - [get_logger](#get_logger)
  - [main](#main)

Main CLI entrypoint for `handsdown`

#### Attributes

- `EXCLUDE_EXPRS` - Path glob expressions to always exclude.
  By default: `build/*`, `tests/*`, `test/*` are excluded.
- `SOURCES_GLOB_EXPR` - Glob expr to lokkup python source files: `**/*.py`

## get_logger

[🔍 find in source code](../handsdown/main.py#l23)

```python
def get_logger(level: int) -> logging.Logger
```

Get stdout stream logger.

#### Arguments

- `level` - Desired logging level.

#### Returns

A `logging.Logger` instance.

## main

[🔍 find in source code](../handsdown/main.py#l47)

```python
def main() -> None
```

Main entrypoint for CLI.
