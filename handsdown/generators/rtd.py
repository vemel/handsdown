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
    module_template_path = templates_path / "module.md.jinja2"

    insert_toc = True
