#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pathlib import Path
from setuptools import setup
from setuptools import find_packages
import __version__ as version_data

root_path = Path(__file__).absolute().parent
readme_path = root_path / "README.md"
description = "Python docstring-based documentation generator for lazy perfectionists."

version = version_data.__version__


setup(
    name=root_path.name,
    version=version,
    description=description,
    long_description=readme_path.read_text(),
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
    install_requires=[],
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
