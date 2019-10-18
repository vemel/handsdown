#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from pathlib2 import Path
except ImportError:
    from pathlib import Path

from setuptools import setup
from setuptools import find_packages
import __version__ as version_data

root_path = Path(__file__).absolute().parent

description = "Python docstring-based documentation generator for lazy perfectionists."


def get_long_description():
    "Remove ToC from README.md as PyPI does not support links."
    lines = []
    readme_path = root_path / "README.md"
    for readme_line in readme_path.read_text().splitlines():
        if "](#" not in readme_line:
            lines.append(readme_line)
    return "\n".join(lines)


long_description = get_long_description()
version = version_data.__version__
install_requires = [
    i for i in Path(root_path / "requirements.txt").read_text().split("\n") if i
]


setup(
    name=root_path.name,
    version=version,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://vemel.github.io/handsdown/",
    author="Vlad Emelianov",
    author_email="vlad.emelianov.nz@gmail.com",
    packages=find_packages(
        exclude=[
            "tests",
            "*.tests",
            "*.tests.*",
            "tests.*",
            "__pycache__",
            "examples",
            "examples.*",
        ]
    ),
    install_requires=install_requires,
    extras_require={},
    include_package_data=False,
    zip_safe=True,
    dependency_links=[],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Framework :: Django",
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Documentation",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    entry_points={"console_scripts": ["handsdown = handsdown.main:main"]},
    project_urls={
        "Source": "https://github.com/vemel/handsdown/",
        "Documentation": "https://vemel.github.io/handsdown/",
    },
)
