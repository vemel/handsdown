import unittest
import logging
from unittest.mock import patch

from handsdown.main import main, get_logger


class TestMain(unittest.TestCase):
    def test_get_logger(self):
        logger = get_logger(logging.INFO)
        self.assertEqual(logger.level, logging.INFO)

    @patch("handsdown.main.get_cli_parser")
    @patch("handsdown.main.Generator")
    def test_main(self, generator_mock, get_cli_parser_mock):
        main()
        generator_mock.assert_called_once()
        get_cli_parser_mock.assert_called_once()
