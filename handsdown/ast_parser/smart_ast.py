# pylint: disable=no-name-in-module
"""
Smart AST.

Provides compatibility between AST 2 and 3.
"""
import os
from ast import (
    AST,
    Add,
    And,
    Assign,
    AsyncFunctionDef,
    Attribute,
    Await,
    BinOp,
    BitAnd,
    BitOr,
    BitXor,
    BoolOp,
    Bytes,
    Call,
    ClassDef,
    Compare,
    Constant,
    Dict,
    DictComp,
    Div,
)
from ast import Ellipsis as ASTEllipsis  # pylint: disable=no-name-in-module
from ast import (
    Eq,
    FloorDiv,
    FormattedValue,
    FunctionDef,
    GeneratorExp,
    Gt,
    GtE,
    IfExp,
    Import,
    ImportFrom,
    In,
    Index,
    Invert,
    Is,
    IsNot,
    JoinedStr,
    Lambda,
    List,
    ListComp,
    LShift,
    Lt,
    LtE,
    Mod,
    Module,
    Mult,
    Name,
    NameConstant,
    NodeVisitor,
    Not,
    NotEq,
    NotIn,
    Num,
    Or,
    Pow,
    RShift,
    Set,
    SetComp,
    Slice,
    Starred,
    Str,
    Sub,
    Subscript,
    Tuple,
    UAdd,
    UnaryOp,
    USub,
    Yield,
    YieldFrom,
    alias,
    arg,
    arguments,
    comprehension,
    expr,
    get_docstring,
    keyword,
    parse,
    stmt,
)


def stub_with_ast27() -> None:
    from typed_ast.ast27 import AST  # type: ignore
    from typed_ast.ast27 import Add  # type: ignore
    from typed_ast.ast27 import And  # type: ignore
    from typed_ast.ast27 import Assign  # type: ignore
    from typed_ast.ast27 import Attribute  # type: ignore
    from typed_ast.ast27 import BinOp  # type: ignore
    from typed_ast.ast27 import BitAnd  # type: ignore
    from typed_ast.ast27 import BitOr  # type: ignore
    from typed_ast.ast27 import BitXor  # type: ignore
    from typed_ast.ast27 import BoolOp  # type: ignore
    from typed_ast.ast27 import Call  # type: ignore
    from typed_ast.ast27 import ClassDef  # type: ignore
    from typed_ast.ast27 import Compare  # type: ignore
    from typed_ast.ast27 import Dict  # type: ignore
    from typed_ast.ast27 import DictComp  # type: ignore
    from typed_ast.ast27 import Div  # type: ignore
    from typed_ast.ast27 import Ellipsis  # type: ignore
    from typed_ast.ast27 import Eq  # type: ignore
    from typed_ast.ast27 import FloorDiv  # type: ignore
    from typed_ast.ast27 import FunctionDef  # type: ignore
    from typed_ast.ast27 import GeneratorExp  # type: ignore
    from typed_ast.ast27 import Gt  # type: ignore
    from typed_ast.ast27 import GtE  # type: ignore
    from typed_ast.ast27 import IfExp  # type: ignore
    from typed_ast.ast27 import Import  # type: ignore
    from typed_ast.ast27 import ImportFrom  # type: ignore
    from typed_ast.ast27 import In  # type: ignore
    from typed_ast.ast27 import Index  # type: ignore
    from typed_ast.ast27 import Invert  # type: ignore
    from typed_ast.ast27 import Is  # type: ignore
    from typed_ast.ast27 import IsNot  # type: ignore
    from typed_ast.ast27 import Lambda  # type: ignore
    from typed_ast.ast27 import List  # type: ignore
    from typed_ast.ast27 import ListComp  # type: ignore
    from typed_ast.ast27 import LShift  # type: ignore
    from typed_ast.ast27 import Lt  # type: ignore
    from typed_ast.ast27 import LtE  # type: ignore
    from typed_ast.ast27 import Mod  # type: ignore
    from typed_ast.ast27 import Module  # type: ignore
    from typed_ast.ast27 import Mult  # type: ignore
    from typed_ast.ast27 import Name  # type: ignore
    from typed_ast.ast27 import NodeVisitor  # type: ignore
    from typed_ast.ast27 import Not  # type: ignore
    from typed_ast.ast27 import NotEq  # type: ignore
    from typed_ast.ast27 import NotIn  # type: ignore
    from typed_ast.ast27 import Num  # type: ignore
    from typed_ast.ast27 import Or  # type: ignore
    from typed_ast.ast27 import Pow  # type: ignore
    from typed_ast.ast27 import RShift  # type: ignore
    from typed_ast.ast27 import Set  # type: ignore
    from typed_ast.ast27 import SetComp  # type: ignore
    from typed_ast.ast27 import Slice  # type: ignore
    from typed_ast.ast27 import Str  # type: ignore
    from typed_ast.ast27 import Sub  # type: ignore
    from typed_ast.ast27 import Subscript  # type: ignore
    from typed_ast.ast27 import Tuple  # type: ignore
    from typed_ast.ast27 import UAdd  # type: ignore
    from typed_ast.ast27 import UnaryOp  # type: ignore
    from typed_ast.ast27 import USub  # type: ignore
    from typed_ast.ast27 import Yield  # type: ignore
    from typed_ast.ast27 import alias  # type: ignore
    from typed_ast.ast27 import arguments  # type: ignore
    from typed_ast.ast27 import comprehension  # type: ignore
    from typed_ast.ast27 import expr  # type: ignore
    from typed_ast.ast27 import get_docstring  # type: ignore
    from typed_ast.ast27 import keyword  # type: ignore
    from typed_ast.ast27 import parse  # type: ignore
    from typed_ast.ast27 import stmt  # type: ignore

    globals()["AST"] = AST
    globals()["Add"] = Add
    globals()["And"] = And
    globals()["Assign"] = Assign
    globals()["Attribute"] = Attribute
    globals()["BinOp"] = BinOp
    globals()["BitAnd"] = BitAnd
    globals()["BitOr"] = BitOr
    globals()["BitXor"] = BitXor
    globals()["BoolOp"] = BoolOp
    globals()["Call"] = Call
    globals()["ClassDef"] = ClassDef
    globals()["Compare"] = Compare
    globals()["Dict"] = Dict
    globals()["DictComp"] = DictComp
    globals()["Div"] = Div
    globals()["Eq"] = Eq
    globals()["FloorDiv"] = FloorDiv
    globals()["FunctionDef"] = FunctionDef
    globals()["GeneratorExp"] = GeneratorExp
    globals()["Gt"] = Gt
    globals()["GtE"] = GtE
    globals()["IfExp"] = IfExp
    globals()["Import"] = Import
    globals()["ImportFrom"] = ImportFrom
    globals()["In"] = In
    globals()["Index"] = Index
    globals()["Invert"] = Invert
    globals()["Is"] = Is
    globals()["IsNot"] = IsNot
    globals()["Lambda"] = Lambda
    globals()["List"] = List
    globals()["ListComp"] = ListComp
    globals()["LShift"] = LShift
    globals()["Lt"] = Lt
    globals()["LtE"] = LtE
    globals()["Mod"] = Mod
    globals()["Module"] = Module
    globals()["Mult"] = Mult
    globals()["Name"] = Name
    globals()["Not"] = Not
    globals()["NotEq"] = NotEq
    globals()["NotIn"] = NotIn
    globals()["Num"] = Num
    globals()["Or"] = Or
    globals()["Pow"] = Pow
    globals()["RShift"] = RShift
    globals()["Set"] = Set
    globals()["SetComp"] = SetComp
    globals()["Slice"] = Slice
    globals()["Str"] = Str
    globals()["Sub"] = Sub
    globals()["Subscript"] = Subscript
    globals()["Tuple"] = Tuple
    globals()["UAdd"] = UAdd
    globals()["UnaryOp"] = UnaryOp
    globals()["USub"] = USub
    globals()["Yield"] = Yield
    globals()["alias"] = alias
    globals()["arguments"] = arguments
    globals()["comprehension"] = comprehension
    globals()["expr"] = expr
    globals()["keyword"] = keyword
    globals()["stmt"] = stmt
    globals()["Ellipsis"] = Ellipsis
    globals()["ASTEllipsis"] = Ellipsis
    globals()["get_docstring"] = get_docstring
    globals()["parse"] = parse
    globals()["NodeVisitor"] = NodeVisitor
    globals()["arg"] = object
    globals()["Bytes"] = object
    globals()["Constant"] = Str
    globals()["NameConstant"] = object
    globals()["Starred"] = object
    globals()["JoinedStr"] = object
    globals()["FormattedValue"] = object
    globals()["YieldFrom"] = object
    globals()["AsyncFunctionDef"] = object
    globals()["Await"] = object


if os.environ.get("PYTHON_VER", "3") == "2":
    stub_with_ast27()

__all__ = [
    "Add",
    "alias",
    "And",
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
