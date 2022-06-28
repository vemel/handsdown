"""
Wrapper for an `ast.FunctionDef` node.
"""
import re
from typing import Iterable, List, Optional, Set

import handsdown.ast_parser.smart_ast as ast
from handsdown.ast_parser.analyzers.function_analyzer import FunctionAnalyzer
from handsdown.ast_parser.node_records.argument_record import ArgumentRecord
from handsdown.ast_parser.node_records.expression_record import ExpressionRecord
from handsdown.ast_parser.node_records.node_record import NodeRecord
from handsdown.ast_parser.node_records.text_record import TextRecord
from handsdown.ast_parser.type_defs import ASTFunctionDef, RenderExpr


class FunctionRecord(NodeRecord):
    """
    Wrapper for an `ast.FunctionDef` and `ast.AsyncFunctionDef` node.

    Arguments:
        node -- AST node.
    """

    _single_type_re = re.compile(r".+#\s*type:\s*(.+)")
    _return_type_re = re.compile(r".*#\s*type:\s*\((.*)\)\s*->\s*(.+)")

    def __init__(self, node: ASTFunctionDef, is_method: bool) -> None:
        super().__init__(node)
        self.argument_records: List[ArgumentRecord] = []
        self.is_method = is_method
        self.return_type_hint: Optional[ExpressionRecord] = None
        self.decorator_records: List[ExpressionRecord] = []
        self.is_staticmethod = False
        self.is_classmethod = False
        self.is_async = isinstance(node, ast.AsyncFunctionDef)
        self.name = node.name
        self.title = self.name
        self.docstring = self._get_docstring()

    @property
    def related_names(self) -> Set[str]:
        """
        Set of related names.
        """
        result: Set[str] = set()
        for decorator_record in self.decorator_records:
            result.update(decorator_record.related_names)
        for argument_record in self.argument_records:
            result.update(argument_record.related_names)
        if self.return_type_hint:
            result.update(self.return_type_hint.related_names)

        return result

    def _parse(self) -> None:
        analyzer = FunctionAnalyzer()
        analyzer.visit(self.node)
        self.argument_records = analyzer.argument_records

        for decorator_node in analyzer.decorator_nodes:
            self.decorator_records.append(ExpressionRecord(decorator_node))

        if analyzer.return_type_hint:
            self.return_type_hint = ExpressionRecord(analyzer.return_type_hint)

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
    def _strip_arg_type(arg_type: str) -> List[str]:
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

            result[-1] = f"{result[-1]}{c}"

        result = [i.strip() for i in result if i.strip() and i.strip() != "..."]
        return result

    def parse_type_comments(self, lines: Iterable[str]) -> None:
        """
        Extract comment type annotations from a function definiition lines.

        Sets `arguments_record` to a new `TextRecord` for each found type annotaiton.
        Also sets `return_type_hint` to a `TextRecord` if function return type found.
        """
        start_line_number = self.line_number
        for relative_line_number, line in enumerate(lines):
            match = self._return_type_re.match(line)
            if match:
                arg_type, return_type = match.groups()
                self.return_type_hint = TextRecord(self.node, return_type)
                arg_types = self._strip_arg_type(arg_type)
                for index, arg_type in enumerate(arg_types):
                    argument_index = len(self.argument_records) - len(arg_types) + index
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

                # find argument index of the next argument
                # because type annotation can be on a different line
                argument_index = -1
                for argument_index, argument in enumerate(self.argument_records):
                    if argument.line_number > line_number:
                        argument_index -= 1
                        break

                if argument_index >= 0:
                    argument = self.argument_records[argument_index]
                    argument.type_hint = TextRecord(argument.node, arg_type.strip())

    def _render_parts(self) -> List[RenderExpr]:
        return [f"def {self.name}()"]

    def is_init(self) -> bool:
        """
        Returns True if function is an __init__ method.
        """
        return self.name == "__init__"
