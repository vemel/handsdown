# Main

[Handsdown API Index](../README.md#handsdown-api-index) /
[Handsdown](./index.md#handsdown) /
Main

> Auto-generated documentation for [handsdown.main](https://github.com/vemel/handsdown/blob/main/handsdown/main.py) module.

## api

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/main.py#L27)

#### Signature

```python
def api(args: CLINamespace) -> None:
    ...
```

#### See also

- [CLINamespace](./cli_parser.md#clinamespace)



## main

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/main.py#L57)

Main entrypoint for CLI.

#### Signature

```python
def main() -> None:
    ...
```



## select_generator_cls

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/main.py#L17)

Select a generator based on the theme.

#### Signature

```python
def select_generator_cls(theme: Theme) -> Type[BaseGenerator]:
    ...
```

#### See also

- [Theme](./constants.md#theme)



