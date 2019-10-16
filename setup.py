#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pathlib import Path
from setuptools import setup
from setuptools import find_packages
import __version__ as version_data

ROOT_PATH = Path(__file__).absolute().parent
README_PATH = ROOT_PATH / "README.md"
DESCRIPTION = README_PATH.read_text().split("\n")[0]
URL = f"https://github.com/vemel/{ROOT_PATH.name}"

version = version_data.__version__

#######################################
# USER INPUTS:
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
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=False,
    zip_safe=True,
    dependency_links=DEPENDENCY_LINKS,
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
        "Source": "https://github.com/vemel/handsdown",
        "Documentation": f"https://github.com/vemel/handsdown/tree/{version}/docs/handsdown_index.md#handsdown",
    },
)
