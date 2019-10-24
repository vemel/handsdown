from typing import Optional, List, Text
import ast

from handsdown.ast_parser.node_records.argument_record import ArgumentRecord
from handsdown.ast_parser.node_records.expression_record import ExpressionRecord
from handsdown.ast_parser.analyzers.base_analyzer import BaseAnalyzer
from handsdown.utils import isinstance_str


class FunctionAnalyzer(BaseAnalyzer):
    def __init__(self):
        # type: () -> None
        super(FunctionAnalyzer, self).__init__()
        self.argument_records = []  # type: List[ArgumentRecord]
        self.decorator_records = []  # type: List[ExpressionRecord]
        self.return_type_hint = None  # type: Optional[ExpressionRecord]

    @staticmethod
    def _get_argument_record(arg, default, prefix=""):
        # type: (ast.arg, Optional[ExpressionRecord], Text) -> ArgumentRecord
        type_hint = None
        if isinstance(arg, ast.Name):
            name = arg.id
        elif isinstance_str(arg):
            name = str(arg)
        else:
            if arg.annotation:
                type_hint = ExpressionRecord(arg.annotation)

            name = arg.arg

        return ArgumentRecord(
            arg, name=name, default=default, type_hint=type_hint, prefix=prefix
        )

    def visit_arguments(self, node):
        # type: (ast.arguments) -> None
        for index, arg in enumerate(node.args):
            default = None
            default_index = len(node.defaults) - len(node.args) + index
            if default_index >= 0:
                default = ExpressionRecord(node.defaults[default_index])

            record = self._get_argument_record(arg, default)
            self.argument_records.append(record)

        # FIXME: this works only for py38
        if hasattr(node, "posonlyargs"):
            for arg in getattr(node, "posonlyargs"):
                record = self._get_argument_record(arg, None)
                self.argument_records.append(record)

        # FIXME: py27 ast.args does not have `kwonlyargs` attribute
        if hasattr(node, "kwonlyargs"):
            for index, arg in enumerate(node.kwonlyargs):
                default = None
                default_index = len(node.kw_defaults) - len(node.kwonlyargs) + index
                if default_index >= 0:
                    default = ExpressionRecord(node.kw_defaults[default_index])

                record = self._get_argument_record(arg, default)
                self.argument_records.append(record)

        if node.vararg is not None:
            record = self._get_argument_record(node.vararg, None, prefix="*")
            self.argument_records.append(record)

        if node.kwarg is not None:
            record = self._get_argument_record(node.kwarg, None, prefix="**")
            self.argument_records.append(record)

    def visit_Name(self, node):
        # type: (ast.Name) -> None
        self.decorator_records.append(ExpressionRecord(node))

    def visit_Attribute(self, node):
        # type: (ast.Attribute) -> None
        self.decorator_records.append(ExpressionRecord(node))

    def visit_FunctionDef(self, node):
        # type: (ast.FunctionDef) -> None
        for decorator_node in node.decorator_list:
            self.visit(decorator_node)
        self.visit(node.args)

        # FIXME: in py27 FunctionDef has no `returns` attribute
        if hasattr(node, "returns") and node.returns:
            self.return_type_hint = ExpressionRecord(node.returns)

    def visit_Subscript(self, node):
        # type: (ast.Subscript) -> None
        self.return_type_hint = ExpressionRecord(node)

    def generic_visit(self, _node):
        # type: (ast.AST) -> None
        # print("node", _node, type(_node), _node.value)
        pass
