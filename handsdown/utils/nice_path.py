"""
Path that represents it as relative to workdir.
"""
import shutil
from pathlib import Path
from typing import Iterable, Iterator, TypeVar

_R = TypeVar("_R", bound=Path)


class NicePath(type(Path())):  # type: ignore
    """
    Path that represents it as relative to workdir.
    """

    def __str__(self) -> str:
        path = Path(self)
        if self.is_absolute():
            cwd = self.cwd()
            if path == cwd or path.parts <= cwd.parts:
                return str(path)

            try:
                path = Path(self).relative_to(cwd)
            except ValueError:
                return str(path)

        if len(path.parts) == 1:
            return f"./{path}"

        return str(path)

    def walk(
        self: _R, exclude: Iterable[Path] = tuple(), glob_pattern: str = "**/*"
    ) -> Iterator[_R]:
        """
        Walk files except for `exclude`.

        Yields:
            Existing Path.
        """
        exclude_strs = {self.__class__(i).as_posix() for i in exclude}
        for path in self.glob(glob_pattern):
            if not path.is_file():
                continue

            if path.as_posix() in exclude_strs:
                continue

            yield self.__class__(path)

    def write_changed(self, content: str, encoding: str) -> bool:
        """
        Write content to file if it's changed.
        """
        if self.exists() and self.read_text(encoding) == content:
            return False

        self.parent.mkdir(exist_ok=True, parents=True)
        self.write_text(content, encoding)
        return True

    def rmtree(self, ignore_errors: bool = True) -> None:
        """
        Remove directory and all its contents.
        """
        if not self.exists():
            return
        shutil.rmtree(self.as_posix(), ignore_errors=ignore_errors)
