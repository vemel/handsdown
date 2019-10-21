import unittest

from mock import patch

from handsdown.utils.logger import get_logger


class TestLogging(unittest.TestCase):
    @patch("handsdown.utils.logger.logging")
    def test_get_logger(self, logging_mock):
        logging_mock.getLogger().handlers = []

        self.assertTrue(get_logger(level=10))
        logging_mock.getLogger.assert_called_with("handsdown")
        logging_mock.getLogger().setLevel.assert_called_with(10)
        logging_mock.StreamHandler().setLevel.assert_called_with(10)
