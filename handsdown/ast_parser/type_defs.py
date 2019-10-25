"""
Different AST-related types collection.
"""
from typing import Union, Text
from handsdown.ast_parser.node_records.node_record import NodeRecord
from handsdown.sentinel import Sentinel
import handsdown.ast_parser.smart_ast as ast

# Ready for render expression
RenderExpr = Union[NodeRecord, Text, Sentinel]

# AST node or text
Node = Union[Text, ast.AST]

# Not ready for render expression, AST has to be wrapped
DirtyRenderExpr = Union[ast.AST, Text, Sentinel]

# Iterable AST types
ASTIterable = Union[ast.List, ast.Set, ast.Tuple]

# AST import node
ASTImport = Union[ast.Import, ast.ImportFrom]
