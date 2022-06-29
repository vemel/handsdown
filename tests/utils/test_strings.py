import unittest

from handsdown.utils.strings import extract_md_title, make_title


class TestUtils(unittest.TestCase):
    def test_make_title(self):
        self.assertEqual(make_title("my_path.py"), "My Path Py")
        self.assertEqual(make_title("my_title"), "My Title")
        self.assertEqual(make_title("__init__.py"), "Init Py")
        self.assertEqual(make_title("__main__"), "Module")

    def test_extract_md_title(self):
        self.assertEqual(extract_md_title("# test\ncontent"), ("test", "content"))
        self.assertEqual(extract_md_title("# test\n\ncontent"), ("test", "\ncontent"))
        self.assertEqual(extract_md_title("## test\n\ncontent"), ("", "## test\n\ncontent"))
        self.assertEqual(extract_md_title("# test"), ("test", ""))
