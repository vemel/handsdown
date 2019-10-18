# Signature

> Auto-generated documentation for [handsdown.signature](https://github.com/vemel/handsdown/blob/master/handsdown/signature.py) module..

Module for function signature generation.

- [Index](../README.md#modules) / [Handsdown](index.md#handsdown) / Signature
  - [Config](#config)
  - [DefaultValue](#defaultvalue)
  - [Parameter](#parameter)
    - [Parameter.create](#parametercreate)
  - [SignatureBuilder](#signaturebuilder)
    - [SignatureBuilder().build](#signaturebuilderbuild)

## Config

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/signature.py#L14)

```python
class Config(*args, **kwargs)
```

Config class to control signature generation.

Attrubutes:
    BREAK_LINES -- True if function parameters should start from a new line.
    MAX_LINE_LENGTH -- Max signature line length: `100`

## DefaultValue

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/signature.py#L27)

```python
class DefaultValue(original: Type)
```

Represent function parameter default value in signature

#### Arguments

- `original` - Original default value.

## Parameter

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/signature.py#L51)

```python
class Parameter(type_hint: Union[Type, NoneType], *args: Any, **kwargs: Any)
```

Represent function parameters in signature

### Parameter.create

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/signature.py#L92)

```python
def create(
    parameter: inspect.Parameter,
    type_hint: Union[Type, NoneType],
) -> handsdown.signature.Parameter
```

Create `ProxyParameter` for original `inspect.Parameter`

#### Arguments

- `parameter` - original `inspect.Parameter`
- `type_hint` - resoled type hint that should replace a lazy annotation

#### See also

- [Parameter](#parameter)

## SignatureBuilder

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/signature.py#L113)

```python
class SignatureBuilder(obj: Any)
```

Renderer for object signature. Support lazy type annotations and tries
to beautify result by splitting lines.

#### Arguments

- `obj` - Object to inspect.

### SignatureBuilder().build

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/signature.py#L167)

```python
def build() -> str
```

Render signature to string.

#### Returns

A string with functions signature.
