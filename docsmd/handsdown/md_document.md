# MDDocument

[Handsdown API Index](../README.md#handsdown-api-index) /
[Handsdown](./index.md#handsdown) /
MDDocument

> Auto-generated documentation for [handsdown.md_document](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py) module.

## MDDocument

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L22)

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

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L303)

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

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L121)

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

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L214)

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

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L133)

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

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L296)

Output path of the document.

#### Signature

```python
@property
def path(self) -> NicePath:
    ...
```

#### See also

- [NicePath](utils/nice_path.md#nicepath)

### MDDocument().read

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L86)

Read and parse content from `source_path`.

#### Arguments

- `source_path` - Input file path. If not provided - [MDDocument().path](#mddocumentpath) is used.
- `encoding` - File encoding.

#### Signature

```python
def read(self, source_path: Optional[Path] = None) -> None:
    ...
```

### MDDocument().render_doc_link

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L172)

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

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L150)

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

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L289)

All non-special `sections` of the document.

#### Signature

```python
@property
def sections(self) -> List[str]:
    ...
```

### MDDocument().subtitle

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L265)

[MDDocument](#mddocument) subtitle or an empty string.

#### Signature

```python
@property
def subtitle(self) -> str:
    ...
```

### MDDocument().subtitle

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L272)

#### Signature

```python
@subtitle.setter
def subtitle(self, subtitle: str) -> None:
    ...
```

### MDDocument().title

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L253)

[MDDocument](#mddocument) title or an empty string.

#### Signature

```python
@property
def title(self) -> str:
    ...
```

### MDDocument().title

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L260)

#### Signature

```python
@title.setter
def title(self, title: str) -> None:
    ...
```

### MDDocument().toc_section

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L277)

Document Tree of Contents section or an empty line.

#### Signature

```python
@property
def toc_section(self) -> str:
    ...
```

### MDDocument().toc_section

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L284)

#### Signature

```python
@toc_section.setter
def toc_section(self, toc_section: str) -> None:
    ...
```

### MDDocument().write

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L245)

Write MD content to [MDDocument().path](#mddocumentpath).

#### Signature

```python
def write(self) -> None:
    ...
```



