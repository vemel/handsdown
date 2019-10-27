"""
Wrapper for an `ast.ClassDef` node.
"""
from typing import List, Set, Text, Generator, Optional, TYPE_CHECKING

from handsdown.ast_parser.node_records.node_record import NodeRecord
from handsdown.ast_parser.analyzers.class_analyzer import ClassAnalyzer
import handsdown.ast_parser.smart_ast as ast
from handsdown.ast_parser.enums import RenderPart
from handsdown.ast_parser.node_records.function_record import FunctionRecord
from handsdown.ast_parser.node_records.expression_record import ExpressionRecord
from handsdown.ast_parser.node_records.attribute_record import AttributeRecord

if TYPE_CHECKING:  # pragma: no cover
    from handsdown.ast_parser.node_records.argument_record import ArgumentRecord
    from handsdown.ast_parser.type_defs import RenderExpr


class ClassRecord(NodeRecord):
    """
    Wrapper for an `ast.ClassDef` node.

    Arguments:
        node -- AST node.
    """

    def __init__(self, node):
        # type: (ast.ClassDef) -> None
        assert isinstance(node, ast.ClassDef)

        super(ClassRecord, self).__init__(node)
        self.method_records = []  # type: List[FunctionRecord]
        self.decorator_records = []  # type: List[ExpressionRecord]
        self.argument_records = []  # type: List[ArgumentRecord]
        self.base_records = []  # type: List[ExpressionRecord]
        self.support_split = True
        self.name = node.name
        self.title = self.name
        self.docstring = self._get_docstring()

    def find_record(self, name):
        # type: (Text) -> Optional[NodeRecord]
        """
        Find child method or attribute record.

        Arguments:
            name -- Record name to lookup.

        Returns:
            Itself or None.
        """
        if name == self.name:
            return self

        for method_record in self.method_records:
            if method_record.name == name:
                return method_record

        for argument_record in self.argument_records:
            if argument_record.name == name:
                return argument_record

        return None

    @property
    def related_names(self):
        # type: () -> Set[Text]
        result = set()  # type: Set[Text]
        for decorator in self.decorator_records:
            result.add(decorator.name)
            result.update(decorator.related_names)
        for base in self.base_records:
            result.add(base.name)
            result.update(base.related_names)
        for method_record in self.method_records:
            if method_record.name == "__init__":
                result.update(method_record.related_names)
        return result

    def iter_records(self):
        # type: () -> Generator[NodeRecord, None, None]
        """
        Iterate over Class public methods.

        Yields:
            A child record.
        """
        for method in self.get_public_methods():
            yield method

        for attribute_record in self.attribute_records:
            yield attribute_record

    def get_public_methods(self):
        # type: () -> List[FunctionRecord]
        """
        Get Class public methods.

        Skips methods with names starting with `_` and magic methods  `__` if
        they have no docstring. Method `__init__` is always skipped.

        Returns:
            A list of child records.
        """
        result = []
        for method_record in self.method_records:
            if method_record.name == "__init__":
                continue

            result.append(method_record)
        return result

    def _parse(self):
        # type: () -> None
        assert isinstance(self.node, ast.ClassDef)

        analyzer = ClassAnalyzer()
        analyzer.visit(self.node)

        for method_node in analyzer.method_nodes:
            self.method_records.append(FunctionRecord(method_node, is_method=True))

        for base_node in analyzer.base_nodes:
            self.base_records.append(ExpressionRecord(base_node))

        for decorator_node in analyzer.decorator_nodes:
            self.decorator_records.append(ExpressionRecord(decorator_node))

        for attribute_node in analyzer.attribute_nodes:
            self.attribute_records.append(AttributeRecord(attribute_node))

        self.method_records.sort(key=lambda x: x.name)

    def _render_parts(self, indent=0):
        # type: (int) -> List[RenderExpr]
        parts = []  # type: List[RenderExpr]
        for decorator_record in self.decorator_records:
            parts.append(decorator_record)
            parts.append(RenderPart.LINE_BREAK)

        parts.append("class ")
        parts.append(self.name)
        parts.append("(")
        if self.base_records:
            parts.append(RenderPart.MULTI_LINE_INDENT)
            base_count = 0
            for base_record in self.base_records:
                if base_count > 0:
                    parts.append(",")
                    parts.append(RenderPart.SINGLE_LINE_SPACE)
                    parts.append(RenderPart.MULTI_LINE_BREAK)
                base_count += 1
                parts.append(base_record)
            parts.append(RenderPart.MULTI_LINE_COMMA)
            parts.append(RenderPart.MULTI_LINE_UNINDENT)
        parts.append("):")

        for method in self.method_records:
            if method.name == "__init__":
                parts.append(RenderPart.LINE_INDENT)
                parts.append(method)
                parts.append(RenderPart.LINE_UNINDENT)

        return parts
