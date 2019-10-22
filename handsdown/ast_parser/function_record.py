import re

from handsdown.ast_parser.node_record import NodeRecord
from handsdown.ast_parser.argument_record import ArgumentRecord
from handsdown.ast_parser.expression_record import ExpressionRecord


class FunctionRecord(NodeRecord):
    _single_type_re = re.compile(r".+#\s*type:\s*(.+)")
    _return_type_re = re.compile(r".*#\s*type:\s*\((.*)\)\s*->\s*(.+)")

    def __init__(self, node, is_method):
        super(FunctionRecord, self).__init__(node)
        self.arguments = []
        self.is_method = is_method
        self.return_type_hint = None
        self.decorators = []
        self.definition_lines = []
        self.support_split = True
        self.is_staticmethod = False
        self.is_classmethod = False

    @property
    def related_names(self):
        result = set()
        for decorator in self.decorators:
            result.update(decorator.related_names)
        for argument in self.arguments:
            result.update(argument.related_names)
        if self.return_type_hint:
            result.update(self.return_type_hint.related_names)

        return result

    def _parse(self):
        self.decorators = []
        for decorator in self.node.decorator_list:
            decorator = ExpressionRecord(decorator)
            if decorator.name == "staticmethod":
                self.is_staticmethod = True
            if decorator.name == "classmethod":
                self.is_classmethod = True
            self.decorators.append(decorator)

        for arg in self.node.args.args:
            record = ArgumentRecord(arg)
            self.arguments.append(record)

        for index, default in enumerate(self.node.args.defaults):
            argument = self.arguments[
                len(self.arguments) - len(self.node.args.defaults) + index
            ]
            argument.default = ExpressionRecord(default)

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
        start_line_number = self.line_number
        for relative_line_number, line in enumerate(lines):
            match = self._return_type_re.match(line)
            if match:
                arg_type, return_type = match.groups()
                self.return_type_hint = ExpressionRecord(return_type)
                arg_types = self._strip_arg_type(arg_type)
                for index, arg_type in enumerate(arg_types):
                    argument_index = len(self.arguments) - 1 - index
                    if argument_index < 0:
                        continue

                    argument = self.arguments[argument_index]
                    argument.type_hint = ExpressionRecord(arg_type.strip())
                    argument_index += 1
                break
            match = self._single_type_re.match(line)
            if match:
                arg_type = match.group(1)
                line_number = start_line_number + relative_line_number
                for argument in self.arguments:
                    if argument.line_number == line_number:
                        argument.type_hint = ExpressionRecord(arg_type.strip())

    def _render_parts(self, indent):
        parts = []
        for decorator in self.decorators:
            parts.append("@")
            parts.append(decorator)
            parts.append(self.FORCE_LINE_BREAK)

        parts.append("def ")
        parts.append(self.name)
        parts.append("(")
        if self.arguments:
            start_index = 0
            if self.is_method and not self.is_staticmethod:
                start_index = 1
            arguments = self.arguments[start_index:]
            if arguments:
                parts.append(self.LINE_INDENT)
                for argument in arguments[:-1]:
                    parts.append(argument)
                    parts.append(",")
                    parts.append(self.SINGLE_LINE_SPACE)
                    parts.append(self.LINE_BREAK)
                parts.append(arguments[-1])
                parts.append(self.MULTI_LINE_COMMA)
                parts.append(self.LINE_UNINDENT)
        parts.append(")")
        if self.return_type_hint:
            parts.append(" -> ")
            parts.append(self.return_type_hint)

        parts.append(":")
        return parts
