# FunctionAnalyzer

[Handsdown](../../../README.md#-handsdown---python-documentation-generator) / [Modules](../../../MODULES.md#modules) / [Handsdown](../../index.md#handsdown) / [AST Parser](../index.md#ast-parser) / [Analyzers](index.md#analyzers) / FunctionAnalyzer

> Auto-generated documentation for [handsdown.ast_parser.analyzers.function_analyzer](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/function_analyzer.py) module.

- [FunctionAnalyzer](#functionanalyzer)

## FunctionAnalyzer

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/function_analyzer.py#L12)

AST analyzer for `ast.FunctionDef` records.

#### Signature

```python
class FunctionAnalyzer(BaseAnalyzer):
    def __init__(self) -> None:
        ...
```

#### See also
- [BaseAnalyzer](base_analyzer.md#baseanalyzer)

### FunctionAnalyzer().generic_visit

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/function_analyzer.py#L161)

Do nothing for unknown `ast.AST` nodes.

#### Arguments

- `node` - AST node.

#### Signature

```python
def generic_visit(self, node: ast.AST) -> None:
    ...
```

### FunctionAnalyzer().visit_AsyncFunctionDef

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/function_analyzer.py#L142)

Entrypoint for the analyzer for asynchronous functions.Visits each node from `node.args`.
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

#### Signature

```python
def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
    ...
```

### FunctionAnalyzer().visit_FunctionDef

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/function_analyzer.py#L123)

Entrypoint for the analyzer.Visits each node from `node.args`.
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

#### Signature

```python
def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
    ...
```

### FunctionAnalyzer().visit_arguments

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/function_analyzer.py#L38)

Parse info about class method statements.Adds new `ArgumentRecord` entry to `argument_records` for each argument.

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

#### Signature

```python
def visit_arguments(self, node: ast.arguments) -> None:
    ...
```


