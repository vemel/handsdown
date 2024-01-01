# ClassAnalyzer

[Handsdown API Index](../../../README.md#handsdown-api-index) / [Handsdown](../../index.md#handsdown) / [AST Parser](../index.md#ast-parser) / [Analyzers](./index.md#analyzers) / ClassAnalyzer

> Auto-generated documentation for [handsdown.ast_parser.analyzers.class_analyzer](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/class_analyzer.py) module.

## ClassAnalyzer

[Show source in class_analyzer.py:11](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/class_analyzer.py#L11)

AST analyzer for `ast.ClassDef` records.

#### Signature

```python
class ClassAnalyzer(BaseAnalyzer):
    def __init__(self) -> None:
        ...
```

#### See also

- [BaseAnalyzer](./base_analyzer.md#baseanalyzer)

### ClassAnalyzer().generic_visit

[Show source in class_analyzer.py:138](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/class_analyzer.py#L138)

Do nothing for unknown `ast.AST` nodes.

#### Arguments

- `node` - AST node.

#### Signature

```python
def generic_visit(self, node: ast.AST) -> None:
    ...
```

### ClassAnalyzer().visit_Assign

[Show source in class_analyzer.py:98](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/class_analyzer.py#L98)

Parse info about class attribute statements.

Adds new `ast.Assign` entry to `attribute_nodes`.
Skips assignments to anything pther that a new variable.
Skips multiple assignments.
Skips assignments with names starting with `_`.

#### Examples

```python
class MyClass:
    MY_MODULE_ATTR = "value"
    my_attr = "value"

    # these entries are skipped
    _MY_MODULE_ATTR = "value"
    multi_attr_1, multi_attr_2 = [1, 2]
    my_object.name = "value"
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_Assign(self, node: ast.Assign) -> None:
    ...
```

### ClassAnalyzer().visit_AsyncFunctionDef

[Show source in class_analyzer.py:80](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/class_analyzer.py#L80)

Parse info about class asynchronous method statements.

Adds new `FunctionRecord` entry to `method_records`.

#### Examples

```python
class MyClass:
    async def my_method(self, arg):
        return await arg
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
    ...
```

### ClassAnalyzer().visit_ClassDef

[Show source in class_analyzer.py:23](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/class_analyzer.py#L23)

Entrypoint for the analyzer.

Adds new `ast.expr` entry to `decorator_nodes` for each node
from `node.decorator_list`.
Adds new `ast.expr` entry to `base_nodes` for each node
from `node.bases`.
Visits each node from `node.body` list to parse methods.

#### Examples

```python
def my_func():
    pass
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_ClassDef(self, node: ast.ClassDef) -> None:
    ...
```

### ClassAnalyzer().visit_FunctionDef

[Show source in class_analyzer.py:62](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/class_analyzer.py#L62)

Parse info about class method statements.

Adds new `FunctionRecord` entry to `method_records`.

#### Examples

```python
class MyClass:
    def my_method(self, arg):
        return arg
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
    ...
```
