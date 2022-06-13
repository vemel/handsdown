# ModuleAnalyzer

[Handsdown](../../../README.md#-handsdown---python-documentation-generator) / [Modules](../../../MODULES.md#modules) / [Handsdown](../../index.md#handsdown) / [AST Parser](../index.md#ast-parser) / [Analyzers](index.md#analyzers) / ModuleAnalyzer

> Auto-generated documentation for [handsdown.ast_parser.analyzers.module_analyzer](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/module_analyzer.py) module.

- [ModuleAnalyzer](#moduleanalyzer)

## ModuleAnalyzer

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/module_analyzer.py#L11)

AST analyzer for `ast.Module` records.

#### Signature

```python
class ModuleAnalyzer(BaseAnalyzer):
    def __init__(self) -> None:
        ...
```

#### See also
- [BaseAnalyzer](base_analyzer.md#baseanalyzer)

### ModuleAnalyzer().visit_Assign

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/module_analyzer.py#L127)

Parse info about module attribute statements.Adds new `ast.Assign` entry to `attribute_nodes`.
Skips assignments to anything pther that a new variable.
Skips multiple assignments.
Skips assignments with names starting with `_`.
Parses `__all__` and add all values to `all_names`

#### Examples

```python
MY_MODULE_ATTR = 'value'
    my_attr = "value"
__all__ = ['MyClass', 'my_func']

# these entries are skipped
_MY_MODULE_ATTR = "value"
multi_attr_1, multi_attr_2 = [1, 2]
my_object.name = "value"
__all__ = all_list
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_Assign(self, node: ast.Assign) -> None:
    ...
```

### ModuleAnalyzer().visit_AsyncFunctionDef

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/module_analyzer.py#L109)

Parse info about module `def ...` statements.Adds `node` entry to `function_nodes`.
Skips nodes with names starting with `_`.

#### Examples

```python
async def my_func(arg1):
    return await arg1
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
    ...
```

### ModuleAnalyzer().visit_ClassDef

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/module_analyzer.py#L58)

Parse info about module `class ...` statements.Adds `node` entry to `class_nodes`.
Skips nodes with names starting with `_`.

#### Examples

```python
class MyClass():
    pass
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_ClassDef(self, node: ast.ClassDef) -> None:
    ...
```

### ModuleAnalyzer().visit_FunctionDef

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/module_analyzer.py#L91)

Parse info about module `def ...` statements.Adds `node` entry to `function_nodes`.
Skips nodes with names starting with `_`.

#### Examples

```python
def my_func(arg1):
    return arg1
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
    ...
```

### ModuleAnalyzer().visit_Import

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/module_analyzer.py#L24)

Parse info about module `import ...` statements.Adds `node` to `import_nodes`.

#### Examples

```python
import my_module
import my_module as my
import my_module.my_class
import my_module.my_class as my_class
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_Import(self, node: ast.Import) -> None:
    ...
```

### ModuleAnalyzer().visit_ImportFrom

[find in source code](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/module_analyzer.py#L42)

Parse info about module `import ... from ...` statements.Adds `node` to `import_nodes`.

#### Examples

```python
from my_module import my_class
from my_module import my_class as new_class
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
    ...
```


