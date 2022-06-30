# Main

[Handsdown API Index](../README.md#handsdown-api-index) /
[Handsdown](./index.md#handsdown) /
Main

> Auto-generated documentation for [handsdown.main](https://github.com/vemel/handsdown/blob/main/handsdown/main.py) module.

## api

[Show source in main.py:27](https://github.com/vemel/handsdown/blob/main/handsdown/main.py#L27)

#### Signature

```python
def api(args: CLINamespace) -> None:
    ...
```

#### See also

- [CLINamespace](./cli_parser.md#clinamespace)



## main

[Show source in main.py:57](https://github.com/vemel/handsdown/blob/main/handsdown/main.py#L57)

Main entrypoint for CLI.

#### Signature

```python
def main() -> None:
    ...
```



## select_generator_cls

[Show source in main.py:17](https://github.com/vemel/handsdown/blob/main/handsdown/main.py#L17)

Select a generator based on the theme.

#### Signature

```python
def select_generator_cls(theme: Theme) -> Type[BaseGenerator]:
    ...
```

#### See also

- [Theme](./constants.md#theme)



