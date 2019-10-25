# pylint: disable=missing-docstring
import unittest
from pathlib import Path

from handsdown.processors.pep257 import PEP257DocstringProcessor


class TestLoader(unittest.TestCase):
    def test_init(self):
        pep257_docstring = (
            Path(__file__).parent.parent / "static" / "pep257_docstring.txt"
        ).read_text()
        processor = PEP257DocstringProcessor()
        sections = processor.build_sections(pep257_docstring)
        self.assertEqual(sections[""].title, "")
        self.assertEqual(
            sections[""].render(),
            "Summary line.\n\nExtended description of method.\n\n",
        )
