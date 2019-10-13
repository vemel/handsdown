# Handsdown: Module record

- [Handsdown: Module record](#handsdown-module-record)
  - [ModuleObjectRecord](#moduleobjectrecord)
  - [ModuleRecord](#modulerecord)
  - [ModuleRecordList](#modulerecordlist)

> Auto-generated documentation for [/.home.vlad.work.vemel.handsdown.handsdown.module_record](..//home/vlad/work/vemel/handsdown/handsdown/module_record.py) module.

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

## ModuleRecord

[🔍 find in source code](../handsdown/module_record.py#L31)

```python
class ModuleRecord(
    source_path: pathlib.Path,
    output_file_name: str,
    module: Any,
    import_string: str,
    objects: List[handsdown.module_record.ModuleObjectRecord],
)
```
Representation of an imported module.

#### Arguments

- `source_path` - Absolute import source path.
- `output_file_name` - MD file name for this module.
- `module` - Imported module.
- `import_string` - Module import string.
- `objects` - List of objects in the module.

## ModuleRecordList

[🔍 find in source code](../handsdown/module_record.py#L50)

```python
class ModuleRecordList()
```