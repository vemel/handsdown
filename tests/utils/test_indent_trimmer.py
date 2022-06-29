from handsdown.utils.indent_trimmer import IndentTrimmer


class TestIndentTrimmer:
    def test_trim_empty_lines(self):
        assert IndentTrimmer.trim_empty_lines("\n  \n test\ntest2\n \n ") == " test\ntest2"
        assert IndentTrimmer.trim_empty_lines("\n  \n\n ") == ""
        assert IndentTrimmer.trim_empty_lines("\n  \n  test \n ") == "  test "

    def test_trim_text(self):
        assert IndentTrimmer.trim_text("  asd\n asd\n   asd\n") == " asd\nasd\n  asd\n"
        assert IndentTrimmer.trim_text("  asd\nasd\n   asd\n") == "  asd\nasd\n   asd\n"
        assert IndentTrimmer.trim_text(" asd\n asd\n  asd\n") == "asd\nasd\n asd\n"

    def test_trim_lines(self):
        assert IndentTrimmer.trim_lines(["  asd", " asd", "   asd"]) == [" asd", "asd", "  asd"]
        assert IndentTrimmer.trim_lines(["  asd", " asd", "", "   asd"]) == [
            " asd",
            "asd",
            "",
            "  asd",
        ]
        assert IndentTrimmer.trim_lines(["  asd", "asd", "   asd", ""]) == [
            "  asd",
            "asd",
            "   asd",
            "",
        ]
        assert IndentTrimmer.trim_lines([]) == []

    def test_get_line_indent(self):
        assert IndentTrimmer.get_line_indent("   test") == 3
        assert IndentTrimmer.get_line_indent("test") == 0
        assert IndentTrimmer.get_line_indent("  ") == 2
        assert IndentTrimmer.get_line_indent("") == 0

    def test_trim_line(self):
        assert IndentTrimmer.trim_line("   test", 2) == " test"
        assert IndentTrimmer.trim_line(" test", 2) == "test"
        assert IndentTrimmer.trim_line("test", 2) == "test"
        assert IndentTrimmer.trim_line("   ", 2) == " "
