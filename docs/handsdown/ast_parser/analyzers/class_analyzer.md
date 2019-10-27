# ClassAnalyzer

> Auto-generated documentation for [handsdown.ast_parser.analyzers.class_analyzer](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/class_analyzer.py) module.

AST analyzer for `ast.ClassDef` records.

- [Handsdown](../../../README.md#-handsdown---python-documentation-generator) / [Modules](../../../MODULES.md#modules) / [Handsdown](../../index.md#handsdown) / [AST Parser](../index.md#ast-parser) / [Analyzers](index.md#analyzers) / ClassAnalyzer
    - [ClassAnalyzer](#classanalyzer)
        - [ClassAnalyzer().generic_visit](#classanalyzergeneric_visit)
        - [ClassAnalyzer().visit_Assign](#classanalyzervisit_assign)
        - [ClassAnalyzer().visit_ClassDef](#classanalyzervisit_classdef)
        - [ClassAnalyzer().visit_FunctionDef](#classanalyzervisit_functiondef)

## ClassAnalyzer

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/class_analyzer.py#L10)

```python
class ClassAnalyzer(BaseAnalyzer):
    def __init__() -> None:
```

AST analyzer for `ast.ClassDef` records.

#### See also

- [BaseAnalyzer](base_analyzer.md#baseanalyzer)

### ClassAnalyzer().generic_visit

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/class_analyzer.py#L119)

```python
def generic_visit(_node: ast.AST) -> None:
```

Do nothing for unknown `ast.AST` nodes.

#### Arguments

- `node` - AST node.

### ClassAnalyzer().visit_Assign

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/class_analyzer.py#L79)

```python
def visit_Assign(node: ast.Assign) -> None:
```

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

### ClassAnalyzer().visit_ClassDef

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/class_analyzer.py#L23)

```python
def visit_ClassDef(node: ast.ClassDef) -> None:
```

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

### ClassAnalyzer().visit_FunctionDef

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/class_analyzer.py#L49)

```python
def visit_FunctionDef(node: ast.FunctionDef) -> None:
```

Parse info about class method statements.

Adds new `FunctionRecord` entry to `method_records`.

#### Examples

class MyClass:
    def my_method(self, arg):
        pass

#### Arguments

- `node` - AST node.
