"""
Read the Docs documentation generator.
"""
from handsdown.generators.base import BaseGenerator
from handsdown.utils.nice_path import NicePath


class RTDGenerator(BaseGenerator):
    """
    Read the Docs documentation generator.
    """

    templates_path = NicePath("readthedocs")
