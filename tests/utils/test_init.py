# pylint: disable=missing-docstring
import unittest

from handsdown.utils import make_title, extract_md_title


class TestUtils(unittest.TestCase):
    def test_make_title(self):
        self.assertEqual(make_title("my_path.py"), "My Path Py")
        self.assertEqual(make_title("my_title"), "My Title")
        self.assertEqual(make_title("__init__.py"), "Init Py")

    def test_extract_md_title(self):
        self.assertEqual(extract_md_title("# test\ncontent"), ("test", "content"))
        self.assertEqual(extract_md_title("# test\n\ncontent"), ("test", "\ncontent"))
        self.assertEqual(
            extract_md_title("## test\n\ncontent"), ("", "## test\n\ncontent")
        )
        self.assertEqual(extract_md_title("# test"), ("test", ""))
