"""
Read the Docs documentation generator.
"""
from pathlib import Path

from handsdown.generators.base import BaseGenerator


class RTDGenerator(BaseGenerator):
    """
    Read the Docs documentation generator.
    """

    templates_path = Path("readthedocs")
    module_template_path = templates_path / "module.md.jinja2"

    insert_toc = True
