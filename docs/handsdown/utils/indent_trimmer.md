# IndentTrimmer

[Handsdown API Index](../../README.md#handsdown-api-index) /
[Handsdown](../index.md#handsdown) /
[Utils](./index.md#utils) /
IndentTrimmer

> Auto-generated documentation for [handsdown.utils.indent_trimmer](https://github.com/vemel/handsdown/blob/main/handsdown/utils/indent_trimmer.py) module.

- [IndentTrimmer](#indenttrimmer)
  - [IndentTrimmer](#indenttrimmer-1)
    - [IndentTrimmer.get_line_indent](#indenttrimmerget_line_indent)
    - [IndentTrimmer.indent_line](#indenttrimmerindent_line)
    - [IndentTrimmer.trim_empty_lines](#indenttrimmertrim_empty_lines)
    - [IndentTrimmer.trim_line](#indenttrimmertrim_line)
    - [IndentTrimmer.trim_lines](#indenttrimmertrim_lines)
    - [IndentTrimmer.trim_text](#indenttrimmertrim_text)

## IndentTrimmer

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/indent_trimmer.py#L10)

Utility for removing indentation for sections and lines.

#### Signature

```python
class IndentTrimmer:
    ...
```

### IndentTrimmer.get_line_indent

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/indent_trimmer.py#L119)

Get indent length of the line.

#### Examples

```python
IndentTrimmer.get_line_indent('   test')
3

IndentTrimmer.get_line_indent('test')
0
```

#### Arguments

- `line` - Line of text.

#### Returns

A number of indentation characters in a beginning of the line.

#### Signature

```python
@staticmethod
def get_line_indent(line: str) -> int:
    ...
```

### IndentTrimmer.indent_line

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/indent_trimmer.py#L140)

Indent line with givent length `indent`.

#### Examples

```python
IndentTrimmer.indent_line('test', 2)
'  test'
```

#### Arguments

- `line` - Line to indent.
- `indent` - Length of indent in spaces.

#### Returns

An indented line.

#### Signature

```python
@staticmethod
def indent_line(line: str, indent: int) -> str:
    ...
```

### IndentTrimmer.trim_empty_lines

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/indent_trimmer.py#L15)

Trim empty lines in the begging and the end of the text.

#### Examples

```python
text = '\n  \n test\ntest2\n \n '
IndentTrimmer.trim_empty_lines(text)
' test\ntest2'
```

#### Returns

A stripped string.

#### Signature

```python
@staticmethod
def trim_empty_lines(text: str) -> str:
    ...
```

### IndentTrimmer.trim_line

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/indent_trimmer.py#L92)

Trim indent from line if it is empty.

#### Examples

```python
IndentTrimmer.trim_line('     test', 2)
'   test'

IndentTrimmer.trim_line('     test', 6)
'test'

IndentTrimmer.trim_line('     test', 1)
'    test'
```

#### Arguments

- `line` - A line of text.

#### Returns

A line with removed indent.

#### Signature

```python
@staticmethod
def trim_line(line: str, indent: int) -> str:
    ...
```

### IndentTrimmer.trim_lines

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/indent_trimmer.py#L57)

Trim minimum indent from each line of text.

#### Examples

```python
IndentTrimmer.trim_lines([
    '  asd',
    ' asd',
    '   asd',
])
[
    ' asd',
    'asd',
    '  asd',
]
```

#### Arguments

- `lines` - List of lines.

#### Returns

A list of lines with trimmed indent.

#### Signature

```python
@classmethod
def trim_lines(cls, lines: Iterable[str]) -> List[str]:
    ...
```

### IndentTrimmer.trim_text

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/utils/indent_trimmer.py#L37)

Trim minimum indent from each line of text.

#### Examples

```python
IndentTrimmer.trim_text('  asd\n asd\n   asd\n')
' asd\nasd\n  asd\n'
```

#### Arguments

- `text` - Multiline text.

#### Returns

A text with trimmed indent.

#### Signature

```python
@classmethod
def trim_text(cls, text: str) -> str:
    ...
```


