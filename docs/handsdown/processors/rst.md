# reStructuredText Docstring Processor.

> Auto-generated documentation for [handsdown.processors.rst](https://github.com/vemel/handsdown/blob/main/handsdown/processors/rst.py) module.

Docstring processor for restructured text docstring format.

- [Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / [Processors](index.md#processors) / reStructuredText Docstring Processor.
    - [RSTDocstringProcessor](#rstdocstringprocessor)

Supported features:

- `:param <name> <?type>: <?description>` directive is added to `Arguments` section
- `:type: <?description>` directive transformed to `Type: <type>`
- `:returns <?type>: <?description>` directive is added to `Returns` section
- `:rtype: <?description>` directive transformed to `Type: <type>`
- `:raises: <?description>` directive is added to `Raises` section
- `.. seealso::` directive is added to `See also` section
- `.. note::` directive is added to `Notes` section
- `.. warning:: <version>` directive is added to `Warnings` section
- `.. versionadded:: <version>` directive is formatted in Sphinx-style and added
  to `Notes` section
- `.. versionchanged:: <version>` directive is formatted in Sphinx-style and added
  to `Notes` section
- `.. deprecated::` directive is formatted in Sphinx-style and added to `Notes` section
- `.. code-block::` directive is formatted as Markdown Python codeblock
- `.. code-block:: <language>` directive is formatted as Markdown codeblock
- `.. math::` directive is formatted as Markdown Python codeblock
- `.. highlight::` directive is formatted as Markdown Python codeblock
- `.. highlight:: <language>` directive is formatted as Markdown codeblock

## RSTDocstringProcessor

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/processors/rst.py#L33)

```python
class RSTDocstringProcessor(BaseDocstringProcessor):
```

Docstring processor for restructured text docstring format.

#### See also

- [BaseDocstringProcessor](base.md#basedocstringprocessor)
