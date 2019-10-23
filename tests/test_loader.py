import unittest

from handsdown.loader import Loader
from handsdown.path_finder import Path


class TestLoader(unittest.TestCase):
    def test_init(self):
        loader = Loader(root_path=Path.cwd(), output_path=Path.cwd() / "docs")
        self.assertIsInstance(loader, Loader)
