# MDDocument

Markdown file builder.

[Handsdown API Index](../README.md#handsdown-api-index) / [Handsdown](./index.md#handsdown) / MDDocument

> Auto-generated documentation for [handsdown.md_document](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py) module.

## MDDocument

[Show source in md_document.py:23](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L23)

Markdown file builder.

Can be used as a context manager, on exit context is written to `path`.

#### Examples

```python
md_doc = MDDocument(path=Path('output.md'))
md_doc.append('## New section')
md_doc.append('some content')
md_doc.title = 'My doc'
md_doc.write()

# output is indented for readability
Path('output.md').read_text()
'''# My doc

- [My doc](#my-doc)
  - [New section](#new-section)

## New section

some content
'''

with MDDocument(path=Path('output.md')) as md_document:
    md_document.title = 'My doc'
    md_doc.append_title('New section', level=2)
    md_doc.append('New line')
```

#### Arguments

- `path` - Path to store document.

#### Signature

```python
class MDDocument:
    def __init__(self, path: Path, encoding: str = ENCODING) -> None:
        ...
```

#### See also

- [ENCODING](./constants.md#encoding)

### MDDocument().append

[Show source in md_document.py:310](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L310)

Append `content` to the document.

Handle trimming and sectioning the content and update
[MDDocument().title](#mddocumenttitle) and [MDDocument().toc_section](#mddocumenttoc_section) fields.

#### Arguments

- `content` - Text to add.

#### Signature

```python
def append(self, content: str) -> None:
    ...
```

### MDDocument.get_anchor

[Show source in md_document.py:128](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L128)

Convert title to a GitHub-friendly anchor link.

#### Returns

A test of anchor link.

#### Signature

```python
@classmethod
def get_anchor(cls, title: str) -> str:
    ...
```

### MDDocument().get_doc_link

[Show source in md_document.py:221](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L221)

Get Markdown link to a local MD document, use relative path as a link.

#### Arguments

- [MDDocument().path](#mddocumentpath) - Path to local MDDocument
- `anchor` - Unescaped or escaped anchor tag

#### Returns

A string with Markdown link.

#### Signature

```python
def get_doc_link(self, path: Path, anchor: str = "") -> str:
    ...
```

### MDDocument.is_toc

[Show source in md_document.py:140](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L140)

Check if the section is Tree of Contents.

#### Returns

True the section is ToC.

#### Signature

```python
@staticmethod
def is_toc(section: str) -> bool:
    ...
```

### MDDocument().path

[Show source in md_document.py:303](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L303)

Output path of the document.

#### Signature

```python
@property
def path(self) -> Path:
    ...
```

### MDDocument().read

[Show source in md_document.py:94](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L94)

Read and parse content from `source_path`.

#### Arguments

- `source_path` - Input file path. If not provided - [MDDocument().path](#mddocumentpath) is used.
- `encoding` - File encoding.

#### Signature

```python
def read(self, path: Path) -> None:
    ...
```

### MDDocument().render_doc_link

[Show source in md_document.py:179](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L179)

Render Markdown link to a local MD document, use relative path as a link.

#### Examples

```python
md_doc = MDDocument(path='/root/parent/doc.md')
MDDocument.render_doc_link(
    'my title',
    anchor='my-anchor',
    target_path=Path('/root/parent/doc.md'
)
'[my title](#my-anchor)'

MDDocument.render_doc_link('my title', target_path=Path('/root/parent/other.md'))
'[my title](other.md)'

MDDocument.render_doc_link('my title', anchor='my-anchor', target_path=Path('doc.md'))
'[my title](doc.md#my-anchor)'

MDDocument.render_doc_link('my title', anchor='my-anchor')
'[my title](#my-anchor)'
```

#### Arguments

- [MDDocument().title](#mddocumenttitle) - Link text.
- `anchor` - Unescaped or escaped anchor tag.
- `target_path` - Target MDDocument path.

#### Returns

A string with Markdown link.

#### Signature

```python
def render_doc_link(
    self, title: str, anchor: str = "", target_path: Optional[Path] = None
) -> str:
    ...
```

### MDDocument.render_link

[Show source in md_document.py:157](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L157)

Render Markdown link wih escaped title.

#### Examples

```python
MDDocument.render_link('my title', 'doc.md#test')
'[my title](doc.md#test)'

MDDocument.render_link('MyClass.__init__', 'my.md')
'[MyClass.__init__](doc.md#my.md)'
```

#### Arguments

- [MDDocument().title](#mddocumenttitle) - Link text.
- `link` - Link target.

#### Returns

A string with Markdown link.

#### Signature

```python
@classmethod
def render_link(cls, title: str, link: str) -> str:
    ...
```

### MDDocument().sections

[Show source in md_document.py:296](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L296)

All non-special `sections` of the document.

#### Signature

```python
@property
def sections(self) -> List[str]:
    ...
```

### MDDocument().source_file_name

[Show source in md_document.py:87](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L87)

Source code file name.

#### Signature

```python
@property
def source_file_name(self) -> str:
    ...
```

### MDDocument().subtitle

[Show source in md_document.py:272](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L272)

[MDDocument](#mddocument) subtitle or an empty string.

#### Signature

```python
@property
def subtitle(self) -> str:
    ...
```

### MDDocument().subtitle

[Show source in md_document.py:279](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L279)

#### Signature

```python
@subtitle.setter
def subtitle(self, subtitle: str) -> None:
    ...
```

### MDDocument().title

[Show source in md_document.py:260](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L260)

[MDDocument](#mddocument) title or an empty string.

#### Signature

```python
@property
def title(self) -> str:
    ...
```

### MDDocument().title

[Show source in md_document.py:267](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L267)

#### Signature

```python
@title.setter
def title(self, title: str) -> None:
    ...
```

### MDDocument().toc_section

[Show source in md_document.py:284](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L284)

Document Tree of Contents section or an empty line.

#### Signature

```python
@property
def toc_section(self) -> str:
    ...
```

### MDDocument().toc_section

[Show source in md_document.py:291](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L291)

#### Signature

```python
@toc_section.setter
def toc_section(self, toc_section: str) -> None:
    ...
```

### MDDocument().write

[Show source in md_document.py:252](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L252)

Write MD content to [MDDocument().path](#mddocumentpath).

#### Signature

```python
def write(self) -> None:
    ...
```
