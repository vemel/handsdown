# Settings

> Auto-generated documentation for [handsdown.settings](https://github.com/vemel/handsdown/blob/master/handsdown/settings.py) module.

Various project constants.

- [Handsdown](../README.md#-handsdown---python-documentation-generator) / [Modules](../MODULES.md#modules) / [Handsdown](index.md#handsdown) / Settings

#### Attributes

- [ASSETS_PATH](#assets_path) - Path to `assets` directory from root.: `os.path.join(HANDSDOWN_PATH, 'assets')`
- [EXCLUDE_EXPRS](#exclude_exprs) - Paths to exclude from docs generation.: `['build/*', 'tests/*', 'test/*', '*/__pycache__/*', '.*/*']`
- [FIND_IN_SOURCE_LABEL](#find_in_source_label) - Find in code link label.: `'[find in source code]'`
- [HANDSDOWN_PATH](#handsdown_path) - Path to handsdown root directory.: `os.path.dirname(__file__)`
- [LOGGER_NAME](#logger_name) - Global `logging.Logger` name.: `'handsdown'`
- [SOURCES_GLOB](#sources_glob) - `glob.glob` expression to ind all Python sources in current directory.: `'**/*.py'`
