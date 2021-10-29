# Type Defs

> Auto-generated documentation for [handsdown.ast_parser.type_defs](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/type_defs.py) module.

Different AST-related types collection.

- [Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / [AST Parser.](index.md#ast-parser) / Type Defs

#### Attributes

- `RenderExpr` - Ready for render expression: `Union[(NodeRecord, str, RenderPart)]`
- `Node` - AST node or text: `Union[(str, ast.AST)]`
- `DirtyRenderExpr` - Not ready for render expression, AST has to be wrapped: `Union[(ast.AST, str, RenderPart)]`
- `ASTIterable` - Iterable AST types: `Union[(ast.List, ast.Set, ast.Tuple)]`
- `ASTImport` - AST import node: `Union[(ast.Import, ast.ImportFrom)]`
- `ASTFunctionDef` - AST import node: `Union[(ast.FunctionDef, ast.AsyncFunctionDef)]`
