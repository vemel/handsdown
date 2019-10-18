# 🙌 Handsdown - Python documentation generator

![PyPI](https://img.shields.io/pypi/v/handsdown)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/handsdown)
![PyPI - Format](https://img.shields.io/pypi/format/handsdown)
![PyPI - Status](https://img.shields.io/pypi/status/handsdown)
![Travis (.org)](https://img.shields.io/travis/vemel/handsdown)
![Codecov](https://img.shields.io/codecov/c/github/vemel/handsdown)

Python docstring-based documentation generator for lazy perfectionists.

- [🙌 Handsdown - Python documentation generator](#%f0%9f%99%8c-handsdown---python-documentation-generator)
  - [🔬 Features](#%f0%9f%94%ac-features)
  - [🤔 Do you need handsdown?](#%f0%9f%a4%94-do-you-need-handsdown)
  - [🐏 Examples](#%f0%9f%90%8f-examples)
  - [🎉 Usage](#%f0%9f%8e%89-usage)
    - [💻 From command line](#%f0%9f%92%bb-from-command-line)
    - [📝 GitHub Pages](#%f0%9f%93%9d-github-pages)
    - [🧩 As a module](#%f0%9f%a7%a9-as-a-module)
  - [🐶 Installation](#%f0%9f%90%b6-installation)
  - [🔧 Development](#%f0%9f%94%a7-development)

## 🔬 Features

- 👓 [PEP 257](https://www.python.org/dev/peps/pep-0257/),
  [Google](http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
  and [reStructuredText](https://www.python.org/dev/peps/pep-0287/)
  docstrings support. All of them are converted to a valid markdown.
- 🐍 Works with [Django](https://www.djangoproject.com/) and [Flask](https://palletsprojects.com/p/flask/) apps
- 🐈 GitHub-friendly. Use your local markdown viewer, open docs
  [right on GitHub](https://github.com/vemel/handsdown/blob/master/docs/README.md) or deploy it on
  [GitHub Pages](https://vemel.github.io/handsdown/)!
- 📚 Signatures for every class, function, property and method.
- 🚀 Support for type annotations. Even for the ones from the `__future__`!
- 📦 Nice list of all modules in [Modules](https://github.com/vemel/handsdown/blob/master/docs/README.md)
- 🔎 Gather all scattered `README.md` in submodules to one place
- 🚧 Find related source code from every doc section.
- #️⃣ Make links by just adding `module.import.String` to docs.
- 💕 Do you use type annotations? Well, you get auto-discovery of related modules for free!

## 🤔 Do you need handsdown?

You definitely *do* if you:

- prefer to automate documentation builds
- work with a team and plan to simplify knowledge sharing
- want to show your project without navigating through a source code
- build `Django` or `Flask` applications, and even if you do not
- are proud of your project and are not afraid to show it
- love Open Source

And probably *do not* if you:

- plan to build html pages locally (Look at
- [pydocmd](https://pypi.org/project/pydoc-markdown/), they are doing a great job!)
- not very into docstrings and type annotations
- like to abstract a documentation away from the way things really are
- use [Pandas docstrings](https://pandas.pydata.org/pandas-docs/stable/development/contributing_docstring.html)
  as they are not supported yet

## 🐏 Examples

`handsdown` built a nice
[documentation](https://github.com/vemel/handsdown/blob/master/docs/README.md) for
itself to show it's abilities. Check how it works under the hood or discover
[examples](https://github.com/vemel/handsdown/blob/master/docs/examples_index.md)
with different docstrings format.

## 🎉 Usage

### 💻 From command line

Just go to your favorite project that has lots of docstrings but missing
auto-generated docs, install dependencies to avoid import errors and let
`handsdown` do the thing.

```bash
cd ~/my/project

# output buolt MD files to docs/*
handsdown

# or provide custom output: output_dir/*
handsdown -o output_dir

# generate docs only for my_module, but no migrations, plz
handsdown my_module --exclude my_module/migrations

# okay, what about Django?
# you need to set `DJANGO_SETTINGS_MODULE`
# and exclude migrations folders as they usually are not very interesting
export DJANGO_SETTINGS_MODULE="settings" # use your path to settings
handsdown --exclude */migrations
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
