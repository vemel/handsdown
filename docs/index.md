# 🙌 Handsdown - Python documentation generator

- [🙌 Handsdown - Python documentation generator](#-handsdown---python-documentation-generator)
- [🙌 Handsdown - Python documentation generator](#-handsdown---python-documentation-generator)
  - [🔬 Features](#-features)
  - [🎉 Usage](#-usage)
    - [💻 From command line](#-from-command-line)
    - [🧩 As a module](#-as-a-module)
  - [🐶 Installation](#-installation)
  - [🔧 Development](#-development)
  - [Modules](#modules)


Python docstring-based documentation generator for lazy perfectionists.

## 🔬 Features

- 👓 PEP257, Google and RST docstrings support. All of them are converted to a valid markdown.
- 🐈 Github-friendly. Use your local markdown viewer or open docs [right on Github](docs/index.md)
- 📚 Signatures for every class, function and method.
- 🚀 Support for type annotations. Even for the ones from the `__future__`!
- 📦 Nice list of all modules in [Modules](docs/index.md#modules)
- 🔎 Gather all scattered `README.md` in submodules to one place
- 🚧 Links to source code from every doc section.
- #️⃣ Create links easily as [Generator().replace_links](./handsdown_generator.md#generatorreplace_links) (check [index.md](docs/index.md#features))
- 💕 Do you love type annotations? Well, you get auto-discovery of related modules for free!

## 🎉 Usage

### 💻 From command line

Just go to your favorite project that has lots of docstrings but missing auto-generated docs and let `handsdown` do the thing.

```bash
cd ~/my/project

# output buolt MD files to docs/*
handsdown

# or provide custom output: output_dir/*
handsdown -o output_dir

# generate docs only for my_module, but no migrations, plz
handsdown my_module --exclude my_module/migrations
```

Navigate to `docs/index.md` to check your new documentation!

### 🧩 As a module

```python
from handsdown import Generator
from handsdown import PathFinder
repo_path = Path.cwd()

handsdown_generator = Generator(
    input_path=repo_path,
    output_path=repo_path / 'output',
    source_paths=PathFinder(repo_path, "**/*.py").list()
)

# generate all docs at once
handsdown_generator.generate()
```

## 🐶 Installation

Install using pip

```bash
pip install handsdown
```

## 🔧 Development

- Install [pipenv](https://pypi.org/project/pipenv/)
- Run `pipenv install -d`
- Use `black` formatter in your IDE


## Modules

- Handsdown
  - [Main](./handsdown___main__.md)
  - [Cli parser](./handsdown_cli_parser.md)
  - [Generator](./handsdown_generator.md)
  - [Indent trimmer](./handsdown_indent_trimmer.md)
  - [Loader](./handsdown_loader.md)
  - [Main](./handsdown_main.md)
  - [Md document](./handsdown_md_document.md)
  - [Module record](./handsdown_module_record.md)
  - [Path finder](./handsdown_path_finder.md)
  - [Processors](./handsdown_processors_index.md)
    - [Base](./handsdown_processors_base.md)
    - [Pep257](./handsdown_processors_pep257.md)
    - [Rst](./handsdown_processors_rst.md)
    - [Smart](./handsdown_processors_smart.md)
  - [Signature](./handsdown_signature.md)
  - [Utils](./handsdown_utils.md)
