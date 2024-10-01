# AST Parser


Collection of tools for analyzing AST and also rendering it back to a valid Python code.

## Usage

Use `handsdown.ast_parser.node_records.ModuleRecord` to parse the source code.

### Examples

```python
from pathlib import Path

from handsdown.utils.import_string import ImportString
from handsdown.ast_parser.node_records import ModuleRecord

source_path = Path("my_module.py")
import_string = ImportString("my_module")
module_record = ModuleRecord.create_from_source(source_path, import_string)
module_record.build_children() # generate records for imports, classes, attributes
and function in module

function_record = module_record.function_records[0] # get the first function in module
print(function_record.render(allow_multiline=True)) # print function definition
print(function_record.return_type_hint.render()) # print function return type annotation
```

[Handsdown API Index](../../README.md#handsdown-api-index) / [Handsdown](../index.md#handsdown) / AST Parser

> Auto-generated documentation for [handsdown.ast_parser](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/__init__.py) module.

## Modules

- [Analyzers](analyzers/index.md)
- [ModuleRecordList](./module_record_list.md)
- [Node Records](node_records/index.md)
- [Smart Ast](./smart_ast.md)
- [Type Defs](./type_defs.md)
