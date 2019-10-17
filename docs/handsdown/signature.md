# Signature

> Auto-generated documentation for [handsdown.signature](../../handsdown/signature.py) module.

- [Index](../README.md#handsdown-index) / [Handsdown](index.md#handsdown) / [Signature](#signature) / Signature
  - [Config](#config)
  - [DefaultValue](#defaultvalue)
  - [Parameter](#parameter)
    - [Parameter.create](#parametercreate)
  - [SignatureBuilder](#signaturebuilder)
    - [SignatureBuilder().build](#signaturebuilderbuild)

## Config

[🔍 find in source code](../../handsdown/signature.py#L10)

```python
class Config(*args, **kwargs)
```

## DefaultValue

[🔍 find in source code](../../handsdown/signature.py#L15)

```python
class DefaultValue(original: Type)
```

Represent function parameter default value in signature

#### Arguments

- `original` - Original default value.

## Parameter

[🔍 find in source code](../../handsdown/signature.py#L39)

```python
class Parameter(type_hint: Union[Type, NoneType], *args: Any, **kwargs: Any)
```

Represent function parameters in signature

### Parameter.create

[🔍 find in source code](../../handsdown/signature.py#L80)

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

[🔍 find in source code](../../handsdown/signature.py#L101)

```python
class SignatureBuilder(obj: Any)
```

Renderer for object signature. Support lazy type annotations and tries
to beautify result by splitting lines.

#### Arguments

- `obj` - Object to inspect.

### SignatureBuilder().build

[🔍 find in source code](../../handsdown/signature.py#L155)

```python
def build() -> str
```

Render signature to string.

#### Returns

A string with functions signature.
