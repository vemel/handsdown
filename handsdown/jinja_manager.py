"""
Jinja2 `Environment` manager.
"""
from pathlib import Path
from typing import Any

import jinja2

from handsdown.exceptions import LoaderError
from handsdown.utils.blackify import blackify


class JinjaManager:
    """
    Jinja2 `Environment` manager.
    """

    TEMPLATES_PATH = Path(__file__).parent / "templates"

    _env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(TEMPLATES_PATH.as_posix()),
        undefined=jinja2.StrictUndefined,
    )

    def __init__(self) -> None:
        self._env.filters.update({"escape_md": self.escape_md, "blackify": blackify})

    @classmethod
    def update_globals(cls, **kwargs: object) -> None:
        """
        Update global variables in `jinja2.Environment`.

        Arguments:
            kwargs -- Globals to set.
        """
        cls._env.globals.update(kwargs)

    @staticmethod
    def escape_md(value: str) -> str:
        """
        Escape underscore characters.
        """
        return value.replace("_", r"\_")

    @property
    def env(self) -> jinja2.Environment:
        """
        Get `jinja2.Environment`.
        """
        return self._env

    def render(self, template_path: Path, **kwargs: Any) -> str:
        template_full_path = self.TEMPLATES_PATH / template_path

        if not template_full_path.exists():
            raise LoaderError(f"Template {template_full_path} not found")

        template = self.env.get_template(template_path.as_posix())
        return template.render(**kwargs)
