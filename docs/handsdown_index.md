# Handsdown

> Auto-generated documentation for [handsdown](../handsdown/__init__.py) module.

- [Handsdown](./README.md#handsdown) / Handsdown
  - [Usage](#usage)
    - [From command line](#from-command-line)
    - [As a module](#as-a-module)
  - [Installation](#installation)
  - [Examples](#examples)
  - Modules
    - [Main](./handsdown___main__.md#main)
    - [Cli Parser](./handsdown_cli_parser.md#cli-parser)
    - [Generator](./handsdown_generator.md#generator)
    - [IndentTrimmer](./handsdown_indent_trimmer.md#indenttrimmer)
    - [Loader](./handsdown_loader.md#loader)
    - [Main](./handsdown_main.md#main)
    - [MDDocument](./handsdown_md_document.md#mddocument)
    - [ModuleRecord](./handsdown_module_record.md#modulerecord)
    - [PathFinder](./handsdown_path_finder.md#pathfinder)
    - [Processors](./handsdown_processors_index.md#processors)
      - [Base](./handsdown_processors_base.md#base)
      - [Pep257](./handsdown_processors_pep257.md#pep257)
      - [Rst](./handsdown_processors_rst.md#rst)
      - [SectionMap](./handsdown_processors_section_map.md#sectionmap)
      - [Smart](./handsdown_processors_smart.md#smart)
    - [Signature](./handsdown_signature.md#signature)
    - [Utils](./handsdown_utils.md#utils)

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
    source_paths=path_finder.list()
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
