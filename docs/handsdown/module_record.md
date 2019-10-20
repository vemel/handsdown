# ModuleRecord

> Auto-generated documentation for [handsdown.module_record](https://github.com/vemel/handsdown/blob/master/handsdown/module_record.py) module.

Dataclass for an imported module.

- [Handsdown](../README.md#-handsdown---python-documentation-generator) / [Modules](../MODULES.md#modules) / [Handsdown](index.md#handsdown) / ModuleRecord
  - [ModuleObjectRecord](#moduleobjectrecord)
    - [ModuleObjectRecord().signature](#moduleobjectrecordsignature)
    - [ModuleObjectRecord().get_reference_objects](#moduleobjectrecordget_reference_objects)
  - [ModuleRecord](#modulerecord)
    - [ModuleRecord().get_import_string_parts](#modulerecordget_import_string_parts)
    - [ModuleRecord.get_reference_objects](#modulerecordget_reference_objects)
    - [ModuleRecord().get_title_parts](#modulerecordget_title_parts)
  - [ModuleRecordList](#modulerecordlist)
    - [ModuleRecordList().add](#modulerecordlistadd)
    - [ModuleRecordList().find_object](#modulerecordlistfind_object)
    - [ModuleRecordList().get_package_names](#modulerecordlistget_package_names)

## ModuleObjectRecord

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/module_record.py#L15)

```python
class ModuleObjectRecord(
    source_path: Path,
    source_line_number: int,
    output_path: Path,
    obj: Any,
    import_string: Text,
    level: int,
    title: Text,
    docstring: Text,
    is_class: bool,
    is_related: bool,
    module_record: ModuleRecord,
) -> None
```

Dataclass for an imported module object.

#### Arguments

- `source_path` - Absolute import source path.
- `source_line_number` - Line number of object definition.
- `output_path` - Path to output MD file.
- `object` - Imported module object.
- `parent` - Imported module object parent.
- `import_string` - Module import string.
- `level` - 0 for classes and functions, 1 for methods.
- `title` - Object human-readable title.
- `docstring` - Object docstring.
- `is_class` - True if object is a class.
- `is_related` - True if object is from a different module
- `signature` - Object signature.

#### See also

- [ModuleRecord](#modulerecord)

### ModuleObjectRecord().signature

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/module_record.py#L15)

```python
@property
def signature() -> Text
```

Get object signature.

#### Returns

A string with object signature.

### ModuleObjectRecord().get_reference_objects

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/module_record.py#L96)

```python
def get_reference_objects() -> List[ModuleObjectRecord]
```

Get a list of all objects referenced in default values or type hints
of the object.

#### Returns

A list of related [ModuleObjectRecord](#moduleobjectrecord).

## ModuleRecord

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/module_record.py#L125)

```python
class ModuleRecord(
    source_path: Path,
    output_path: Path,
    module: Any,
    title: Text,
    import_string: Text,
    objects: List[ModuleObjectRecord],
    docstring: Text,
) -> None
```

Dataclass for an imported module.

#### Arguments

- `source_path` - Absolute import source path.
- `output_path` - Path to output MD file.
- `module` - Imported module.
- `title` - Human readable module title.
- `import_string` - Module import string.
- `objects` - List of objects in the module.
- `docstring` - Module docstring.

#### See also

- [ModuleObjectRecord](#moduleobjectrecord)

### ModuleRecord().get_import_string_parts

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/module_record.py#L162)

```python
def get_import_string_parts() -> List[Text]
```

Get parts of module `import_string`.

#### Examples

```python
ModuleRecord(..., import_string='my_module.utils.parsers').get_title_parts()
['My my_module', 'utils', 'parsers']

ModuleRecord(..., import_string='my_module.__main__').get_title_parts()
['my_module', '__main__']

ModuleRecord(..., import_string='my_module.my_lib', title='MyLibrary').get_title_parts()
['my_module', 'my_lib']
```

#### Returns

A list of import string parts as strings.

### ModuleRecord.get_reference_objects

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/module_record.py#L214)

```python
@staticmethod
def get_reference_objects() -> List[ModuleObjectRecord]
```

Get a list of all objects referenced in default values or type hints
of the object.

For module no related objects are listed, added for compatibility
with [ModuleObjectRecord](#moduleobjectrecord).

#### Returns

An empty list.

#### See also

- [ModuleObjectRecord](#moduleobjectrecord)

### ModuleRecord().get_title_parts

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/module_record.py#L183)

```python
def get_title_parts() -> List[Text]
```

Get parts of module title from module import string.
If `title` is set, last part replaced with `title`.

#### Examples

```python
ModuleRecord(..., import_string='my_module.utils.parsers').get_title_parts()
['My module', 'Utils', 'parsers']

ModuleRecord(..., import_string='my_module.__main__').get_title_parts()
['My module', 'Main']

ModuleRecord(..., import_string='my_module.my_lib', title='MyLibrary').get_title_parts()
['My module', 'MyLibrary']
```

#### Returns

A list of title parts as strings.

## ModuleRecordList

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/module_record.py#L230)

```python
class ModuleRecordList() -> None
```

Aggregation of [ModuleRecord](#modulerecord) objects.

### ModuleRecordList().add

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/module_record.py#L263)

```python
def add(module_record: ModuleRecord) -> None
```

Add new [ModuleRecord](#modulerecord).

#### Arguments

- `module_record` - A new [ModuleRecord](#modulerecord)

#### See also

- [ModuleRecord](#modulerecord)

### ModuleRecordList().find_object

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/module_record.py#L240)

```python
def find_object(import_string: Text) -> Optional[ModuleObjectRecord]
```

Find [ModuleObjectRecord](#moduleobjectrecord) by it's import string.

#### Arguments

- `import_string` - Object import string.

#### Returns

Found [ModuleObjectRecord](#moduleobjectrecord) instance or None.

#### See also

- [ModuleObjectRecord](#moduleobjectrecord)

### ModuleRecordList().get_package_names

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/module_record.py#L253)

```python
def get_package_names() -> Set[Text]
```

Get top level import strings.

#### Returns

A set of top level imports as strings.
