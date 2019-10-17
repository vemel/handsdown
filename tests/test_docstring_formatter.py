import unittest

from handsdown.docstring_formatter import DocstringFormatter


class TestIndentTrimmer(unittest.TestCase):
    def test_flask(self):
        docstring = """
            flask.app
            ~~~~~~~~~

            Docstring.
        """
        print(DocstringFormatter(docstring).render())
        self.assertEqual(
            DocstringFormatter(docstring).render(), "\n# flask.app\n\nDocstring.\n"
        )

    def test_wrong_indent(self):
        docstring = """Wrong indent

            Correct indent.
        """
        print(DocstringFormatter(docstring).render())
        self.assertEqual(
            DocstringFormatter(docstring).render(),
            "\nWrong indent\n\nCorrect indent.\n",
        )
