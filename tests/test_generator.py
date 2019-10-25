import unittest
from pathlib import Path

from handsdown.generator import Generator


class TestGenerator(unittest.TestCase):
    def test_init(self):
        generator = Generator(
            project_name="test",
            input_path=Path.cwd(),
            output_path=Path.cwd() / "docs",
            source_paths=[],
        )
        self.assertIsInstance(generator, Generator)
