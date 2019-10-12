#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pathlib import Path
from setuptools import setup
from setuptools import find_packages
import __version__ as v

ROOT_PATH = Path(__file__).absolute().parent
README_PATH = ROOT_PATH / "README.md"
DESCRIPTION = README_PATH.read_text().split("\n")[0]
URL = f"https://github.com/vemel/{ROOT_PATH.name}"

version = v.__version__

#######################################
# USER INPUTS:
REQUIRES_PYTHON = ">=3.7"
AUTHOR = "Vlad Emelianov"
AUTHOR_EMAIL = "vlad.emelianov.nz@gmail.com"

# Required Packages
REQUIRED = []

# EXTERNAL DEPENDENCY LINKS
DEPENDENCY_LINKS = []

# Optional Packages
EXTRAS = {}


setup(
    name=ROOT_PATH.name,
    version=version,
    description=DESCRIPTION,
    long_description=README_PATH.read_text(),
    long_description_content_type="text/markdown",
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(
        exclude=["tests", "*.tests", "*.tests.*", "tests.*", "__pycache__"]
    ),
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    zip_safe=False,
    dependency_links=DEPENDENCY_LINKS,
    classifiers=["Programming Language :: Python :: 3.7"],
    entry_points={"console_scripts": [f"handsdown = {ROOT_PATH.name}.main:main"]},
)
