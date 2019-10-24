import ast
from typing import List, Text, Union, Set, TYPE_CHECKING

from handsdown.ast_parser.analyzers.base_analyzer import BaseAnalyzer

if TYPE_CHECKING:
    from typing import Optional


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


class ExpressionAnalyzer(BaseAnalyzer):
    def __init__(self):
        # type: () -> None
        self.result = []  # type: List[Text]
        self.indent_with = "    "
        self.indentation = 0
        self.new_lines = 0
        self._names = set()  # type: Set[Text]

    @property
    def related_names(self):
        # type: () -> Set[Text]
        return self._names

    def write(self, x):
        # type: (Text) -> None
        if self.new_lines:
            if self.result:
                self.result.append("\n" * self.new_lines)
            self.result.append(self.indent_with * self.indentation)
            self.new_lines = 0
        self.result.append(x)

    def newline(self, extra=0):
        # type: (int) -> None
        self.new_lines = max(self.new_lines, 1 + extra)

    def body(self, statements):
        # type: (List[ast.stmt]) -> None
        self.indentation += 1
        for stmt in statements:
            self.visit(stmt)
        self.indentation -= 1

    def body_or_else(self, node):
        # type: (Union[ast.For, ast.AsyncFor, ast.While, ast.If, ast.Try]) -> None
        self.body(node.body)
        if node.orelse:
            self.newline()
            self.write("else:")
            self.body(node.orelse)

    def decorators(self, node):
        # type: (Union[ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef]) -> None
        for decorator in node.decorator_list:
            self.newline()
            self.write("@")
            self.visit(decorator)

    # Statements

    def visit_Assert(self, node):
        # type: (ast.Assert) -> None
        self.newline()
        self.write("assert ")
        self.visit(node.test)
        if node.msg is not None:
            self.write(", ")
            self.visit(node.msg)

    def visit_Assign(self, node):
        # type: (ast.Assign) -> None
        self.newline()
        for idx, target in enumerate(node.targets):
            if idx:
                self.write(", ")
            self.visit(target)
        self.write(" = ")
        self.visit(node.value)

    def visit_AugAssign(self, node):
        # type: (ast.AugAssign) -> None
        self.newline()
        self.visit(node.target)
        self.write(" " + BINOP_SYMBOLS[type(node.op)] + "= ")
        self.visit(node.value)

    def visit_ImportFrom(self, node):
        # type: (ast.ImportFrom) -> None
        self.newline()
        self.write("from %s%s import " % ("." * node.level, node.module))
        for idx, alias in enumerate(node.names):
            if idx:
                self.write(", ")
            self.write(alias.name)
            if alias.asname:
                self.write(alias.asname)

    def visit_Import(self, node):
        # type: (ast.Import) -> None
        self.newline()
        for item in node.names:
            self.write("import ")
            self.visit(item)

    def visit_Expr(self, node):
        # type: (ast.Expr) -> None
        self.newline()
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        # type: (ast.FunctionDef) -> None
        self.newline(extra=1)
        self.decorators(node)
        self.newline()
        self.write("def %s(" % node.name)
        self.visit(node.args)
        self.write("):")
        self.body(node.body)

    def visit_ClassDef(self, node):
        # type: (ast.ClassDef) -> None
        self.newline(extra=2)
        self.decorators(node)
        self.newline()
        self.write("class %s" % node.name)
        if node.bases:
            for base in node.bases:
                self.visit(base)
                if base != node.bases[-1]:
                    self.write(", ")
            self.write(")")
        self.write(":")
        for keyword in node.keywords:
            if keyword.arg:
                self.write(keyword.arg + "=")
            self.visit(keyword.value)
            if keyword != node.keywords[-1]:
                self.write(", ")
        self.body(node.body)

    def visit_If(self, node):
        # type: (ast.If) -> None
        self.newline()
        self.write("if ")
        self.visit(node.test)
        self.write(":")
        self.body(node.body)
        while True:
            else_ = node.orelse
            if len(else_) == 0:
                break
            if len(else_) == 1 and isinstance(else_[0], ast.If):
                node = else_[0]
                self.newline()
                self.write("elif ")
                self.visit(node.test)
                self.write(":")
                self.body(node.body)
            else:
                self.newline()
                self.write("else:")
                self.body(else_)
                break

    def visit_For(self, node):
        # type: (ast.For) -> None
        self.newline()
        self.write("for ")
        self.visit(node.target)
        self.write(" in ")
        self.visit(node.iter)
        self.write(":")
        self.body_or_else(node)

    def visit_While(self, node):
        # type: (ast.While) -> None
        self.newline()
        self.write("while ")
        self.visit(node.test)
        self.write(":")
        self.body_or_else(node)

    def visit_With(self, node):
        # type: (ast.With) -> None
        self.newline()
        self.write("with ")
        for item in node.items:
            self.visit(item.context_expr)
            if item.optional_vars is not None:
                self.write(" as ")
                self.visit(item.optional_vars)
        self.write(":")
        self.body(node.body)

    def visit_Pass(self, _node):
        # type: (ast.Pass) -> None
        self.newline()
        self.write("pass")

    def visit_Delete(self, node):
        # type: (ast.Delete) -> None
        self.newline()
        self.write("del ")
        for idx, target in enumerate(node.targets):
            if idx:
                self.write(", ")
            self.visit(target)

    def visit_Try(self, node):
        # type: (ast.Try) -> None
        self.newline()
        self.write("try:")
        self.body(node.body)
        for handler in node.handlers:
            self.visit(handler)
        if node.finalbody:
            self.write("finally:")
            for finalbody in node.finalbody:
                self.visit(finalbody)

    def visit_Global(self, node):
        # type: (ast.Global) -> None
        self.newline()
        self.write("global " + ", ".join(node.names))

    def visit_Nonlocal(self, node):
        # type: (ast.Nonlocal) -> None
        self.newline()
        self.write("nonlocal " + ", ".join(node.names))

    def visit_Return(self, node):
        # type: (ast.Return) -> None
        self.newline()
        if node.value is None:
            self.write("return")
        else:
            self.write("return ")
            self.visit(node.value)

    def visit_Break(self, _node):
        # type: (ast.Break) -> None
        self.newline()
        self.write("break")

    def visit_Continue(self, _node):
        # type: (ast.Continue) -> None
        self.newline()
        self.write("continue")

    def visit_Raise(self, node):
        # type: (ast.Raise) -> None
        self.newline()
        self.write("raise")
        if node.exc is not None:
            self.write(" ")
            self.visit(node.exc)
            if node.cause is not None:
                self.write(" from ")
                self.visit(node.cause)

    # Expressions

    def visit_Attribute(self, node):
        # type: (ast.Attribute) -> None
        self.visit(node.value)
        self.write("." + node.attr)

    def visit_Call(self, node):
        # type: (ast.Call) -> None
        delimiter = ""

        self.visit(node.func)
        self.write("(")
        for arg in node.args:
            self.write(delimiter)
            delimiter = ", "
            self.visit(arg)
        for keyword in node.keywords:
            self.write(delimiter)
            delimiter = ", "
            if keyword.arg is not None:
                self.write(keyword.arg + "=")
            self.visit(keyword.value)
        self.write(")")

    def visit_Name(self, node):
        # type: (ast.Name) -> None
        self._names.add(node.id)
        self.write(node.id)

    def visit_NameConstant(self, node):
        # type: (ast.NameConstant) -> None
        self.write(str(node.value))

    def visit_Str(self, node):
        # type: (ast.Str) -> None
        self.write(repr(node.s))

    def visit_Bytes(self, node):
        # type: (ast.Bytes) -> None
        self.write(repr(node.s))

    def visit_Num(self, node):
        # type: (ast.Num) -> None
        self.write(repr(node.n))

    def visit_Tuple(self, node):
        # type: (ast.Tuple) -> None
        self.write("(")
        if node.elts:
            for idx, item in enumerate(node.elts):
                if idx:
                    self.write(", ")
                self.visit(item)
        else:
            self.write(",")
        self.write(")")

    def _visit_sequence(self, elts, left, right):
        # type: (List[ast.expr], Text, Text) -> None
        self.write(left)
        for idx, item in enumerate(elts):
            if idx:
                self.write(", ")
            self.visit(item)
        self.write(right)

    def visit_List(self, node):
        # type: (ast.List) -> None
        self._visit_sequence(node.elts, "[", "]")

    def visit_Set(self, node):
        # type: (ast.Set) -> None
        self._visit_sequence(node.elts, "{", "}")

    def visit_Dict(self, node):
        # type: (ast.Dict) -> None
        self.write("{")
        for idx, (key, value) in enumerate(zip(node.keys, node.values)):
            if idx:
                self.write(", ")
            self.visit(key)
            self.write(": ")
            self.visit(value)
        self.write("}")

    def visit_BinOp(self, node):
        # type: (ast.BinOp) -> None
        self.visit(node.left)
        self.write(" %s " % BINOP_SYMBOLS[type(node.op)])
        self.visit(node.right)

    def visit_BoolOp(self, node):
        # type: (ast.BoolOp) -> None
        for idx, value in enumerate(node.values):
            if idx:
                self.write(" %s " % BOOLOP_SYMBOLS[type(node.op)])
            self.visit(value)

    def visit_Compare(self, node):
        # type: (ast.Compare) -> None
        self.visit(node.left)
        for op, right in zip(node.ops, node.comparators):
            self.write(" %s " % CMPOP_SYMBOLS[type(op)])
            self.visit(right)

    def visit_UnaryOp(self, node):
        # type: (ast.UnaryOp) -> None
        self.write("(")
        op = UNARYOP_SYMBOLS[type(node.op)]
        self.write(op)
        if op == "not":
            self.write(" ")
        self.visit(node.operand)
        self.write(")")

    def visit_Subscript(self, node):
        # type: (ast.Subscript) -> None
        self.visit(node.value)
        self.write("[")
        self.visit(node.slice)
        self.write("]")

    def visit_Slice(self, node):
        # type: (ast.Slice) -> None
        if node.lower is not None:
            self.visit(node.lower)
        self.write(":")
        if node.upper is not None:
            self.visit(node.upper)
        if node.step is not None:
            self.write(":")
            if not (isinstance(node.step, ast.Name) and node.step.id == "None"):
                self.visit(node.step)

    def visit_ExtSlice(self, node):
        # type: (ast.ExtSlice) -> None
        for idx, item in enumerate(node.dims):
            if idx:
                self.write(", ")
            self.visit(item)

    def visit_Yield(self, node):
        # type: (ast.Yield) -> None
        self.write("yield")
        if node.value is not None:
            self.write(" ")
            self.visit(node.value)

    def visit_Lambda(self, node):
        # type: (ast.Lambda) -> None
        self.write("lambda ")
        self.visit(node.args)
        self.write(": ")
        self.visit(node.body)

    def visit_Ellipsis(self, _node):
        # type: (ast.Ellipsis) -> None
        self.write("...")

    def _visit_generator(self, elt, generators, left, right):
        # type: (ast.expr, List[ast.comprehension], Text, Text) -> None
        self.write(left)
        self.visit(elt)
        for comprehension in generators:
            self.visit(comprehension)
        self.write(right)

    def visit_ListComp(self, node):
        # type: (ast.ListComp) -> None
        return self._visit_generator(node.elt, node.generators, "[", "]")

    def visit_GeneratorExp(self, node):
        # type: (ast.GeneratorExp) -> None
        return self._visit_generator(node.elt, node.generators, "(", ")")

    def visit_SetComp(self, node):
        # type: (ast.SetComp) -> None
        return self._visit_generator(node.elt, node.generators, "{", "}")

    def visit_DictComp(self, node):
        # type: (ast.DictComp) -> None
        self.write("{")
        self.visit(node.key)
        self.write(": ")
        self.visit(node.value)
        for comprehension in node.generators:
            self.visit(comprehension)
        self.write("}")

    def visit_IfExp(self, node):
        # type: (ast.IfExp) -> None
        self.visit(node.body)
        self.write(" if ")
        self.visit(node.test)
        self.write(" else ")
        self.visit(node.orelse)

    def visit_Starred(self, node):
        # type: (ast.Starred) -> None
        self.write("*")
        self.visit(node.value)

    # Helper Nodes

    def visit_alias(self, node):
        # type: (ast.alias) -> None
        self.write(node.name)
        if node.asname is not None:
            self.write(" as " + node.asname)

    def visit_comprehension(self, node):
        # type: (ast.comprehension) -> None
        self.write(" for ")
        self.visit(node.target)
        self.write(" in ")
        self.visit(node.iter)
        if node.ifs:
            for if_ in node.ifs:
                self.write(" if ")
                self.visit(if_)

    def visit_ExceptHandler(self, node):
        # type: (ast.ExceptHandler) -> None
        self.newline()
        self.write("except")
        if node.type is not None:
            self.write(" ")
            self.visit(node.type)
            if node.name is not None:
                self.write(" as ")
                self.write(node.name)
        self.write(":")
        self.body(node.body)

    def visit_arguments(self, node):
        # type: (ast.arguments) -> None
        delimiter = ""

        defaults = [None] * (
            len(node.args) - len(node.defaults)
        )  # type: List[Union[None, ast.expr]]
        defaults.extend(node.defaults)
        for arg, default in zip(node.args, defaults):
            self.write(delimiter)
            delimiter = ", "
            self.visit(arg)
            if default is not None:
                self.write("=")
                self.visit(default)
        if node.vararg is not None:
            self.write(delimiter)
            delimiter = ", "
            self.write("**{}".format(node.vararg.arg))
        if node.kwarg is not None:
            self.write(delimiter)
            delimiter = ", "
            self.write("**{}".format(node.kwarg.arg))
