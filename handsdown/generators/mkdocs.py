"""
MkDocs documentation generator.
"""
from handsdown.generators.base import BaseGenerator
from handsdown.utils.nice_path import NicePath


class MkdocsGenerator(BaseGenerator):
    """
    MkDocs documentation generator.
    """

    templates_path = NicePath("mkdocs")
