"""
AST analyzer for `ast.ClassDef` records.
"""
from typing import List

from handsdown.ast_parser.node_records.function_record import FunctionRecord
from handsdown.ast_parser.node_records.attribute_record import AttributeRecord
from handsdown.ast_parser.node_records.expression_record import ExpressionRecord
from handsdown.ast_parser.analyzers.base_analyzer import BaseAnalyzer
import handsdown.ast_parser.smart_ast as ast


class ClassAnalyzer(BaseAnalyzer):
    """
    AST analyzer for `ast.ClassDef` records.
    """

    def __init__(self):
        # type: () -> None
        super(ClassAnalyzer, self).__init__()
        self.base_records = []  # type: List[ExpressionRecord]
        self.decorator_records = []  # type: List[ExpressionRecord]

    def visit_ClassDef(self, node):
        # type: (ast.ClassDef) -> None
        """
        Entrypoint for the analyzer.

        Visits each node from `node.decorator_list` and `node.args`.
        Adds new `ExpressionRecord` entries to `decorator_records`.

        Examples::

            def my_func():
                pass

        Arguments:
            node -- AST node.
        """
        for decorator_node in node.decorator_list:
            self.decorator_records.append(ExpressionRecord(decorator_node))
        for base_node in node.bases:
            self.base_records.append(ExpressionRecord(base_node))
        for element in node.body:
            self.visit(element)

    def visit_FunctionDef(self, node):
        # type: (ast.FunctionDef) -> None
        """
        Parse info about class method statements.

        Adds new `FunctionRecord` entry to `method_records`.

        Examples:

            class MyClass:
                def my_method(self, arg):
                    pass

        Arguments:
            node -- AST node.
        """

        name = node.name

        # skip private methods
        if name.startswith("_") and not name.startswith("__"):
            return

        # skip magic methods with no docstrings
        if name != "__init__":
            if name.startswith("__") and not ast.get_docstring(node):
                return

        record = FunctionRecord(node, is_method=True)
        self.method_records.append(record)

    def visit_Assign(self, node):
        # type: (ast.Assign) -> None
        """
        Parse info about class attribute statements.

        Adds new `AttributeRecord` entry to `attribute_records` if it is
        a simple one-item assign.

        Examples::

            class MyClass:
                MY_MODULE_ATTR = 'value'

        Arguments:
            node -- AST node.
        """
        # skip multiple assignments
        if len(node.targets) != 1:
            return

        # skip complex assignments
        if not isinstance(node.targets[0], ast.Name):
            return

        name = node.targets[0].id

        # skip private attributes
        if name.startswith("_"):
            return

        record = AttributeRecord(node)
        self.attribute_records.append(record)

    def generic_visit(self, _node):
        # type: (ast.AST) -> None
        """
        Do nothing for unknown `ast.AST` nodes.

        Arguments:
            node -- AST node.
        """
