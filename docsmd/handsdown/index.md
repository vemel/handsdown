# Handsdown

Root of `handsdown` source code.

# Handsdown

Python package `handsdown` provides types, functions, and a command-line interface
for accessing public documentation of Python modules, and for presenting it in a
Markdown format ready to be publiched to GitHub Pages or Read the Docs.

`handsdown` extracts documentation of:

- Modules
  - docstring
  - submodules
  - function definitions
  - class definitions
  - global variables documented in comment-style
  - global objects mentioned in docstring
- Functions
  - docstring
  - arguments
  - decorators
  - type annotations
  - global objects mentioned in docstring
  - parent module objects mentioned in docstring
- Classes
  - docstring
  - `__init__` method
  - public methods
  - magic methods with defined docstring
  - attributes documented in comment-style
  - decorators
  - base classes
  - global objects mentioned in docstring
  - parent module objects mentioned in docstring
- Class methods
  - docstring
  - arguments
  - decorators
  - type annotations
  - global objects mentioned in docstring
  - parent class objects mentioned in docstring
  - parent module objects mentioned in docstring

## Prepare your code

```python
# main_example.py
"""
This is a module docstring. It will appear in documentation.

## Notes

You can use Markdown here to make it nicer. Also, in any docstring you
can put a global object import string in backticks, like `other_module.OtherClass`,
and it will be transformed to a link.
"""
from typing import Text, TYPE_CHECKING

from my_project.other_module import BaseClass  # pylint: disable=import-error

if TYPE_CHECKING:
    from my_project.type_defs import StuffCallable  # pylint: disable=import-error

# This is a comment-style documented global variable, so it is added to
# `main_example` module attributes with this comment as a documentation for it
# FIXME: FIXME and TODO comments are igonred
MODULE_NAME = "My Module"

# Private args never appear in docs
_PRIVATE_ATTR = "Private attr"


def hello(name: Text) -> Text:
    """
    This is module function and it is added to documentation even if it does
    not have a docstring. Function signature will be also generated respecting
    regular and comment-style type annotations. Let's use PEP 257 format here.

    Examples::

        # Google-style code block here, but we could use Markdown code block as well
        >>> hello('John')
        'Hello, John!'

        >>> hello('')
        'Hello!'

    Arguments:
        name -- Name of the person to greet.

    Returns:
        A greeting. No need to put types here if you use type annotations.
    """
    if not name:
        return "Hello!"

    return f"Hello, {name}!"


class MyClass(BaseClass):
    """
    MyClass documentation here.

    .. note:: This time we use RST docstrings format.
    """

    # This is a comment-style documented class attribute, so it is added to
    # `main_example.MyClass` attributes with this comment as a documentation for it.
    STUFF_COUNT = 3

    @classmethod
    def do_something(cls, stuff):
        # type: (StuffCallable) -> bool
        """
        This is a public method that uses comment-style type annotations. If decorators
        or types from annotations are from your project, links to them will be added
        to `See also` section. Since this function depends on `STUFF_COUNT`, we can add
        it to a docstring in backticks and it will be transformed to a link.

        .. code-block:: python

            # usage example
            def my_stuff(amount):
                return amount > 5

            MyClass.do_something(my_stuff)  # False

        .. versionadded:: 1.3
        .. deprecated:: 1.8
        .. versionchanged:: 1.4
            All these directives are added to `Notes` section and formatted in Sphinx-style.

        :param stuff: Function do execute.
        :returns: `stuff` result.
        """
        return stuff(cls.STUFF_COUNT)

    def __bool__(self):
        # type: () -> bool
        """
        Magic methods are added to docs only if they have docstrings.

        :returns: True if `STUFF_COUNT` is not zero
        """
        return self.STUFF_COUNT
```

## Usage

### From command line

Just go to your favorite project that has lots of docstrings but missing
auto-generated docs and let `handsdown` do the thing.

```bash
cd ~/my/project

# build documentation *.md* files in docs/* directory
handsdown

# or provide custom output directory: output_dir/*
handsdown -o output_dir

# generate docs only for my_module, but exclude migrations
handsdown my_module --exclude 'build/*' 'tests/*' 'test/*' '*/__pycache__/*' '.*/*' 'my_module/migrations'

# generate documentation for deployment
handsdown --external `git config --get remote.origin.url` -n ProjectName
```

Navigate to `docs/README.md` to check your new documentation!

### As a module

```python
from handsdown.generator import Generator
from handsdown.utils.path_finder import PathFinder

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

## More examples

- All documentation in this project
- [Main](https://github.com/vemel/handsdown/blob/main/examples/main_example.py) with [generated output](https://github.com/vemel/handsdown/tree/main/docs/examples/main_example.md)
- [RST docstrings](https://github.com/vemel/handsdown/blob/main/examples/rst_docstrings.py) with [generated output](https://github.com/vemel/handsdown/tree/main/docs/examples/rst_docstrings.md)
- [Google docstrings](https://github.com/vemel/handsdown/blob/main/examples/google_docstrings.py) with [generated output](https://github.com/vemel/handsdown/tree/main/docs/examples/google_docstrings.md)
- [PEP 257 docstrings](https://github.com/vemel/handsdown/blob/main/examples/pep257_docstrings.py) with [generated output](https://github.com/vemel/handsdown/tree/main/docs/examples/pep257_docstrings.md)
- [Sphinx docstrings](https://github.com/vemel/handsdown/blob/main/examples/sphinx_docstrings.py) with [generated output](https://github.com/vemel/handsdown/tree/main/docs/examples/sphinx_docstrings.md)
- [Type annotations](https://github.com/vemel/handsdown/blob/main/examples/typed.py) with [generated output](https://github.com/vemel/handsdown/tree/main/docs/examples/typed.md)
- [Comment-style type annotations](https://github.com/vemel/handsdown/blob/main/examples/comment_typed.py) with [generated output](https://github.com/vemel/handsdown/tree/main/docs/examples/comment_typed.md)


[Handsdown API Index](../README.md#handsdown-api-index) / Handsdown

> Auto-generated documentation for [handsdown](https://github.com/vemel/handsdown/blob/main/handsdown/__init__.py) module.

## Modules

- [Module](./module.md)
- [AST Parser](ast_parser/index.md)
- [Cli Parser](./cli_parser.md)
- [Constants](./constants.md)
- [Exceptions](./exceptions.md)
- [Generators](generators/index.md)
- [JinjaManager](./jinja_manager.md)
- [Loader](./loader.md)
- [Main](./main.md)
- [MDDocument](./md_document.md)
- [Processors](processors/index.md)
- [Utils](utils/index.md)
