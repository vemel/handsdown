import unittest
from unittest.mock import patch

from handsdown.main import main


class TestMain(unittest.TestCase):
    @patch("handsdown.main.get_logger")
    @patch("handsdown.main.Generator")
    def test_main(self, generator_mock, _get_logger_mock):

        with patch("handsdown.main.sys.argv", []):
            self.assertIsNone(main())
        generator_mock.assert_called_once()
