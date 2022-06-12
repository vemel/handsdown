# JinjaManager

> Auto-generated documentation for [handsdown.jinja_manager](https://github.com/vemel/handsdown/blob/main/handsdown/jinja_manager.py) module.

Jinja2 `Environment` manager.

- [Handsdown](../README.md#-handsdown---python-documentation-generator) / [Modules](../MODULES.md#modules) / [Handsdown](index.md#handsdown) / JinjaManager
    - [JinjaManager](#jinjamanager)
        - [JinjaManager.escape_md](#jinjamanagerescape_md)
        - [JinjaManager.get_environment](#jinjamanagerget_environment)
        - [JinjaManager().render](#jinjamanagerrender)
        - [JinjaManager.update_globals](#jinjamanagerupdate_globals)

## JinjaManager

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/jinja_manager.py#L10)

```python
class JinjaManager():
```

Jinja2 `Environment` manager.

### JinjaManager.escape_md

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/jinja_manager.py#L32)

```python
@staticmethod
def escape_md(value: str) -> str:
```

Escape underscore characters.

### JinjaManager.get_environment

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/jinja_manager.py#L39)

```python
@classmethod
def get_environment() -> jinja2.Environment:
```

Get `jinja2.Environment`.

### JinjaManager().render

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/jinja_manager.py#L47)

```python
def render(template_path: Path, **kwargs: Any) -> str:
```

### JinjaManager.update_globals

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/jinja_manager.py#L22)

```python
@classmethod
def update_globals(**kwargs: object) -> None:
```

Update global variables in `jinja2.Environment`.

#### Arguments

- `kwargs` - Globals to set.
