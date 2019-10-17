import unittest
from pathlib import Path

from handsdown.path_finder import PathFinder


class TestPathFinder(unittest.TestCase):
    def test_get_relative_path(self):
        self.assertEqual(
            PathFinder.get_relative_path(
                Path("/root/parent/source.py"), Path("/root/target.py")
            ),
            Path("../target.py"),
        )
        self.assertEqual(
            PathFinder.get_relative_path(
                Path("/root/source.py"), Path("/root/parent/target.py")
            ),
            Path("parent/target.py"),
        )
        self.assertEqual(
            PathFinder.get_relative_path(
                Path("/root/parent/source.py"), Path("/root/other/target.py")
            ),
            Path("../other/target.py"),
        )
        self.assertEqual(
            PathFinder.get_relative_path(
                Path("/root/parent/source.py"), Path("/root/parent/source.py")
            ),
            Path("source.py"),
        )
        self.assertEqual(
            PathFinder.get_relative_path(
                Path("parent/source.py"), Path("second/source.py")
            ),
            Path("../second/source.py"),
        )
        self.assertEqual(
            PathFinder.get_relative_path(Path("parent/_"), Path("second/source.py")),
            Path("../second/source.py"),
        )
