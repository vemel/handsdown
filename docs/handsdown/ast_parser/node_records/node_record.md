# NodeRecord

> Auto-generated documentation for [handsdown.ast_parser.node_records.node_record](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/node_record.py) module.

Base class for all node records.

- [Handsdown](../../../README.md#-handsdown---python-documentation-generator) / [Modules](../../../MODULES.md#modules) / [Handsdown](../../index.md#handsdown) / [AST Parser](../index.md#ast-parser) / [Node Records](index.md#node-records) / NodeRecord
    - [NodeRecord](#noderecord)
        - [NodeRecord().get_documented_attribute_strings](#noderecordget_documented_attribute_strings)
        - [NodeRecord.is_line_fit](#noderecordis_line_fit)
        - [NodeRecord().line_number](#noderecordline_number)
        - [NodeRecord().line_number](#noderecordline_number)
        - [NodeRecord().parse](#noderecordparse)
        - [NodeRecord().related_names](#noderecordrelated_names)
        - [NodeRecord().render](#noderecordrender)
        - [NodeRecord.render_indent](#noderecordrender_indent)

## NodeRecord

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/node_record.py#L14)

```python
class NodeRecord():
    def __init__(node: ast.AST) -> None:
```

Base class for all node records.

#### Attributes

- `LINE_LENGTH` - Max length for a multi-line render result: `79`
- `SINGLE_LINE_LENGTH` - Max length for a single-line render result: `50`
- `INDENT_SPACES` - Amount of spaces per `indent`: `4`
- `MAX_INDENT` - Replace render resul with ellipsis on too deep indendation: `4`
- `ELLIPSIS` - Ellipsis string value: `'...'`

### NodeRecord().get_documented_attribute_strings

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/node_record.py#L263)

```python
def get_documented_attribute_strings() -> List[str]:
```

Render each of `attribute_records` to a Markdown string.

Includes `name`, `docstring` and `value` of an `ArgumentRecord`.

#### Returns

A list of rendered strings.

### NodeRecord.is_line_fit

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/node_record.py#L216)

```python
@classmethod
def is_line_fit(line: str, indent: int) -> bool:
```

Check if line fits to [LINE_LENGTH](#noderecord) with given `indent`.

#### Examples

```python
NodeRecord.is_line_fit("a" * 40, 0)
False

NodeRecord.is_line_fit("a" * 80, 0)
False

NodeRecord.is_line_fit("a" * 70, 2)
True

NodeRecord.is_line_fit("a" * 70, 4)
False
```

#### Returns

A string representation of indent.

### NodeRecord().line_number

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/node_record.py#L48)

```python
@property
def line_number() -> int:
```

Return node line number in source.

#### Returns

A line number startign with 1.

### NodeRecord().line_number

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/node_record.py#L63)

```python
@line_number.setter
def line_number(value: int) -> None:
```

### NodeRecord().parse

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/node_record.py#L90)

```python
def parse() -> None:
```

Get all information from a node.

Executes only once if called multiple times.

### NodeRecord().related_names

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/node_record.py#L74)

```python
@property
def related_names() -> Set[str]:
```

Get a set of referenced object names in `node`.

Returns an empty set, should be overriden by a child class.

#### Returns

A set of referenced object name.

### NodeRecord().render

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/node_record.py#L156)

```python
def render(indent: int = 0, allow_multiline: bool = False) -> str:
```

Render node to a string.

If `allow_multiline` is True, tries to fit the result into [LINE_LENGTH](#noderecord),
otherwise does not break lines and trims result to [SINGLE_LINE_LENGTH](#noderecord).

#### Arguments

- `indent` - Indent for lines after the first, `indent=2` means 8 spaces.
- `allow_multiline` - allow line breaks in redner result.

#### Returns

A string representation of `node`.

### NodeRecord.render_indent

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/node_record.py#L240)

```python
@classmethod
def render_indent(indent: int) -> str:
```

Render indent to a string.

Each indent adds [INDENT_SPACES](#noderecord) spaces.

#### Examples

```python
NodeRecord.render_indent(0)
""

NodeRecord.render_indent(1)
"    "

NodeRecord.render_indent(4)
"                "
```

#### Returns

A string representation of indent.
