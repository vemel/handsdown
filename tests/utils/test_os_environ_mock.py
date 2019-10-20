import unittest

from handsdown.utils.os_environ_mock import OSEnvironMock


class TestOSEnvironMock(unittest.TestCase):
    def test_main(self):
        mock = OSEnvironMock({"key": "value"})
        self.assertEqual(mock["key"], "value")
        self.assertEqual(mock["missing"], "env")

        mock["test"] = "mytest"
        self.assertEqual(mock["test"], "mytest")
