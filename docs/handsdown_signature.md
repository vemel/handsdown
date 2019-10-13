# Handsdown: Signature

- [Handsdown: Signature](#handsdown-signature)
  - [Config](#config)
  - [ProxyDefaultValue](#proxydefaultvalue)
  - [ProxyParameter](#proxyparameter)
    - [ProxyParameter.create](#proxyparametercreate)
  - [SignatureBuilder](#signaturebuilder)
    - [SignatureBuilder().build](#signaturebuilderbuild)

> Auto-generated documentation for [handsdown.signature](../handsdown/signature.py) module.

## Config

[🔍 find in source code](../handsdown/signature.py#L10)

```python
class Config(*args, **kwargs)
```

## ProxyDefaultValue

[🔍 find in source code](../handsdown/signature.py#L15)

```python
class ProxyDefaultValue(original: Type) -> None
```

Proxy class to represent function parameter default value in signature

#### Arguments

- `original` - Original value.

## ProxyParameter

[🔍 find in source code](../handsdown/signature.py#L39)

```python
class ProxyParameter(type_hint: Union[Type, NoneType], *args: Any, **kwargs: Any) -> None
```

Helper class to represent function parameters in signature

### ProxyParameter.create

[🔍 find in source code](../handsdown/signature.py#L57)

```python
def create(
    parameter: inspect.Parameter,
    type_hint: Union[Type, NoneType],
) -> handsdown.signature.ProxyParameter
```

Helper class to represent function parameters in signature

#### See also

- [ProxyParameter](#proxyparameter)

## SignatureBuilder

[🔍 find in source code](../handsdown/signature.py#L78)

```python
class SignatureBuilder(obj: Any)
```

Renderer for object signature. Support lazy type annotations and tries
to beautify result by splitting lines.

#### Arguments

- `obj` - Object to inspect.

### SignatureBuilder().build

[🔍 find in source code](../handsdown/signature.py#L137)

```python
def build() -> str
```

Renderer for object signature. Support lazy type annotations and tries
to beautify result by splitting lines.

#### Arguments

- `obj` - Object to inspect.
