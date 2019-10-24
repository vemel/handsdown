# FunctionAnalyzer

> Auto-generated documentation for [handsdown.ast_parser.analyzers.function_analyzer](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/function_analyzer.py) module.

- [Handsdown](../../../README.md#-handsdown---python-documentation-generator) / [Modules](../../../MODULES.md#modules) / [Handsdown](../../index.md#handsdown) / [Ast Parser](../index.md#ast-parser) / [Analyzers](index.md#analyzers) / FunctionAnalyzer
  - [FunctionAnalyzer](#functionanalyzer)
    - [FunctionAnalyzer().generic_visit](#functionanalyzergeneric_visit)
    - [FunctionAnalyzer().visit_Attribute](#functionanalyzervisit_attribute)
    - [FunctionAnalyzer().visit_FunctionDef](#functionanalyzervisit_functiondef)
    - [FunctionAnalyzer().visit_Name](#functionanalyzervisit_name)
    - [FunctionAnalyzer().visit_Subscript](#functionanalyzervisit_subscript)
    - [FunctionAnalyzer().visit_arguments](#functionanalyzervisit_arguments)

## FunctionAnalyzer

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/function_analyzer.py#L10)

```python
class FunctionAnalyzer(BaseAnalyzer):
    def __init__() -> None:
```

### FunctionAnalyzer().generic_visit

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/function_analyzer.py#L75)

```python
def generic_visit(_node: ast.AST) -> None:
```

### FunctionAnalyzer().visit_Attribute

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/function_analyzer.py#L57)

```python
def visit_Attribute(node: ast.Attribute) -> None:
```

### FunctionAnalyzer().visit_FunctionDef

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/function_analyzer.py#L61)

```python
def visit_FunctionDef(node: ast.FunctionDef) -> None:
```

### FunctionAnalyzer().visit_Name

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/function_analyzer.py#L53)

```python
def visit_Name(node: ast.Name) -> None:
```

### FunctionAnalyzer().visit_Subscript

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/function_analyzer.py#L71)

```python
def visit_Subscript(node: ast.Subscript) -> None:
```

### FunctionAnalyzer().visit_arguments

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/function_analyzer.py#L35)

```python
def visit_arguments(node: ast.arguments) -> None:
```
