import unittest

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

from handsdown.loader import Loader
from handsdown.path_finder import Path
from handsdown.utils import OSEnvironMock


class TestLoader(unittest.TestCase):
    @patch("os.environ", OSEnvironMock())
    def test_init(self):
        loader = Loader(
            root_path=Path.cwd(), output_path=Path.cwd() / "docs", logger=None
        )
        self.assertIsInstance(loader, Loader)
