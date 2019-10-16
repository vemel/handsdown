from __future__ import annotations

from pathlib import Path
import fnmatch

from typing import Text, Generator, List, Iterable


class PathFinder:
    """
    Find matching paths inside `root` path.

    Examples::

        path_finder = PathFinder(root=Path.cwd(), glob_expr='*.txt')
        path_finder.list()
        ['my_new.txt', 'my.txt', 'new.txt']

        path_finder.include('my*').list()
        ['my_new.txt', 'my.txt']

        path_finder.exclude('*new*').list()
        ['my.txt']

    Arguments:
        root -- Path to root folder.
        glob_expr -- `glob` expression to lookup in `root`
    """

    def __init__(self, root: Path, glob_expr: Text) -> None:
        self._root = root
        self._glob_expr = glob_expr
        self.include_exprs: List[Text] = []
        self.exclude_exprs: List[Text] = []

    def _copy(
        self, include_exprs: Iterable[Text], exclude_exprs: Iterable[Text]
    ) -> PathFinder:
        new_copy = PathFinder(root=self._root, glob_expr=self._glob_expr)
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

    def __iter__(self) -> Generator[Path, None, None]:
        """
        Iterate over matched paths respecting `include` and `exclude` patterns.

        Returns:
            A generator of matched paths.
        """
        for path in self._root.glob(self._glob_expr):
            relative_path = path.relative_to(self._root)
            if not self._match_include(relative_path):
                continue
            if self._match_exclude(relative_path):
                continue

            yield path

    def list(self) -> List[Path]:
        """
        Return all matching paths as a list.

        Returns:
            A list of all matched paths.
        """
        return list(self)
