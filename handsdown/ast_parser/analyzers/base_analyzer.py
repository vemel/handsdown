"""
Base AST analyzer.
"""
from typing import List, Text, TYPE_CHECKING

import handsdown.ast_parser.smart_ast as ast

if TYPE_CHECKING:  # pragma: no cover
    from handsdown.ast_parser.node_records.function_record import FunctionRecord
    from handsdown.ast_parser.node_records.attribute_record import AttributeRecord
    from handsdown.ast_parser.node_records.class_record import ClassRecord
    from handsdown.ast_parser.node_records.import_record import ImportRecord
    from handsdown.ast_parser.node_records.argument_record import ArgumentRecord
    from handsdown.ast_parser.node_records.argument_record import ExpressionRecord
    from handsdown.ast_parser.type_defs import DirtyRenderExpr


class BaseAnalyzer(ast.NodeVisitor):
    """
    Base AST analyzer.

    Has lists for all objects for different analyzers.
    """

    def __init__(self):
        # type: () -> None
        self.import_records = []  # type: List[ImportRecord]
        self.class_records = []  # type: List[ClassRecord]
        self.function_records = []  # type: List[FunctionRecord]
        self.method_records = []  # type: List[FunctionRecord]
        self.attribute_records = []  # type: List[AttributeRecord]
        self.parts = []  # type: List[DirtyRenderExpr]
        self.related_names = []  # type: List[Text]
