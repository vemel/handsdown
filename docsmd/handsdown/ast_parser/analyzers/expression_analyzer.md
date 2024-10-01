# ExpressionAnalyzer

AST analyzer for `ast.expr` records.

[Handsdown API Index](../../../README.md#handsdown-api-index) / [Handsdown](../../index.md#handsdown) / [AST Parser](../index.md#ast-parser) / [Analyzers](./index.md#analyzers) / ExpressionAnalyzer

> Auto-generated documentation for [handsdown.ast_parser.analyzers.expression_analyzer](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py) module.

## ExpressionAnalyzer

[Show source in expression_analyzer.py:13](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L13)

#### Attributes

- `UNKNOWN` - dummy value to replace unknown nodes and operators: '...'

- `BINOP_SYMBOLS`: `Dict[Type[ast.AST], str]` - representation map for binary operators: {ast.Add: '+', ast.Sub: '-', ast.Mult: '*', ast.Div: '/', ast.Mod: '%', ast.Pow: '**', ast.LShift: '<<', ast.RShift: '>>', ast.BitOr: '|', ast.BitXor: '^', ast.BitAnd: '&', ast.FloorDiv: '//'}

- `BOOLOP_SYMBOLS`: `Dict[Type[ast.AST], str]` - representation map for boolean operators: {ast.And: 'and', ast.Or: 'or'}

- `CMPOP_SYMBOLS`: `Dict[Type[ast.AST], str]` - representation map for comparison operators: {ast.Eq: '==', ast.NotEq: '!=', ast.Lt: '<', ast.LtE: '<=', ast.Gt: '>', ast.GtE: '>=', ast.Is: 'is', ast.IsNot: 'is not', ast.In: 'in', ast.NotIn: 'not in'}

- `UNARYOP_SYMBOLS`: `Dict[Type[ast.AST], str]` - representation map for unary operators: {ast.Invert: '~', ast.Not: 'not', ast.UAdd: '+', ast.USub: '-'}


AST analyzer for `ast.expr` records.

Prepares `parts` for `NodeRecord.render` method.

#### Signature

```python
class ExpressionAnalyzer(BaseAnalyzer):
    def __init__(self) -> None:
        ...
```

#### See also

- [BaseAnalyzer](./base_analyzer.md#baseanalyzer)

### ExpressionAnalyzer()._visit_iterable

[Show source in expression_analyzer.py:181](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L181)

Parse info from an iterable node and put it to `parts`.

Used for `ast.Tuple`, `ast.Subscript`, `ast.List`, `ast.Set`

#### Examples

```python
[1, 2, 3]
{1, 2, 3}
(1, 2, 3)
Union[str, bool]
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def _visit_iterable(self, node: ASTIterable) -> None:
    ...
```

#### See also

- [ASTIterable](../type_defs.md#astiterable)

### ExpressionAnalyzer().generic_visit

[Show source in expression_analyzer.py:754](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L754)

Parse info from an unknown `ast.AST` node and put `...` to `parts`.

Logs warning with node class.

#### Arguments

- `node` - AST node.

#### Signature

```python
def generic_visit(self, node: ast.AST) -> None:
    ...
```

### ExpressionAnalyzer().visit_Attribute

[Show source in expression_analyzer.py:166](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L166)

Parse info from `ast.Attribute` node and put it to `parts`.

#### Examples

```python
my_object.attribute
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_Attribute(self, node: ast.Attribute) -> None:
    ...
```

### ExpressionAnalyzer().visit_Await

[Show source in expression_analyzer.py:709](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L709)

Parse info from `ast.Await` node and put it to `parts`.

#### Examples

```python
await result
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_Await(self, node: ast.Await) -> None:
    ...
```

### ExpressionAnalyzer().visit_BinOp

[Show source in expression_analyzer.py:367](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L367)

Parse info from `ast.BinOp` node and put it to `parts`.

#### Examples

```python
1 + 5
value + 1
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_BinOp(self, node: ast.BinOp) -> None:
    ...
```

### ExpressionAnalyzer().visit_BoolOp

[Show source in expression_analyzer.py:388](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L388)

Parse info from `ast.BoolOp` node and put it to `parts`.

#### Examples

```python
value or True
a and b
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_BoolOp(self, node: ast.BoolOp) -> None:
    ...
```

### ExpressionAnalyzer().visit_Bytes

[Show source in expression_analyzer.py:85](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L85)

Parse info from `ast.Bytes` node and put it to `parts`.

#### Examples

```python
b"my_string"
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_Bytes(self, node: ast.Bytes) -> None:
    ...
```

### ExpressionAnalyzer().visit_Call

[Show source in expression_analyzer.py:257](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L257)

Parse info from `ast.Call` node and put it to `parts`.

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_Call(self, node: ast.Call) -> None:
    ...
```

### ExpressionAnalyzer().visit_Compare

[Show source in expression_analyzer.py:344](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L344)

Parse info from `ast.Compare` node and put it to `parts`.

#### Examples

```python
value < 5
1 < weekday < 7
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_Compare(self, node: ast.Compare) -> None:
    ...
```

### ExpressionAnalyzer().visit_Dict

[Show source in expression_analyzer.py:326](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L326)

Parse info from `ast.Dict` node and put it to `parts`.

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_Dict(self, node: ast.Dict) -> None:
    ...
```

### ExpressionAnalyzer().visit_DictComp

[Show source in expression_analyzer.py:618](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L618)

Parse info from `ast.DictComp` node and put it to `parts`.

#### Examples

```python
{k: 1 for k in range(3)}
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_DictComp(self, node: ast.DictComp) -> None:
    ...
```

### ExpressionAnalyzer().visit_Ellipsis

[Show source in expression_analyzer.py:525](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L525)

Parse info from `ast.Ellipsis` node and put it to `parts`.

#### Examples

```python
...
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_Ellipsis(self, node: ast.ASTEllipsis) -> None:
    ...
```

### ExpressionAnalyzer().visit_FormattedValue

[Show source in expression_analyzer.py:584](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L584)

Parse info from `ast.FormattedValue` node and put it to `parts`.

#### Examples

```python
f"{formatted_value}"
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_FormattedValue(self, node: ast.FormattedValue) -> None:
    ...
```

### ExpressionAnalyzer().visit_GeneratorExp

[Show source in expression_analyzer.py:674](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L674)

Parse info from `ast.GeneratorExp` node and put it to `parts`.

#### Examples

```python
(k + 1 for k in range(3))
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_GeneratorExp(self, node: ast.GeneratorExp) -> None:
    ...
```

### ExpressionAnalyzer().visit_IfExp

[Show source in expression_analyzer.py:692](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L692)

Parse info from `ast.IfExp` node and put it to `parts`.

#### Examples

```python
5 if my_value else 6
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_IfExp(self, node: ast.IfExp) -> None:
    ...
```

### ExpressionAnalyzer().visit_Index

[Show source in expression_analyzer.py:508](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L508)

Parse info from `ast.Index` node and put it to `parts`.

#### Examples

```python
Union[str, bool]
Union[str]
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_Index(self, node: ast.Index) -> None:
    ...
```

### ExpressionAnalyzer().visit_JoinedStr

[Show source in expression_analyzer.py:562](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L562)

Parse info from `ast.JoinedStr` node and put it to `parts`.

#### Examples

```python
f'str: {my_string}'
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_JoinedStr(self, node: ast.JoinedStr) -> None:
    ...
```

### ExpressionAnalyzer().visit_Lambda

[Show source in expression_analyzer.py:432](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L432)

Parse info from `ast.Lambda` node and put it to `parts`.

#### Examples

```python
lambda x: x + 5
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_Lambda(self, node: ast.Lambda) -> None:
    ...
```

### ExpressionAnalyzer().visit_List

[Show source in expression_analyzer.py:212](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L212)

Parse info from `ast.List` node and put it to `parts`.

#### Examples

```python
[1, 2, 3]
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_List(self, node: ast.List) -> None:
    ...
```

### ExpressionAnalyzer().visit_ListComp

[Show source in expression_analyzer.py:638](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L638)

Parse info from `ast.ListComp` node and put it to `parts`.

#### Examples

```python
[k + 1 for k in range(3)]
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_ListComp(self, node: ast.ListComp) -> None:
    ...
```

### ExpressionAnalyzer().visit_Name

[Show source in expression_analyzer.py:114](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L114)

Parse info from `ast.Name` node and put it to `parts`.

#### Examples

```python
my_value
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_Name(self, node: ast.Name) -> None:
    ...
```

### ExpressionAnalyzer().visit_NameConstant

[Show source in expression_analyzer.py:128](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L128)

Parse info from `ast.NameConstant` node and put it to `parts`.

#### Examples

```python
None
True
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_NameConstant(self, node: ast.NameConstant) -> None:
    ...
```

### ExpressionAnalyzer().visit_Num

[Show source in expression_analyzer.py:99](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L99)

Parse info from `ast.Num` node and put it to `parts`.

#### Examples

```python
123
123.456
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_Num(self, node: ast.Num) -> None:
    ...
```

### ExpressionAnalyzer().visit_Set

[Show source in expression_analyzer.py:227](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L227)

Parse info from `ast.Set` node and put it to `parts`.

#### Examples

```python
{1, 2, 3}
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_Set(self, node: ast.Set) -> None:
    ...
```

### ExpressionAnalyzer().visit_SetComp

[Show source in expression_analyzer.py:656](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L656)

Parse info from `ast.SetComp` node and put it to `parts`.

#### Examples

```python
{k + 1 for k in range(3)}
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_SetComp(self, node: ast.SetComp) -> None:
    ...
```

### ExpressionAnalyzer().visit_Slice

[Show source in expression_analyzer.py:538](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L538)

Parse info from `ast.Slice` node and put it to `parts`.

#### Examples

```python
[1:]
[:2]
[1:2]
[1:2:-1]
[::-1]
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_Slice(self, node: ast.Slice) -> None:
    ...
```

### ExpressionAnalyzer().visit_Starred

[Show source in expression_analyzer.py:291](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L291)

Parse info from `ast.Starred` node and put it to `parts`.

#### Examples

```python
*arg
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_Starred(self, node: ast.Starred) -> None:
    ...
```

### ExpressionAnalyzer().visit_Str

[Show source in expression_analyzer.py:69](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L69)

Parse info from `ast.Str` node and put it to `parts`.

#### Examples

```python
"my_string"
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_Str(self, node: ast.Str) -> None:
    ...
```

### ExpressionAnalyzer().visit_Subscript

[Show source in expression_analyzer.py:142](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L142)

Parse info from `ast.Subscript` node and put it to `parts`.

Type annotations are also matched by this method.

#### Examples

```python
Union[Name, bool]
List[1:4]
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_Subscript(self, node: ast.Subscript) -> None:
    ...
```

### ExpressionAnalyzer().visit_Tuple

[Show source in expression_analyzer.py:242](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L242)

Parse info from `ast.Tuple` node and put it to `parts`.

#### Examples

```python
(1, 2, 3)
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_Tuple(self, node: ast.Tuple) -> None:
    ...
```

### ExpressionAnalyzer().visit_UnaryOp

[Show source in expression_analyzer.py:410](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L410)

Parse info from `ast.UnaryOp` node and put it to `parts`.

#### Examples

```python
+5
-12
~1
not True
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_UnaryOp(self, node: ast.UnaryOp) -> None:
    ...
```

### ExpressionAnalyzer().visit_Yield

[Show source in expression_analyzer.py:723](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L723)

Parse info from `ast.Yield` node and put it to `parts`.

#### Examples

```python
yield
yield value
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_Yield(self, node: ast.Yield) -> None:
    ...
```

### ExpressionAnalyzer().visit_YieldFrom

[Show source in expression_analyzer.py:740](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L740)

Parse info from `ast.YieldFrom` node and put it to `parts`.

#### Examples

```python
yield from my_generator
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_YieldFrom(self, node: ast.YieldFrom) -> None:
    ...
```

### ExpressionAnalyzer().visit_arg

[Show source in expression_analyzer.py:491](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L491)

Parse info from `ast.arg` node and put it to `parts`.

#### Examples

```python
def my_func(arg)
def my_func(arg: str)
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_arg(self, node: ast.arg) -> None:
    ...
```

### ExpressionAnalyzer().visit_arguments

[Show source in expression_analyzer.py:448](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L448)

Parse info from `ast.arguments` node and put it to `parts`.

#### Examples

```python
def my_func(arg, *args, **kwargs)
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_arguments(self, node: ast.arguments) -> None:
    ...
```

### ExpressionAnalyzer().visit_comprehension

[Show source in expression_analyzer.py:599](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L599)

Parse info from `ast.comprehension` node and put it to `parts`.

#### Examples

```python
for k in range(3) if k > 0 if True
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_comprehension(self, node: ast.comprehension) -> None:
    ...
```

### ExpressionAnalyzer().visit_keyword

[Show source in expression_analyzer.py:305](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L305)

Parse info from `ast.keyword` node and put it to `parts`.

#### Examples

```python
my_func(**{"kwarg": "value"})
my_func(kwarg="value")
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_keyword(self, node: ast.keyword) -> None:
    ...
```
