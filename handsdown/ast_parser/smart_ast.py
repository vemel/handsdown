"""
Smart AST.

Re-export a stable subset of the stdlib `ast` module for Python 3.8+.
"""
import ast as _ast

AST = _ast.AST
Add = _ast.Add
And = _ast.And
AnnAssign = _ast.AnnAssign
Assign = _ast.Assign
AsyncFunctionDef = _ast.AsyncFunctionDef
Attribute = _ast.Attribute
Await = _ast.Await
BinOp = _ast.BinOp
BitAnd = _ast.BitAnd
BitOr = _ast.BitOr
BitXor = _ast.BitXor
BoolOp = _ast.BoolOp
Call = _ast.Call
ClassDef = _ast.ClassDef
Compare = _ast.Compare
Constant = _ast.Constant
Dict = _ast.Dict
DictComp = _ast.DictComp
Div = _ast.Div
Eq = _ast.Eq
FloorDiv = _ast.FloorDiv
FormattedValue = _ast.FormattedValue
FunctionDef = _ast.FunctionDef
GeneratorExp = _ast.GeneratorExp
Gt = _ast.Gt
GtE = _ast.GtE
IfExp = _ast.IfExp
Import = _ast.Import
ImportFrom = _ast.ImportFrom
In = _ast.In
Invert = _ast.Invert
Is = _ast.Is
IsNot = _ast.IsNot
JoinedStr = _ast.JoinedStr
Lambda = _ast.Lambda
List = _ast.List
ListComp = _ast.ListComp
LShift = _ast.LShift
Lt = _ast.Lt
LtE = _ast.LtE
Mod = _ast.Mod
Module = _ast.Module
Mult = _ast.Mult
Name = _ast.Name
NodeVisitor = _ast.NodeVisitor
Not = _ast.Not
NotEq = _ast.NotEq
NotIn = _ast.NotIn
Or = _ast.Or
Pow = _ast.Pow
RShift = _ast.RShift
Set = _ast.Set
SetComp = _ast.SetComp
Slice = _ast.Slice
Starred = _ast.Starred
Sub = _ast.Sub
Subscript = _ast.Subscript
Tuple = _ast.Tuple
UAdd = _ast.UAdd
UnaryOp = _ast.UnaryOp
USub = _ast.USub
Yield = _ast.Yield
YieldFrom = _ast.YieldFrom
alias = _ast.alias
arg = _ast.arg
arguments = _ast.arguments
comprehension = _ast.comprehension
expr = _ast.expr
get_docstring = _ast.get_docstring
keyword = _ast.keyword
parse = _ast.parse
stmt = _ast.stmt

# Deprecated AST classes were removed in Python 3.14; keep aliases so imports stay stable.
ASTEllipsis = getattr(_ast, "Ellipsis", _ast.Constant)
Bytes = getattr(_ast, "Bytes", _ast.Constant)
NameConstant = getattr(_ast, "NameConstant", _ast.Constant)
Num = getattr(_ast, "Num", _ast.Constant)
Str = getattr(_ast, "Str", _ast.Constant)
Index = getattr(_ast, "Index", type("Index", (_ast.AST,), {}))

__all__ = [
    "Add",
    "alias",
    "And",
    "AnnAssign",
    "arg",
    "arguments",
    "Assign",
    "AST",
    "AsyncFunctionDef",
    "Attribute",
    "Await",
    "BinOp",
    "BitAnd",
    "BitOr",
    "BitXor",
    "BoolOp",
    "Bytes",
    "Call",
    "ClassDef",
    "Compare",
    "comprehension",
    "Constant",
    "Dict",
    "DictComp",
    "Div",
    "ASTEllipsis",
    "Eq",
    "expr",
    "FloorDiv",
    "FormattedValue",
    "FunctionDef",
    "GeneratorExp",
    "get_docstring",
    "Gt",
    "GtE",
    "IfExp",
    "Import",
    "ImportFrom",
    "In",
    "Index",
    "Invert",
    "Is",
    "IsNot",
    "JoinedStr",
    "keyword",
    "Lambda",
    "List",
    "ListComp",
    "LShift",
    "Lt",
    "LtE",
    "Mod",
    "Module",
    "Mult",
    "Name",
    "NameConstant",
    "NodeVisitor",
    "Not",
    "NotEq",
    "NotIn",
    "Num",
    "Or",
    "parse",
    "Pow",
    "RShift",
    "Set",
    "SetComp",
    "Slice",
    "Starred",
    "stmt",
    "Str",
    "Sub",
    "Subscript",
    "Tuple",
    "UAdd",
    "UnaryOp",
    "USub",
    "Yield",
    "YieldFrom",
]
