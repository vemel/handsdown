import unittest

from handsdown.generator import Generator
from handsdown.path_finder import Path


class TestGenerator(unittest.TestCase):
    def test_init(self):
        generator = Generator(
            input_path=Path.cwd(), output_path=Path.cwd() / "docs", source_paths=[]
        )
        self.assertIsInstance(generator, Generator)
