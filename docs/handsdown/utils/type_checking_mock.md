# TypeCheckingMock

> Auto-generated documentation for [handsdown.utils.type_checking_mock](https://github.com/vemel/handsdown/blob/master/handsdown/utils/type_checking_mock.py) module.

Helper to turn on or off `TYPE_CHECKING` to avoid sircular imports.

- [Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / [Utils](index.md#utils) / TypeCheckingMock
  - [TypeCheckingMock](#typecheckingmock)

## TypeCheckingMock

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/utils/type_checking_mock.py#L11)

```python
class TypeCheckingMock(target_file_path: Path) -> None:
```

Helper to turn on or off `TYPE_CHECKING` to avoid sircular imports.

Returns `True` for usage from the `target_file_path`.

#### Examples

```python
import_string = fet_import_string_from_path(file_path)
with patch("typing.TYPE_CHECKING", TypeCheckingMock(file_path)):
    module = importlib.import_module(import_string)
```

#### Arguments

- `target_file_path` - Source path where `typing.TYPE_CHECKING` should be `True`
