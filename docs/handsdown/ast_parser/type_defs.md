# Type Defs

> Auto-generated documentation for [handsdown.ast_parser.type_defs](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/type_defs.py) module.

- [Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / [Ast Parser](index.md#ast-parser) / Type Defs

#### Attributes

- `ASTImport` - AST import node: `Union[ast.Import, ast.ImportFrom]`
- `ASTIterable` - Iterable AST types: `Union[ast.List, ast.Set, ast.Tuple]`
- `DirtyRenderExpr` - Not ready for render expression, AST has to be wrapped: `Union[ast.AST, Text, Sentinel]`
- `Node` - AST node or text: `Union[Text, ast.AST]`
- `RenderExpr` - Ready for render expression: `Union[NodeRecord, Text, Sentinel]`
