import ast
from typing import List

from handsdown.ast_parser.node_records.import_record import ImportRecord
from handsdown.ast_parser.node_records.class_record import ClassRecord
from handsdown.ast_parser.node_records.function_record import FunctionRecord
from handsdown.ast_parser.node_records.attribute_record import AttributeRecord


class ModuleAnalyzer(ast.NodeVisitor):
    def __init__(self):
        # type: () -> None
        self.import_records = []  # type: List[ImportRecord]
        self.class_records = []  # type: List[ClassRecord]
        self.function_records = []  # type: List[FunctionRecord]
        self.attribute_records = []  # type: List[AttributeRecord]

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
