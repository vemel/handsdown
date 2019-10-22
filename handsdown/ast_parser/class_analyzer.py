import ast

from handsdown.ast_parser.function_record import FunctionRecord


class ClassAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.method_records = []

    def visit_FunctionDef(self, node):
        if node.name.startswith("_") and not node.name.startswith("__"):
            return
        record = FunctionRecord(node, is_method=True)
        self.method_records.append(record)
