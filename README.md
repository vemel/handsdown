# 🙌 Handsdown - Python documentation generator

Python docstring-based documentation generator for lazy perfectionists.

- [🙌 Handsdown - Python documentation generator](#%f0%9f%99%8c-handsdown---python-documentation-generator)
  - [🔬 Features](#%f0%9f%94%ac-features)
  - [🐏 Examples](#%f0%9f%90%8f-examples)
  - [🎉 Usage](#%f0%9f%8e%89-usage)
    - [💻 From command line](#%f0%9f%92%bb-from-command-line)
    - [🧩 As a module](#%f0%9f%a7%a9-as-a-module)
  - [🐶 Installation](#%f0%9f%90%b6-installation)
  - [🔧 Development](#%f0%9f%94%a7-development)

## 🔬 Features

- 👓 PEP257, Google and RST docstrings support. All of them are converted to a valid markdown.
- 🐍 Works with Django and Flask apps
- 🐈 Github-friendly. Use your local markdown viewer or open docs
  [right on Github](https://github.com/vemel/handsdown/blob/master/docs/README.md)
- 📚 Signatures for every class, function and method.
- 🚀 Support for type annotations. Even for the ones from the `__future__`!
- 📦 Nice list of all modules in [Modules](https://github.com/vemel/handsdown/blob/master/docs/README.md)
- 🔎 Gather all scattered `README.md` in submodules to one place
- 🚧 Links to source code from every doc section.
- #️⃣ Make links by just adding `module.import.String` to docs. 
- 💕 Do you love type annotations? Well, you get auto-discovery of related modules for free!

## 🐏 Examples

`handsdown` built a nice
[documentation](https://github.com/vemel/handsdown/blob/master/docs/README.md) for
itself to show it's abilities. Check how it works under the hood or discover
[examples](https://github.com/vemel/handsdown/blob/master/docs/examples_index.md)
with different docstrings format.

## 🎉 Usage

### 💻 From command line

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

### 🧩 As a module

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

## 🐶 Installation

Install using pip

```bash
pip install handsdown
```

## 🔧 Development

- Install [pipenv](https://pypi.org/project/pipenv/)
- Run `pipenv install -d`
- Use `black` formatter in your IDE
