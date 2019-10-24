# Settings

> Auto-generated documentation for [handsdown.settings](https://github.com/vemel/handsdown/blob/master/handsdown/settings.py) module.

Various project constants.

- [Handsdown](../README.md#-handsdown---python-documentation-generator) / [Modules](../MODULES.md#modules) / [Handsdown](index.md#handsdown) / Settings

#### Attributes

- []() - Path to `assets` directory from root.: `os.path.join(HANDSDOWN_PATH, 'assets')`
- []() - Paths to exclude from docs generation.: `['build/*', 'tests/*', 'test/*', '*/__pycache__/*', '.*/*']`
- []() - Find in code link label.: `'🔍 find in source code'`
- []() - Path to handsdown root directory.: `os.path.dirname(__file__)`
- []() - Global `logging.Logger` name.: `'handsdown'`
- []() - `glob.glob` expression to ind all Python sources in current directory.: `'**/*.py'`

## 

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/settings.py#L12)

```python
ASSETS_PATH = os.path.join(HANDSDOWN_PATH, 'assets')
```

Path to `assets` directory from root.

## 

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/settings.py#L18)

```python
EXCLUDE_EXPRS = ['build/*', 'tests/*', 'test/*', '*/__pycache__/*', '.*/*']
```

Paths to exclude from docs generation.

## 

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/settings.py#L24)

```python
FIND_IN_SOURCE_LABEL = '🔍 find in source code'
```

Find in code link label.

## 

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/settings.py#L9)

```python
HANDSDOWN_PATH = os.path.dirname(__file__)
```

Path to handsdown root directory.

## 

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/settings.py#L15)

```python
LOGGER_NAME = 'handsdown'
```

Global `logging.Logger` name.

## 

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/settings.py#L21)

```python
SOURCES_GLOB = '**/*.py'
```

`glob.glob` expression to ind all Python sources in current directory.
