# Handsdown 🙌

- [Handsdown 🙌](#handsdown-)
  - [Features](#features)
  - [Usage](#usage)
    - [From command line](#from-command-line)
    - [As a module](#as-a-module)
  - [Installation](#installation)
  - [Modules](#modules)

Python docstring-based documentation generator for lazy people.

## Features

- 👓 PEP257, Google and RST docstrings support. All of them are converted to a valid markdown.
- 🐈 Github-friendly. Use your local markdown viewer or open docs [right on Github](docs/index.md)
- 📚 Signatures for every class, function and method.
- 🚀 Support for type annotations. Even for the ones from the `__future__`!
- 📦 Nice list of all modules in [Modules](docs/index.md#modules)
- 🔎 Gather all scattered `README.md` in submodules to one place
- 🚧 Links to source code from every doc section.
- #️⃣ Create cross-references easily [Handsdown.replace_links](./handsdown_handsdown.md#handsdownreplace_links) (check [index.md](docs/index.md#features))
- 💕 Do you love type annotations? Well, you get auto-discovery of related modules for free!

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

## Modules

- Handsdown
  - [Handsdown](./handsdown_handsdown.md)
  - [Indent trimmer](./handsdown_indent_trimmer.md)
  - [Loader](./handsdown_loader.md)
  - Processors
    - [Base](./handsdown_processors_base.md)
    - [Pep257](./handsdown_processors_pep257.md)
    - [Rst](./handsdown_processors_rst.md)
    - [Smart](./handsdown_processors_smart.md)
  - [Signature](./handsdown_signature.md)
  - [Utils](./handsdown_utils.md)