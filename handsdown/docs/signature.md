# Signature

- [Signature](#signature)
  - [get_type_hints](#get_type_hints)
  - [Config](#config)
  - [ProxyDefaultValue](#proxydefaultvalue)
  - [ProxyParameter](#proxyparameter)
    - [ProxyParameter.create](#proxyparametercreate)
  - [SignatureBuilder](#signaturebuilder)
    - [SignatureBuilder().build](#signaturebuilderbuild)

> Auto-generated documentation for [signature](../signature.py) module.

## get_type_hints

[🔍 find in source code](../signature.py#L926)

```python
def get_type_hints(obj, globalns=None, localns=None)
```
Return type hints for an object.

    This is often the same as obj.__annotations__, but it handles
    forward references encoded as string literals, and if necessary
    adds Optional[t] if a default value equal to None is set.

    The argument may be a module, class, method, or function. The annotations
    are returned as a dictionary. For classes, annotations include also
    inherited members.

    TypeError is raised if the argument is not of a type that can contain
    annotations, and an empty dictionary is returned if no annotations are
    present.

    BEWARE -- the behavior of globalns and localns is counterintuitive
    (unless you are familiar with how eval() and exec() work).  The
    search order is locals first, then globals.

    - If no dict arguments are passed, an attempt is made to use the
      globals from obj (or the respective module's globals for classes),
      and these are also used as the locals.  If the object does not appear
      to have globals, an empty dictionary is used.

    - If one dict argument is passed, it is used for both globals and
      locals.

    - If two dict arguments are passed, they specify globals and
      locals, respectively.
    

## Config

[🔍 find in source code](../signature.py#L10)

```python
class Config(*args, **kwargs)
```
## ProxyDefaultValue

[🔍 find in source code](../signature.py#L15)

```python
class ProxyDefaultValue(original: Type) -> None
```
"
    Proxy class to represent function parameter default value in signature

    Arguments:
        original -- Original value.
    

## ProxyParameter

[🔍 find in source code](../signature.py#L39)

```python
class ProxyParameter(type_hint: Union[Type, NoneType], *args: Any, **kwargs: Any) -> None
```
Helper class to represent function parameters in signature

### ProxyParameter.create

[🔍 find in source code](../signature.py#L57)

```python
def create(
    parameter: inspect.Parameter,
    type_hint: Union[Type, NoneType],
) -> signature.ProxyParameter
```
Create `ProxyParameter` for original `inspect.Parameter`

#### Arguments

- `parameter` - original `inspect.Parameter`
- `type_hint` - resoled type hint that should replace a lazy annotation

## SignatureBuilder

[🔍 find in source code](../signature.py#L78)

```python
class SignatureBuilder(obj: Any)
```
Renderer for object signature. Support lazy type annotations and tries
to beautify result by splitting lines.

#### Arguments

- `obj` - Object to inspect.

### SignatureBuilder().build

[🔍 find in source code](../signature.py#L134)

```python
def build() -> str
```
Render signature to string.

#### Returns

A string with functions signature.
