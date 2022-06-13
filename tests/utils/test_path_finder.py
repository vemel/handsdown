import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from handsdown.utils.path_finder import PathFinder, PathFinderError


class TestPathFinder(unittest.TestCase):
    @patch("handsdown.utils.path_finder.Path")
    def test_init(self, PathMock):
        path = PathMock()
        self.assertIsInstance(PathFinder(path), PathFinder)

        path.is_absolute.return_value = False
        with self.assertRaises(PathFinderError):
            self.assertIsInstance(PathFinder(path), PathFinder)

        path.is_absolute.return_value = True
        path.exists.return_value = True
        path.is_dir.return_value = False
        with self.assertRaises(PathFinderError):
            self.assertIsInstance(PathFinder(path), PathFinder)

        path.is_dir.return_value = True
        self.assertIsInstance(PathFinder(path), PathFinder)

    def test_relative(self):
        path_finder = PathFinder(Path("/root/parent/"))
        self.assertEqual(path_finder.relative(Path("/root/target.py")), Path("../target.py"))
        self.assertEqual(path_finder.relative(Path("/root/parent/target.py")), Path("target.py"))
        self.assertEqual(
            path_finder.relative(Path("/root2/other/target.py")),
            Path("../../root2/other/target.py"),
        )
        self.assertEqual(path_finder.relative(Path("/root/parent/source.py")), Path("source.py"))
        with self.assertRaises(PathFinderError):
            path_finder.relative(Path("second/source.py"))

    @patch("handsdown.utils.path_finder.Path")
    def test_include(self, PathMock):
        path = PathMock()
        path_finder = PathFinder(path)
        self.assertEqual(path_finder.include_exprs, [])
        path_finder = path_finder.include("my_dir", "expr/**/*")
        self.assertEqual(path_finder.include_exprs, ["my_dir/*", "expr/**/*"])

    @patch("handsdown.utils.path_finder.Path")
    def test_exclude(self, PathMock):
        path = PathMock()
        path_finder = PathFinder(path)
        self.assertEqual(path_finder.exclude_exprs, [])
        path_finder = path_finder.exclude("my_dir", "expr/**/*")
        self.assertEqual(path_finder.exclude_exprs, ["my_dir/*", "expr/**/*"])

    @patch("handsdown.utils.path_finder.Path")
    def test_glob(self, PathMock):
        path = PathMock()
        include_file_mock = MagicMock()
        include_file_mock.relative_to().as_posix.return_value = "include/file.py"
        exclude_file_mock = MagicMock()
        exclude_file_mock.relative_to().as_posix.return_value = "exclude/file.py"
        path.glob.return_value = [include_file_mock, exclude_file_mock]
        path_finder = PathFinder(path)
        self.assertEqual(
            list(path_finder.glob("glob_expr")), [include_file_mock, exclude_file_mock]
        )
        path_finder.exclude_exprs = ["exclude/*"]
        self.assertEqual(list(path_finder.glob("glob_expr")), [include_file_mock])

        path_finder.include_exprs = ["include/*"]
        self.assertEqual(list(path_finder.glob("glob_expr")), [include_file_mock])

    @patch("handsdown.utils.path_finder.Path")
    def test_mkdir(self, _PathMock):
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

        with self.assertRaises(PathFinderError):
            path_finder.mkdir(force=False)
