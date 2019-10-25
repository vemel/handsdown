# ModuleAnalyzer

> Auto-generated documentation for [handsdown.ast_parser.analyzers.module_analyzer](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/module_analyzer.py) module.

AST analyzer for `ast.Module` records.

- [Handsdown](../../../README.md#-handsdown---python-documentation-generator) / [Modules](../../../MODULES.md#modules) / [Handsdown](../../index.md#handsdown) / [AST Parser](../index.md#ast-parser) / [Analyzers](index.md#analyzers) / ModuleAnalyzer
    - [ModuleAnalyzer](#moduleanalyzer)
        - [ModuleAnalyzer().visit_Assign](#moduleanalyzervisit_assign)
        - [ModuleAnalyzer().visit_ClassDef](#moduleanalyzervisit_classdef)
        - [ModuleAnalyzer().visit_FunctionDef](#moduleanalyzervisit_functiondef)
        - [ModuleAnalyzer().visit_Import](#moduleanalyzervisit_import)
        - [ModuleAnalyzer().visit_ImportFrom](#moduleanalyzervisit_importfrom)

## ModuleAnalyzer

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/module_analyzer.py#L12)

```python
class ModuleAnalyzer(BaseAnalyzer):
```

AST analyzer for `ast.Module` records.

#### See also

- [BaseAnalyzer](base_analyzer.md#baseanalyzer)

### ModuleAnalyzer().visit_Assign

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/module_analyzer.py#L93)

```python
def visit_Assign(node: ast.Assign) -> None:
```

Parse info about module attribute statements.

Adds new `AttributeRecord` entry to `attribute_records`.

#### Examples

```python
MY_MODULE_ATTR = 'value'
```

#### Arguments

- `node` - AST node.

### ModuleAnalyzer().visit_ClassDef

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/module_analyzer.py#L57)

```python
def visit_ClassDef(node: ast.ClassDef) -> None:
```

Parse info about module `class ...` statements.

Adds new `ClassRecord` entry to `class_records`.

#### Examples

```python
class MyClass():
    pass
```

#### Arguments

- `node` - AST node.

### ModuleAnalyzer().visit_FunctionDef

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/module_analyzer.py#L75)

```python
def visit_FunctionDef(node: ast.FunctionDef) -> None:
```

Parse info about module `def ...` statements.

Adds new `FunctionRecord` entry to `function_records`.

#### Examples

```python
def my_func(arg1):
    pass
```

#### Arguments

- `node` - AST node.

### ModuleAnalyzer().visit_Import

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/module_analyzer.py#L17)

```python
def visit_Import(node: ast.Import) -> None:
```

Parse info about module `import ...` statements.

Adds new `ImportRecord` entry to `import_records`.

#### Examples

```python
import my_module
import my_module as my
import my_module.my_class
import my_module.my_class as my_class
```

#### Arguments

- `node` - AST node.

### ModuleAnalyzer().visit_ImportFrom

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/module_analyzer.py#L38)

```python
def visit_ImportFrom(node: ast.ImportFrom) -> None:
```

Parse info about module `import ... from ...` statements.

Adds new `ImportRecord` entry to `import_records`.

#### Examples

```python
from my_module import my_class
from my_module import my_class as new_class
```

#### Arguments

- `node` - AST node.
