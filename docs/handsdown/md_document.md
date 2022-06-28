# MDDocument

[🙌 Handsdown - Python documentation generator](../README.md#-handsdown---python-documentation-generator) /
[Modules](../MODULES.md#modules) /
[Handsdown](index.md#handsdown) /
MDDocument

> Auto-generated documentation for [handsdown.md_document](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py) module.

- [MDDocument](#mddocument)
  - [MDDocument](#mddocument-1)
    - [MDDocument().add_toc_if_not_exists](#mddocument()add_toc_if_not_exists)
    - [MDDocument().append](#mddocument()append)
    - [MDDocument().generate_toc_section](#mddocument()generate_toc_section)
    - [MDDocument.get_anchor](#mddocumentget_anchor)
    - [MDDocument().get_doc_link](#mddocument()get_doc_link)
    - [MDDocument.get_toc_line](#mddocumentget_toc_line)
    - [MDDocument.is_toc](#mddocumentis_toc)
    - [MDDocument().path](#mddocument()path)
    - [MDDocument().read](#mddocument()read)
    - [MDDocument().render_doc_link](#mddocument()render_doc_link)
    - [MDDocument.render_link](#mddocumentrender_link)
    - [MDDocument().render_md_doc_link](#mddocument()render_md_doc_link)
    - [MDDocument().sections](#mddocument()sections)
    - [MDDocument().subtitle](#mddocument()subtitle)
    - [MDDocument().subtitle](#mddocument()subtitle-1)
    - [MDDocument().title](#mddocument()title)
    - [MDDocument().title](#mddocument()title-1)
    - [MDDocument().toc_section](#mddocument()toc_section)
    - [MDDocument().toc_section](#mddocument()toc_section-1)
    - [MDDocument().write](#mddocument()write)

## MDDocument

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L21)

#### Attributes

- `TOC_INDENT` - Indent in spaces for nested ToC lines: `4`


Markdown file builder.Can be used as a context manager, on exit context is written to `path`.

#### Examples

```python
md_doc = MDDocument(path=Path('output.md'))
md_doc.append('## New section')
md_doc.append('some content')
md_doc.title = 'My doc'
md_doc.add_toc_if_not_exists()
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

- [ENCODING](settings.md#encoding)

### MDDocument().add_toc_if_not_exists

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L124)

Check if ToC exists in the document or create one.

#### Signature

```python
def add_toc_if_not_exists(self) -> None:
    ...
```

### MDDocument().append

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L330)

Append `content` to the document.Handle trimming and sectioning the content and update
`title` and `toc_section` fields.

#### Arguments

- `content` - Text to add.

#### Signature

```python
def append(self, content: str) -> None:
    ...
```

### MDDocument().generate_toc_section

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L351)

Generate Table of Contents MD content.

#### Arguments

- `max_depth` - Add headers to ToC only up to this level.

#### Returns

A string with ToC.

#### Signature

```python
def generate_toc_section(self, max_depth: int = 3) -> str:
    ...
```

### MDDocument.get_anchor

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L131)

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

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L241)

Get Markdown link to a local MD document, use relative path as a link.

#### Arguments

- `path` - Path to local MDDocument
- `anchor` - Unescaped or escaped anchor tag

#### Returns

A string with Markdown link.

#### Signature

```python
def get_doc_link(self, path: Path, anchor: str = "") -> str:
    ...
```

### MDDocument.get_toc_line

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L398)

Get ToC `line` of given `level`.

#### Arguments

- `line` - Line to prepare.
- `level` - Line level, starts with `0`.

#### Returns

Ready to insert ToC line.

#### Signature

```python
@classmethod
def get_toc_line(cls, line: str, level: int = 0) -> str:
    ...
```

### MDDocument.is_toc

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L143)

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

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L323)

Output path of the document.

#### Signature

```python
@property
def path(self) -> Path:
    ...
```

### MDDocument().read

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L89)

Read and parse content from `source_path`.

#### Arguments

- `source_path` - Input file path. If not provided - `path` is used.
- `encoding` - File encoding.

#### Signature

```python
def read(self, source_path: Optional[Path] = None) -> None:
    ...
```

### MDDocument().render_doc_link

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L199)

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

- `title` - Link text.
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

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L160)

Render Markdown link wih escaped title.

#### Examples

```python
MDDocument.render_link('my title', 'doc.md#test')
'[my title](doc.md#test)'

MDDocument.render_link('MyClass.__init__', 'my.md')
'[MyClass.__init__](doc.md#my.md)'
```

#### Arguments

- `title` - Link text.
- `link` - Link target.

#### Returns

A string with Markdown link.

#### Signature

```python
@classmethod
def render_link(cls, title: str, link: str) -> str:
    ...
```

### MDDocument().render_md_doc_link

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L182)

Render Markdown link to `target_md_document` header path with a correct title.

#### Arguments

- `target_md_document` - Target `MDDocument`.
- `title` - Link text. If not provided `target_md_document.title` is used.

#### Returns

A string with Markdown link.

#### Signature

```python
def render_md_doc_link(
    self: _R, target_md_document: _R, title: Optional[str] = None
) -> str:
    ...
```

### MDDocument().sections

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L316)

All non-special `sections` of the document.

#### Signature

```python
@property
def sections(self) -> List[str]:
    ...
```

### MDDocument().subtitle

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L292)

`MDDocument` subtitle or an empty string.

#### Signature

```python
@property
def subtitle(self) -> str:
    ...
```

### MDDocument().subtitle

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L299)

#### Signature

```python
@subtitle.setter
def subtitle(self, subtitle: str) -> None:
    ...
```

### MDDocument().title

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L280)

`MDDocument` title or an empty string.

#### Signature

```python
@property
def title(self) -> str:
    ...
```

### MDDocument().title

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L287)

#### Signature

```python
@title.setter
def title(self, title: str) -> None:
    ...
```

### MDDocument().toc_section

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L304)

Document Tree of Contents section or an empty line.

#### Signature

```python
@property
def toc_section(self) -> str:
    ...
```

### MDDocument().toc_section

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L311)

#### Signature

```python
@toc_section.setter
def toc_section(self, toc_section: str) -> None:
    ...
```

### MDDocument().write

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/md_document.py#L272)

Write MD content to `path`.

#### Signature

```python
def write(self) -> None:
    ...
```


