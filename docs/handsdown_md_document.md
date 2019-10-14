# Handsdown: MDDocument

- [Handsdown: MDDocument](#handsdown-mddocument)
  - [MDDocument](#mddocument)
    - [MDDocument().append](#mddocumentappend)
    - [MDDocument().ensure_toc_exists](#mddocumentensure_toc_exists)
    - [MDDocument().generate_toc_section](#mddocumentgenerate_toc_section)
    - [MDDocument.get_anchor_link](#mddocumentget_anchor_link)
    - [MDDocument.is_toc](#mddocumentis_toc)
    - [MDDocument().write](#mddocumentwrite)

> Auto-generated documentation for [handsdown.md_document](../handsdown/md_document.py) module.

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

[🔍 find in source code](../handsdown/md_document.py#L132)

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

### MDDocument().generate_toc_section

[🔍 find in source code](../handsdown/md_document.py#L149)

```python
def generate_toc_section(max_depth: int = 3) -> str
```

Generate Table of Contents MD content.

#### Arguments

- `max_depth` - Add headers to ToC only up to this level.

#### Returns

A string with ToC.

### MDDocument.get_anchor_link

[🔍 find in source code](../handsdown/md_document.py#L76)

```python
def get_anchor_link(title: str) -> str
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

### MDDocument().write

[🔍 find in source code](../handsdown/md_document.py#L122)

```python
def write(path: pathlib.Path) -> None
```

Write MD content to `path`.

#### Arguments

- `path` - Output path.
