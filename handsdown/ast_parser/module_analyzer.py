import ast
from typing import List

from handsdown.ast_parser.import_record import ImportRecord
from handsdown.ast_parser.class_record import ClassRecord
from handsdown.ast_parser.function_record import FunctionRecord


class ModuleAnalyzer(ast.NodeVisitor):
    def __init__(self):
        # type: () -> None
        self.import_records = []  # type: List[ImportRecord]
        self.class_records = []  # type: List[ClassRecord]
        self.function_records = []  # type: List[FunctionRecord]

    def visit_Import(self, node):
        # type: (ast.Import) -> None
        for alias in node.names:
            record = ImportRecord(node, alias)
            self.import_records.append(record)

    def visit_ImportFrom(self, node):
        # type: (ast.ImportFrom) -> None
        for alias in node.names:
            record = ImportRecord(node, alias)
            self.import_records.append(record)

    def visit_ClassDef(self, node):
        # type: (ast.ClassDef) -> None
        record = ClassRecord(node)
        self.class_records.append(record)

    def visit_FunctionDef(self, node):
        # type: (ast.FunctionDef) -> None
        record = FunctionRecord(node, is_method=False)
        self.function_records.append(record)
