# Enums

> Auto-generated documentation for [handsdown.ast_parser.enums](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/enums.py) module.

Enums for AST parsing.

- [Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / [AST Parser](index.md#ast-parser) / Enums
    - [RenderPart](#renderpart)
        - [RenderPart().is_line_break](#renderpartis_line_break)

## RenderPart

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/enums.py#L7)

```python
class RenderPart(enum.Enum):
```

Special render part for [render](node_records/node_record.md#render)
function.

#### Attributes

- `LINE_BREAK` - Replaced with a line break, does not change indent: `'LINE_BREAK'`
- `LINE_INDENT` - Replaced with a line break, adds one indent level: `'LINE_INDENT'`
- `LINE_UNINDENT` - Replaced with a line break, removes one indent level: `'LINE_UNINDENT'`
- `MULTI_LINE_BREAK` - Replaced with a line break for a multi-line render, does not change indent: `'MULTI_LINE_BREAK'`
- `MULTI_LINE_COMMA` - Replaced with a comma in a multi-line render: `'MULTI_LINE_COMMA'`
- `MULTI_LINE_INDENT` - Replaced with a line break for a multi-line render, adds one indent level: `'MULTI_LINE_INDENT'`
- `MULTI_LINE_UNINDENT` - Replaced with a line break for a multi-line render, removes one indent level: `'MULTI_LINE_UNINDENT'`
- `SINGLE_LINE_SPACE` - Replaced with a space in a single-line render: `'SINGLE_LINE_SPACE'`

### RenderPart().is_line_break

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/enums.py#L37)

```python
def is_line_break() -> bool:
```

Check if it is a mandatory line break.

#### Returns

True if part is a line break.
