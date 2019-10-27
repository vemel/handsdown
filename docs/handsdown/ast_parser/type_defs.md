# Type Defs

> Auto-generated documentation for [handsdown.ast_parser.type_defs](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/type_defs.py) module.

Different AST-related types collection.

- [Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / [AST Parser](index.md#ast-parser) / Type Defs

#### Attributes

- `RenderExpr` - Ready for render expression: `Union[NodeRecord, Text, RenderPart]`
- `Node` - AST node or text: `Union[Text, ast.AST]`
- `DirtyRenderExpr` - Not ready for render expression, AST has to be wrapped: `Union[ast.AST, Text, RenderPart]`
- `ASTIterable` - Iterable AST types: `Union[ast.List, ast.Set, ast.Tuple]`
- `ASTImport` - AST import node: `Union[ast.Import, ast.ImportFrom]`
