# ModuleRecord

[Handsdown API Index](../../../README.md#handsdown-api-index) / [Handsdown](../../index.md#handsdown) / [AST Parser](../index.md#ast-parser) / [Node Records](./index.md#node-records) / ModuleRecord

> Auto-generated documentation for [handsdown.ast_parser.node_records.module_record](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/module_record.py) module.

## ModuleRecord

[Show source in module_record.py:20](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/module_record.py#L20)

Wrapper for an `ast.Module` node with corresponding node info.

Responsible for parsing Python source as well.

#### Arguments

- `node` - Result of `ast.parse`.

#### Signature

```python
class ModuleRecord(NodeRecord):
    def __init__(self, node: ast.Module) -> None:
        ...
```

#### See also

- [NodeRecord](./node_record.md#noderecord)

### ModuleRecord()._get_comment_docstring

[Show source in module_record.py:218](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/module_record.py#L218)

Get comment docstring preceding the object from the source code.

Returns only lines starting with `#`, lines joined with a single space.

#### Arguments

- `node_record` - Node record for source lookup.

#### Returns

A docstring as a string.

#### Signature

```python
def _get_comment_docstring(self, node_record: NodeRecord) -> str:
    ...
```

#### See also

- [NodeRecord](./node_record.md#noderecord)

### ModuleRecord()._get_function_def_lines

[Show source in module_record.py:195](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/module_record.py#L195)

Get all function definition lines for comment type hints lookup.

Removes indentation.

#### Arguments

- `function_record` - Function record for source lookup.

#### Returns

Function definition lines as an array.

#### Signature

```python
def _get_function_def_lines(self, function_record: FunctionRecord) -> List[str]:
    ...
```

#### See also

- [FunctionRecord](./function_record.md#functionrecord)

### ModuleRecord().build_children

[Show source in module_record.py:136](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/module_record.py#L136)

Collect full information about Module child records.

Used only when doc for this ModuleRecord is building.

#### Signature

```python
def build_children(self) -> None:
    ...
```

### ModuleRecord.create_from_source

[Show source in module_record.py:44](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/module_record.py#L44)

Create new [ModuleRecord](#modulerecord) from path.

#### Arguments

- `source_path` - Path to a Python source file.
- `import_string` - File absolute import string.
- `encoding` - File encoding.

#### Returns

New [ModuleRecord](#modulerecord) instance.

#### Signature

```python
@classmethod
def create_from_source(
    cls, source_path: Path, import_string: ImportString, encoding: str = ENCODING
) -> "ModuleRecord":
    ...
```

#### See also

- [ENCODING](../../constants.md#encoding)
- [ImportString](../../utils/import_string.md#importstring)

### ModuleRecord().find_record

[Show source in module_record.py:72](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/module_record.py#L72)

Find child in the Module by an absolute or relative import string.

#### Attributes

- `import_string` - record import string.

#### Returns

Found child record on None.

#### Signature

```python
def find_record(self, import_string: ImportString) -> Optional[NodeRecord]:
    ...
```

#### See also

- [ImportString](../../utils/import_string.md#importstring)
- [NodeRecord](./node_record.md#noderecord)

### ModuleRecord().get_related_import_strings

[Show source in module_record.py:250](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/module_record.py#L250)

Get a set of `related_names` found in module class, function, method and attribute records.

#### Returns

A set of absolute import strings found.

#### Signature

```python
def get_related_import_strings(self, node_record: NodeRecord) -> Set[ImportString]:
    ...
```

#### See also

- [ImportString](../../utils/import_string.md#importstring)
- [NodeRecord](./node_record.md#noderecord)

### ModuleRecord().is_init

[Show source in module_record.py:280](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/module_record.py#L280)

Check if this module is the __init__.py file.

#### Returns

True if this module is the __init__.py file.

#### Signature

```python
def is_init(self) -> bool:
    ...
```

### ModuleRecord().iter_records

[Show source in module_record.py:91](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/node_records/module_record.py#L91)

Iterate over Module class, method and fucntion records.

#### Yields

A child record.

#### Signature

```python
def iter_records(self) -> Iterator[NodeRecord]:
    ...
```

#### See also

- [NodeRecord](./node_record.md#noderecord)
