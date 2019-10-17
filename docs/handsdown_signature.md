# Signature

> Auto-generated documentation for [handsdown.signature](../handsdown/signature.py) module.

- [Handsdown](README.md#handsdown) / [Handsdown](handsdown_index.md#handsdown) / Signature
  - [Config](#config)
  - [ProxyDefaultValue](#proxydefaultvalue)
  - [ProxyParameter](#proxyparameter)
    - [ProxyParameter.create](#proxyparametercreate)
  - [SignatureBuilder](#signaturebuilder)
    - [SignatureBuilder().build](#signaturebuilderbuild)

## Config

[🔍 find in source code](../handsdown/signature.py#l10)

```python
class Config(*args, **kwargs)
```

## ProxyDefaultValue

[🔍 find in source code](../handsdown/signature.py#l15)

```python
class ProxyDefaultValue(original: Type)
```

Proxy class to represent function parameter default value in signature

#### Arguments

- `original` - Original value.

## ProxyParameter

[🔍 find in source code](../handsdown/signature.py#l39)

```python
class ProxyParameter(type_hint: Union[Type, NoneType], *args: Any, **kwargs: Any)
```

Helper class to represent function parameters in signature

### ProxyParameter.create

[🔍 find in source code](../handsdown/signature.py#l57)

```python
def create(
    parameter: inspect.Parameter,
    type_hint: Union[Type, NoneType],
) -> handsdown.signature.ProxyParameter
```

Create [ProxyParameter](#proxyparameter) for original `inspect.Parameter`

#### Arguments

- `parameter` - original `inspect.Parameter`
- `type_hint` - resoled type hint that should replace a lazy annotation

#### See also

- [ProxyParameter](#proxyparameter)

## SignatureBuilder

[🔍 find in source code](../handsdown/signature.py#l78)

```python
class SignatureBuilder(obj: Any)
```

Renderer for object signature. Support lazy type annotations and tries
to beautify result by splitting lines.

#### Arguments

- `obj` - Object to inspect.

### SignatureBuilder().build

[🔍 find in source code](../handsdown/signature.py#l132)

```python
def build() -> str
```

Render signature to string.

#### Returns

A string with functions signature.
