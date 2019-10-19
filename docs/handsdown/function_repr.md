# FunctionRepr

> Auto-generated documentation for [handsdown.function_repr](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py) module.

- [Index](../README.md#modules) / [Handsdown](index.md#handsdown) / FunctionRepr
  - [ClassRepr](#classrepr)
  - [FunctionData](#functiondata)
    - [FunctionData().render](#functiondatarender)
  - [FunctionRepr](#functionrepr)
    - [FunctionRepr().get_type_hints](#functionreprget_type_hints)
    - [FunctionRepr().render](#functionreprrender)
  - [NotSetValue](#notsetvalue)
  - [ParameterData](#parameterdata)
    - [ParameterData().render](#parameterdatarender)
  - [TypeHintData](#typehintdata)
    - [TypeHintData().get_class_names](#typehintdataget_class_names)
    - [TypeHintData().render](#typehintdatarender)

## ClassRepr

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L230)

```python
class ClassRepr(cls)
```

## FunctionData

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L63)

```python
class FunctionData(name)
```

### FunctionData().render

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L70)

```python
def render(multi_line=False)
```

## FunctionRepr

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L89)

```python
class FunctionRepr(func)
```

### FunctionRepr().get_type_hints

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L189)

```python
def get_type_hints()
```

### FunctionRepr().render

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L215)

```python
def render()
```

## NotSetValue

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L37)

```python
class NotSetValue(args, kwargs)
```

## ParameterData

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L41)

```python
class ParameterData(name)
```

### ParameterData().render

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L47)

```python
def render()
```

## TypeHintData

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L9)

```python
class TypeHintData(type_hint)
```

### TypeHintData().get_class_names

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L30)

```python
def get_class_names()
```

### TypeHintData().render

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L15)

```python
def render()
```
