"""
Glob helper for matching paths inside `root` path.

Supports `.gitignore`-like `include` and `exclude` patterns.
"""

import fnmatch
from pathlib import Path
from typing import Iterable, Iterator, List, TypeVar

from handsdown.exceptions import PathFinderError
from handsdown.utils.nice_path import NicePath

_R = TypeVar("_R", bound="PathFinder")

__all__ = ["PathFinder"]


class PathFinder:
    """
    Glob helper for matching paths inside `root` path.

    With `.gitignore`-like `include` and `exclude` patterns.

    Examples:
        ```python
        path_finder = PathFinder(Path.cwd())
        list(path_finder.glob('*.txt'))
        ['my_new.txt', 'my.txt', 'new.txt']

        list(path_finder.include('my*').glob('*.txt'))
        ['my_new.txt', 'my.txt']

        list(path_finder.exclude('*new*').glob('*.txt'))
        ['my.txt']
        ```

    Arguments:
        root -- Path to root folder.
        glob_expr -- `glob` expression to lookup in `root`

    Raises:
        PathFinderError -- If `root` is not absolute or not a directory.
    """

    def __init__(self, root: Path) -> None:
        if not root.is_absolute():
            raise PathFinderError(f"Root path {root} is not absolute")
        try:
            if root.exists() and not root.is_dir():
                raise PathFinderError(f"Root path {root} is not a directory")
        except OSError:
            pass

        self._root = root
        self.include_exprs: List[str] = []
        self.exclude_exprs: List[str] = []

    def _copy(self: _R, include_exprs: Iterable[str], exclude_exprs: Iterable[str]) -> _R:
        new_copy = self.__class__(self._root)
        new_copy.include_exprs = list(include_exprs)
        new_copy.exclude_exprs = list(exclude_exprs)
        return new_copy

    def include(self: _R, *fn_exrps: str) -> _R:
        """
        Add `fnmatch` expression to white list.

        If white list is empty - no white list filtration applied.
        If expression does not have `*` or `.` characters, appends `/*` to it.

        Arguments:
            fn_exrps -- One or more `fnmatch` expressions.

        Returns:
            A copy of itself.
        """
        include_exprs = []
        include_exprs.extend(self.include_exprs)
        for fn_exrp in fn_exrps:
            if "*" not in fn_exrp and "." not in fn_exrp:
                fn_exrp = f"{fn_exrp}/*"
            include_exprs.append(fn_exrp)
        return self._copy(include_exprs=include_exprs, exclude_exprs=self.exclude_exprs)

    def exclude(self: _R, *fn_exrps: str) -> _R:
        """
        Add `fnmatch` expression to black list.

        If black list is empty - no black list filtration applied.
        If expression does not have `*` or `.` characters, appends `/*` to it.

        Arguments:
            fn_exrps -- One or more `fnmatch` expressions.

        Returns:
            A copy of itself.
        """
        exclude_exprs = []
        exclude_exprs.extend(self.exclude_exprs)
        for fn_exrp in fn_exrps:
            if "*" not in fn_exrp and "." not in fn_exrp:
                fn_exrp = f"{fn_exrp}/*"
            exclude_exprs.append(fn_exrp)
        return self._copy(include_exprs=self.include_exprs, exclude_exprs=exclude_exprs)

    def _match_include(self, path: Path) -> bool:
        if not self.include_exprs:
            return True

        posix_path = path.as_posix()
        for include_expr in self.include_exprs:
            if fnmatch.fnmatch(posix_path, include_expr):
                return True

        return False

    def _match_exclude(self, path: Path) -> bool:
        if not self.exclude_exprs:
            return False

        posix_path = path.as_posix()
        for exclude_expr in self.exclude_exprs:
            if fnmatch.fnmatch(posix_path, exclude_expr):
                return True

        return False

    def glob(self, glob_expr: str) -> Iterator[NicePath]:
        """
        Find all matching `Path` objects respecting `include` and `exclude` patterns.

        Yields:
            Matching `Path` objects.
        """
        for path in self._root.glob(glob_expr):
            relative_path = path.relative_to(self._root)
            if not self._match_include(relative_path):
                continue
            if self._match_exclude(relative_path):
                continue

            yield NicePath(path)

    def relative(self, target: Path) -> NicePath:
        """
        Find a relative path from `root` to `target`.

        `target` should be an absolute path.

        Arguments:
            target -- Target path.

        Returns:
            A relative path to `target`.
        """
        if not target.is_absolute():
            raise PathFinderError(f"Target path should be absolute, got {target}")

        relative_target = Path()
        up_path = Path()
        parents = [self._root] + list(self._root.parents)
        for parent in parents:
            try:
                relative_target = target.relative_to(parent)
            except ValueError:
                up_path = up_path / ".."
                continue
            else:
                break

        return NicePath(up_path) / relative_target

    def mkdir(self, force: bool = False) -> None:
        """
        Create directories up to `root` if they do not exist.

        Arguments:
            force -- Delete existing parent if it is not a directory.

        Raises:
            PathFinderError -- If any existing parent is not a directory and not in `force` mode.
        """
        parents = [self._root] + list(self._root.parents)
        missing_parents = []
        for parent in parents:
            if not parent.exists():
                missing_parents.append(parent)
                continue

            if not parent.is_dir() and force:
                parent.unlink()
                missing_parents.append(parent)
                continue

            if not parent.is_dir():
                raise PathFinderError(f"{parent} is not a directory, delete it manually")

            break

        for parent in reversed(missing_parents):
            parent.mkdir()
