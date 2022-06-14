"""
Different AST-related types collection.
"""
from typing import TYPE_CHECKING, Union

import handsdown.ast_parser.smart_ast as ast

if TYPE_CHECKING:
    from handsdown.ast_parser.node_records.node_record import NodeRecord
else:
    NodeRecord = object

# Ready for render expression
RenderExpr = Union[NodeRecord, str]

# AST node or text
Node = Union[str, ast.AST]

# Iterable AST types
ASTIterable = Union[ast.List, ast.Set, ast.Tuple]

# AST import node
ASTImport = Union[ast.Import, ast.ImportFrom]

# AST import node
ASTFunctionDef = Union[ast.FunctionDef, ast.AsyncFunctionDef]
