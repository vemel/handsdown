# ModuleRecord

- [Handsdown](./README.md) / [Handsdown](./handsdown_index.md) / ModuleRecord
  - [ModuleObjectRecord](#moduleobjectrecord)
  - [ModuleRecord](#modulerecord)
    - [ModuleRecord().get_import_string_parts](#modulerecordget_import_string_parts)
    - [ModuleRecord().get_title_parts](#modulerecordget_title_parts)
  - [ModuleRecordList](#modulerecordlist)
    - [ModuleRecordList().__iter__](#modulerecordlist__iter__)
    - [ModuleRecordList().add](#modulerecordlistadd)
    - [ModuleRecordList().find_object](#modulerecordlistfind_object)
    - [ModuleRecordList().get_output_file_names](#modulerecordlistget_output_file_names)
    - [ModuleRecordList().get_package_names](#modulerecordlistget_package_names)

> Auto-generated documentation for [handsdown.module_record](../handsdown/module_record.py) module

## ModuleObjectRecord

[🔍 find in source code](../handsdown/module_record.py#L9)

```python
class ModuleObjectRecord(
    source_path: pathlib.Path,
    source_line_number: int,
    output_file_name: str,
    object: Any,
    import_string: str,
    level: int,
    title: str,
    docstring: Union[str, NoneType],
    is_class: bool,
)
```

Representation of an imported module object.

#### Arguments

- `source_path` - Absolute import source path.
- `source_line_number` - Line number of object definition.
- `output_file_name` - MD file name for this module.
- `object` - Imported module object.
- `import_string` - Module import string.
- `level` - 0 for classes and functions, 1 for methods.
- `title` - Object human-readable title.
- `docstring` - Object docstring.
- `is_class` - True if object is a class.

## ModuleRecord

[🔍 find in source code](../handsdown/module_record.py#L37)

```python
class ModuleRecord(
    source_path: pathlib.Path,
    output_file_name: str,
    module: Any,
    title: str,
    import_string: str,
    objects: List[handsdown.module_record.ModuleObjectRecord],
    docstring: Union[str, NoneType],
)
```

Representation of an imported module.

#### Arguments

- `source_path` - Absolute import source path.
- `output_file_name` - MD file name for this module.
- `module` - Imported module.
- `title` - Human readable module title.
- `import_string` - Module import string.
- `objects` - List of objects in the module.
- `docstring` - Module docstring.

### ModuleRecord().get_import_string_parts

[🔍 find in source code](../handsdown/module_record.py#L59)

```python
def get_import_string_parts() -> List[str]
```

Get parts of module `import_string`.

#### Examples

```python
ModuleRecord(..., import_string='my_module.utils.parsers').get_title_parts()
# ['My my_module', 'utils', 'parsers']
ModuleRecord(..., import_string='my_module.__main__').get_title_parts()
# ['my_module', '__main__']
ModuleRecord(..., import_string='my_module.my_lib', title='MyLibrary').get_title_parts()
# ['my_module', 'my_lib']
```

#### Returns

A list of import string parts as strings.

### ModuleRecord().get_title_parts

[🔍 find in source code](../handsdown/module_record.py#L79)

```python
def get_title_parts() -> List[str]
```

Get parts of module title from module import string.
If `title` is set, last part replaced with `title`.

#### Examples

```python
ModuleRecord(..., import_string='my_module.utils.parsers').get_title_parts()
# ['My module', 'Utils', 'parsers']
ModuleRecord(..., import_string='my_module.__main__').get_title_parts()
# ['My module', 'Main']
ModuleRecord(..., import_string='my_module.my_lib', title='MyLibrary').get_title_parts()
# ['My module', 'MyLibrary']
```

#### Returns

A list of title parts as strings.

## ModuleRecordList

[🔍 find in source code](../handsdown/module_record.py#L110)

```python
class ModuleRecordList()
```

Aggregation of [ModuleRecord](#modulerecord) objects.

### ModuleRecordList().__iter__

[🔍 find in source code](../handsdown/module_record.py#L162)

```python
def __iter__() -> Generator[handsdown.module_record.ModuleRecord, NoneType, NoneType]
```

Iterate over all added [ModuleRecord](#modulerecord) entries.

#### Returns

A generator iterating over [ModuleRecord](#modulerecord) entries.

#### See also

- [ModuleRecord](#modulerecord)

### ModuleRecordList().add

[🔍 find in source code](../handsdown/module_record.py#L149)

```python
def add(module_record: handsdown.module_record.ModuleRecord) -> None
```

Add new [ModuleRecord](#modulerecord).

#### Arguments

- `module_record` - A new [ModuleRecord](#modulerecord)

#### See also

- [ModuleRecord](#modulerecord)

### ModuleRecordList().find_object

[🔍 find in source code](../handsdown/module_record.py#L119)

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

### ModuleRecordList().get_output_file_names

[🔍 find in source code](../handsdown/module_record.py#L131)

```python
def get_output_file_names() -> Set[str]
```

Get all output MD file names.

#### Returns

A set of output names as strings.

### ModuleRecordList().get_package_names

[🔍 find in source code](../handsdown/module_record.py#L140)

```python
def get_package_names() -> Set[str]
```

Get top level import strings.

#### Returns

A set of top level imports as strings.
