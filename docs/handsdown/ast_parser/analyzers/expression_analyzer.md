# ExpressionAnalyzer

> Auto-generated documentation for [handsdown.ast_parser.analyzers.expression_analyzer](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py) module.

- [Handsdown](../../../README.md#-handsdown---python-documentation-generator) / [Modules](../../../MODULES.md#modules) / [Handsdown](../../index.md#handsdown) / [Ast Parser](../index.md#ast-parser) / [Analyzers](index.md#analyzers) / ExpressionAnalyzer
  - [ExpressionAnalyzer](#expressionanalyzer)
    - [ExpressionAnalyzer().body](#expressionanalyzerbody)
    - [ExpressionAnalyzer().body_or_else](#expressionanalyzerbody_or_else)
    - [ExpressionAnalyzer().decorators](#expressionanalyzerdecorators)
    - [ExpressionAnalyzer().newline](#expressionanalyzernewline)
    - [ExpressionAnalyzer().related_names](#expressionanalyzerrelated_names)
    - [ExpressionAnalyzer().visit_Assert](#expressionanalyzervisit_assert)
    - [ExpressionAnalyzer().visit_Assign](#expressionanalyzervisit_assign)
    - [ExpressionAnalyzer().visit_Attribute](#expressionanalyzervisit_attribute)
    - [ExpressionAnalyzer().visit_AugAssign](#expressionanalyzervisit_augassign)
    - [ExpressionAnalyzer().visit_BinOp](#expressionanalyzervisit_binop)
    - [ExpressionAnalyzer().visit_BoolOp](#expressionanalyzervisit_boolop)
    - [ExpressionAnalyzer().visit_Break](#expressionanalyzervisit_break)
    - [ExpressionAnalyzer().visit_Bytes](#expressionanalyzervisit_bytes)
    - [ExpressionAnalyzer().visit_Call](#expressionanalyzervisit_call)
    - [ExpressionAnalyzer().visit_ClassDef](#expressionanalyzervisit_classdef)
    - [ExpressionAnalyzer().visit_Compare](#expressionanalyzervisit_compare)
    - [ExpressionAnalyzer().visit_Continue](#expressionanalyzervisit_continue)
    - [ExpressionAnalyzer().visit_Delete](#expressionanalyzervisit_delete)
    - [ExpressionAnalyzer().visit_Dict](#expressionanalyzervisit_dict)
    - [ExpressionAnalyzer().visit_DictComp](#expressionanalyzervisit_dictcomp)
    - [ExpressionAnalyzer().visit_Ellipsis](#expressionanalyzervisit_ellipsis)
    - [ExpressionAnalyzer().visit_ExceptHandler](#expressionanalyzervisit_excepthandler)
    - [ExpressionAnalyzer().visit_Expr](#expressionanalyzervisit_expr)
    - [ExpressionAnalyzer().visit_ExtSlice](#expressionanalyzervisit_extslice)
    - [ExpressionAnalyzer().visit_For](#expressionanalyzervisit_for)
    - [ExpressionAnalyzer().visit_FunctionDef](#expressionanalyzervisit_functiondef)
    - [ExpressionAnalyzer().visit_GeneratorExp](#expressionanalyzervisit_generatorexp)
    - [ExpressionAnalyzer().visit_Global](#expressionanalyzervisit_global)
    - [ExpressionAnalyzer().visit_If](#expressionanalyzervisit_if)
    - [ExpressionAnalyzer().visit_IfExp](#expressionanalyzervisit_ifexp)
    - [ExpressionAnalyzer().visit_Import](#expressionanalyzervisit_import)
    - [ExpressionAnalyzer().visit_ImportFrom](#expressionanalyzervisit_importfrom)
    - [ExpressionAnalyzer().visit_Lambda](#expressionanalyzervisit_lambda)
    - [ExpressionAnalyzer().visit_List](#expressionanalyzervisit_list)
    - [ExpressionAnalyzer().visit_ListComp](#expressionanalyzervisit_listcomp)
    - [ExpressionAnalyzer().visit_Name](#expressionanalyzervisit_name)
    - [ExpressionAnalyzer().visit_NameConstant](#expressionanalyzervisit_nameconstant)
    - [ExpressionAnalyzer().visit_Nonlocal](#expressionanalyzervisit_nonlocal)
    - [ExpressionAnalyzer().visit_Num](#expressionanalyzervisit_num)
    - [ExpressionAnalyzer().visit_Pass](#expressionanalyzervisit_pass)
    - [ExpressionAnalyzer().visit_Raise](#expressionanalyzervisit_raise)
    - [ExpressionAnalyzer().visit_Return](#expressionanalyzervisit_return)
    - [ExpressionAnalyzer().visit_Set](#expressionanalyzervisit_set)
    - [ExpressionAnalyzer().visit_SetComp](#expressionanalyzervisit_setcomp)
    - [ExpressionAnalyzer().visit_Slice](#expressionanalyzervisit_slice)
    - [ExpressionAnalyzer().visit_Starred](#expressionanalyzervisit_starred)
    - [ExpressionAnalyzer().visit_Str](#expressionanalyzervisit_str)
    - [ExpressionAnalyzer().visit_Subscript](#expressionanalyzervisit_subscript)
    - [ExpressionAnalyzer().visit_Try](#expressionanalyzervisit_try)
    - [ExpressionAnalyzer().visit_Tuple](#expressionanalyzervisit_tuple)
    - [ExpressionAnalyzer().visit_UnaryOp](#expressionanalyzervisit_unaryop)
    - [ExpressionAnalyzer().visit_While](#expressionanalyzervisit_while)
    - [ExpressionAnalyzer().visit_With](#expressionanalyzervisit_with)
    - [ExpressionAnalyzer().visit_Yield](#expressionanalyzervisit_yield)
    - [ExpressionAnalyzer().visit_alias](#expressionanalyzervisit_alias)
    - [ExpressionAnalyzer().visit_arguments](#expressionanalyzervisit_arguments)
    - [ExpressionAnalyzer().visit_comprehension](#expressionanalyzervisit_comprehension)
    - [ExpressionAnalyzer().write](#expressionanalyzerwrite)

## ExpressionAnalyzer

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L43)

```python
class ExpressionAnalyzer(BaseAnalyzer):
    def __init__() -> None:
```

### ExpressionAnalyzer().body

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L70)

```python
def body(statements: List[ast.stmt]) -> None:
```

### ExpressionAnalyzer().body_or_else

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L77)

```python
def body_or_else(
    node: Union[ast.For, ast.AsyncFor, ast.While, ast.If, ast.Try],
) -> None:
```

### ExpressionAnalyzer().decorators

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L85)

```python
def decorators(
    node: Union[ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef],
) -> None:
```

### ExpressionAnalyzer().newline

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L66)

```python
def newline(extra: int = 0) -> None:
```

### ExpressionAnalyzer().related_names

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L52)

```python
@property
def related_names() -> Set[Text]:
```

### ExpressionAnalyzer().visit_Assert

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L94)

```python
def visit_Assert(node: ast.Assert) -> None:
```

### ExpressionAnalyzer().visit_Assign

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L103)

```python
def visit_Assign(node: ast.Assign) -> None:
```

### ExpressionAnalyzer().visit_Attribute

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L296)

```python
def visit_Attribute(node: ast.Attribute) -> None:
```

### ExpressionAnalyzer().visit_AugAssign

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L113)

```python
def visit_AugAssign(node: ast.AugAssign) -> None:
```

### ExpressionAnalyzer().visit_BinOp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L380)

```python
def visit_BinOp(node: ast.BinOp) -> None:
```

### ExpressionAnalyzer().visit_BoolOp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L386)

```python
def visit_BoolOp(node: ast.BoolOp) -> None:
```

### ExpressionAnalyzer().visit_Break

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L273)

```python
def visit_Break(_node: ast.Break) -> None:
```

### ExpressionAnalyzer().visit_Bytes

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L332)

```python
def visit_Bytes(node: ast.Bytes) -> None:
```

### ExpressionAnalyzer().visit_Call

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L301)

```python
def visit_Call(node: ast.Call) -> None:
```

### ExpressionAnalyzer().visit_ClassDef

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L153)

```python
def visit_ClassDef(node: ast.ClassDef) -> None:
```

### ExpressionAnalyzer().visit_Compare

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L393)

```python
def visit_Compare(node: ast.Compare) -> None:
```

### ExpressionAnalyzer().visit_Continue

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L278)

```python
def visit_Continue(_node: ast.Continue) -> None:
```

### ExpressionAnalyzer().visit_Delete

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L233)

```python
def visit_Delete(node: ast.Delete) -> None:
```

### ExpressionAnalyzer().visit_Dict

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L369)

```python
def visit_Dict(node: ast.Dict) -> None:
```

### ExpressionAnalyzer().visit_DictComp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L474)

```python
def visit_DictComp(node: ast.DictComp) -> None:
```

### ExpressionAnalyzer().visit_Ellipsis

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L450)

```python
def visit_Ellipsis(_node: ast.Ellipsis) -> None:
```

### ExpressionAnalyzer().visit_ExceptHandler

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L516)

```python
def visit_ExceptHandler(node: ast.ExceptHandler) -> None:
```

### ExpressionAnalyzer().visit_Expr

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L138)

```python
def visit_Expr(node: ast.Expr) -> None:
```

### ExpressionAnalyzer().visit_ExtSlice

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L429)

```python
def visit_ExtSlice(node: ast.ExtSlice) -> None:
```

### ExpressionAnalyzer().visit_For

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L198)

```python
def visit_For(node: ast.For) -> None:
```

### ExpressionAnalyzer().visit_FunctionDef

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L143)

```python
def visit_FunctionDef(node: ast.FunctionDef) -> None:
```

### ExpressionAnalyzer().visit_GeneratorExp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L466)

```python
def visit_GeneratorExp(node: ast.GeneratorExp) -> None:
```

### ExpressionAnalyzer().visit_Global

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L254)

```python
def visit_Global(node: ast.Global) -> None:
```

### ExpressionAnalyzer().visit_If

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L174)

```python
def visit_If(node: ast.If) -> None:
```

### ExpressionAnalyzer().visit_IfExp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L484)

```python
def visit_IfExp(node: ast.IfExp) -> None:
```

### ExpressionAnalyzer().visit_Import

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L131)

```python
def visit_Import(node: ast.Import) -> None:
```

### ExpressionAnalyzer().visit_ImportFrom

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L120)

```python
def visit_ImportFrom(node: ast.ImportFrom) -> None:
```

### ExpressionAnalyzer().visit_Lambda

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L443)

```python
def visit_Lambda(node: ast.Lambda) -> None:
```

### ExpressionAnalyzer().visit_List

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L361)

```python
def visit_List(node: ast.List) -> None:
```

### ExpressionAnalyzer().visit_ListComp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L462)

```python
def visit_ListComp(node: ast.ListComp) -> None:
```

### ExpressionAnalyzer().visit_Name

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L319)

```python
def visit_Name(node: ast.Name) -> None:
```

### ExpressionAnalyzer().visit_NameConstant

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L324)

```python
def visit_NameConstant(node: ast.NameConstant) -> None:
```

### ExpressionAnalyzer().visit_Nonlocal

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L259)

```python
def visit_Nonlocal(node: ast.Nonlocal) -> None:
```

### ExpressionAnalyzer().visit_Num

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L336)

```python
def visit_Num(node: ast.Num) -> None:
```

### ExpressionAnalyzer().visit_Pass

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L228)

```python
def visit_Pass(_node: ast.Pass) -> None:
```

### ExpressionAnalyzer().visit_Raise

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L283)

```python
def visit_Raise(node: ast.Raise) -> None:
```

### ExpressionAnalyzer().visit_Return

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L264)

```python
def visit_Return(node: ast.Return) -> None:
```

### ExpressionAnalyzer().visit_Set

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L365)

```python
def visit_Set(node: ast.Set) -> None:
```

### ExpressionAnalyzer().visit_SetComp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L470)

```python
def visit_SetComp(node: ast.SetComp) -> None:
```

### ExpressionAnalyzer().visit_Slice

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L417)

```python
def visit_Slice(node: ast.Slice) -> None:
```

### ExpressionAnalyzer().visit_Starred

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L492)

```python
def visit_Starred(node: ast.Starred) -> None:
```

### ExpressionAnalyzer().visit_Str

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L328)

```python
def visit_Str(node: ast.Str) -> None:
```

### ExpressionAnalyzer().visit_Subscript

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L410)

```python
def visit_Subscript(node: ast.Subscript) -> None:
```

### ExpressionAnalyzer().visit_Try

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L242)

```python
def visit_Try(node: ast.Try) -> None:
```

### ExpressionAnalyzer().visit_Tuple

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L340)

```python
def visit_Tuple(node: ast.Tuple) -> None:
```

### ExpressionAnalyzer().visit_UnaryOp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L400)

```python
def visit_UnaryOp(node: ast.UnaryOp) -> None:
```

### ExpressionAnalyzer().visit_While

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L208)

```python
def visit_While(node: ast.While) -> None:
```

### ExpressionAnalyzer().visit_With

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L216)

```python
def visit_With(node: ast.With) -> None:
```

### ExpressionAnalyzer().visit_Yield

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L436)

```python
def visit_Yield(node: ast.Yield) -> None:
```

### ExpressionAnalyzer().visit_alias

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L499)

```python
def visit_alias(node: ast.alias) -> None:
```

### ExpressionAnalyzer().visit_arguments

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L529)

```python
def visit_arguments(node: ast.arguments) -> None:
```

### ExpressionAnalyzer().visit_comprehension

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L505)

```python
def visit_comprehension(node: ast.comprehension) -> None:
```

### ExpressionAnalyzer().write

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L57)

```python
def write(x: Text) -> None:
```
