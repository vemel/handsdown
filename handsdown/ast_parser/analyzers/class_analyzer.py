"""
AST analyzer for `ast.ClassDef` records.
"""
from typing import List

from handsdown.ast_parser.analyzers.base_analyzer import BaseAnalyzer
import handsdown.ast_parser.smart_ast as ast


class ClassAnalyzer(BaseAnalyzer):
    """
    AST analyzer for `ast.ClassDef` records.
    """

    def __init__(self):
        # type: () -> None
        super(ClassAnalyzer, self).__init__()
        self.base_nodes = []  # type: List[ast.expr]
        self.decorator_nodes = []  # type: List[ast.expr]
        self.method_nodes = []  # type: List[ast.FunctionDef]
        self.attribute_nodes = []  # type: List[ast.Assign]

    def visit_ClassDef(self, node):
        # type: (ast.ClassDef) -> None
        """
        Entrypoint for the analyzer.

        Adds new `ast.expr` entry to `decorator_nodes` for each node
        from `node.decorator_list`.
        Adds new `ast.expr` entry to `base_nodes` for each node
        from `node.bases`.
        Visits each node from `node.body` list to parse methods.

        Examples::

            def my_func():
                pass

        Arguments:
            node -- AST node.
        """
        for decorator_node in node.decorator_list:
            self.decorator_nodes.append(decorator_node)
        for base_node in node.bases:
            self.base_nodes.append(base_node)
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
            if name.startswith("__") and not ast.get_docstring(node, clean=False):
                return

        self.method_nodes.append(node)

    def visit_Assign(self, node):
        # type: (ast.Assign) -> None
        """
        Parse info about class attribute statements.

        Adds new `ast.Assign` entry to `attribute_nodes`.
        Skips assignments to anything pther that a new variable.
        Skips multiple assignments.
        Skips assignments with names starting with `_`.

        Examples::

            class MyClass:
                MY_MODULE_ATTR = "value"
                my_attr = "value"

                # these entries are skipped
                _MY_MODULE_ATTR = "value"
                multi_attr_1, multi_attr_2 = [1, 2]
                my_object.name = "value"

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

        self.attribute_nodes.append(node)

    def generic_visit(self, _node):
        # type: (ast.AST) -> None
        """
        Do nothing for unknown `ast.AST` nodes.

        Arguments:
            node -- AST node.
        """
