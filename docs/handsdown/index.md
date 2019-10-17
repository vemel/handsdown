# Handsdown

> Auto-generated documentation for [handsdown](../../handsdown/__init__.py) module.

- [Index](../README.md#modules) / Handsdown
- [Handsdown](#handsdown)
  - [Usage](#usage)
    - [From command line](#from-command-line)
    - [As a module](#as-a-module)
  - [Installation](#installation)
  - [Examples](#examples)
  - Modules
    - [Main](__main__.md#main)
    - [Cli Parser](cli_parser.md#cli-parser)
    - [DocstringFormatter](docstring_formatter.md#docstringformatter)
    - [Generator](generator.md#generator)
    - [IndentTrimmer](indent_trimmer.md#indenttrimmer)
    - [Loader](loader.md#loader)
    - [Main](main.md#main)
    - [MDDocument](md_document.md#mddocument)
    - [ModuleRecord](module_record.md#modulerecord)
    - [PathFinder](path_finder.md#pathfinder)
    - [Processors](processors/index.md#processors)
      - [Base](processors/base.md#base)
      - [Pep257](processors/pep257.md#pep257)
      - [Rst](processors/rst.md#rst)
      - [SectionMap](processors/section_map.md#sectionmap)
      - [Smart](processors/smart.md#smart)
    - [Signature](signature.md#signature)
    - [Utils](utils.md#utils)

Root of `handsdown` source code.

# Handsdown

## Usage

### From command line

Just go to your favorite project that has lots of docstrings but missing
auto-generated docs and let `handsdown` do the thing.

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
