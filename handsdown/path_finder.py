from __future__ import annotations

from pathlib import Path
import fnmatch

from typing import Text, List, Iterable, Generator


__all__ = ["PathFinder"]


class PathFinder:
    """
    Find matching paths inside `root` path.

    Examples::

        path_finder = PathFinder(Path.cwd())
        path_finder.list()
        ['my_new.txt', 'my.txt', 'new.txt']

        path_finder.include('my*').list('*.txt')
        ['my_new.txt', 'my.txt']

        path_finder.exclude('*new*').list('*.txt')
        ['my.txt']

    Arguments:
        root -- Path to root folder.
        glob_expr -- `glob` expression to lookup in `root`
    """

    def __init__(self, root: Path) -> None:
        self._root = root.absolute()
        self.include_exprs: List[Text] = []
        self.exclude_exprs: List[Text] = []

    def _copy(
        self, include_exprs: Iterable[Text], exclude_exprs: Iterable[Text]
    ) -> PathFinder:
        new_copy = PathFinder(self._root)
        new_copy.include_exprs = list(include_exprs)
        new_copy.exclude_exprs = list(exclude_exprs)
        return new_copy

    def include(self, *fn_exrps: Text) -> PathFinder:
        """
        Add `fnmatch` expression to white list.
        If white list is empty - no white list filtration applied.
        If expression does not have `*` or `.` characters, appends `/*` to it.

        Arguments:
            fn_exrps - One or more `fnmatch` expressions.

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

    def exclude(self, *fn_exrps: Text) -> PathFinder:
        """
        Add `fnmatch` expression to black list.
        If black list is empty - no black list filtration applied.
        If expression does not have `*` or `.` characters, appends `/*` to it.

        Arguments:
            fn_exrps - One or more `fnmatch` expressions.

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

    def glob(self, glob_expr: Text) -> Generator[Path, None, None]:
        """
        Find all matching `Path` objects respecting `include` and
        `exclude` patterns.

        Yields:
            Matching `Path` objects.
        """
        for path in self._root.glob(glob_expr):
            relative_path = path.relative_to(self._root)
            if not self._match_include(relative_path):
                continue
            if self._match_exclude(relative_path):
                continue

            yield path

    def relative(self, target: Path) -> Path:
        """
        Find a relative path from `root` to `target`.
        `target` should be an absolute path.

        Arguments:
            target -- Target path.

        Returns:
            A relative path to `target`.

        Raises:
            ValueError -- if `target` is not absolute.
        """
        if not target.is_absolute():
            raise ValueError("Target path should be absolute")

        relative_target = Path()
        up_path = Path()
        for parent in self._root.parents:
            try:
                relative_target = target.relative_to(parent)
            except ValueError:
                up_path = up_path / ".."
                continue
            else:
                break

        return up_path / relative_target

    def mkdir(self, force=False):
        """
        Create directories up to `root` if they do not exist.

        Arguments:
            force -- Delete existing parent if it is not a directory.

        Raises:
            ValueError -- If any existing parent is not a directory and not in `safe` mode.
        """
        parents = self._root.parents
        missing_parents = []
        for parent in parents:
            if not parent.exists():
                missing_parents.append(parent)
                continue

            if not parent.is_dir() and force:
                parent.unlink()
                continue

            if not parent.is_dir():
                raise ValueError(f"{parent} is not a directory")

            break

        for parent in reversed(missing_parents):
            parent.mkdir()
