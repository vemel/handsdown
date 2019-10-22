import ast

from handsdown.ast_parser.import_record import ImportRecord
from handsdown.ast_parser.class_record import ClassRecord
from handsdown.ast_parser.function_record import FunctionRecord


class ModuleAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.import_records = []
        self.class_records = []
        self.function_records = []

    def visit_Import(self, node):
        for alias in node.names:
            record = ImportRecord(node, alias)
            record.source = alias.name
            record.local_name = alias.asname
            self.import_records.append(record)

    def visit_ImportFrom(self, node):
        for alias in node.names:
            record = ImportRecord(node, alias)
            record.source = node.module
            record.name = alias.name
            record.local_name = alias.asname
            self.import_records.append(record)

    def visit_ClassDef(self, node):
        record = ClassRecord(node)
        self.class_records.append(record)

    def visit_FunctionDef(self, node):
        record = FunctionRecord(node)
        self.function_records.append(record)
