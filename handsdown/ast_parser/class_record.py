import ast

from handsdown.ast_parser.node_record import NodeRecord
from handsdown.ast_parser.expression_record import ExpressionRecord
from handsdown.ast_parser.class_analyzer import ClassAnalyzer


class ClassRecord(NodeRecord):
    def __init__(self, node):
        super(ClassRecord, self).__init__(node)
        self.method_records = []
        self.decorators = []
        self.bases = []
        self.support_split = True
        self._parse_node()

    def get_doc_methods(self):
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

    def _parse_node(self):
        self.name = self.node.name
        self.docstring = ast.get_docstring(self.node)
        self.decorators = []
        for decorator in self.node.decorator_list:
            record = ExpressionRecord(decorator)
            self.decorators.append(record)
            self.related_names.update(record.related_names)

        self.bases = []
        for base in self.node.bases:
            record = ExpressionRecord(base)
            self.bases.append(record)
            self.related_names.update(record.related_names)

        analyzer = ClassAnalyzer()
        analyzer.visit(self.node)
        for record in analyzer.method_records:
            self.method_records.append(record)

    def _render_parts(self, indent=0):
        parts = []
        for decorator in self.decorators:
            parts.append(decorator.render(indent))
            parts.append(self.FORCE_LINE_BREAK)

        parts.append("class ")
        parts.append(self.name)
        parts.append("(")
        if self.bases:
            parts.append(self.LINE_INDENT)
            for base in self.bases:
                parts.append(base)
                parts.append(self.LINE_BREAK)
            parts.append(self.LINE_UNINDENT)
        parts.append("):")

        for method in self.method_records:
            if method.name == "__init__":
                parts.append(self.FORCE_LINE_INDENT)
                parts.append(method)

        return parts
