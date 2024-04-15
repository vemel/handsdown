from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from handsdown.utils.path_finder import PathFinder, PathFinderError


class TestPathFinder:
    @patch("handsdown.utils.path_finder.Path")
    def test_init(self, PathMock):
        path = PathMock()
        assert isinstance(PathFinder(path), PathFinder)

        path.is_absolute.return_value = False
        with pytest.raises(PathFinderError):
            assert isinstance(PathFinder(path), PathFinder)

        path.is_absolute.return_value = True
        path.exists.return_value = True
        path.is_dir.return_value = False
        with pytest.raises(PathFinderError):
            assert isinstance(PathFinder(path), PathFinder)

        path.is_dir.return_value = True
        assert isinstance(PathFinder(path), PathFinder)

    def test_relative(self):
        path_finder = PathFinder(Path("/root/parent/"))
        assert path_finder.relative(Path("/root/target.py")) == Path("../target.py")
        assert path_finder.relative(Path("/root/parent/target.py")) == Path("target.py")
        assert path_finder.relative(Path("/root2/other/target.py")) == Path(
            "../../root2/other/target.py"
        )
        assert path_finder.relative(Path("/root/parent/source.py")) == Path("source.py")
        with pytest.raises(PathFinderError):
            path_finder.relative(Path("second/source.py"))

    @patch("handsdown.utils.path_finder.Path")
    def test_include(self, PathMock):
        path = PathMock()
        path_finder = PathFinder(path)
        assert path_finder.include_exprs == []
        path_finder = path_finder.include("my_dir", "expr/**/*")
        assert path_finder.include_exprs == ["my_dir/*", "expr/**/*"]

    @patch("handsdown.utils.path_finder.Path")
    def test_exclude(self, PathMock):
        path = PathMock()
        path_finder = PathFinder(path)
        assert path_finder.exclude_exprs == []
        path_finder = path_finder.exclude("my_dir", "expr/**/*")
        assert path_finder.exclude_exprs == ["my_dir/*", "expr/**/*"]

    def test_glob(self):
        import tempfile

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_dir = Path(temp_dir)
            temp_dir.joinpath("include").mkdir()
            temp_dir.joinpath("exclude").mkdir()
            temp_dir.joinpath("include/file.py").touch()
            temp_dir.joinpath("exclude/file.py").touch()

            path_finder = PathFinder(temp_dir)
            assert list(sorted(path_finder.glob("*/*.py"))) == [
                temp_dir.joinpath("exclude/file.py"),
                temp_dir.joinpath("include/file.py"),
            ]
            path_finder.exclude_exprs = ["exclude/*"]
            assert list(path_finder.glob("*/*.py")) == [temp_dir.joinpath("include/file.py")]

            path_finder.include_exprs = ["include/*"]
            assert list(path_finder.glob("*/*.py")) == [temp_dir.joinpath("include/file.py")]

    def test_mkdir(self):
        path = MagicMock()
        path.exists.return_value = False
        parent_path = MagicMock()
        parent_path.exists.return_value = True
        parent_path.is_dir.return_value = False
        top_parent_path = MagicMock()
        top_parent_path.exists.return_value = True
        top_parent_path.is_dir.return_value = True
        path.parents = [parent_path, top_parent_path]
        path_finder = PathFinder(path)

        path_finder.mkdir(force=True)
        parent_path.unlink.assert_called_with()
        parent_path.mkdir.assert_called_with()
        path.mkdir.assert_called_with()

        with pytest.raises(PathFinderError):
            path_finder.mkdir(force=False)
