import unittest
import logging

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

from handsdown.main import main, get_logger


class TestMain(unittest.TestCase):
    def test_get_logger(self):
        logger = get_logger(logging.INFO)
        self.assertEqual(logger.level, logging.INFO)

    @patch("handsdown.main.get_cli_parser")
    @patch("handsdown.main.Generator")
    def test_main(self, _generator_mock, _get_cli_parser_mock):
        self.assertIsNone(main())
        # does not work on py27
        # generator_mock.assert_called_once()
        # get_cli_parser_mock.assert_called_once()
