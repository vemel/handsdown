# IndentTrimmer

- [Handsdown](./README.md#handsdown) / [Handsdown](./handsdown_index.md#handsdown) / IndentTrimmer
  - [IndentTrimmer](#indenttrimmer)
    - [IndentTrimmer.get_line_indent](#indenttrimmerget_line_indent)
    - [IndentTrimmer.trim_empty_lines](#indenttrimmertrim_empty_lines)
    - [IndentTrimmer.trim_line](#indenttrimmertrim_line)
    - [IndentTrimmer.trim_lines](#indenttrimmertrim_lines)
    - [IndentTrimmer.trim_text](#indenttrimmertrim_text)

> Auto-generated documentation for [handsdown.indent_trimmer](../handsdown/indent_trimmer.py) module.

## IndentTrimmer

[🔍 find in source code](../handsdown/indent_trimmer.py#L4)

```python
class IndentTrimmer(*args, **kwargs)
```

Utility class for removing indentation for sections and lines.

### IndentTrimmer.get_line_indent

[🔍 find in source code](../handsdown/indent_trimmer.py#L105)

```python
def get_line_indent(line: str) -> int
```

Get indent length of the line.

#### Examples

```python
IndentTrimmer.get_line_indent('   test') # 3
IndentTrimmer.get_line_indent('test') # 0
```

#### Arguments

- `line` - Line of text.

#### Returns

A number of indentation characters in a beginning of the line.

### IndentTrimmer.trim_empty_lines

[🔍 find in source code](../handsdown/indent_trimmer.py#L9)

```python
def trim_empty_lines(text: str) -> str
```

Trim empty lines in the begging and the end of the text.

#### Examples

```python
text = '\n  \n test\ntest2\n \n '
IndentTrimmer.trim_empty_lines(text)
# ' test\ntest2'
```

#### Returns

A stripped string.

### IndentTrimmer.trim_line

[🔍 find in source code](../handsdown/indent_trimmer.py#L81)

```python
def trim_line(line: str, indent: int) -> str
```

Trim indent from line if it is empty.

#### Examples

```python
IndentTrimmer.trim_line('     test', 2) # '   test'
IndentTrimmer.trim_line('     test', 6) # 'test'
IndentTrimmer.trim_line('     test', 1) # '    test'
```

#### Arguments

- `line` - A line of text.

#### Returns

A line with removed indent.

### IndentTrimmer.trim_lines

[🔍 find in source code](../handsdown/indent_trimmer.py#L48)

```python
def trim_lines(lines: Iterable[str]) -> List[str]
```

Trim minimum indent from each line of text.

#### Examples

```python
IndentTrimmer.trim_lines([
    '  asd',
    ' asd',
    '   asd',
)
# [
#     ' asd',
#     'asd',
#     '  asd',
# ]
```

#### Arguments

- `lines` - List of lines.

#### Returns

A list of lines with trimmed indent.

### IndentTrimmer.trim_text

[🔍 find in source code](../handsdown/indent_trimmer.py#L27)

```python
def trim_text(text: str) -> str
```

Trim minimum indent from each line of text.

#### Examples

```python
IndentTrimmer.trim_text('  asd\n asd\n   asd\n')
# ' asd\nasd\n  asd\n'
```

#### Arguments

- `text` - Multiline text.

#### Returns

A text with trimmed indent.
