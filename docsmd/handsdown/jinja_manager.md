# JinjaManager

Jinja2 `Environment` manager.

[Handsdown API Index](../README.md#handsdown-api-index) / [Handsdown](./index.md#handsdown) / JinjaManager

> Auto-generated documentation for [handsdown.jinja_manager](https://github.com/vemel/handsdown/blob/main/handsdown/jinja_manager.py) module.

## JinjaManager

[Show source in jinja_manager.py:13](https://github.com/vemel/handsdown/blob/main/handsdown/jinja_manager.py#L13)

Jinja2 `Environment` manager.

#### Signature

```python
class JinjaManager:
    def __init__(self) -> None:
        ...
```

### JinjaManager().env

[Show source in jinja_manager.py:45](https://github.com/vemel/handsdown/blob/main/handsdown/jinja_manager.py#L45)

Get `jinja2.Environment`.

#### Signature

```python
@property
def env(self) -> jinja2.Environment:
    ...
```

### JinjaManager.escape_md

[Show source in jinja_manager.py:38](https://github.com/vemel/handsdown/blob/main/handsdown/jinja_manager.py#L38)

Escape underscore characters.

#### Signature

```python
@staticmethod
def escape_md(value: str) -> str:
    ...
```

### JinjaManager().render

[Show source in jinja_manager.py:59](https://github.com/vemel/handsdown/blob/main/handsdown/jinja_manager.py#L59)

#### Signature

```python
def render(self, template_path: Path, **kwargs: Any) -> str:
    ...
```

### JinjaManager.trim_eof

[Show source in jinja_manager.py:52](https://github.com/vemel/handsdown/blob/main/handsdown/jinja_manager.py#L52)

Trim EOF newlines and add one newline.

#### Signature

```python
@staticmethod
def trim_eof(value: str) -> str:
    ...
```

### JinjaManager.update_globals

[Show source in jinja_manager.py:28](https://github.com/vemel/handsdown/blob/main/handsdown/jinja_manager.py#L28)

Update global variables in `jinja2.Environment`.

#### Arguments

- `kwargs` - Globals to set.

#### Signature

```python
@classmethod
def update_globals(cls, **kwargs: object) -> None:
    ...
```
