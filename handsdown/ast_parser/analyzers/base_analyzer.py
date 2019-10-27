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


class BaseAnalyzer(ast.NodeVisitor):
    """
    Base AST analyzer.

    Has lists for all objects for different analyzers.
    """

    def __init__(self):
        # type: () -> None
        self.related_names = []  # type: List[Text]
