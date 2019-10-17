# 🙌 Handsdown - Python documentation generator

> Auto-generated documentation index..

![PyPI](https://img.shields.io/pypi/v/handsdown)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/handsdown)
![PyPI - Format](https://img.shields.io/pypi/format/handsdown)
![PyPI - Status](https://img.shields.io/pypi/status/handsdown)
![Travis (.org)](https://img.shields.io/travis/vemel/handsdown)
![Codecov](https://img.shields.io/codecov/c/github/vemel/handsdown)

Python docstring-based documentation generator for lazy perfectionists.

- [🙌 Handsdown - Python documentation generator](#%f0%9f%99%8c-handsdown---python-documentation-generator)
  - [🔬 Features](#%f0%9f%94%ac-features)
  - [🐏 Examples](#%f0%9f%90%8f-examples)
  - [🎉 Usage](#%f0%9f%8e%89-usage)
    - [💻 From command line](#%f0%9f%92%bb-from-command-line)
    - [📝 GitHub Pages](#%f0%9f%93%9d-github-pages)
    - [🧩 As a module](#%f0%9f%a7%a9-as-a-module)
  - [🐶 Installation](#%f0%9f%90%b6-installation)
  - [🔧 Development](#%f0%9f%94%a7-development)
  - [Modules](#modules)

## 🔬 Features

- 👓 [PEP 257](https://www.python.org/dev/peps/pep-0257/), [Google](http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) and [reStructuredText](https://www.python.org/dev/peps/pep-0287/) docstrings support. All of them are converted to a valid markdown.
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

### 📝 GitHub Pages

`handsdown` comes with built-in support for [GitHub Pages](https://pages.github.com/),
although some setup is required. By default documentation uses relative links to source files,
so for `GitHub Pages` we need absolute URLs to a GitHub repositore for `find in source code`
links to work.

Now let's generate `GitHub Pages`-friendly documentation

```bash
# Generate documentation that points to master branch
# do not use custom output location, as as `GitHub Pages`
# works only with `docs` directory
handsdown --gh-pages `git config --get remote.origin.url`

# or specify GitHub url directly
handsdown --gh-pages https://github.com/<user>/<project>/blob/master/
```

Commit your changes and enable `GitHub Pages` by setting your project
`Settings` > `GitHub Pages` > `Source` to `master branch /docs folder`

That's it, you are good to go! Add plugins to `docs/_config.yml` or change
theme to add your own touch.

If you still want to have relative links to source, e.g. for using docs locally,
generate docs to another folder

```bash
handsdown -o docs_local # `docs_local` folder will be created in your project root
```

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

- [Examples](examples/index.md#examples)
  - [Google docstrings examples](examples/google_docstrings.md#google-docstrings-examples)
  - [PEP 257 - reStructuredText docstrings examples](examples/pep257_docstrings.md#pep-257---restructuredtext-docstrings-examples)
  - [PEP 287 - reStructuredText docstrings examples](examples/rst_docstrings.md#pep-287---restructuredtext-docstrings-examples)
- [Handsdown](handsdown/index.md#handsdown)
  - [Main](handsdown/__main__.md#main)
  - [CLI Parser](handsdown/cli_parser.md#cli-parser)
  - [DocstringFormatter](handsdown/docstring_formatter.md#docstringformatter)
  - [Generator](handsdown/generator.md#generator)
  - [IndentTrimmer](handsdown/indent_trimmer.md#indenttrimmer)
  - [Loader](handsdown/loader.md#loader)
  - [Main](handsdown/main.md#main)
  - [MDDocument](handsdown/md_document.md#mddocument)
  - [ModuleRecord](handsdown/module_record.md#modulerecord)
  - [PathFinder](handsdown/path_finder.md#pathfinder)
  - [Processors](handsdown/processors/index.md#processors)
    - [Base](handsdown/processors/base.md#base)
    - [Pep257](handsdown/processors/pep257.md#pep257)
    - [Rst](handsdown/processors/rst.md#rst)
    - [SectionMap](handsdown/processors/section_map.md#sectionmap)
    - [Smart](handsdown/processors/smart.md#smart)
  - [Signature](handsdown/signature.md#signature)
  - [Utils](handsdown/utils.md#utils)
