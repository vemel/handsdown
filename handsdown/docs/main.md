# Main

> Auto-generated documentation for [main](../main.py) module..

Main CLI entrypoint for `handsdown`

- [Index](README.md#modules) / Main
  - [get_logger](#get_logger)
  - [main](#main)

#### Attributes

- `EXCLUDE_EXPRS` - Path glob expressions to always exclude.
    By default `build/*`, `tests/*`, `test/*`, `*/__pycache__/*` are excluded.
- `SOURCES_GLOB` - Glob expr to lokkup python source files: `**/*.py`

## get_logger

[🔍 find in source code](../main.py#L24)

```python
def get_logger(level: int) -> logging.Logger
```

Get stdout stream logger.

#### Returns

A `logging.Logger` instance.

#### Arguments

- `level` - Desired logging level.

## main

[🔍 find in source code](../main.py#L49)

```python
def main() -> None
```

Main entrypoint for CLI.
