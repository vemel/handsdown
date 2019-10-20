import unittest

from handsdown.utils import make_title


class TestUtils(unittest.TestCase):
    def test_make_title(self):
        self.assertEqual(make_title("my_path.py"), "My Path Py")
        self.assertEqual(make_title("my_title"), "My Title")
        self.assertEqual(make_title("__init__.py"), "Init Py")
