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

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/class_analyzer.py#L13)

```python
class ClassAnalyzer(BaseAnalyzer):
    def __init__() -> None:
```

AST analyzer for `ast.ClassDef` records.

#### See also

- [BaseAnalyzer](base_analyzer.md#baseanalyzer)

### ClassAnalyzer().generic_visit

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/class_analyzer.py#L113)

```python
def generic_visit(_node: ast.AST) -> None:
```

Do nothing for unknown `ast.AST` nodes.

#### Arguments

- `node` - AST node.

### ClassAnalyzer().visit_Assign

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/class_analyzer.py#L80)

```python
def visit_Assign(node: ast.Assign) -> None:
```

Parse info about class attribute statements.

Adds new `AttributeRecord` entry to `attribute_records` if it is
a simple one-item assign.

#### Examples

```python
class MyClass:
    MY_MODULE_ATTR = 'value'
```

#### Arguments

- `node` - AST node.

### ClassAnalyzer().visit_ClassDef

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/class_analyzer.py#L26)

```python
def visit_ClassDef(node: ast.ClassDef) -> None:
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
