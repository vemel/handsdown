# pylint: disable=missing-docstring
import unittest
from pathlib import Path

from handsdown.loader import Loader


class TestLoader(unittest.TestCase):
    def test_init(self):
        loader = Loader(root_path=Path.cwd(), output_path=Path.cwd() / "docs")
        self.assertIsInstance(loader, Loader)
