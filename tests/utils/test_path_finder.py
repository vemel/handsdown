# pylint: disable=missing-docstring
import unittest
from unittest.mock import patch
from pathlib import Path

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
        self.assertEqual(
            path_finder.relative(Path("/root/target.py")), Path("../target.py")
        )
        self.assertEqual(
            path_finder.relative(Path("/root/parent/target.py")), Path("target.py")
        )
        self.assertEqual(
            path_finder.relative(Path("/root2/other/target.py")),
            Path("../../root2/other/target.py"),
        )
        self.assertEqual(
            path_finder.relative(Path("/root/parent/source.py")), Path("source.py")
        )
        with self.assertRaises(PathFinderError):
            path_finder.relative(Path("second/source.py"))
