import unittest

from mock import patch

from handsdown.loader import Loader
from handsdown.path_finder import Path
from handsdown.utils.os_environ_mock import OSEnvironMock


class TestLoader(unittest.TestCase):
    @patch("os.environ", OSEnvironMock())
    def test_init(self):
        loader = Loader(
            root_path=Path.cwd(), output_path=Path.cwd() / "docs", logger=None
        )
        self.assertIsInstance(loader, Loader)
