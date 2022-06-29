from handsdown.utils.docstring_formatter import DocstringFormatter


class TestDocstringFormatter:
    def test_flask(self):
        docstring = """
            flask.app
            ~~~~~~~~~

            Docstring.
        """
        assert DocstringFormatter(docstring).render() == "# flask.app\n\nDocstring."

    def test_wrong_indent(self):
        docstring = """Wrong indent

            Correct indent.
        """
        assert DocstringFormatter(docstring).render() == "Wrong indent\n\nCorrect indent."
