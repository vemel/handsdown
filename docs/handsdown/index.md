# Handsdown

> Auto-generated documentation for [handsdown](https://github.com/vemel/handsdown/blob/master/handsdown/__init__.py) module.

Root of [Handsdown](#handsdown) source code.

- [Handsdown](../README.md#-handsdown---python-documentation-generator) / [Modules](../MODULES.md#modules) / Handsdown
- [Handsdown](#handsdown)
    - [Usage](#usage)
        - [From command line](#from-command-line)
        - [As a module](#as-a-module)
    - [Installation](#installation)
    - [Examples](#examples)
    - Modules
        - [Main](magic_main.md#main)
        - [AST Parser](ast_parser/index.md#ast-parser)
            - [Analyzers](ast_parser/analyzers/index.md#analyzers)
                - [BaseAnalyzer](ast_parser/analyzers/base_analyzer.md#baseanalyzer)
                - [ClassAnalyzer](ast_parser/analyzers/class_analyzer.md#classanalyzer)
                - [ExpressionAnalyzer](ast_parser/analyzers/expression_analyzer.md#expressionanalyzer)
                - [FunctionAnalyzer](ast_parser/analyzers/function_analyzer.md#functionanalyzer)
                - [ModuleAnalyzer](ast_parser/analyzers/module_analyzer.md#moduleanalyzer)
            - [Enums](ast_parser/enums.md#enums)
            - [ModuleRecordList](ast_parser/module_record_list.md#modulerecordlist)
            - [Node Records](ast_parser/node_records/index.md#node-records)
                - [ArgumentRecord](ast_parser/node_records/argument_record.md#argumentrecord)
                - [AttributeRecord](ast_parser/node_records/attribute_record.md#attributerecord)
                - [ClassRecord](ast_parser/node_records/class_record.md#classrecord)
                - [ExpressionRecord](ast_parser/node_records/expression_record.md#expressionrecord)
                - [FunctionRecord](ast_parser/node_records/function_record.md#functionrecord)
                - [ImportRecord](ast_parser/node_records/import_record.md#importrecord)
                - [ModuleRecord](ast_parser/node_records/module_record.md#modulerecord)
                - [NodeRecord](ast_parser/node_records/node_record.md#noderecord)
                - [TextRecord](ast_parser/node_records/text_record.md#textrecord)
            - [Smart AST](ast_parser/smart_ast.md#smart-ast)
            - [Type Defs](ast_parser/type_defs.md#type-defs)
        - [CLI Parser](cli_parser.md#cli-parser)
        - [DocstringFormatter](docstring_formatter.md#docstringformatter)
        - [Generator](generator.md#generator)
        - [IndentTrimmer](indent_trimmer.md#indenttrimmer)
        - [Loader](loader.md#loader)
        - [Main](main.md#main)
        - [MDDocument](md_document.md#mddocument)
        - [PathFinder](path_finder.md#pathfinder)
        - [Processors](processors/index.md#processors)
            - [Base Docstring Processor](processors/base.md#base-docstring-processor)
            - [PEP 257 Docstring Processor](processors/pep257.md#pep-257-docstring-processor)
            - [reStructuredText Docstring Processor](processors/rst.md#restructuredtext-docstring-processor)
            - [SectionMap](processors/section_map.md#sectionmap)
            - [Smart Docstring Processor](processors/smart.md#smart-docstring-processor)
        - [Sentinel](sentinel.md#sentinel)
        - [Settings](settings.md#settings)
        - [Utils](utils/index.md#utils)
            - [ImportString](utils/import_string.md#importstring)
            - [Logger](utils/logger.md#logger)
        - [Version](version.md#version)

# Handsdown

## Usage

### From command line

Just go to your favorite project that has lots of docstrings but missing
auto-generated docs and let [Handsdown](#handsdown) do the thing.

```bash
cd ~/my/project

# output buolt MD files to docs/*
handsdown

# or provide custom output: output_dir/*
handsdown -o output_dir

# generate docs only for my_module, but no migrations, plz
handsdown my_module --exclude my_module/migrations
```

Navigate to `docs/README.md` to check your new documentation!

### As a module

```python
from handsdown import Generator, PathFinder

# this is our project root directory
repo_path = Path.cwd()

# this little tool works like `pathlib.Path.glob` with some extra magic
# but in this case `repo_path.glob("**/*.py")` would do as well
path_finder = PathFinder(repo_path, "**/*.py")

# no docs for tests and build
path_finder.exclude("tests/*", "build/*")

# initialize generator
handsdown = Generator(
    input_path=repo_path,
    output_path=repo_path / 'output',
    source_paths=path_finder.glob("**/*.py")
)

# generate all docs at once
handsdown.generate_docs()

# or generate just for one doc
handsdown.generate_doc(repo_path / 'my_module' / 'source.py')

# and generate index.md file
handsdown.generate_index()

# navigate to `output` dir and check results
```

## Installation

Install using pip

```bash
pip install handsdown
```

## Examples

- All Markdown documentation in this project
- [RST docstrings](../examples/rst_example.py) with [generated output](/docs/examples_rst_example.md#rstexample)
