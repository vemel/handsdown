# Handsdown: Module record

- [Handsdown: Module record](#handsdown-module-record)
  - [ModuleObjectRecord](#moduleobjectrecord)
  - [ModuleRecord](#modulerecord)
  - [ModuleRecordList](#modulerecordlist)
    - [ModuleRecordList().add](#modulerecordlistadd)
    - [ModuleRecordList().find_object](#modulerecordlistfind_object)
    - [ModuleRecordList().get_output_file_names](#modulerecordlistget_output_file_names)
    - [ModuleRecordList().get_package_names](#modulerecordlistget_package_names)

> Auto-generated documentation for [handsdown.module_record](../handsdown/module_record.py) module.

## ModuleObjectRecord

[🔍 find in source code](../handsdown/module_record.py#L7)

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

## ModuleRecord

[🔍 find in source code](../handsdown/module_record.py#L33)

```python
class ModuleRecord(
    source_path: pathlib.Path,
    output_file_name: str,
    module: Any,
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
- `import_string` - Module import string.
- `objects` - List of objects in the module.
- `docstring` - Module docstring.

## ModuleRecordList

[🔍 find in source code](../handsdown/module_record.py#L58)

```python
class ModuleRecordList() -> None
```

Aggregation of [ModuleRecord](#modulerecord) objects.

### ModuleRecordList().add

[🔍 find in source code](../handsdown/module_record.py#L97)

```python
def add(module_record: handsdown.module_record.ModuleRecord) -> None
```

Aggregation of [ModuleRecord](#modulerecord) objects.

#### See also

- [ModuleRecord](#modulerecord)

### ModuleRecordList().find_object

[🔍 find in source code](../handsdown/module_record.py#L67)

```python
def find_object(import_string: str) -> Union[handsdown.module_record.ModuleObjectRecord, NoneType]
```

Aggregation of [ModuleRecord](#modulerecord) objects.

#### See also

- [ModuleObjectRecord](#moduleobjectrecord)

### ModuleRecordList().get_output_file_names

[🔍 find in source code](../handsdown/module_record.py#L79)

```python
def get_output_file_names() -> Set[str]
```

Aggregation of [ModuleRecord](#modulerecord) objects.

### ModuleRecordList().get_package_names

[🔍 find in source code](../handsdown/module_record.py#L88)

```python
def get_package_names() -> Set[str]
```

Aggregation of [ModuleRecord](#modulerecord) objects.
