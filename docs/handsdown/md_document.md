# MDDocument

> Auto-generated documentation for [handsdown.md_document](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py) module.

Markdown file builder.

- [Handsdown](../README.md#-handsdown---python-documentation-generator) / [Modules](../MODULES.md#modules) / [Handsdown](index.md#handsdown) / MDDocument
  - [MDDocument](#mddocument)
    - [MDDocument().add_toc_if_not_exists](#mddocumentadd_toc_if_not_exists)
    - [MDDocument().append](#mddocumentappend)
    - [MDDocument().append_title](#mddocumentappend_title)
    - [MDDocument().generate_toc_section](#mddocumentgenerate_toc_section)
    - [MDDocument.get_anchor](#mddocumentget_anchor)
    - [MDDocument.is_toc](#mddocumentis_toc)
    - [MDDocument().path](#mddocumentpath)
    - [MDDocument().read](#mddocumentread)
    - [MDDocument().render_doc_link](#mddocumentrender_doc_link)
    - [MDDocument.render_link](#mddocumentrender_link)
    - [MDDocument().render_md_doc_link](#mddocumentrender_md_doc_link)
    - [MDDocument().sections](#mddocumentsections)
    - [MDDocument().subtitle](#mddocumentsubtitle)
    - [MDDocument().subtitle](#mddocumentsubtitle)
    - [MDDocument().title](#mddocumenttitle)
    - [MDDocument().title](#mddocumenttitle)
    - [MDDocument().toc_section](#mddocumenttoc_section)
    - [MDDocument().toc_section](#mddocumenttoc_section)
    - [MDDocument().write](#mddocumentwrite)

## MDDocument

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L22)

```python
class MDDocument(object):
    def __init__(path: Path) -> None:
```

Markdown file builder.

Can be used as a context manager, on exit context is written to `path`.

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

### MDDocument().add_toc_if_not_exists

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L127)

```python
def add_toc_if_not_exists() -> None:
```

Check if ToC exists in the document or create one.

### MDDocument().append

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L324)

```python
def append(content: Text) -> None:
```

Append `content` to the document.
Handle trimming and sectioning the content and update
`title` and `toc_section` fields.

#### Arguments

- `content` - Text to add.

### MDDocument().append_title

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L345)

```python
def append_title(title: int, level: Text) -> None:
```

Append `title` of a given `level` to the document.
Handle trimming and sectioning the content and update
`title` and `toc_section` fields.

#### Arguments

- `title` - Title to add.
- `level` - Title level, number of `#` symbols.

### MDDocument().generate_toc_section

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L360)

```python
def generate_toc_section(max_depth: int = 3) -> Text:
```

Generate Table of Contents MD content.

#### Arguments

- `max_depth` - Add headers to ToC only up to this level.

#### Returns

A string with ToC.

### MDDocument.get_anchor

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L135)

```python
@classmethod
def get_anchor(title: Text) -> Text:
```

Convert title to a GitHub-friendly anchor link.

#### Returns

A test of anchor link.

### MDDocument.is_toc

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L148)

```python
@staticmethod
def is_toc(section: Text) -> bool:
```

Check if the section is Tree of Contents.

#### Returns

True the section is ToC.

### MDDocument().path

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L316)

```python
@property
def path() -> Path:
```

Output path of the document.

### MDDocument().read

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L88)

```python
def read(source_path: Optional[Path] = None) -> None:
```

Read and parse content from `source_path`.

#### Arguments

- `source_path` - Input file path. If not provided - `path` is used.

### MDDocument().render_doc_link

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L207)

```python
def render_doc_link(
    title: Optional[Path],
    anchor: Text = '',
    target_path: Text = None,
) -> Text:
```

Render Markdown link to a local MD document, use relative path as a link.

#### Examples

```python
md_doc = MDDocument(path='/root/parent/doc.md')
MDDocument.render_doc_link('my title', anchor='my-anchor', target_path=Path('/root/parent/doc.md')
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

### MDDocument.render_link

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L166)

```python
@classmethod
def render_link(title: Text, link: Text) -> Text:
```

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

### MDDocument().render_md_doc_link

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L189)

```python
def render_md_doc_link(
    target_md_document: Optional[Text],
    title: MDDocument = None,
) -> Text:
```

Render Markdown link to `target_md_document` header path with a correct title.

#### Arguments

- `target_md_document` - Target [MDDocument](#mddocument).
- `title` - Link text. If not provided `target_md_document.title` is used.

#### Returns

A string with Markdown link.

### MDDocument().sections

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L308)

```python
@property
def sections() -> List[Text]:
```

All non-special `sections` of the document.

### MDDocument().subtitle

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L280)

```python
@property
def subtitle() -> Text:
```

[MDDocument](#mddocument) subtitle or an empty string.

### MDDocument().subtitle

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L288)

```python
@subtitle.setter
def subtitle(subtitle: Text) -> None:
```

### MDDocument().title

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L266)

```python
@property
def title() -> Text:
```

[MDDocument](#mddocument) title or an empty string.

### MDDocument().title

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L274)

```python
@title.setter
def title(title: Text) -> None:
```

### MDDocument().toc_section

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L294)

```python
@property
def toc_section() -> Text:
```

Document Tree of Contents section or an empty line.

### MDDocument().toc_section

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L302)

```python
@toc_section.setter
def toc_section(toc_section: Text) -> None:
```

### MDDocument().write

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L257)

```python
def write() -> None:
```

Write MD content to `path`.

## 

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L19)

```python
__all__ = ['MDDocument']
```
