# 🙌 Handsdown - Python documentation generator

- [🙌 Handsdown - Python documentation generator](#%f0%9f%99%8c-handsdown---python-documentation-generator)
  - [🔬 Features](#%f0%9f%94%ac-features)
  - [🎉 Usage](#%f0%9f%8e%89-usage)
    - [💻 From command line](#%f0%9f%92%bb-from-command-line)
    - [🧩 As a module](#%f0%9f%a7%a9-as-a-module)
  - [🐶 Installation](#%f0%9f%90%b6-installation)
  - [🔧 Development](#%f0%9f%94%a7-development)

Python docstring-based documentation generator for lazy perfectionists.

## 🔬 Features

- 👓 PEP257, Google and RST docstrings support. All of them are converted to a valid markdown.
- 🐈 Github-friendly. Use your local markdown viewer or open docs [right on Github](docs/index.md)
- 📚 Signatures for every class, function and method.
- 🚀 Support for type annotations. Even for the ones from the `__future__`!
- 📦 Nice list of all modules in [Modules](docs/index.md#modules)
- 🔎 Gather all scattered `README.md` in submodules to one place
- 🚧 Links to source code from every doc section.
- #️⃣ Create links easily as `handsdown.generator.Generator.replace_links` (check [index.md](docs/index.md#features))
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
