# Type Defs

> Auto-generated documentation for [handsdown.ast_parser.type_defs](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/type_defs.py) module.

Different AST-related types collection.

- [Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / [Ast Parser](index.md#ast-parser) / Type Defs

#### Attributes

- [ASTImport](#astimport) - AST import node: `Union[ast.Import, ast.ImportFrom]`
- [ASTIterable](#astiterable) - Iterable AST types: `Union[ast.List, ast.Set, ast.Tuple]`
- [DirtyRenderExpr](#dirtyrenderexpr) - Not ready for render expression, AST has to be wrapped: `Union[ast.AST, Text, Sentinel]`
- [Node](#node) - AST node or text: `Union[Text, ast.AST]`
- [RenderExpr](#renderexpr) - Ready for render expression: `Union[NodeRecord, Text, Sentinel]`
