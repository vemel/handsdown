import unittest

from handsdown.processors.base import BaseDocstringProcessor


class TestLoader(unittest.TestCase):
    def test_init(self):
        processor = BaseDocstringProcessor()
        sections = processor.build_sections("asd\n\n  test\n test2")
        self.assertEqual(sections[""].title, "")
        self.assertEqual(sections[""].blocks[0].lines, ["asd"])
        self.assertEqual(sections[""].blocks[1].lines, ["  test", " test2"])
