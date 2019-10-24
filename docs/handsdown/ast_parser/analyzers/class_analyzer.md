# ClassAnalyzer

> Auto-generated documentation for [handsdown.ast_parser.analyzers.class_analyzer](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/class_analyzer.py) module.

- [Handsdown](../../../README.md#-handsdown---python-documentation-generator) / [Modules](../../../MODULES.md#modules) / [Handsdown](../../index.md#handsdown) / [Ast Parser](../index.md#ast-parser) / [Analyzers](index.md#analyzers) / ClassAnalyzer
    - [ClassAnalyzer](#classanalyzer)
        - [ClassAnalyzer().visit_Assign](#classanalyzervisit_assign)
        - [ClassAnalyzer().visit_FunctionDef](#classanalyzervisit_functiondef)

## ClassAnalyzer

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/class_analyzer.py#L8)

```python
class ClassAnalyzer(BaseAnalyzer):
```

#### See also

- [BaseAnalyzer](base_analyzer.md#baseanalyzer)

### ClassAnalyzer().visit_Assign

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/class_analyzer.py#L16)

```python
def visit_Assign(node: ast.Assign) -> None:
```

### ClassAnalyzer().visit_FunctionDef

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/analyzers/class_analyzer.py#L9)

```python
def visit_FunctionDef(node: ast.FunctionDef) -> None:
```
