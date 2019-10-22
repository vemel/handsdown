import ast

from handsdown.ast_parser.function_record import FunctionRecord


class ClassAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.method_records = []

    def visit_FunctionDef(self, node):
        record = FunctionRecord(node)
        self.method_records.append(record)
