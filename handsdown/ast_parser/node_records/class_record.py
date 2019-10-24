import ast
from typing import List, Set, Text, Generator, TYPE_CHECKING

from handsdown.ast_parser.node_records.node_record import NodeRecord
from handsdown.ast_parser.node_records.expression_record import ExpressionRecord
from handsdown.ast_parser.analyzers.class_analyzer import ClassAnalyzer

if TYPE_CHECKING:
    from handsdown.ast_parser.node_records.function_record import FunctionRecord
    from handsdown.ast_parser.node_records.argument_record import ArgumentRecord
    from handsdown.ast_parser.type_defs import RenderExpr


class ClassRecord(NodeRecord):
    def __init__(self, node):
        # type: (ast.ClassDef) -> None
        assert isinstance(node, ast.ClassDef)

        super(ClassRecord, self).__init__(node)
        self.method_records = []  # type: List[FunctionRecord]
        self.decorators = []  # type: List[ExpressionRecord]
        self.argument_records = []  # type: List[ArgumentRecord]
        self.bases = []  # type: List[ExpressionRecord]
        self.support_split = True
        self.name = node.name
        self.title = self.name
        self.docstring = self._get_docstring()

    @property
    def related_names(self):
        # type: () -> Set[Text]
        result = set()  # type: Set[Text]
        for decorator in self.decorators:
            result.add(decorator.name)
            result.update(decorator.related_names)
        for base in self.bases:
            result.add(base.name)
            result.update(base.related_names)
        for method_record in self.method_records:
            if method_record.name == "__init__":
                result.update(method_record.related_names)
        return result

    def iter_records(self):
        # type: () -> Generator[NodeRecord, None, None]
        for method in self.get_public_methods():
            yield method

    def get_public_methods(self):
        # type: () -> List[FunctionRecord]
        result = []
        for method_record in self.method_records:
            if method_record.name == "__init__":
                continue
            if method_record.name.startswith("__") and not method_record.docstring:
                continue
            if method_record.name.startswith("_"):
                continue

            result.append(method_record)
        return result

    def _parse(self):
        # type: () -> None
        assert isinstance(self.node, ast.ClassDef)
        self.decorators = []
        for decorator in self.node.decorator_list:
            record = ExpressionRecord(decorator)
            self.decorators.append(record)

        self.bases = []
        for base in self.node.bases:
            record = ExpressionRecord(base)
            self.bases.append(record)

        analyzer = ClassAnalyzer()
        analyzer.visit(self.node)
        self.method_records = sorted(analyzer.method_records, key=lambda x: x.name)
        self.attribute_records = sorted(
            analyzer.attribute_records, key=lambda x: x.name
        )

    def _render_parts(self, indent=0):
        # type: (int) -> List[RenderExpr]
        parts = []  # type: List[RenderExpr]
        for decorator in self.decorators:
            parts.append(decorator)
            parts.append(self.LINE_BREAK)

        parts.append("class ")
        parts.append(self.name)
        parts.append("(")
        if self.bases:
            parts.append(self.MULTI_LINE_INDENT)
            base_count = 0
            for base in self.bases:
                if base_count > 0:
                    parts.append(",")
                    parts.append(self.SINGLE_LINE_SPACE)
                    parts.append(self.MULTI_LINE_BREAK)
                base_count += 1
                parts.append(base)
            parts.append(self.MULTI_LINE_COMMA)
            parts.append(self.MULTI_LINE_UNINDENT)
        parts.append("):")

        for method in self.method_records:
            if method.name == "__init__":
                parts.append(self.LINE_INDENT)
                parts.append(method)
                parts.append(self.LINE_UNINDENT)

        return parts
