# FunctionRepr

> Auto-generated documentation for [handsdown.function_repr](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py) module.

Function sgnature builder.

- [Handsdown](../README.md#-handsdown---python-documentation-generator) / [Modules](../MODULES.md#modules) / [Handsdown](index.md#handsdown) / FunctionRepr
  - [ClassRepr](#classrepr)
  - [DefaultValueData](#defaultvaluedata)
    - [DefaultValueData().get_class_names](#defaultvaluedataget_class_names)
    - [DefaultValueData().render](#defaultvaluedatarender)
  - [FunctionData](#functiondata)
    - [FunctionData().render](#functiondatarender)
  - [FunctionRepr](#functionrepr)
    - [FunctionRepr().get_defaults](#functionreprget_defaults)
    - [FunctionRepr().get_type_hints](#functionreprget_type_hints)
    - [FunctionRepr().render](#functionreprrender)
  - [ParameterData](#parameterdata)
    - [ParameterData().render](#parameterdatarender)
  - [TypeHintData](#typehintdata)
    - [TypeHintData().get_class_names](#typehintdataget_class_names)
    - [TypeHintData().render](#typehintdatarender)

## ClassRepr

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L539)

```python
class ClassRepr(inspect_class: Any) -> None:
```

Renderer of a class `__init__` function signature.

Built on top of [FunctionRepr](#functionrepr), and changes definition to `class`.

#### Arguments

- `inspect_class` - Class to represent.

## DefaultValueData

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L90)

```python
class DefaultValueData(value: Any) -> None:
```

Represent parameter default value.

#### Arguments

- `value` - Real default value.

### DefaultValueData().get_class_names

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L138)

```python
def get_class_names() -> List[Text]:
```

Get import strings from a rendered default value.

If import string has several parts, it retuned all possible import
cases, e.g. for `my_module.test.Test` it produces `Test`, `test.Test`
and `my_module.test.Test`.

#### Returns

A list of import strings.

### DefaultValueData().render

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L104)

```python
def render() -> Text:
```

Render default value to a string.

`repr` of `value` is used, dynamic hash part is removed for dynamic objects
and `u`  flag is removed for unicode strings.

#### Returns

A default value representation.

## FunctionData

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L218)

```python
class FunctionData(name: Text) -> None:
```

Represent function data.

#### Arguments

- `name` - Function name.

### FunctionData().render

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L233)

```python
def render(multi_line: bool = False) -> Text:
```

Render function data to a string.

Result is a valid Python function definition.

#### Returns

A function representation.

## FunctionRepr

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L268)

```python
class FunctionRepr(func: Any) -> None:
```

Renderer of a function signature.

Inspired a lot by built-in `inspect.Signature`.

#### Arguments

- `func` - Function to represent.

### FunctionRepr().get_defaults

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L472)

```python
def get_defaults() -> Dict[Text, DefaultValueData]:
```

Return a list of [DefaultValueData](#defaultvaluedata) for all parameters.

Can be used to find related objects in the project.

#### Returns

A list of all set [DefaultValueData](#defaultvaluedata)

#### See also

- [DefaultValueData](#defaultvaluedata)

### FunctionRepr().get_type_hints

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L451)

```python
def get_type_hints() -> Dict[Text, TypeHintData]:
```

Return a list of [TypeHintData](#typehintdata) for all parameters.

Can be used to find related objects in the project.

#### Returns

A list of all set [TypeHintData](#typehintdata)

#### See also

- [TypeHintData](#typehintdata)

### FunctionRepr().render

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L502)

```python
def render() -> Text:
```

Render function data to a string.

Result is a valid Python function definition. If result is too long -
splits it to multiple lines.

#### Returns

A representaion of a function.

## ParameterData

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L167)

```python
class ParameterData(name: Text) -> None:
```

Represent function parameter.

#### Arguments

- `name` - Argument name.

#### Attributes

- `NOT_SET` - Sentinel value to use if default value or type hint are not set.

### ParameterData().render

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L186)

```python
def render() -> Text:
```

Render parameter data to a string.

#### Returns

A parameter representation.

## TypeHintData

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L16)

```python
class TypeHintData(type_hint: Any) -> None:
```

Represent parameter type hint object.

#### Arguments

- `type_hint` - Real type hint value

### TypeHintData().get_class_names

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L65)

```python
def get_class_names() -> List[Text]:
```

Get class names for a rendered type hint.

#### Returns

A list of parsed class names.

### TypeHintData().render

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L30)

```python
def render() -> Text:
```

Render type hint to a string.

If `type_hint`:
- is a string - it returned as it is.
- has name - name is used as an output.
- otherwise raw `str` is used, `typing.` prefix removed

#### Returns

A type hint representation.
