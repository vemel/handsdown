# FunctionAnalyzer

> Auto-generated documentation for [handsdown.ast_parser.analyzers.function_analyzer](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/function_analyzer.py) module.

AST analyzer for `ast.FunctionDef` records.

- [Handsdown](../../../README.md#-handsdown---python-documentation-generator) / [Modules](../../../MODULES.md#modules) / [Handsdown](../../index.md#handsdown) / [Ast Parser](../index.md#ast-parser) / [Analyzers](index.md#analyzers) / FunctionAnalyzer
    - [FunctionAnalyzer](#functionanalyzer)
        - [FunctionAnalyzer().generic_visit](#functionanalyzergeneric_visit)
        - [FunctionAnalyzer().visit_FunctionDef](#functionanalyzervisit_functiondef)
        - [FunctionAnalyzer().visit_Subscript](#functionanalyzervisit_subscript)
        - [FunctionAnalyzer().visit_arguments](#functionanalyzervisit_arguments)

## FunctionAnalyzer

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/function_analyzer.py#L12)

```python
class FunctionAnalyzer(BaseAnalyzer):
    def __init__() -> None:
```

AST analyzer for `ast.FunctionDef` records.

#### See also

- [BaseAnalyzer](base_analyzer.md#baseanalyzer)

### FunctionAnalyzer().generic_visit

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/function_analyzer.py#L159)

```python
def generic_visit(_node: ast.AST) -> None:
```

Do nothing for unknown `ast.AST` nodes.

#### Arguments

- `node` - AST node.

### FunctionAnalyzer().visit_FunctionDef

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/function_analyzer.py#L118)

```python
def visit_FunctionDef(node: ast.FunctionDef) -> None:
```

Entrypoint for the analyzer.

Visits each node from `node.decorator_list` and `node.args`.
Adds new `ExpressionRecord` entries to `decorator_records`.

#### Examples

```python
def my_func():
    pass
```

#### Arguments

- `node` - AST node.

### FunctionAnalyzer().visit_Subscript

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/function_analyzer.py#L142)

```python
def visit_Subscript(node: ast.Subscript) -> None:
```

Parse info about function return type annotation.

Sets `return_type_hint` to a new `ExpressionRecord`.

#### Examples

```python
def my_func() -> List[Text]:
    pass
```

#### Arguments

- `node` - AST node.

### FunctionAnalyzer().visit_arguments

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/function_analyzer.py#L42)

```python
def visit_arguments(node: ast.arguments) -> None:
```

Parse info about class method statements.

Adds new `FunctionRecord` entry to `method_records`.

#### Examples

```python
# simple arguments
def my_func(
    arg1,
    arg_default="value",
    *args,
    **kwargs,
):
    pass

# type annotated arguments
def my_func_typed(
    arg1: Text,
    arg_default: Text="value",
):
    pass

# keyword-only arguments
def my_func_kw_only(
    *,
    kw_only_arg
):
    pass

# pos-only arguments for py38
def my_func_kw_only(
    pos_only_arg,
    /
):
    pass
```

#### Arguments

- `node` - AST node.
