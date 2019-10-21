import unittest

from mock import MagicMock, patch

from handsdown.utils.type_checking_mock import TypeCheckingMock


class TestTypeCheckingMock(unittest.TestCase):
    @patch("handsdown.utils.type_checking_mock.traceback.extract_stack")
    def test_init(self, extract_stack_mock):
        path = MagicMock()
        path.as_posix.return_value = "my/path"
        type_checking_mock = TypeCheckingMock(path)
        self.assertEqual(type_checking_mock.target_file_path_str, "my/path")

        call_mock = MagicMock()
        call_mock.filename = "my/path"
        extract_stack_mock.return_value = [call_mock]
        self.assertTrue(type_checking_mock)

        call_mock.filename = "other/path"
        self.assertFalse(type_checking_mock)

        call_mock.filename = "my/path"
        self.assertTrue(type_checking_mock)
