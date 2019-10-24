import ast
from typing import List

from handsdown.ast_parser.node_records.function_record import FunctionRecord
from handsdown.ast_parser.node_records.attribute_record import AttributeRecord


class ClassAnalyzer(ast.NodeVisitor):
    def __init__(self):
        # type: () -> None
        self.method_records = []  # type: List[FunctionRecord]
        self.attribute_records = []  # type: List[AttributeRecord]

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
