import re
import ast
from typing import List, Any, Set, Text, Optional

from handsdown.ast_parser.node_records.node_record import NodeRecord
from handsdown.ast_parser.node_records.text_record import TextRecord
from handsdown.ast_parser.node_records.argument_record import ArgumentRecord
from handsdown.ast_parser.node_records.expression_record import ExpressionRecord


class FunctionRecord(NodeRecord):
    _single_type_re = re.compile(r".+#\s*type:\s*(.+)")
    _return_type_re = re.compile(r".*#\s*type:\s*\((.*)\)\s*->\s*(.+)")

    def __init__(self, node, is_method):
        # type: (ast.FunctionDef, bool) -> None
        assert isinstance(node, ast.FunctionDef)

        super(FunctionRecord, self).__init__(node)
        self.arguments = []  # type: List[ArgumentRecord]
        self.is_method = is_method
        self.return_type_hint = None  # type: Optional[ExpressionRecord]
        self.decorators = []  # type: List[ExpressionRecord]
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
        for decorator in self.decorators:
            result.update(decorator.related_names)
        for argument in self.arguments:
            result.update(argument.related_names)
        if self.return_type_hint:
            result.update(self.return_type_hint.related_names)

        return result

    def _parse_decorators(self):
        # type: () -> None
        assert isinstance(self.node, ast.FunctionDef)

        self.decorators = []
        for index, expr in enumerate(self.node.decorator_list):
            decorator = ExpressionRecord(expr)

            # FIXME: py38 sets start line to def/class,
            # move it to the first decorator
            if index == 0:
                self.line_number = decorator.line_number

            decorator_name = ""
            if isinstance(decorator.node, ast.Name):
                decorator_name = decorator.node.id
                if decorator_name == "staticmethod":
                    self.is_staticmethod = True
                if decorator_name == "classmethod":
                    self.is_classmethod = True

            self.decorators.append(decorator)

    def _parse(self):
        # type: () -> None
        assert isinstance(self.node, ast.FunctionDef)

        self._parse_decorators()

        for arg in self.node.args.args:
            record = ArgumentRecord(arg)
            self.arguments.append(record)

        for index, default in enumerate(self.node.args.defaults):
            argument = self.arguments[
                len(self.arguments) - len(self.node.args.defaults) + index
            ]
            argument.default = ExpressionRecord(default)

        if getattr(self.node.args, "kwonlyargs", None):
            for arg in self.node.args.kwonlyargs:
                record = ArgumentRecord(arg)
                self.arguments.append(record)
            for index, default in enumerate(self.node.args.kw_defaults):
                argument = self.arguments[
                    len(self.arguments) - len(self.node.args.kw_defaults) + index
                ]
            argument.default = ExpressionRecord(default)

        if self.node.args.vararg:
            record = ArgumentRecord(self.node.args.vararg)
            record.prefix = "*"
            self.arguments.append(record)
        if self.node.args.kwarg:
            record = ArgumentRecord(self.node.args.kwarg)
            record.prefix = "**"
            self.arguments.append(record)

        # FIXME: py27 FunctionDef does not have return
        if hasattr(self.node, "returns") and self.node.returns:
            self.return_type_hint = ExpressionRecord(self.node.returns)

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
                    argument_index = len(self.arguments) - 1 - index
                    if argument_index < 0:
                        continue

                    argument = self.arguments[argument_index]
                    argument.type_hint = TextRecord(argument.node, arg_type.strip())
                    argument_index += 1
                break
            match = self._single_type_re.match(line)
            if match:
                arg_type = match.group(1)
                line_number = start_line_number + relative_line_number
                for argument in self.arguments:
                    if argument.line_number == line_number:
                        argument.type_hint = TextRecord(argument.node, arg_type.strip())

    def _render_parts(self, indent):
        # type: (int) -> List[Any]
        parts = []  # type: List[Any]
        for decorator in self.decorators:
            parts.append("@")
            parts.append(decorator)
            parts.append(self.LINE_BREAK)

        parts.append("def ")
        parts.append(self.name)
        parts.append("(")
        if self.arguments:
            start_index = 0
            if self.is_method and not self.is_staticmethod:
                start_index = 1
            arguments = self.arguments[start_index:]
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
