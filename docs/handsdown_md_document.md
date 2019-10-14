# MDDocument

- [MDDocument](#mddocument)
  - [MDDocument](#mddocument)
    - [MDDocument().append](#mddocumentappend)
    - [MDDocument().ensure_toc_exists](#mddocumentensure_toc_exists)
    - [MDDocument.extract_title](#mddocumentextract_title)
    - [MDDocument().generate_toc_section](#mddocumentgenerate_toc_section)
    - [MDDocument.get_anchor](#mddocumentget_anchor)
    - [MDDocument.is_toc](#mddocumentis_toc)
    - [MDDocument.render_doc_link](#mddocumentrender_doc_link)
    - [MDDocument.render_link](#mddocumentrender_link)
    - [MDDocument().write](#mddocumentwrite)

> Auto-generated documentation for [Handsdown](./README.md#modules) / [MDDocument](#mddocument) module ([md_document.py](../handsdown/md_document.py))

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

[🔍 find in source code](../handsdown/md_document.py#L179)

```python
def append(content: str) -> None
```

Append `content` to the document.
Handle trimming and sectioning the content and update
`title` and `toc_section` fields.

#### Arguments

- `content` - Text to add.

### MDDocument().ensure_toc_exists

[🔍 find in source code](../handsdown/md_document.py#L69)

```python
def ensure_toc_exists() -> None
```

Check if ToC exists in the document or create one.

### MDDocument.extract_title

[🔍 find in source code](../handsdown/md_document.py#L240)

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

### MDDocument().generate_toc_section

[🔍 find in source code](../handsdown/md_document.py#L196)

```python
def generate_toc_section(max_depth: int = 3) -> str
```

Generate Table of Contents MD content.

#### Arguments

- `max_depth` - Add headers to ToC only up to this level.

#### Returns

A string with ToC.

### MDDocument.get_anchor

[🔍 find in source code](../handsdown/md_document.py#L76)

```python
def get_anchor(title: str) -> str
```

Convert title to Github-compatible anchor link.

#### Returns

A test of anchor link.

### MDDocument.is_toc

[🔍 find in source code](../handsdown/md_document.py#L88)

```python
def is_toc(section: str) -> bool
```

Check if the section is Tree of Contents.

#### Returns

True the section is ToC.

### MDDocument.render_doc_link

[🔍 find in source code](../handsdown/md_document.py#L125)

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

### MDDocument.render_link

[🔍 find in source code](../handsdown/md_document.py#L105)

```python
def render_link(title: str, link: str) -> str
```

Render Markdown link.

#### Examples

```python
MDDocument.render_link('my title', 'doc.md#test') # [my title](doc.md#test)
```

#### Arguments

- `title` - Link text.
- `link` - Link target.

#### Returns

A string with Markdown link.

### MDDocument().write

[🔍 find in source code](../handsdown/md_document.py#L169)

```python
def write(path: pathlib.Path) -> None
```

Write MD content to `path`.

#### Arguments

- `path` - Output path.
