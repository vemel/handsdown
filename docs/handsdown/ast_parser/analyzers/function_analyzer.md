# FunctionAnalyzer

> Auto-generated documentation for [handsdown.ast_parser.analyzers.function_analyzer](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/function_analyzer.py) module.

AST analyzer for `ast.FunctionDef` records.

- [Handsdown](../../../README.md#-handsdown---python-documentation-generator) / [Modules](../../../MODULES.md#modules) / [Handsdown](../../index.md#handsdown) / [AST Parser](../index.md#ast-parser) / [Analyzers](index.md#analyzers) / FunctionAnalyzer
    - [FunctionAnalyzer](#functionanalyzer)
        - [FunctionAnalyzer().generic_visit](#functionanalyzergeneric_visit)
        - [FunctionAnalyzer().visit_AsyncFunctionDef](#functionanalyzervisit_asyncfunctiondef)
        - [FunctionAnalyzer().visit_FunctionDef](#functionanalyzervisit_functiondef)
        - [FunctionAnalyzer().visit_arguments](#functionanalyzervisit_arguments)

## FunctionAnalyzer

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/function_analyzer.py#L12)

```python
class FunctionAnalyzer(BaseAnalyzer):
    def __init__() -> None:
```

AST analyzer for `ast.FunctionDef` records.

#### See also

- [BaseAnalyzer](base_analyzer.md#baseanalyzer)

### FunctionAnalyzer().generic_visit

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/function_analyzer.py#L161)

```python
def generic_visit(node: ast.AST) -> None:
```

Do nothing for unknown `ast.AST` nodes.

#### Arguments

- `node` - AST node.

### FunctionAnalyzer().visit_AsyncFunctionDef

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/function_analyzer.py#L142)

```python
def visit_AsyncFunctionDef(node: ast.AsyncFunctionDef) -> None:
```

Entrypoint for the analyzer for asynchronous functions.

Visits each node from `node.args`.
Adds new `ast.expr` entry to `decorator_nodes` for each node
from `node.decorator_list`.
Sets `return_type_hint` to `node.returns` if it defined.

#### Examples

```python
async def my_func():
    return await result
```

#### Arguments

- `node` - AST node.

### FunctionAnalyzer().visit_FunctionDef

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/function_analyzer.py#L123)

```python
def visit_FunctionDef(node: ast.FunctionDef) -> None:
```

Entrypoint for the analyzer.

Visits each node from `node.args`.
Adds new `ast.expr` entry to `decorator_nodes` for each node
from `node.decorator_list`.
Sets `return_type_hint` to `node.returns` if it defined.

#### Examples

```python
def my_func():
    return result
```

#### Arguments

- `node` - AST node.

### FunctionAnalyzer().visit_arguments

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/function_analyzer.py#L38)

```python
def visit_arguments(node: ast.arguments) -> None:
```

Parse info about class method statements.

Adds new `ArgumentRecord` entry to `argument_records` for each argument.

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
    arg1: str,
    arg_default: str = "value",
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
