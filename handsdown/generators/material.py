"""
Read the Docs documentation generator.
"""
from pathlib import Path
from typing import Tuple

from handsdown.generators.base import BaseGenerator


class MaterialGenerator(BaseGenerator):
    """
    Read the Docs documentation generator.
    """

    templates_path = Path("material")
    module_template_path = templates_path / "module.md.jinja2"

    insert_toc = False

    def get_external_configs_templates(self) -> Tuple[Tuple[Path, Path], ...]:
        """
        Get a tuple with pairs of template path to project path
        """
        return (
            *super().get_external_configs_templates(),
            (
                self.templates_path / "requirements.mkdocs.txt.jinja2",
                self._output_path.parent / "requirements.mkdocs.txt",
            ),
        )
