import re
from typing import List, Any, Set, Text, Optional, TYPE_CHECKING

from handsdown.ast_parser.node_records.node_record import NodeRecord
from handsdown.ast_parser.node_records.text_record import TextRecord
from handsdown.ast_parser.analyzers.function_analyzer import FunctionAnalyzer
import handsdown.ast_parser.smart_ast as ast

if TYPE_CHECKING:
    from handsdown.ast_parser.node_records.expression_record import ExpressionRecord
    from handsdown.ast_parser.node_records.argument_record import ArgumentRecord


class FunctionRecord(NodeRecord):
    _single_type_re = re.compile(r".+#\s*type:\s*(.+)")
    _return_type_re = re.compile(r".*#\s*type:\s*\((.*)\)\s*->\s*(.+)")

    def __init__(self, node, is_method):
        # type: (ast.FunctionDef, bool) -> None
        assert isinstance(node, ast.FunctionDef)

        super(FunctionRecord, self).__init__(node)
        self.argument_records = []  # type: List[ArgumentRecord]
        self.is_method = is_method
        self.return_type_hint = None  # type: Optional[ExpressionRecord]
        self.decorator_records = []  # type: List[ExpressionRecord]
        self.definition_lines = []  # type: List[Text]
        self.support_split = True
        self.is_staticmethod = False
        self.is_classmethod = False
        self.name = node.name
        self.title = self.name
        self.docstring = self._get_docstring()

    @property
    def related_names(self):
        # type: () -> Set[Text]
        result = set()  # type: Set[Text]
        for decorator_record in self.decorator_records:
            result.update(decorator_record.related_names)
        for argument_record in self.argument_records:
            result.update(argument_record.related_names)
        if self.return_type_hint:
            result.update(self.return_type_hint.related_names)

        return result

    # def _parse_decorators(self):
    #     # type: () -> None
    #     assert isinstance(self.node, ast.FunctionDef)

    #     self.decorators = []
    #     for index, expr in enumerate(self.node.decorator_list):
    #         decorator = ExpressionRecord(expr)

    #         # FIXME: py38 sets start line to def/class,
    #         # move it to the first decorator
    #         if index == 0:
    #             self.line_number = decorator.line_number

    #         decorator_name = ""
    #         if isinstance(decorator.node, ast.Name):
    #             decorator_name = decorator.node.id
    #             if decorator_name == "staticmethod":
    #                 self.is_staticmethod = True
    #             if decorator_name == "classmethod":
    #                 self.is_classmethod = True

    #         self.decorators.append(decorator)

    def _parse(self):
        # type: () -> None
        assert isinstance(self.node, ast.FunctionDef)

        analyzer = FunctionAnalyzer()
        analyzer.visit(self.node)
        self.argument_records = analyzer.argument_records
        self.decorator_records = analyzer.decorator_records
        self.return_type_hint = analyzer.return_type_hint

        # FIXME: py38 sets start line to def/class,
        # move it to the first decorator
        if self.decorator_records:
            self.line_number = self.decorator_records[0].line_number

        for decorator in self.decorator_records:
            if isinstance(decorator.node, ast.Name):
                decorator_name = decorator.node.id
                if decorator_name == "staticmethod":
                    self.is_staticmethod = True
                if decorator_name == "classmethod":
                    self.is_classmethod = True

    @staticmethod
    def _strip_arg_type(arg_type):
        # type: (Text) -> List[Text]
        bracket_count = 0
        result = [""]
        for c in arg_type:
            if c == "," and bracket_count == 0:
                result.append("")
                continue
            if c == "[":
                bracket_count += 1
            if c == "]":
                bracket_count -= 1

            result[-1] = "{}{}".format(result[-1], c)

        result = [i.strip() for i in result if i.strip() and i.strip() != "..."]
        return result

    def parse_type_comments(self, lines):
        # type: (List[Text]) -> None
        start_line_number = self.line_number
        for relative_line_number, line in enumerate(lines):
            match = self._return_type_re.match(line)
            if match:
                arg_type, return_type = match.groups()
                self.return_type_hint = TextRecord(self.node, return_type)
                arg_types = self._strip_arg_type(arg_type)
                for index, arg_type in enumerate(arg_types):
                    argument_index = len(self.argument_records) - 1 - index
                    if argument_index < 0:
                        continue

                    argument = self.argument_records[argument_index]
                    argument.type_hint = TextRecord(argument.node, arg_type.strip())
                    argument_index += 1
                break
            match = self._single_type_re.match(line)
            if match:
                arg_type = match.group(1)
                line_number = start_line_number + relative_line_number
                for argument in self.argument_records:
                    if argument.line_number == line_number:
                        argument.type_hint = TextRecord(argument.node, arg_type.strip())

    def _render_parts(self, indent):
        # type: (int) -> List[Any]
        parts = []  # type: List[Any]
        for decorator in self.decorator_records:
            parts.append("@")
            parts.append(decorator)
            parts.append(self.LINE_BREAK)

        parts.append("def ")
        parts.append(self.name)
        parts.append("(")
        if self.argument_records:
            start_index = 0
            if self.is_method and not self.is_staticmethod:
                start_index = 1
            arguments = self.argument_records[start_index:]
            if arguments:
                parts.append(self.MULTI_LINE_INDENT)
                for argument in arguments[:-1]:
                    parts.append(argument)
                    parts.append(",")
                    parts.append(self.SINGLE_LINE_SPACE)
                    parts.append(self.MULTI_LINE_BREAK)
                parts.append(arguments[-1])
                parts.append(self.MULTI_LINE_COMMA)
                parts.append(self.MULTI_LINE_UNINDENT)
        parts.append(")")
        if self.return_type_hint:
            parts.append(" -> ")
            parts.append(self.return_type_hint)

        parts.append(":")
        return parts
