import ast
from typing import List

from handsdown.ast_parser.function_record import FunctionRecord


class ClassAnalyzer(ast.NodeVisitor):
    def __init__(self):
        # type: () -> None
        self.method_records = []  # type: List[FunctionRecord]

    def visit_FunctionDef(self, node):
        # type: (ast.FunctionDef) -> None
        if node.name.startswith("_") and not node.name.startswith("__"):
            return
        record = FunctionRecord(node, is_method=True)
        self.method_records.append(record)
