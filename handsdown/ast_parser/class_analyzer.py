import ast
from typing import List

from handsdown.ast_parser.function_record import FunctionRecord
from handsdown.ast_parser.attribute_record import AttributeRecord


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
        # raise ValueError(node.targets[0].id, node.value.s)
        record = AttributeRecord(node)
        self.attribute_records.append(record)
