"""
AST analyzer for `ast.FunctionDef` records.
"""
from typing import Optional, List, Text

from handsdown.ast_parser.node_records.argument_record import ArgumentRecord
from handsdown.ast_parser.node_records.expression_record import ExpressionRecord
from handsdown.ast_parser.analyzers.base_analyzer import BaseAnalyzer
import handsdown.ast_parser.smart_ast as ast


class FunctionAnalyzer(BaseAnalyzer):
    """
    AST analyzer for `ast.FunctionDef` records.
    """

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
        elif isinstance(arg, str):
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
        """
        Parse info about class method statements.

        Adds new `FunctionRecord` entry to `method_records`.

        Examples::

            # simple arguments
            def my_func(
                arg1,
                arg_default="value",
                *args,
                **kwargs,
            ):
                pass

            # type annotated arguments
            def my_func_typed(
                arg1: Text,
                arg_default: Text="value",
            ):
                pass

            # keyword-only arguments
            def my_func_kw_only(
                *,
                kw_only_arg
            ):
                pass

            # pos-only arguments for py38
            def my_func_kw_only(
                pos_only_arg,
                /
            ):
                pass

        Arguments:
            node -- AST node.
        """
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

        # FIXME: `AST2` ast.args does not have `kwonlyargs` attribute
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

    def visit_FunctionDef(self, node):
        # type: (ast.FunctionDef) -> None
        """
        Entrypoint for the analyzer.

        Visits each node from `node.decorator_list` and `node.args`.
        Adds new `ExpressionRecord` entries to `decorator_records`.

        Examples::

            def my_func():
                pass

        Arguments:
            node -- AST node.
        """
        for decorator_node in node.decorator_list:
            self.decorator_records.append(ExpressionRecord(decorator_node))
        self.visit(node.args)

        # FIXME: `AST2` FunctionDef has no `returns` attribute
        if hasattr(node, "returns") and node.returns:
            self.return_type_hint = ExpressionRecord(node.returns)

    def visit_Subscript(self, node):
        # type: (ast.Subscript) -> None
        """
        Parse info about function return type annotation.

        Sets `return_type_hint` to a new `ExpressionRecord`.

        Examples::

            def my_func() -> List[Text]:
                pass

        Arguments:
            node -- AST node.
        """
        self.return_type_hint = ExpressionRecord(node)

    def generic_visit(self, _node):
        # type: (ast.AST) -> None
        """
        Do nothing for unknown `ast.AST` nodes.

        Arguments:
            node -- AST node.
        """
        print("node", _node, ExpressionRecord(_node).render())
