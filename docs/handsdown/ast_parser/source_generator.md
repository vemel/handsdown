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

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L41)

```python
class SourceGenerator(ast.NodeVisitor):
    def __init__() -> None:
```

This visitor is able to transform a well formed syntax tree into python
sourcecode.  For more details have a look at the docstring of the
`node_to_source` function.

### SourceGenerator().body

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L73)

```python
def body(statements: List[ast.stmt]) -> None:
```

### SourceGenerator().body_or_else

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L80)

```python
def body_or_else(
    node: Union[ast.For, ast.AsyncFor, ast.While, ast.If, ast.Try],
) -> None:
```

### SourceGenerator().decorators

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L88)

```python
def decorators(
    node: Union[ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef],
) -> None:
```

### SourceGenerator().newline

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L69)

```python
def newline(extra: int = 0) -> None:
```

### SourceGenerator().related_names

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L55)

```python
@property
def related_names() -> Set[Text]:
```

### SourceGenerator().visit_Assert

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L97)

```python
def visit_Assert(node: ast.Assert) -> None:
```

### SourceGenerator().visit_Assign

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L106)

```python
def visit_Assign(node: ast.Assign) -> None:
```

### SourceGenerator().visit_Attribute

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L299)

```python
def visit_Attribute(node: ast.Attribute) -> None:
```

### SourceGenerator().visit_AugAssign

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L116)

```python
def visit_AugAssign(node: ast.AugAssign) -> None:
```

### SourceGenerator().visit_BinOp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L383)

```python
def visit_BinOp(node: ast.BinOp) -> None:
```

### SourceGenerator().visit_BoolOp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L389)

```python
def visit_BoolOp(node: ast.BoolOp) -> None:
```

### SourceGenerator().visit_Break

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L276)

```python
def visit_Break(_node: ast.Break) -> None:
```

### SourceGenerator().visit_Bytes

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L335)

```python
def visit_Bytes(node: ast.Bytes) -> None:
```

### SourceGenerator().visit_Call

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L304)

```python
def visit_Call(node: ast.Call) -> None:
```

### SourceGenerator().visit_ClassDef

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L156)

```python
def visit_ClassDef(node: ast.ClassDef) -> None:
```

### SourceGenerator().visit_Compare

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L396)

```python
def visit_Compare(node: ast.Compare) -> None:
```

### SourceGenerator().visit_Continue

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L281)

```python
def visit_Continue(_node: ast.Continue) -> None:
```

### SourceGenerator().visit_Delete

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L236)

```python
def visit_Delete(node: ast.Delete) -> None:
```

### SourceGenerator().visit_Dict

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L372)

```python
def visit_Dict(node: ast.Dict) -> None:
```

### SourceGenerator().visit_DictComp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L477)

```python
def visit_DictComp(node: ast.DictComp) -> None:
```

### SourceGenerator().visit_Ellipsis

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L453)

```python
def visit_Ellipsis(_node: ast.Ellipsis) -> None:
```

### SourceGenerator().visit_ExceptHandler

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L519)

```python
def visit_ExceptHandler(node: ast.ExceptHandler) -> None:
```

### SourceGenerator().visit_Expr

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L141)

```python
def visit_Expr(node: ast.Expr) -> None:
```

### SourceGenerator().visit_ExtSlice

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L432)

```python
def visit_ExtSlice(node: ast.ExtSlice) -> None:
```

### SourceGenerator().visit_For

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L201)

```python
def visit_For(node: ast.For) -> None:
```

### SourceGenerator().visit_FunctionDef

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L146)

```python
def visit_FunctionDef(node: ast.FunctionDef) -> None:
```

### SourceGenerator().visit_GeneratorExp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L469)

```python
def visit_GeneratorExp(node: ast.GeneratorExp) -> None:
```

### SourceGenerator().visit_Global

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L257)

```python
def visit_Global(node: ast.Global) -> None:
```

### SourceGenerator().visit_If

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L177)

```python
def visit_If(node: ast.If) -> None:
```

### SourceGenerator().visit_IfExp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L487)

```python
def visit_IfExp(node: ast.IfExp) -> None:
```

### SourceGenerator().visit_Import

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L134)

```python
def visit_Import(node: ast.Import) -> None:
```

### SourceGenerator().visit_ImportFrom

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L123)

```python
def visit_ImportFrom(node: ast.ImportFrom) -> None:
```

### SourceGenerator().visit_Lambda

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L446)

```python
def visit_Lambda(node: ast.Lambda) -> None:
```

### SourceGenerator().visit_List

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L364)

```python
def visit_List(node: ast.List) -> None:
```

### SourceGenerator().visit_ListComp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L465)

```python
def visit_ListComp(node: ast.ListComp) -> None:
```

### SourceGenerator().visit_Name

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L322)

```python
def visit_Name(node: ast.Name) -> None:
```

### SourceGenerator().visit_NameConstant

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L327)

```python
def visit_NameConstant(node: ast.NameConstant) -> None:
```

### SourceGenerator().visit_Nonlocal

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L262)

```python
def visit_Nonlocal(node: ast.Nonlocal) -> None:
```

### SourceGenerator().visit_Num

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L339)

```python
def visit_Num(node: ast.Num) -> None:
```

### SourceGenerator().visit_Pass

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L231)

```python
def visit_Pass(_node: ast.Pass) -> None:
```

### SourceGenerator().visit_Raise

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L286)

```python
def visit_Raise(node: ast.Raise) -> None:
```

### SourceGenerator().visit_Return

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L267)

```python
def visit_Return(node: ast.Return) -> None:
```

### SourceGenerator().visit_Set

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L368)

```python
def visit_Set(node: ast.Set) -> None:
```

### SourceGenerator().visit_SetComp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L473)

```python
def visit_SetComp(node: ast.SetComp) -> None:
```

### SourceGenerator().visit_Slice

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L420)

```python
def visit_Slice(node: ast.Slice) -> None:
```

### SourceGenerator().visit_Starred

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L495)

```python
def visit_Starred(node: ast.Starred) -> None:
```

### SourceGenerator().visit_Str

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L331)

```python
def visit_Str(node: ast.Str) -> None:
```

### SourceGenerator().visit_Subscript

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L413)

```python
def visit_Subscript(node: ast.Subscript) -> None:
```

### SourceGenerator().visit_Try

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L245)

```python
def visit_Try(node: ast.Try) -> None:
```

### SourceGenerator().visit_Tuple

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L343)

```python
def visit_Tuple(node: ast.Tuple) -> None:
```

### SourceGenerator().visit_UnaryOp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L403)

```python
def visit_UnaryOp(node: ast.UnaryOp) -> None:
```

### SourceGenerator().visit_While

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L211)

```python
def visit_While(node: ast.While) -> None:
```

### SourceGenerator().visit_With

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L219)

```python
def visit_With(node: ast.With) -> None:
```

### SourceGenerator().visit_Yield

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L439)

```python
def visit_Yield(node: ast.Yield) -> None:
```

### SourceGenerator().visit_alias

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L502)

```python
def visit_alias(node: ast.alias) -> None:
```

### SourceGenerator().visit_arguments

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L532)

```python
def visit_arguments(node: ast.arguments) -> None:
```

### SourceGenerator().visit_comprehension

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L508)

```python
def visit_comprehension(node: ast.comprehension) -> None:
```

### SourceGenerator().write

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/source_generator.py#L60)

```python
def write(x: Text) -> None:
```
