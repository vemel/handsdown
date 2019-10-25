"""
AST analyzer for `ast.expr` records.
"""
from typing import TYPE_CHECKING

from handsdown.ast_parser.analyzers.base_analyzer import BaseAnalyzer
from handsdown.ast_parser.enums import RenderPart
import handsdown.ast_parser.smart_ast as ast

if TYPE_CHECKING:  # pragma: no cover
    from typing import Optional
    from handsdown.ast_parser.type_defs import ASTIterable


class ExpressionAnalyzer(BaseAnalyzer):
    """
    AST analyzer for `ast.expr` records.

    Prepares `parts` for `NodeRecord.render` method.
    """

    BINOP_SYMBOLS = {
        ast.Add: "+",
        ast.Sub: "-",
        ast.Mult: "*",
        ast.Div: "/",
        ast.Mod: "%",
        ast.Pow: "**",
        ast.LShift: "<<",
        ast.RShift: ">>",
        ast.BitOr: "|",
        ast.BitXor: "^",
        ast.BitAnd: "&",
        ast.FloorDiv: "//",
    }

    BOOLOP_SYMBOLS = {ast.And: "and", ast.Or: "or"}

    CMPOP_SYMBOLS = {
        ast.Eq: "==",
        ast.NotEq: "!=",
        ast.Lt: "<",
        ast.LtE: "<=",
        ast.Gt: ">",
        ast.GtE: ">=",
        ast.Is: "is",
        ast.IsNot: "is not",
        ast.In: "in",
        ast.NotIn: "not in",
    }

    UNARYOP_SYMBOLS = {ast.Invert: "~", ast.Not: "not", ast.UAdd: "+", ast.USub: "-"}

    def visit_Str(self, node):
        # type: (ast.Str) -> None
        """
        Parse info from `ast.Str` node and put it to `parts`.

        Arguments:
            node -- AST node.
        """
        value = node.s
        if isinstance(value, bytes):
            value = value.decode("utf-8")
        self.parts.append(repr(value))

    def visit_Bytes(self, node):
        # type: (ast.Bytes) -> None
        """
        Parse info from `ast.Bytes` node and put it to `parts`.

        Arguments:
            node -- AST node.
        """
        value = node.s
        self.parts.append(repr(value))

    def visit_Num(self, node):
        # type: (ast.Num) -> None
        """
        Parse info from `ast.Num` node and put it to `parts`.

        Arguments:
            node -- AST node.
        """
        value = node.n
        self.parts.append(repr(value))

    def visit_Name(self, node):
        # type: (ast.Name) -> None
        """
        Parse info from `ast.Name` node and put it to `parts`.

        Arguments:
            node -- AST node.
        """
        self.parts.append(node.id)
        self.related_names.append(node.id)

    def visit_NameConstant(self, node):
        # type: (ast.NameConstant) -> None
        """
        Parse info from `ast.NameConstant` node and put it to `parts`.

        Arguments:
            node -- AST node.
        """
        self.parts.append(repr(node.value))

    def visit_Subscript(self, node):
        # type: (ast.Subscript) -> None
        """
        Parse info from `ast.Subscript` node and put it to `parts`.

        Type annotations are also matched by this method.

        Arguments:
            node -- AST node.
        """
        self.parts.append(node.value)
        self.parts.append("[")
        if isinstance(node.slice, ast.Index) and isinstance(
            node.slice.value, ast.Tuple
        ):
            self._visit_iterable(node.slice.value)
        else:
            self.parts.append(node.slice)
        self.parts.append("]")

    def visit_Attribute(self, node):
        # type: (ast.Attribute) -> None
        """
        Parse info from `ast.Attribute` node and put it to `parts`.

        Arguments:
            node -- AST node.
        """
        self.parts.append(node.value)
        self.parts.append(".")
        self.parts.append(node.attr)

    def _visit_iterable(self, node):
        # type: (ASTIterable) -> None
        """
        Parse info from an iterable node and put it to `parts`.

        Used for `ast.Tuple`, `ast.Subscript`, `ast.List`, `ast.Set`

        Arguments:
            node -- AST node.
        """
        args_count = 0
        if node.elts:
            self.parts.append(RenderPart.MULTI_LINE_INDENT)
            for element in node.elts:
                if args_count:
                    self.parts.append(",")
                    self.parts.append(RenderPart.SINGLE_LINE_SPACE)
                    self.parts.append(RenderPart.MULTI_LINE_BREAK)
                args_count += 1
                self.parts.append(element)
            self.parts.append(RenderPart.MULTI_LINE_COMMA)
            self.parts.append(RenderPart.MULTI_LINE_UNINDENT)

    def visit_List(self, node):
        # type: (ast.List) -> None
        """
        Parse info from `ast.List` node and put it to `parts`.

        Arguments:
            node -- AST node.
        """
        self.parts.append("[")
        self._visit_iterable(node)
        self.parts.append("]")

    def visit_Set(self, node):
        # type: (ast.Set) -> None
        """
        Parse info from `ast.Set` node and put it to `parts`.

        Arguments:
            node -- AST node.
        """
        self.parts.append("{")
        self._visit_iterable(node)
        self.parts.append("}")

    def visit_Tuple(self, node):
        # type: (ast.Tuple) -> None
        """
        Parse info from `ast.Tuple` node and put it to `parts`.

        Arguments:
            node -- AST node.
        """
        self.parts.append("(")
        self._visit_iterable(node)
        self.parts.append(")")

    def visit_Call(self, node):
        # type: (ast.Call) -> None
        """
        Parse info from `ast.Call` node and put it to `parts`.

        Arguments:
            node -- AST node.
        """
        self.parts.append(node.func)
        self.parts.append("(")
        self.parts.append(RenderPart.MULTI_LINE_INDENT)
        args_count = 0
        for element in node.args:
            if args_count:
                self.parts.append(",")
                self.parts.append(RenderPart.SINGLE_LINE_SPACE)
                self.parts.append(RenderPart.MULTI_LINE_BREAK)
            args_count += 1
            self.parts.append(element)
        for kwelement in node.keywords:
            if args_count:
                self.parts.append(",")
                self.parts.append(RenderPart.SINGLE_LINE_SPACE)
                self.parts.append(RenderPart.MULTI_LINE_BREAK)
            args_count += 1
            self.parts.append(kwelement)
        if args_count:
            self.parts.append(RenderPart.MULTI_LINE_COMMA)
        self.parts.append(RenderPart.MULTI_LINE_UNINDENT)
        self.parts.append(")")

    def visit_Starred(self, node):
        # type: (ast.Starred) -> None
        """
        Parse info from `ast.Starred` node and put it to `parts`.

        Arguments:
            node -- AST node.
        """
        self.parts.append("*")
        self.parts.append(node.value)

    def visit_keyword(self, node):
        # type: (ast.keyword) -> None
        """
        Parse info from `ast.keyword` node and put it to `parts`.

        Arguments:
            node -- AST node.
        """
        if not node.arg:
            self.parts.append("**")
            self.parts.append(node.value)
        else:
            self.parts.append(node.arg)
            self.parts.append("=")
            self.parts.append(node.value)

    def visit_Dict(self, node):
        # type: (ast.Dict) -> None
        """
        Parse info from `ast.Dict` node and put it to `parts`.

        Arguments:
            node -- AST node.
        """
        self.parts.append("{")
        if node.keys:
            self.parts.append(RenderPart.MULTI_LINE_INDENT)
            key_count = 0
            for index, key in enumerate(node.keys):
                if key_count:
                    self.parts.append(",")
                    self.parts.append(RenderPart.SINGLE_LINE_SPACE)
                    self.parts.append(RenderPart.MULTI_LINE_BREAK)
                key_count += 1
                self.parts.append(key)
                self.parts.append(": ")
                self.parts.append(node.values[index])
            self.parts.append(RenderPart.MULTI_LINE_COMMA)
            self.parts.append(RenderPart.MULTI_LINE_UNINDENT)
        self.parts.append("}")

    def visit_Compare(self, node):
        # type: (ast.Compare) -> None
        """
        Parse info from `ast.Compare` node and put it to `parts`.

        Arguments:
            node -- AST node.
        """
        self.parts.append(node.left)
        for op, right in zip(node.ops, node.comparators):
            self.parts.append(" ")
            self.parts.append(self.CMPOP_SYMBOLS[type(op)])
            self.parts.append(" ")
            self.parts.append(right)

    def visit_BinOp(self, node):
        # type: (ast.BinOp) -> None
        """
        Parse info from `ast.BinOp` node and put it to `parts`.

        Arguments:
            node -- AST node.
        """
        self.parts.append(node.left)
        self.parts.append(" ")
        self.parts.append(self.BINOP_SYMBOLS[type(node.op)])
        self.parts.append(" ")
        self.parts.append(node.right)

    def visit_BoolOp(self, node):
        # type: (ast.BoolOp) -> None
        """
        Parse info from `ast.BoolOp` node and put it to `parts`.

        Arguments:
            node -- AST node.
        """
        for idx, value in enumerate(node.values):
            if idx:
                self.parts.append(" ")
                self.parts.append(self.BOOLOP_SYMBOLS[type(node.op)])
                self.parts.append(" ")
            self.parts.append(value)

    def visit_UnaryOp(self, node):
        # type: (ast.UnaryOp) -> None
        """
        Parse info from `ast.UnaryOp` node and put it to `parts`.

        Arguments:
            node -- AST node.
        """
        op = self.UNARYOP_SYMBOLS[type(node.op)]
        self.parts.append(op)
        if op == "not":
            self.parts.append(" ")
        self.parts.append(node.operand)

    def visit_Lambda(self, node):
        # type: (ast.Lambda) -> None
        """
        Parse info from `ast.Lambda` node and put it to `parts`.

        Arguments:
            node -- AST node.
        """
        self.parts.append("lambda ")
        self.parts.append(node.args)
        self.parts.append(": ")
        self.parts.append(node.body)

    def visit_arguments(self, node):
        # type: (ast.arguments) -> None
        """
        Parse info from `ast.arguments` node and put it to `parts`.

        Arguments:
            node -- AST node.
        """
        arg_count = 0
        for index, arg in enumerate(node.args):
            if arg_count:
                self.parts.append(",")
                self.parts.append(RenderPart.SINGLE_LINE_SPACE)
                self.parts.append(RenderPart.MULTI_LINE_BREAK)
            arg_count += 1
            default = None
            default_index = len(node.args) - len(node.defaults) + index
            if default_index < len(node.defaults):
                default = node.defaults[default_index]

            self.parts.append(arg)
            if default is not None:
                self.parts.append("=")
                self.parts.append(default)
        if node.vararg is not None:
            if arg_count:
                self.parts.append(",")
                self.parts.append(RenderPart.SINGLE_LINE_SPACE)
                self.parts.append(RenderPart.MULTI_LINE_BREAK)

            arg_count += 1
            self.parts.append("*")
            self.parts.append(node.vararg)
        if node.kwarg is not None:
            if arg_count:
                self.parts.append(",")
                self.parts.append(RenderPart.SINGLE_LINE_SPACE)
                self.parts.append(RenderPart.MULTI_LINE_BREAK)

            arg_count += 1
            self.parts.append("**")
            self.parts.append(node.kwarg)

        if arg_count:
            self.parts.append(RenderPart.MULTI_LINE_COMMA)

    def visit_arg(self, node):
        # type: (ast.arg) -> None
        """
        Parse info from `ast.arg` node and put it to `parts`.

        Arguments:
            node -- AST node.
        """
        self.parts.append(node.arg)
        if node.annotation:
            self.parts.append(": ")
            self.parts.append(node.annotation)

    def visit_Index(self, node):
        # type: (ast.Index) -> None
        """
        Parse info from `ast.Index` node and put it to `parts`.

        Arguments:
            node -- AST node.
        """
        if isinstance(node.value, ast.Tuple):
            self._visit_iterable(node.value)
            return
        self.parts.append(node.value)

    def visit_Ellipsis(self, _node):
        # type: (ast.ASTEllipsis) -> None
        """
        Parse info from `ast.Ellipsis` node and put it to `parts`.

        Arguments:
            node -- AST node.
        """
        self.parts.append("...")

    def generic_visit(self, node):
        # type: (ast.AST) -> None
        """
        Parse info from an unknown `ast.AST` node and put `...` to `parts`.

        Arguments:
            node -- AST node.
        """
        self.parts.append("...")
