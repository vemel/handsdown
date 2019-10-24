import ast
from typing import Union, Text
from handsdown.ast_parser.node_records.expression_record import ExpressionRecord
from handsdown.sentinel import Sentinel

RenderExpr = Union[ExpressionRecord, Text, Sentinel]
Node = Union[Text, ast.AST]
