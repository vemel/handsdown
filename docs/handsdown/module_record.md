# ModuleRecord

> Auto-generated documentation for [handsdown.module_record](../../handsdown/module_record.py) module.

- [Index](../README.md#handsdown-index) / [Handsdown](index.md#handsdown) / [ModuleRecord](#modulerecord) / ModuleRecord
  - [ModuleObjectRecord](#moduleobjectrecord)
  - [ModuleRecord](#modulerecord)
    - [ModuleRecord().get_import_string_parts](#modulerecordget_import_string_parts)
    - [ModuleRecord().get_title_parts](#modulerecordget_title_parts)
  - [ModuleRecordList](#modulerecordlist)
    - [ModuleRecordList().add](#modulerecordlistadd)
    - [ModuleRecordList().find_object](#modulerecordlistfind_object)
    - [ModuleRecordList().get_package_names](#modulerecordlistget_package_names)

## ModuleObjectRecord

[🔍 find in source code](../../handsdown/module_record.py#L9)

```python
class ModuleObjectRecord(
    source_path: pathlib.Path,
    source_line_number: int,
    output_path: pathlib.Path,
    object: Any,
    import_string: str,
    level: int,
    title: str,
    docstring: str,
    is_class: bool,
    is_related: bool,
    signature: str,
)
```

Dataclass for an imported module object.

#### Arguments

- `source_path` - Absolute import source path.
- `source_line_number` - Line number of object definition.
- `output_path` - Path to output MD file.
- `object` - Imported module object.
- `import_string` - Module import string.
- `level` - 0 for classes and functions, 1 for methods.
- `title` - Object human-readable title.
- `docstring` - Object docstring.
- `is_class` - True if object is a class.
- `is_related` - True if object is from a different module
- `signature` - Object signature.

## ModuleRecord

[🔍 find in source code](../../handsdown/module_record.py#L41)

```python
class ModuleRecord(
    source_path: pathlib.Path,
    output_path: pathlib.Path,
    module: Any,
    title: str,
    import_string: str,
    objects: List[handsdown.module_record.ModuleObjectRecord],
    docstring: str,
)
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

### ModuleRecord().get_import_string_parts

[🔍 find in source code](../../handsdown/module_record.py#L63)

```python
def get_import_string_parts() -> List[str]
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

### ModuleRecord().get_title_parts

[🔍 find in source code](../../handsdown/module_record.py#L83)

```python
def get_title_parts() -> List[str]
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

[🔍 find in source code](../../handsdown/module_record.py#L114)

```python
class ModuleRecordList()
```

Aggregation of [ModuleRecord](#modulerecord) objects.

### ModuleRecordList().add

[🔍 find in source code](../../handsdown/module_record.py#L144)

```python
def add(module_record: handsdown.module_record.ModuleRecord) -> None
```

Add new [ModuleRecord](#modulerecord).

#### Arguments

- `module_record` - A new [ModuleRecord](#modulerecord)

#### See also

- [ModuleRecord](#modulerecord)

### ModuleRecordList().find_object

[🔍 find in source code](../../handsdown/module_record.py#L123)

```python
def find_object(import_string: str) -> Union[handsdown.module_record.ModuleObjectRecord, NoneType]
```

Find [ModuleObjectRecord](#moduleobjectrecord) by it's import string.

#### Arguments

- `import_string` - Object import string.

#### Returns

Found [ModuleObjectRecord](#moduleobjectrecord) instance or None.

#### See also

- [ModuleObjectRecord](#moduleobjectrecord)

### ModuleRecordList().get_package_names

[🔍 find in source code](../../handsdown/module_record.py#L135)

```python
def get_package_names() -> Set[str]
```

Get top level import strings.

#### Returns

A set of top level imports as strings.
