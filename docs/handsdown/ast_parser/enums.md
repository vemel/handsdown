# Enums

[Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / [AST Parser](index.md#ast-parser) / Enums

> Auto-generated documentation for [handsdown.ast_parser.enums](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/enums.py) module.

- [Enums](#enums)

## RenderPart

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/enums.py#L7)

#### Attributes

- `MULTI_LINE_BREAK` - Replaced with a line break for a multi-line render, does not change indent: `'MULTI_LINE_BREAK'`

- `MULTI_LINE_INDENT` - Replaced with a line break for a multi-line render, adds one indent level: `'MULTI_LINE_INDENT'`

- `MULTI_LINE_UNINDENT` - Replaced with a line break for a multi-line render, removes one indent level: `'MULTI_LINE_UNINDENT'`

- `LINE_BREAK` - Replaced with a line break, does not change indent: `'LINE_BREAK'`

- `LINE_INDENT` - Replaced with a line break, adds one indent level: `'LINE_INDENT'`

- `LINE_UNINDENT` - Replaced with a line break, removes one indent level: `'LINE_UNINDENT'`

- `SINGLE_LINE_SPACE` - Replaced with a space in a single-line render: `'SINGLE_LINE_SPACE'`

- `MULTI_LINE_COMMA` - Replaced with a comma in a multi-line render: `'MULTI_LINE_COMMA'`


Special render part.For `handsdown.ast_parser.node_records.node_record.NodeRecord.render` function.

#### Signature

```python
class RenderPart(enum.Enum):
    ...
```

### RenderPart().is_line_break

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/enums.py#L38)

Check if it is a mandatory line break.

#### Returns

True if part is a line break.

#### Signature

```python
def is_line_break(self) -> bool:
    ...
```


