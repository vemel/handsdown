"""
Different AST-related types collection.
"""
from typing import TYPE_CHECKING, Union

import handsdown.ast_parser.smart_ast as ast

if TYPE_CHECKING:
    from handsdown.ast_parser.enums import RenderPart
    from handsdown.ast_parser.node_records.node_record import NodeRecord
else:
    RenderPart = object
    NodeRecord = object

# Ready for render expression
RenderExpr = Union[NodeRecord, str, RenderPart]

# AST node or text
Node = Union[str, ast.AST]

# Not ready for render expression, AST has to be wrapped
DirtyRenderExpr = Union[ast.AST, str, RenderPart]

# Iterable AST types
ASTIterable = Union[ast.List, ast.Set, ast.Tuple]

# AST import node
ASTImport = Union[ast.Import, ast.ImportFrom]

# AST import node
ASTFunctionDef = Union[ast.FunctionDef, ast.AsyncFunctionDef]
