# ExpressionAnalyzer

> Auto-generated documentation for [handsdown.ast_parser.analyzers.expression_analyzer](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py) module.

- [Handsdown](../../../README.md#-handsdown---python-documentation-generator) / [Modules](../../../MODULES.md#modules) / [Handsdown](../../index.md#handsdown) / [Ast Parser](../index.md#ast-parser) / [Analyzers](index.md#analyzers) / ExpressionAnalyzer
    - [ExpressionAnalyzer](#expressionanalyzer)
        - [ExpressionAnalyzer().generic_visit](#expressionanalyzergeneric_visit)
        - [ExpressionAnalyzer().visit_Attribute](#expressionanalyzervisit_attribute)
        - [ExpressionAnalyzer().visit_BinOp](#expressionanalyzervisit_binop)
        - [ExpressionAnalyzer().visit_BoolOp](#expressionanalyzervisit_boolop)
        - [ExpressionAnalyzer().visit_Bytes](#expressionanalyzervisit_bytes)
        - [ExpressionAnalyzer().visit_Call](#expressionanalyzervisit_call)
        - [ExpressionAnalyzer().visit_Compare](#expressionanalyzervisit_compare)
        - [ExpressionAnalyzer().visit_Dict](#expressionanalyzervisit_dict)
        - [ExpressionAnalyzer().visit_Ellipsis](#expressionanalyzervisit_ellipsis)
        - [ExpressionAnalyzer().visit_Index](#expressionanalyzervisit_index)
        - [ExpressionAnalyzer().visit_Lambda](#expressionanalyzervisit_lambda)
        - [ExpressionAnalyzer().visit_List](#expressionanalyzervisit_list)
        - [ExpressionAnalyzer().visit_Name](#expressionanalyzervisit_name)
        - [ExpressionAnalyzer().visit_NameConstant](#expressionanalyzervisit_nameconstant)
        - [ExpressionAnalyzer().visit_Num](#expressionanalyzervisit_num)
        - [ExpressionAnalyzer().visit_Set](#expressionanalyzervisit_set)
        - [ExpressionAnalyzer().visit_Starred](#expressionanalyzervisit_starred)
        - [ExpressionAnalyzer().visit_Str](#expressionanalyzervisit_str)
        - [ExpressionAnalyzer().visit_Subscript](#expressionanalyzervisit_subscript)
        - [ExpressionAnalyzer().visit_Tuple](#expressionanalyzervisit_tuple)
        - [ExpressionAnalyzer().visit_UnaryOp](#expressionanalyzervisit_unaryop)
        - [ExpressionAnalyzer().visit_arg](#expressionanalyzervisit_arg)
        - [ExpressionAnalyzer().visit_arguments](#expressionanalyzervisit_arguments)
        - [ExpressionAnalyzer().visit_keyword](#expressionanalyzervisit_keyword)

## ExpressionAnalyzer

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L12)

```python
class ExpressionAnalyzer(BaseAnalyzer):
```

#### See also

- [BaseAnalyzer](base_analyzer.md#baseanalyzer)

### ExpressionAnalyzer().generic_visit

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L284)

```python
def generic_visit(node: ast.AST) -> None:
```

### ExpressionAnalyzer().visit_Attribute

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L87)

```python
def visit_Attribute(node: ast.Attribute) -> None:
```

### ExpressionAnalyzer().visit_BinOp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L194)

```python
def visit_BinOp(node: ast.BinOp) -> None:
```

### ExpressionAnalyzer().visit_BoolOp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L202)

```python
def visit_BoolOp(node: ast.BoolOp) -> None:
```

### ExpressionAnalyzer().visit_Bytes

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L58)

```python
def visit_Bytes(node: ast.Bytes) -> None:
```

### ExpressionAnalyzer().visit_Call

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L126)

```python
def visit_Call(node: ast.Call) -> None:
```

### ExpressionAnalyzer().visit_Compare

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L185)

```python
def visit_Compare(node: ast.Compare) -> None:
```

### ExpressionAnalyzer().visit_Dict

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L166)

```python
def visit_Dict(node: ast.Dict) -> None:
```

### ExpressionAnalyzer().visit_Ellipsis

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L280)

```python
def visit_Ellipsis(_node: ast.Ellipsis) -> None:
```

### ExpressionAnalyzer().visit_Index

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L273)

```python
def visit_Index(node: ast.Index) -> None:
```

### ExpressionAnalyzer().visit_Lambda

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L219)

```python
def visit_Lambda(node: ast.Lambda) -> None:
```

### ExpressionAnalyzer().visit_List

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L108)

```python
def visit_List(node: ast.List) -> None:
```

### ExpressionAnalyzer().visit_Name

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L66)

```python
def visit_Name(node: ast.Name) -> None:
```

### ExpressionAnalyzer().visit_NameConstant

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L71)

```python
def visit_NameConstant(node: ast.NameConstant) -> None:
```

### ExpressionAnalyzer().visit_Num

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L62)

```python
def visit_Num(node: ast.Num) -> None:
```

### ExpressionAnalyzer().visit_Set

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L114)

```python
def visit_Set(node: ast.Set) -> None:
```

### ExpressionAnalyzer().visit_Starred

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L151)

```python
def visit_Starred(node: ast.Starred) -> None:
```

### ExpressionAnalyzer().visit_Str

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L54)

```python
def visit_Str(node: ast.Str) -> None:
```

### ExpressionAnalyzer().visit_Subscript

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L75)

```python
def visit_Subscript(node: ast.Subscript) -> None:
```

### ExpressionAnalyzer().visit_Tuple

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L120)

```python
def visit_Tuple(node: ast.Tuple) -> None:
```

### ExpressionAnalyzer().visit_UnaryOp

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L211)

```python
def visit_UnaryOp(node: ast.UnaryOp) -> None:
```

### ExpressionAnalyzer().visit_arg

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L266)

```python
def visit_arg(node: ast.arg) -> None:
```

### ExpressionAnalyzer().visit_arguments

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L226)

```python
def visit_arguments(node: ast.arguments) -> None:
```

### ExpressionAnalyzer().visit_keyword

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L156)

```python
def visit_keyword(node: ast.keyword) -> None:
```
