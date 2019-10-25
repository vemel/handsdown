# pylint: disable=missing-docstring
import unittest

from handsdown.docstring_formatter import DocstringFormatter


class TestDocstringFormatter(unittest.TestCase):
    def test_flask(self):
        docstring = """
            flask.app
            ~~~~~~~~~

            Docstring.
        """
        self.assertEqual(
            DocstringFormatter(docstring).render(), "# flask.app\n\nDocstring."
        )

    def test_wrong_indent(self):
        docstring = """Wrong indent

            Correct indent.
        """
        self.assertEqual(
            DocstringFormatter(docstring).render(), "Wrong indent\n\nCorrect indent."
        )
