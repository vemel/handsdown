# ExpressionAnalyzer

> Auto-generated documentation for [handsdown.ast_parser.analyzers.expression_analyzer](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py) module.

AST analyzer for `ast.expr` records.

- [Handsdown](../../../README.md#-handsdown---python-documentation-generator) / [Modules](../../../MODULES.md#modules) / [Handsdown](../../index.md#handsdown) / [AST Parser](../index.md#ast-parser) / [Analyzers](index.md#analyzers) / ExpressionAnalyzer
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

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L15)

```python
class ExpressionAnalyzer(BaseAnalyzer):
    def __init__() -> None:
```

AST analyzer for `ast.expr` records.

Prepares `parts` for `NodeRecord.render` method.

#### See also

- [BaseAnalyzer](base_analyzer.md#baseanalyzer)

### ExpressionAnalyzer().generic_visit

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L442)

```python
def generic_visit(node: ast.AST) -> None:
```

Parse info from an unknown `ast.AST` node and put `...` to `parts`.

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_Attribute

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L135)

```python
def visit_Attribute(node: ast.Attribute) -> None:
```

Parse info from `ast.Attribute` node and put it to `parts`.

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_BinOp

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L304)

```python
def visit_BinOp(node: ast.BinOp) -> None:
```

Parse info from `ast.BinOp` node and put it to `parts`.

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_BoolOp

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L318)

```python
def visit_BoolOp(node: ast.BoolOp) -> None:
```

Parse info from `ast.BoolOp` node and put it to `parts`.

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_Bytes

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L72)

```python
def visit_Bytes(node: ast.Bytes) -> None:
```

Parse info from `ast.Bytes` node and put it to `parts`.

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_Call

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L206)

```python
def visit_Call(node: ast.Call) -> None:
```

Parse info from `ast.Call` node and put it to `parts`.

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_Compare

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L289)

```python
def visit_Compare(node: ast.Compare) -> None:
```

Parse info from `ast.Compare` node and put it to `parts`.

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_Dict

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L264)

```python
def visit_Dict(node: ast.Dict) -> None:
```

Parse info from `ast.Dict` node and put it to `parts`.

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_Ellipsis

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L432)

```python
def visit_Ellipsis(_node: ast.ASTEllipsis) -> None:
```

Parse info from `ast.Ellipsis` node and put it to `parts`.

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_Index

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L419)

```python
def visit_Index(node: ast.Index) -> None:
```

Parse info from `ast.Index` node and put it to `parts`.

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_Lambda

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L347)

```python
def visit_Lambda(node: ast.Lambda) -> None:
```

Parse info from `ast.Lambda` node and put it to `parts`.

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_List

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L170)

```python
def visit_List(node: ast.List) -> None:
```

Parse info from `ast.List` node and put it to `parts`.

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_Name

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L94)

```python
def visit_Name(node: ast.Name) -> None:
```

Parse info from `ast.Name` node and put it to `parts`.

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_NameConstant

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L105)

```python
def visit_NameConstant(node: ast.NameConstant) -> None:
```

Parse info from `ast.NameConstant` node and put it to `parts`.

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_Num

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L83)

```python
def visit_Num(node: ast.Num) -> None:
```

Parse info from `ast.Num` node and put it to `parts`.

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_Set

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L182)

```python
def visit_Set(node: ast.Set) -> None:
```

Parse info from `ast.Set` node and put it to `parts`.

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_Starred

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L237)

```python
def visit_Starred(node: ast.Starred) -> None:
```

Parse info from `ast.Starred` node and put it to `parts`.

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_Str

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L59)

```python
def visit_Str(node: ast.Str) -> None:
```

Parse info from `ast.Str` node and put it to `parts`.

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_Subscript

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L115)

```python
def visit_Subscript(node: ast.Subscript) -> None:
```

Parse info from `ast.Subscript` node and put it to `parts`.

Type annotations are also matched by this method.

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_Tuple

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L194)

```python
def visit_Tuple(node: ast.Tuple) -> None:
```

Parse info from `ast.Tuple` node and put it to `parts`.

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_UnaryOp

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L333)

```python
def visit_UnaryOp(node: ast.UnaryOp) -> None:
```

Parse info from `ast.UnaryOp` node and put it to `parts`.

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_arg

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L406)

```python
def visit_arg(node: ast.arg) -> None:
```

Parse info from `ast.arg` node and put it to `parts`.

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_arguments

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L360)

```python
def visit_arguments(node: ast.arguments) -> None:
```

Parse info from `ast.arguments` node and put it to `parts`.

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_keyword

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/expression_analyzer.py#L248)

```python
def visit_keyword(node: ast.keyword) -> None:
```

Parse info from `ast.keyword` node and put it to `parts`.

#### Arguments

- `node` - AST node.
