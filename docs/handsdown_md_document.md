# MDDocument

> Auto-generated documentation for [handsdown.md_document](../handsdown/md_document.py) module.

- [Handsdown](./README.md#handsdown) / [Handsdown](./handsdown_index.md#handsdown) / MDDocument
  - [MDDocument](#mddocument)
    - [MDDocument().append](#mddocumentappend)
    - [MDDocument().append\_title](#mddocumentappend_title)
    - [MDDocument().ensure\_toc\_exists](#mddocumentensure_toc_exists)
    - [MDDocument.extract\_title](#mddocumentextract_title)
    - [MDDocument().generate\_toc\_section](#mddocumentgenerate_toc_section)
    - [MDDocument.get\_anchor](#mddocumentget_anchor)
    - [MDDocument.is\_toc](#mddocumentis_toc)
    - [MDDocument.render\_doc\_link](#mddocumentrender_doc_link)
    - [MDDocument.render\_link](#mddocumentrender_link)
    - [MDDocument().write](#mddocumentwrite)

## MDDocument

[🔍 find in source code](../handsdown/md_document.py#L8)

```python
class MDDocument(content: str = '')
```

MD file wrapper. Controls document title and Table of Contents.

#### Examples

```python
md_doc = MDDocument('hello')
md_doc.append('## New section')
md_doc.append('some content')
md_doc.title = 'My doc'
md_doc.ensure_toc_exists()
md_doc.write(Path('output.md'))

Path('output.md').read_text()
# # My doc
#
# - [My doc](#my-doc)
#   - [New section](#new-section)
#
# ## New section
#
# some content
#
```

#### Arguments

- `content` - Initial MD content.

### MDDocument().append

[🔍 find in source code](../handsdown/md_document.py#L213)

```python
def append(content: str) -> None
```

Append `content` to the document.
Handle trimming and sectioning the content and update
`title` and `toc_section` fields.

#### Arguments

- `content` - Text to add.

### MDDocument().append\_title

[🔍 find in source code](../handsdown/md_document.py#L229)

```python
def append_title(title: str, level: int) -> None
```

Append `title` to the document.

#### Arguments

- `title` - Title to add.
- `level` - Title level, number of `#` characters.

### MDDocument().ensure\_toc\_exists

[🔍 find in source code](../handsdown/md_document.py#L73)

```python
def ensure_toc_exists() -> None
```

Check if ToC exists in the document or create one.

### MDDocument.extract\_title

[🔍 find in source code](../handsdown/md_document.py#L282)

```python
def extract_title(content: str) -> Tuple[str, str]
```

Extract title from the first line of content.
If title is present -  return a title and a remnaing content.
if not - return an empty title and untouched content.

#### Examples

```python
MDDocument.extract_title('# Title\ncontent') # ('Title', 'content')
MDDocument.extract_title('no title\ncontent') # ('', 'no title\ncontent')
```

#### Returns

A tuple fo title and remaining content.

### MDDocument().generate\_toc\_section

[🔍 find in source code](../handsdown/md_document.py#L241)

```python
def generate_toc_section(max_depth: int = 3) -> str
```

Generate Table of Contents MD content.

#### Arguments

- `max_depth` - Add headers to ToC only up to this level.

#### Returns

A string with ToC.

### MDDocument.get\_anchor

[🔍 find in source code](../handsdown/md_document.py#L80)

```python
def get_anchor(title: str) -> str
```

Convert title to Github-compatible anchor link.

#### Returns

A test of anchor link.

### MDDocument.is\_toc

[🔍 find in source code](../handsdown/md_document.py#L92)

```python
def is_toc(section: str) -> bool
```

Check if the section is Tree of Contents.

#### Returns

True the section is ToC.

### MDDocument.render\_doc\_link

[🔍 find in source code](../handsdown/md_document.py#L131)

```python
def render_doc_link(title: str, anchor: str = '', md_name: str = '') -> str
```

Render Markdown link to a local MD document.

#### Examples

```python
MDDocument.render_doc_link('my title', anchor='My anchor') # [my title](#my-anchor)
MDDocument.render_doc_link('my title', md_name='doc.md') # [my title](./doc.md)
MDDocument.render_doc_link('my title', anchor='My anchor', md_name='doc.md')
# [my title](./doc.md#my-anchor)
```

#### Arguments

- `title` - Link text.
- `anchor` - Unescaped or exacped anchor tag.
- `md_name` - Name of local MD document.

#### Returns

A string with Markdown link.

### MDDocument.render\_link

[🔍 find in source code](../handsdown/md_document.py#L109)

```python
def render_link(title: str, link: str) -> str
```

Render Markdown link wih escaped title.

#### Examples

```python
MDDocument.render_link('my title', 'doc.md#test') # [my title](doc.md#test)
MDDocument.render_link('MyClass.__init__', 'my.md')
# [MyClass.\_\_init\_\_](doc.md#my.md)
```

#### Arguments

- `title` - Link text.
- `link` - Link target.

#### Returns

A string with Markdown link.

### MDDocument().write

[🔍 find in source code](../handsdown/md_document.py#L177)

```python
def write(path: pathlib.Path) -> None
```

Write MD content to `path`.

#### Arguments

- `path` - Output path.
