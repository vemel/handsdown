# JinjaManager

[Handsdown](../README.md#-handsdown---python-documentation-generator) / [Modules](../MODULES.md#modules) / [Handsdown](index.md#handsdown) / JinjaManager

> Auto-generated documentation for [handsdown.jinja_manager](https://github.com/vemel/handsdown/blob/main/handsdown/jinja_manager.py) module.

- [JinjaManager](#jinjamanager)

## JinjaManager

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/jinja_manager.py#L12)

Jinja2 `Environment` manager.

#### Signature

```python
class JinjaManager:
    def __init__(self) -> None:
        ...
```

### JinjaManager().env

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/jinja_manager.py#L44)

Get `jinja2.Environment`.

#### Signature

```python
@property
def env(self) -> jinja2.Environment:
    ...
```

### JinjaManager.escape_md

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/jinja_manager.py#L37)

Escape underscore characters.

#### Signature

```python
@staticmethod
def escape_md(value: str) -> str:
    ...
```

### JinjaManager().render

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/jinja_manager.py#L51)

#### Signature

```python
def render(self, template_path: Path, **kwargs: Any) -> str:
    ...
```

### JinjaManager.update_globals

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/jinja_manager.py#L27)

Update global variables in `jinja2.Environment`.

#### Arguments

- `kwargs` - Globals to set.

#### Signature

```python
@classmethod
def update_globals(cls, **kwargs: object) -> None:
    ...
```


