# BaseAnalyzer

Base AST analyzer.

[Handsdown API Index](../../../README.md#handsdown-api-index) / [Handsdown](../../index.md#handsdown) / [AST Parser](../index.md#ast-parser) / [Analyzers](./index.md#analyzers) / BaseAnalyzer

> Auto-generated documentation for [handsdown.ast_parser.analyzers.base_analyzer](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/base_analyzer.py) module.

## BaseAnalyzer

[Show source in base_analyzer.py:9](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/base_analyzer.py#L9)

Base AST analyzer.

Has lists for all objects for different analyzers.

#### Signature

```python
class BaseAnalyzer(ast.NodeVisitor):
    def __init__(self) -> None:
        ...
```

### BaseAnalyzer().get_docstring

[Show source in base_analyzer.py:19](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/base_analyzer.py#L19)

Get docstring from node.

#### Arguments

- `node` - AST node.

#### Returns

Docstring.

#### Signature

```python
def get_docstring(self, node: ast.AST) -> str:
    ...
```
