# Handsdown

Python docstring-based documentation generator for lazy people. It generates Github-friendly Markdown
documents for PEP257, Google and RST docstrings.

## Features

- PEP257, Google aand RST docstrings support. All of them are converted to a valid markdown.
- Github-friendly. Use your local markdown viewer or open docs [right on Github](docs/index.md)
- Signatures for every class, function and method.
- Support for type annotations. Even for the ones from the `__future__`!
- Nice list of all modules in [Modules](docs/index.md#modules)
- Gather all scattered `README.md` in submodules to one place
- Links to source code from every doc section.

## Usage

### From command line

Just got to your favorite project that has docstring but missing auto-generated docs and let `handsdown` do the thing.

```bash
handsdown -o docs
```

Navigate to `docs/index.md` to see the result.

### As a module

```python
from handsdown.handsdown import Handsdown
handsdown = Handsdown(
    input_path=Path('path/to/my/repo'),
    output_path=Path('path/to/output'),
)

# generate all docs at once
handsdown.generate()

# or generate one doc
output_file_path = handsdown.generate_doc(Path('path/to/my/repo/source.py'))
output_file_path # Path('path/to/output/source.md')
```

## Installation

Install using pip

```bash
pip install handsdown
```