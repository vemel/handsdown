# SourceGenerator

> Auto-generated documentation for [handsdown.ast_parser.source_generator](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py) module.

- [Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / [Ast Parser](index.md#ast-parser) / SourceGenerator
  - [SourceGenerator](#sourcegenerator)
    - [SourceGenerator().body](#sourcegeneratorbody)
    - [SourceGenerator().body_or_else](#sourcegeneratorbody_or_else)
    - [SourceGenerator().decorators](#sourcegeneratordecorators)
    - [SourceGenerator().newline](#sourcegeneratornewline)
    - [SourceGenerator().related_names](#sourcegeneratorrelated_names)
    - [SourceGenerator().visit_Assert](#sourcegeneratorvisit_assert)
    - [SourceGenerator().visit_Assign](#sourcegeneratorvisit_assign)
    - [SourceGenerator().visit_Attribute](#sourcegeneratorvisit_attribute)
    - [SourceGenerator().visit_AugAssign](#sourcegeneratorvisit_augassign)
    - [SourceGenerator().visit_BinOp](#sourcegeneratorvisit_binop)
    - [SourceGenerator().visit_BoolOp](#sourcegeneratorvisit_boolop)
    - [SourceGenerator().visit_Break](#sourcegeneratorvisit_break)
    - [SourceGenerator().visit_Bytes](#sourcegeneratorvisit_bytes)
    - [SourceGenerator().visit_Call](#sourcegeneratorvisit_call)
    - [SourceGenerator().visit_ClassDef](#sourcegeneratorvisit_classdef)
    - [SourceGenerator().visit_Compare](#sourcegeneratorvisit_compare)
    - [SourceGenerator().visit_Continue](#sourcegeneratorvisit_continue)
    - [SourceGenerator().visit_Delete](#sourcegeneratorvisit_delete)
    - [SourceGenerator().visit_Dict](#sourcegeneratorvisit_dict)
    - [SourceGenerator().visit_DictComp](#sourcegeneratorvisit_dictcomp)
    - [SourceGenerator().visit_Ellipsis](#sourcegeneratorvisit_ellipsis)
    - [SourceGenerator().visit_ExceptHandler](#sourcegeneratorvisit_excepthandler)
    - [SourceGenerator().visit_Expr](#sourcegeneratorvisit_expr)
    - [SourceGenerator().visit_ExtSlice](#sourcegeneratorvisit_extslice)
    - [SourceGenerator().visit_For](#sourcegeneratorvisit_for)
    - [SourceGenerator().visit_FunctionDef](#sourcegeneratorvisit_functiondef)
    - [SourceGenerator().visit_GeneratorExp](#sourcegeneratorvisit_generatorexp)
    - [SourceGenerator().visit_Global](#sourcegeneratorvisit_global)
    - [SourceGenerator().visit_If](#sourcegeneratorvisit_if)
    - [SourceGenerator().visit_IfExp](#sourcegeneratorvisit_ifexp)
    - [SourceGenerator().visit_Import](#sourcegeneratorvisit_import)
    - [SourceGenerator().visit_ImportFrom](#sourcegeneratorvisit_importfrom)
    - [SourceGenerator().visit_Lambda](#sourcegeneratorvisit_lambda)
    - [SourceGenerator().visit_List](#sourcegeneratorvisit_list)
    - [SourceGenerator().visit_ListComp](#sourcegeneratorvisit_listcomp)
    - [SourceGenerator().visit_Name](#sourcegeneratorvisit_name)
    - [SourceGenerator().visit_NameConstant](#sourcegeneratorvisit_nameconstant)
    - [SourceGenerator().visit_Nonlocal](#sourcegeneratorvisit_nonlocal)
    - [SourceGenerator().visit_Num](#sourcegeneratorvisit_num)
    - [SourceGenerator().visit_Pass](#sourcegeneratorvisit_pass)
    - [SourceGenerator().visit_Raise](#sourcegeneratorvisit_raise)
    - [SourceGenerator().visit_Return](#sourcegeneratorvisit_return)
    - [SourceGenerator().visit_Set](#sourcegeneratorvisit_set)
    - [SourceGenerator().visit_SetComp](#sourcegeneratorvisit_setcomp)
    - [SourceGenerator().visit_Slice](#sourcegeneratorvisit_slice)
    - [SourceGenerator().visit_Starred](#sourcegeneratorvisit_starred)
    - [SourceGenerator().visit_Str](#sourcegeneratorvisit_str)
    - [SourceGenerator().visit_Subscript](#sourcegeneratorvisit_subscript)
    - [SourceGenerator().visit_Try](#sourcegeneratorvisit_try)
    - [SourceGenerator().visit_Tuple](#sourcegeneratorvisit_tuple)
    - [SourceGenerator().visit_UnaryOp](#sourcegeneratorvisit_unaryop)
    - [SourceGenerator().visit_While](#sourcegeneratorvisit_while)
    - [SourceGenerator().visit_With](#sourcegeneratorvisit_with)
    - [SourceGenerator().visit_Yield](#sourcegeneratorvisit_yield)
    - [SourceGenerator().visit_alias](#sourcegeneratorvisit_alias)
    - [SourceGenerator().visit_arguments](#sourcegeneratorvisit_arguments)
    - [SourceGenerator().visit_comprehension](#sourcegeneratorvisit_comprehension)
    - [SourceGenerator().write](#sourcegeneratorwrite)

## SourceGenerator

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L42)

```python
class SourceGenerator(ast.NodeVisitor):
    def __init__() -> None:
```

This visitor is able to transform a well formed syntax tree into python
sourcecode.  For more details have a look at the docstring of the
`node_to_source` function.

### SourceGenerator().body

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L74)

```python
def body(statements: List[ast.stmt]) -> None:
```

### SourceGenerator().body_or_else

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L81)

```python
def body_or_else(
    node: Union[ast.For, ast.AsyncFor, ast.While, ast.If, ast.Try],
) -> None:
```

### SourceGenerator().decorators

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L89)

```python
def decorators(
    node: Union[ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef],
) -> None:
```

### SourceGenerator().newline

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L70)

```python
def newline(extra: int = 0) -> None:
```

### SourceGenerator().related_names

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L56)

```python
@property
def related_names() -> Set[Text]:
```

### SourceGenerator().visit_Assert

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L98)

```python
def visit_Assert(node: ast.Assert) -> None:
```

### SourceGenerator().visit_Assign

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L107)

```python
def visit_Assign(node: ast.Assign) -> None:
```

### SourceGenerator().visit_Attribute

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L300)

```python
def visit_Attribute(node: ast.Attribute) -> None:
```

### SourceGenerator().visit_AugAssign

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L117)

```python
def visit_AugAssign(node: ast.AugAssign) -> None:
```

### SourceGenerator().visit_BinOp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L384)

```python
def visit_BinOp(node: ast.BinOp) -> None:
```

### SourceGenerator().visit_BoolOp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L390)

```python
def visit_BoolOp(node: ast.BoolOp) -> None:
```

### SourceGenerator().visit_Break

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L277)

```python
def visit_Break(_node: ast.Break) -> None:
```

### SourceGenerator().visit_Bytes

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L336)

```python
def visit_Bytes(node: ast.Bytes) -> None:
```

### SourceGenerator().visit_Call

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L305)

```python
def visit_Call(node: ast.Call) -> None:
```

### SourceGenerator().visit_ClassDef

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L157)

```python
def visit_ClassDef(node: ast.ClassDef) -> None:
```

### SourceGenerator().visit_Compare

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L397)

```python
def visit_Compare(node: ast.Compare) -> None:
```

### SourceGenerator().visit_Continue

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L282)

```python
def visit_Continue(_node: ast.Continue) -> None:
```

### SourceGenerator().visit_Delete

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L237)

```python
def visit_Delete(node: ast.Delete) -> None:
```

### SourceGenerator().visit_Dict

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L373)

```python
def visit_Dict(node: ast.Dict) -> None:
```

### SourceGenerator().visit_DictComp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L478)

```python
def visit_DictComp(node: ast.DictComp) -> None:
```

### SourceGenerator().visit_Ellipsis

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L454)

```python
def visit_Ellipsis(_node: ast.Ellipsis) -> None:
```

### SourceGenerator().visit_ExceptHandler

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L520)

```python
def visit_ExceptHandler(node: ast.ExceptHandler) -> None:
```

### SourceGenerator().visit_Expr

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L142)

```python
def visit_Expr(node: ast.Expr) -> None:
```

### SourceGenerator().visit_ExtSlice

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L433)

```python
def visit_ExtSlice(node: ast.ExtSlice) -> None:
```

### SourceGenerator().visit_For

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L202)

```python
def visit_For(node: ast.For) -> None:
```

### SourceGenerator().visit_FunctionDef

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L147)

```python
def visit_FunctionDef(node: ast.FunctionDef) -> None:
```

### SourceGenerator().visit_GeneratorExp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L470)

```python
def visit_GeneratorExp(node: ast.GeneratorExp) -> None:
```

### SourceGenerator().visit_Global

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L258)

```python
def visit_Global(node: ast.Global) -> None:
```

### SourceGenerator().visit_If

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L178)

```python
def visit_If(node: ast.If) -> None:
```

### SourceGenerator().visit_IfExp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L488)

```python
def visit_IfExp(node: ast.IfExp) -> None:
```

### SourceGenerator().visit_Import

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L135)

```python
def visit_Import(node: ast.Import) -> None:
```

### SourceGenerator().visit_ImportFrom

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L124)

```python
def visit_ImportFrom(node: ast.ImportFrom) -> None:
```

### SourceGenerator().visit_Lambda

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L447)

```python
def visit_Lambda(node: ast.Lambda) -> None:
```

### SourceGenerator().visit_List

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L365)

```python
def visit_List(node: ast.List) -> None:
```

### SourceGenerator().visit_ListComp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L466)

```python
def visit_ListComp(node: ast.ListComp) -> None:
```

### SourceGenerator().visit_Name

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L323)

```python
def visit_Name(node: ast.Name) -> None:
```

### SourceGenerator().visit_NameConstant

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L328)

```python
def visit_NameConstant(node: ast.NameConstant) -> None:
```

### SourceGenerator().visit_Nonlocal

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L263)

```python
def visit_Nonlocal(node: ast.Nonlocal) -> None:
```

### SourceGenerator().visit_Num

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L340)

```python
def visit_Num(node: ast.Num) -> None:
```

### SourceGenerator().visit_Pass

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L232)

```python
def visit_Pass(_node: ast.Pass) -> None:
```

### SourceGenerator().visit_Raise

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L287)

```python
def visit_Raise(node: ast.Raise) -> None:
```

### SourceGenerator().visit_Return

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L268)

```python
def visit_Return(node: ast.Return) -> None:
```

### SourceGenerator().visit_Set

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L369)

```python
def visit_Set(node: ast.Set) -> None:
```

### SourceGenerator().visit_SetComp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L474)

```python
def visit_SetComp(node: ast.SetComp) -> None:
```

### SourceGenerator().visit_Slice

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L421)

```python
def visit_Slice(node: ast.Slice) -> None:
```

### SourceGenerator().visit_Starred

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L496)

```python
def visit_Starred(node: ast.Starred) -> None:
```

### SourceGenerator().visit_Str

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L332)

```python
def visit_Str(node: ast.Str) -> None:
```

### SourceGenerator().visit_Subscript

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L414)

```python
def visit_Subscript(node: ast.Subscript) -> None:
```

### SourceGenerator().visit_Try

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L246)

```python
def visit_Try(node: ast.Try) -> None:
```

### SourceGenerator().visit_Tuple

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L344)

```python
def visit_Tuple(node: ast.Tuple) -> None:
```

### SourceGenerator().visit_UnaryOp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L404)

```python
def visit_UnaryOp(node: ast.UnaryOp) -> None:
```

### SourceGenerator().visit_While

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L212)

```python
def visit_While(node: ast.While) -> None:
```

### SourceGenerator().visit_With

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L220)

```python
def visit_With(node: ast.With) -> None:
```

### SourceGenerator().visit_Yield

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L440)

```python
def visit_Yield(node: ast.Yield) -> None:
```

### SourceGenerator().visit_alias

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L503)

```python
def visit_alias(node: ast.alias) -> None:
```

### SourceGenerator().visit_arguments

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L533)

```python
def visit_arguments(node: ast.arguments) -> None:
```

### SourceGenerator().visit_comprehension

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L509)

```python
def visit_comprehension(node: ast.comprehension) -> None:
```

### SourceGenerator().write

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L61)

```python
def write(x: Text) -> None:
```
