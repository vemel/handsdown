# Handsdown: Indent trimmer

- [Handsdown: Indent trimmer](#handsdown-indent-trimmer)
  - [IndentTrimmer](#indenttrimmer)
    - [IndentTrimmer.get_line_indent](#indenttrimmerget_line_indent)
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

[🔍 find in source code](../handsdown/indent_trimmer.py#L87)

```python
def get_line_indent(line: str) -> int
```

Utility class for removing indentation for sections and lines.

### IndentTrimmer.trim_line

[🔍 find in source code](../handsdown/indent_trimmer.py#L63)

```python
def trim_line(line: str, indent: int) -> str
```

Utility class for removing indentation for sections and lines.

### IndentTrimmer.trim_lines

[🔍 find in source code](../handsdown/indent_trimmer.py#L30)

```python
def trim_lines(lines: Iterable[str]) -> List[str]
```

Utility class for removing indentation for sections and lines.

### IndentTrimmer.trim_text

[🔍 find in source code](../handsdown/indent_trimmer.py#L9)

```python
def trim_text(text: str) -> str
```

Utility class for removing indentation for sections and lines.
