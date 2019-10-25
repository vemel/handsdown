"""
AST analyzer for `ast.ClassDef` records.
"""
from handsdown.ast_parser.node_records.function_record import FunctionRecord
from handsdown.ast_parser.node_records.attribute_record import AttributeRecord
from handsdown.ast_parser.analyzers.base_analyzer import BaseAnalyzer
import handsdown.ast_parser.smart_ast as ast


class ClassAnalyzer(BaseAnalyzer):
    """
    AST analyzer for `ast.ClassDef` records.
    """

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
        if node.name.startswith("_") and not node.name.startswith("__"):
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

        record = AttributeRecord(node)
        self.attribute_records.append(record)

    # def generic_visit(self, _node):
    #     # type: (ast.AST) -> None
    #     pass
