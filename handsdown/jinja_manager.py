"""
Jinja2 `Environment` manager.
"""
from pathlib import Path
from typing import Any

import jinja2


class JinjaManager:
    """
    Jinja2 `Environment` manager.
    """

    TEMPLATES_PATH = Path(__file__).parent / "templates"

    _environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader(TEMPLATES_PATH.as_posix()),
        undefined=jinja2.StrictUndefined,
    )

    @classmethod
    def update_globals(cls, **kwargs: object) -> None:
        """
        Update global variables in `jinja2.Environment`.

        Arguments:
            kwargs -- Globals to set.
        """
        cls._environment.globals.update(kwargs)

    @staticmethod
    def escape_md(value: str) -> str:
        """
        Escape underscore characters.
        """
        return value.replace("_", r"\_")

    @classmethod
    def get_environment(cls) -> jinja2.Environment:
        """
        Get `jinja2.Environment`.
        """
        cls._environment.filters["escape_md"] = cls.escape_md
        return cls._environment

    def render(self, template_path: Path, **kwargs: Any) -> str:
        template_full_path = self.TEMPLATES_PATH / template_path

        if not template_full_path.exists():
            raise ValueError(f"Template {template_full_path} not found")

        template = self.get_environment().get_template(template_path.as_posix())
        return template.render(**kwargs)
