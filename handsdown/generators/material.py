"""
Read the Docs documentation generator.
"""
from handsdown.generators.base import BaseGenerator
from handsdown.utils.nice_path import NicePath


class MaterialGenerator(BaseGenerator):
    """
    Read the Docs documentation generator.
    """

    templates_path = NicePath("material")
    module_template_path = templates_path / "module.md.jinja2"
