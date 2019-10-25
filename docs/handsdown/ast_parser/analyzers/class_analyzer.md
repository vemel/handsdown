# ClassAnalyzer

> Auto-generated documentation for [handsdown.ast_parser.analyzers.class_analyzer](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/class_analyzer.py) module.

AST analyzer for `ast.ClassDef` records.

- [Handsdown](../../../README.md#-handsdown---python-documentation-generator) / [Modules](../../../MODULES.md#modules) / [Handsdown](../../index.md#handsdown) / [Ast Parser](../index.md#ast-parser) / [Analyzers](index.md#analyzers) / ClassAnalyzer
    - [ClassAnalyzer](#classanalyzer)
        - [ClassAnalyzer().visit_Assign](#classanalyzervisit_assign)
        - [ClassAnalyzer().visit_FunctionDef](#classanalyzervisit_functiondef)

## ClassAnalyzer

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/class_analyzer.py#L10)

```python
class ClassAnalyzer(BaseAnalyzer):
```

AST analyzer for `ast.ClassDef` records.

#### See also

- [BaseAnalyzer](base_analyzer.md#baseanalyzer)

### ClassAnalyzer().visit_Assign

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/class_analyzer.py#L36)

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

### ClassAnalyzer().visit_FunctionDef

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/class_analyzer.py#L15)

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
