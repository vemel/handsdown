# IndentTrimmer

> Auto-generated documentation for [handsdown.indent_trimmer](https://github.com/vemel/handsdown/blob/master/handsdown/indent_trimmer.py) module.

Utility for removing indentation for sections and lines.

- [Handsdown](../README.md#-handsdown---python-documentation-generator) / [Modules](../MODULES.md#modules) / [Handsdown](index.md#handsdown) / IndentTrimmer
  - [IndentTrimmer](#indenttrimmer)
    - [IndentTrimmer.get_line_indent](#indenttrimmerget_line_indent)
    - [IndentTrimmer.indent_line](#indenttrimmerindent_line)
    - [IndentTrimmer.trim_empty_lines](#indenttrimmertrim_empty_lines)
    - [IndentTrimmer.trim_line](#indenttrimmertrim_line)
    - [IndentTrimmer.trim_lines](#indenttrimmertrim_lines)
    - [IndentTrimmer.trim_text](#indenttrimmertrim_text)

## IndentTrimmer

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/indent_trimmer.py#L11)

```python
class IndentTrimmer(object):
```

Utility for removing indentation for sections and lines.

### IndentTrimmer.get_line_indent

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/indent_trimmer.py#L123)

```python
@staticmethod
def get_line_indent(line: Text) -> int:
```

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

### IndentTrimmer.indent_line

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/indent_trimmer.py#L145)

```python
@staticmethod
def indent_line(line: int, indent: Text) -> Text:
```

Indent line with givent length `indent`

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

### IndentTrimmer.trim_empty_lines

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/indent_trimmer.py#L16)

```python
@staticmethod
def trim_empty_lines(text: Text) -> Text:
```

Trim empty lines in the begging and the end of the text.

#### Examples

```python
text = '\n  \n test\ntest2\n \n '
IndentTrimmer.trim_empty_lines(text)
' test\ntest2'
```

#### Returns

A stripped string.

### IndentTrimmer.trim_line

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/indent_trimmer.py#L95)

```python
@staticmethod
def trim_line(line: int, indent: Text) -> Text:
```

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

### IndentTrimmer.trim_lines

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/indent_trimmer.py#L59)

```python
@classmethod
def trim_lines(lines: Iterable[Text]) -> List[Text]:
```

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

### IndentTrimmer.trim_text

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/indent_trimmer.py#L39)

```python
@classmethod
def trim_text(text: Text) -> Text:
```

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

## 

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/indent_trimmer.py#L8)

```python
__all__ = ['IndentTrimmer']
```
