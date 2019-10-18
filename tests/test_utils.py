import unittest

from handsdown.utils import OSEnvironMock, get_title_from_path_part


class TestUtils(unittest.TestCase):
    def test_os_environ_mock(self):
        mock = OSEnvironMock({"key": "value"})
        self.assertEqual(mock["key"], "value")
        self.assertEqual(mock["missing"], "env")

        mock["test"] = "mytest"
        self.assertEqual(mock["test"], "mytest")

    def test_get_title_from_path_part(self):
        self.assertEqual(get_title_from_path_part("my_path.py"), "My Path Py")
        self.assertEqual(get_title_from_path_part("my_title"), "My Title")
        self.assertEqual(get_title_from_path_part("__init__.py"), "Init Py")
