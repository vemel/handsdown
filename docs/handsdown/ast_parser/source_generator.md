# SourceGenerator

> Auto-generated documentation for [handsdown.ast_parser.source_generator](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py) module.

- [Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / [Ast Parser](index.md#ast-parser) / SourceGenerator
  - [SourceGenerator](#sourcegenerator)
    - [SourceGenerator().body](#sourcegeneratorbody)
    - [SourceGenerator().body_or_else](#sourcegeneratorbody_or_else)
    - [SourceGenerator().decorators](#sourcegeneratordecorators)
    - [SourceGenerator().newline](#sourcegeneratornewline)
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
    - [SourceGenerator().visit_Print](#sourcegeneratorvisit_print)
    - [SourceGenerator().visit_Raise](#sourcegeneratorvisit_raise)
    - [SourceGenerator().visit_Return](#sourcegeneratorvisit_return)
    - [SourceGenerator().visit_Set](#sourcegeneratorvisit_set)
    - [SourceGenerator().visit_SetComp](#sourcegeneratorvisit_setcomp)
    - [SourceGenerator().visit_Slice](#sourcegeneratorvisit_slice)
    - [SourceGenerator().visit_Starred](#sourcegeneratorvisit_starred)
    - [SourceGenerator().visit_Str](#sourcegeneratorvisit_str)
    - [SourceGenerator().visit_Subscript](#sourcegeneratorvisit_subscript)
    - [SourceGenerator().visit_TryExcept](#sourcegeneratorvisit_tryexcept)
    - [SourceGenerator().visit_TryFinally](#sourcegeneratorvisit_tryfinally)
    - [SourceGenerator().visit_Tuple](#sourcegeneratorvisit_tuple)
    - [SourceGenerator().visit_UnaryOp](#sourcegeneratorvisit_unaryop)
    - [SourceGenerator().visit_While](#sourcegeneratorvisit_while)
    - [SourceGenerator().visit_With](#sourcegeneratorvisit_with)
    - [SourceGenerator().visit_Yield](#sourcegeneratorvisit_yield)
    - [SourceGenerator().visit_alias](#sourcegeneratorvisit_alias)
    - [SourceGenerator().visit_arguments](#sourcegeneratorvisit_arguments)
    - [SourceGenerator().visit_comprehension](#sourcegeneratorvisit_comprehension)
    - [SourceGenerator().visit_excepthandler](#sourcegeneratorvisit_excepthandler)
    - [SourceGenerator().write](#sourcegeneratorwrite)

## SourceGenerator

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L37)

```python
class SourceGenerator(ast.NodeVisitor):
    def __init__(indent_with, add_line_information=False):
```

This visitor is able to transform a well formed syntax tree into python
sourcecode.  For more details have a look at the docstring of the
`node_to_source` function.

### SourceGenerator().body

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L65)

```python
def body(statements):
```

### SourceGenerator().body_or_else

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L71)

```python
def body_or_else(node):
```

### SourceGenerator().decorators

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L78)

```python
def decorators(node):
```

### SourceGenerator().newline

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L59)

```python
def newline(node=None, extra=0):
```

### SourceGenerator().visit_Assert

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L86)

```python
def visit_Assert(node):
```

### SourceGenerator().visit_Assign

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L94)

```python
def visit_Assign(node):
```

### SourceGenerator().visit_Attribute

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L305)

```python
def visit_Attribute(node):
```

### SourceGenerator().visit_AugAssign

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L103)

```python
def visit_AugAssign(node):
```

### SourceGenerator().visit_BinOp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L378)

```python
def visit_BinOp(node):
```

### SourceGenerator().visit_BoolOp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L383)

```python
def visit_BoolOp(node: ast.BoolOp) -> None:
```

### SourceGenerator().visit_Break

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L277)

```python
def visit_Break(node):
```

### SourceGenerator().visit_Bytes

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L339)

```python
def visit_Bytes(node):
```

### SourceGenerator().visit_Call

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L309)

```python
def visit_Call(node):
```

### SourceGenerator().visit_ClassDef

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L136)

```python
def visit_ClassDef(node):
```

### SourceGenerator().visit_Compare

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L390)

```python
def visit_Compare(node: ast.Compare) -> None:
```

### SourceGenerator().visit_Continue

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L281)

```python
def visit_Continue(node):
```

### SourceGenerator().visit_Delete

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L238)

```python
def visit_Delete(node):
```

### SourceGenerator().visit_Dict

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L368)

```python
def visit_Dict(node):
```

### SourceGenerator().visit_DictComp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L471)

```python
def visit_DictComp(node: ast.DictComp) -> None:
```

### SourceGenerator().visit_Ellipsis

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L447)

```python
def visit_Ellipsis(_node: ast.Ellipsis) -> None:
```

### SourceGenerator().visit_Expr

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L123)

```python
def visit_Expr(node):
```

### SourceGenerator().visit_ExtSlice

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L426)

```python
def visit_ExtSlice(node: ast.ExtSlice) -> None:
```

### SourceGenerator().visit_For

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L192)

```python
def visit_For(node):
```

### SourceGenerator().visit_FunctionDef

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L127)

```python
def visit_FunctionDef(node):
```

### SourceGenerator().visit_GeneratorExp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L463)

```python
def visit_GeneratorExp(node: ast.GeneratorExp) -> None:
```

### SourceGenerator().visit_Global

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L261)

```python
def visit_Global(node):
```

### SourceGenerator().visit_If

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L169)

```python
def visit_If(node):
```

### SourceGenerator().visit_IfExp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L481)

```python
def visit_IfExp(node: ast.IfExp) -> None:
```

### SourceGenerator().visit_Import

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L117)

```python
def visit_Import(node):
```

### SourceGenerator().visit_ImportFrom

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L109)

```python
def visit_ImportFrom(node):
```

### SourceGenerator().visit_Lambda

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L440)

```python
def visit_Lambda(node: ast.Lambda) -> None:
```

### SourceGenerator().visit_List

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L362)

```python
def visit_List(node):
```

### SourceGenerator().visit_ListComp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L459)

```python
def visit_ListComp(node: ast.ListComp) -> None:
```

### SourceGenerator().visit_Name

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L329)

```python
def visit_Name(node):
```

### SourceGenerator().visit_NameConstant

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L333)

```python
def visit_NameConstant(node):
```

### SourceGenerator().visit_Nonlocal

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L265)

```python
def visit_Nonlocal(node):
```

### SourceGenerator().visit_Num

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L342)

```python
def visit_Num(node):
```

### SourceGenerator().visit_Pass

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L218)

```python
def visit_Pass(node):
```

### SourceGenerator().visit_Print

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L222)

```python
def visit_Print(node):
```

### SourceGenerator().visit_Raise

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L285)

```python
def visit_Raise(node):
```

### SourceGenerator().visit_Return

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L269)

```python
def visit_Return(node):
```

### SourceGenerator().visit_Set

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L365)

```python
def visit_Set(node):
```

### SourceGenerator().visit_SetComp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L467)

```python
def visit_SetComp(node: ast.SetComp) -> None:
```

### SourceGenerator().visit_Slice

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L414)

```python
def visit_Slice(node: ast.Slice) -> None:
```

### SourceGenerator().visit_Starred

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L489)

```python
def visit_Starred(node: ast.Starred) -> None:
```

### SourceGenerator().visit_Str

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L336)

```python
def visit_Str(node):
```

### SourceGenerator().visit_Subscript

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L407)

```python
def visit_Subscript(node: ast.Subscript) -> None:
```

### SourceGenerator().visit_TryExcept

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L246)

```python
def visit_TryExcept(node):
```

### SourceGenerator().visit_TryFinally

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L253)

```python
def visit_TryFinally(node):
```

### SourceGenerator().visit_Tuple

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L345)

```python
def visit_Tuple(node):
```

### SourceGenerator().visit_UnaryOp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L397)

```python
def visit_UnaryOp(node: ast.UnaryOp) -> None:
```

### SourceGenerator().visit_While

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L201)

```python
def visit_While(node):
```

### SourceGenerator().visit_With

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L208)

```python
def visit_With(node):
```

### SourceGenerator().visit_Yield

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L433)

```python
def visit_Yield(node: ast.Yield) -> None:
```

### SourceGenerator().visit_alias

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L496)

```python
def visit_alias(node: ast.alias) -> None:
```

### SourceGenerator().visit_arguments

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L526)

```python
def visit_arguments(node: ast.arguments) -> None:
```

### SourceGenerator().visit_comprehension

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L502)

```python
def visit_comprehension(node: ast.comprehension) -> None:
```

### SourceGenerator().visit_excepthandler

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L513)

```python
def visit_excepthandler(node: ast.ExceptHandler) -> None:
```

### SourceGenerator().write

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L51)

```python
def write(x):
```
