# Type Defs

[Handsdown API Index](../../README.md#handsdown-api-index) / [Handsdown](../index.md#handsdown) / [AST Parser](./index.md#ast-parser) / Type Defs

> Auto-generated documentation for [handsdown.ast_parser.type_defs](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/type_defs.py) module.

#### Attributes

- `RenderExpr` - Ready for render expression: `Union[NodeRecord, str]`

- `Node` - AST node or text: `Union[str, ast.AST]`

- `ASTIterable` - Iterable AST types: `Union[ast.List, ast.Set, ast.Tuple]`

- `ASTImport` - AST import node: `Union[ast.Import, ast.ImportFrom]`

- `ASTFunctionDef` - AST import node: `Union[ast.FunctionDef, ast.AsyncFunctionDef]`
