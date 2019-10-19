#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path

from setuptools import setup
from setuptools import find_packages
import __version__ as version_data

root_path = path.dirname(path.abspath(__file__))

description = "Python docstring-based documentation generator for lazy perfectionists."


def get_long_description():
    "Remove ToC from README.md as PyPI does not support links."
    lines = []
    readme_path = path.join(root_path, "README.md")
    with open(readme_path) as readme_file:
        for readme_line in readme_file.readlines():
            if "](#" not in readme_line:
                lines.append(readme_line.rstrip("\n"))
    return "\n".join(lines)


def get_install_requires():
    install_requires = []
    requirements_path = path.join(root_path, "requirements.txt")
    with open(requirements_path) as f:
        for line in f.readlines():
            line = line.rstrip(" \n")
            if line:
                install_requires.append(line)

    return install_requires


long_description = get_long_description()
version = version_data.__version__


setup(
    name="handsdown",
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
    install_requires=get_install_requires(),
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
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
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
