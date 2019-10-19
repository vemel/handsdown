import unittest

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

from handsdown.generator import Generator
from handsdown.path_finder import Path
from handsdown.utils import OSEnvironMock


class TestGenerator(unittest.TestCase):
    @patch("os.environ", OSEnvironMock())
    def test_init(self):
        generator = Generator(
            input_path=Path.cwd(), output_path=Path.cwd() / "docs", source_paths=[]
        )
        self.assertIsInstance(generator, Generator)
