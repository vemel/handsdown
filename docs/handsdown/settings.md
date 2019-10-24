# Settings

> Auto-generated documentation for [handsdown.settings](https://github.com/vemel/handsdown/blob/master/handsdown/settings.py) module.

Various project constants.

- [Handsdown](../README.md#-handsdown---python-documentation-generator) / [Modules](../MODULES.md#modules) / [Handsdown](index.md#handsdown) / Settings

#### Attributes

- `ASSETS_PATH` - Path to `assets` directory from root.: `os.path.join(HANDSDOWN_PATH, 'assets')`
- `EXCLUDE_EXPRS` - Paths to exclude from docs generation.: `['build/*', 'tests/*', 'test/*', '*/__pycache__/*', '.*/*']`
- `FIND_IN_SOURCE_LABEL` - Find in code link label.: `'🔍 find in source code'`
- `HANDSDOWN_PATH` - Path to handsdown root directory.: `os.path.dirname(__file__)`
- `LOGGER_NAME` - Global `logging.Logger` name.: `'handsdown'`
- `SOURCES_GLOB` - `glob.glob` expression to ind all Python sources in current directory.: `'**/*.py'`
