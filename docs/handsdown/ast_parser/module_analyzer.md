# ModuleAnalyzer

> Auto-generated documentation for [handsdown.ast_parser.module_analyzer](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/module_analyzer.py) module.

- [Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / [Ast Parser](index.md#ast-parser) / ModuleAnalyzer
  - [ModuleAnalyzer](#moduleanalyzer)
    - [ModuleAnalyzer().visit_ClassDef](#moduleanalyzervisit_classdef)
    - [ModuleAnalyzer().visit_FunctionDef](#moduleanalyzervisit_functiondef)
    - [ModuleAnalyzer().visit_Import](#moduleanalyzervisit_import)
    - [ModuleAnalyzer().visit_ImportFrom](#moduleanalyzervisit_importfrom)

## ModuleAnalyzer

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/module_analyzer.py#L9)

```python
class ModuleAnalyzer(ast.NodeVisitor):
    def __init__() -> None:
```

### ModuleAnalyzer().visit_ClassDef

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/module_analyzer.py#L28)

```python
def visit_ClassDef(node: ast.ClassDef) -> None:
```

### ModuleAnalyzer().visit_FunctionDef

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/module_analyzer.py#L33)

```python
def visit_FunctionDef(node: ast.FunctionDef) -> None:
```

### ModuleAnalyzer().visit_Import

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/module_analyzer.py#L16)

```python
def visit_Import(node: ast.Import) -> None:
```

### ModuleAnalyzer().visit_ImportFrom

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/module_analyzer.py#L22)

```python
def visit_ImportFrom(node: ast.ImportFrom) -> None:
```
