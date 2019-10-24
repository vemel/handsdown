import ast
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from handsdown.ast_parser.node_records.function_record import FunctionRecord
    from handsdown.ast_parser.node_records.attribute_record import AttributeRecord
    from handsdown.ast_parser.node_records.class_record import ClassRecord
    from handsdown.ast_parser.node_records.import_record import ImportRecord


class BaseAnalyzer(ast.NodeVisitor):
    def __init__(self):
        # type: () -> None
        self.import_records = []  # type: List[ImportRecord]
        self.class_records = []  # type: List[ClassRecord]
        self.function_records = []  # type: List[FunctionRecord]
        self.method_records = []  # type: List[FunctionRecord]
        self.attribute_records = []  # type: List[AttributeRecord]
