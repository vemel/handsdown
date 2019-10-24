import ast

from handsdown.ast_parser.node_records.function_record import FunctionRecord
from handsdown.ast_parser.node_records.attribute_record import AttributeRecord
from handsdown.ast_parser.analyzers.base_analyzer import BaseAnalyzer


class ClassAnalyzer(BaseAnalyzer):
    def visit_FunctionDef(self, node):
        # type: (ast.FunctionDef) -> None
        if node.name.startswith("_") and not node.name.startswith("__"):
            return
        record = FunctionRecord(node, is_method=True)
        self.method_records.append(record)

    def visit_Assign(self, node):
        # type: (ast.Assign) -> None
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
