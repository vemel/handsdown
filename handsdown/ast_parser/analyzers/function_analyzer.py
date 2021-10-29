"""
AST analyzer for `ast.FunctionDef` records.
"""
from typing import Any, List, Optional, Sequence

import handsdown.ast_parser.smart_ast as ast
from handsdown.ast_parser.analyzers.base_analyzer import BaseAnalyzer
from handsdown.ast_parser.node_records.argument_record import ArgumentRecord
from handsdown.ast_parser.type_defs import ASTFunctionDef


class FunctionAnalyzer(BaseAnalyzer):
    """
    AST analyzer for `ast.FunctionDef` records.
    """

    def __init__(self) -> None:
        super().__init__()
        self.argument_records: List[ArgumentRecord] = []
        self.decorator_nodes: List[ast.expr] = []
        self.return_type_hint: Optional[ast.expr] = None

    @staticmethod
    def _get_argument_record(arg: ast.arg, prefix: str = "") -> ArgumentRecord:
        type_hint = None
        if isinstance(arg, ast.Name):
            name = arg.id
        elif isinstance(arg, str):
            name = str(arg)
        else:
            if arg.annotation:
                type_hint = arg.annotation

            name = arg.arg

        return ArgumentRecord(arg, name=name, type_hint=type_hint, prefix=prefix)

    def visit_arguments(self, node: ast.arguments) -> None:
        """
        Parse info about class method statements.

        Adds new `ArgumentRecord` entry to `argument_records` for each argument.

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
                arg1: str,
                arg_default: str = "value",
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
        # FIXME: this works only for py38
        if hasattr(node, "posonlyargs"):
            for arg in getattr(node, "posonlyargs"):
                record = self._get_argument_record(arg)
                self.argument_records.append(record)

        for arg in node.args:
            record = self._get_argument_record(arg)
            self.argument_records.append(record)

        for index, default in enumerate(node.defaults):
            argument_index = len(self.argument_records) - len(node.defaults) + index
            self.argument_records[argument_index].set_default(default)

        # FIXME: `AST2` ast.args does not have `kwonlyargs` attribute
        if hasattr(node, "kwonlyargs"):
            kwonlyargs: Sequence[ast.arg] = node.kwonlyargs  # type: ignore
            for arg in kwonlyargs:
                record = self._get_argument_record(arg)
                self.argument_records.append(record)

            kw_defaults: Sequence[Any] = node.kw_defaults  # type: ignore
            for index, default in enumerate(kw_defaults):
                argument_index = len(self.argument_records) - len(kw_defaults) + index
                self.argument_records[argument_index].set_default(default)

        if node.vararg is not None:
            record = self._get_argument_record(node.vararg, prefix="*")
            self.argument_records.append(record)

        if node.kwarg is not None:
            record = self._get_argument_record(node.kwarg, prefix="**")
            self.argument_records.append(record)

    def _visit_FunctionDef(self, node: ASTFunctionDef) -> None:
        for decorator_node in node.decorator_list:
            self.decorator_nodes.append(decorator_node)
        self.visit(node.args)

        # FIXME: `AST2` FunctionDef has no `returns` attribute
        if hasattr(node, "returns") and node.returns:  # type: ignore
            returns: ast.expr = node.returns  # type: ignore
            self.return_type_hint = returns

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        """
        Entrypoint for the analyzer.

        Visits each node from `node.args`.
        Adds new `ast.expr` entry to `decorator_nodes` for each node
        from `node.decorator_list`.
        Sets `return_type_hint` to `node.returns` if it defined.

        Examples::

            def my_func():
                return result

        Arguments:
            node -- AST node.
        """
        self._visit_FunctionDef(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        """
        Entrypoint for the analyzer for asynchronous functions.

        Visits each node from `node.args`.
        Adds new `ast.expr` entry to `decorator_nodes` for each node
        from `node.decorator_list`.
        Sets `return_type_hint` to `node.returns` if it defined.

        Examples::

            async def my_func():
                return await result

        Arguments:
            node -- AST node.
        """
        self._visit_FunctionDef(node)

    def generic_visit(self, node: ast.AST) -> None:
        """
        Do nothing for unknown `ast.AST` nodes.

        Arguments:
            node -- AST node.
        """
