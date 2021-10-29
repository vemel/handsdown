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
        - [MDDocument.get_toc_line](#mddocumentget_toc_line)
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

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L20)

```python
class MDDocument():
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

#### Attributes

- `TOC_INDENT` - Indent in spaces for nested ToC lines: `4`

### MDDocument().add_toc_if_not_exists

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L120)

```python
def add_toc_if_not_exists() -> None:
```

Check if ToC exists in the document or create one.

### MDDocument().append

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L309)

```python
def append(content: str) -> None:
```

Append `content` to the document.

Handle trimming and sectioning the content and update
[MDDocument().title](#mddocumenttitle) and [MDDocument().toc_section](#mddocumenttoc_section) fields.

#### Arguments

- `content` - Text to add.

### MDDocument().append_title

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L330)

```python
def append_title(title: str, level: int) -> None:
```

Append [MDDocument().title](#mddocumenttitle) of a given `level` to the document.

Handle trimming and sectioning the content and update
[MDDocument().title](#mddocumenttitle) and [MDDocument().toc_section](#mddocumenttoc_section) fields.

#### Arguments

- `title` - Title to add.
- `level` - Title level, number of `#` symbols.

### MDDocument().generate_toc_section

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L346)

```python
def generate_toc_section(max_depth: int = 3) -> str:
```

Generate Table of Contents MD content.

#### Arguments

- `max_depth` - Add headers to ToC only up to this level.

#### Returns

A string with ToC.

### MDDocument.get_anchor

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L127)

```python
@classmethod
def get_anchor(title: str) -> str:
```

Convert title to a GitHub-friendly anchor link.

#### Returns

A test of anchor link.

### MDDocument.get_toc_line

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L393)

```python
@classmethod
def get_toc_line(line: str, level: int = 0) -> str:
```

Get ToC `line` of given `level`.

#### Arguments

- `line` - Line to prepare.
- `level` - Line level, starts with `0`.

#### Returns

Ready to insert ToC line.

### MDDocument.is_toc

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L139)

```python
@staticmethod
def is_toc(section: str) -> bool:
```

Check if the section is Tree of Contents.

#### Returns

True the section is ToC.

### MDDocument().path

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L302)

```python
@property
def path() -> Path:
```

Output path of the document.

### MDDocument().read

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L86)

```python
def read(source_path: Optional[Path] = None) -> None:
```

Read and parse content from `source_path`.

#### Arguments

- `source_path` - Input file path. If not provided - [MDDocument().path](#mddocumentpath) is used.

### MDDocument().render_doc_link

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L197)

```python
def render_doc_link(
    title: str,
    anchor: str = '',
    target_path: Optional[Path] = None,
) -> str:
```

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

### MDDocument.render_link

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L156)

```python
@classmethod
def render_link(title: str, link: str) -> str:
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

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L178)

```python
def render_md_doc_link(
    target_md_document: _MDDocument,
    title: Optional[str] = None,
) -> str:
```

Render Markdown link to `target_md_document` header path with a correct title.

#### Arguments

- `target_md_document` - Target [MDDocument](#mddocument).
- `title` - Link text. If not provided `target_md_document.title` is used.

#### Returns

A string with Markdown link.

### MDDocument().sections

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L295)

```python
@property
def sections() -> List[str]:
```

All non-special `sections` of the document.

### MDDocument().subtitle

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L271)

```python
@property
def subtitle() -> str:
```

[MDDocument](#mddocument) subtitle or an empty string.

### MDDocument().subtitle

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L278)

```python
@subtitle.setter
def subtitle(subtitle: str) -> None:
```

### MDDocument().title

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L259)

```python
@property
def title() -> str:
```

[MDDocument](#mddocument) title or an empty string.

### MDDocument().title

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L266)

```python
@title.setter
def title(title: str) -> None:
```

### MDDocument().toc_section

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L283)

```python
@property
def toc_section() -> str:
```

Document Tree of Contents section or an empty line.

### MDDocument().toc_section

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L290)

```python
@toc_section.setter
def toc_section(toc_section: str) -> None:
```

### MDDocument().write

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/md_document.py#L251)

```python
def write() -> None:
```

Write MD content to [MDDocument().path](#mddocumentpath).
