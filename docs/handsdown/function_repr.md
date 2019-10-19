# FunctionRepr

> Auto-generated documentation for [handsdown.function_repr](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py) module.

- [Index](../README.md#modules) / [Handsdown](index.md#handsdown) / FunctionRepr
  - [ClassRepr](#classrepr)
  - [FunctionData](#functiondata)
    - [FunctionData().render](#functiondatarender)
  - [FunctionRepr](#functionrepr)
    - [FunctionRepr().get_type_hints](#functionreprget_type_hints)
    - [FunctionRepr().render](#functionreprrender)
  - [ParameterData](#parameterdata)
    - [ParameterData().render](#parameterdatarender)
  - [TypeHintData](#typehintdata)
    - [TypeHintData().get_class_names](#typehintdataget_class_names)
    - [TypeHintData().render](#typehintdatarender)

## ClassRepr

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L244)

```python
class ClassRepr(inspect_class: Any) -> None
```

## FunctionData

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L72)

```python
class FunctionData(name: Text) -> None
```

### FunctionData().render

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L80)

```python
def render(multi_line: bool = False) -> Text
```

## FunctionRepr

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L100)

```python
class FunctionRepr(func: Any) -> None
```

### FunctionRepr().get_type_hints

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L206)

```python
def get_type_hints() -> Dict[Text, TypeHintData]
```

### FunctionRepr().render

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L228)

```python
def render() -> Text
```

## ParameterData

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L45)

```python
class ParameterData(name: Text) -> None
```

### ParameterData().render

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L54)

```python
def render() -> Text
```

## TypeHintData

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L12)

```python
class TypeHintData(type_hint: Any) -> None
```

### TypeHintData().get_class_names

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L37)

```python
def get_class_names() -> List[Text]
```

### TypeHintData().render

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L19)

```python
def render() -> Text
```
