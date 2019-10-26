# pylint: disable=missing-docstring
import unittest

from handsdown.utils.indent_trimmer import IndentTrimmer


class TestIndentTrimmer(unittest.TestCase):
    def test_trim_empty_lines(self):
        self.assertEqual(
            IndentTrimmer.trim_empty_lines("\n  \n test\ntest2\n \n "), " test\ntest2"
        )
        self.assertEqual(IndentTrimmer.trim_empty_lines("\n  \n\n "), "")
        self.assertEqual(IndentTrimmer.trim_empty_lines("\n  \n  test \n "), "  test ")

    def test_trim_text(self):
        self.assertEqual(
            IndentTrimmer.trim_text("  asd\n asd\n   asd\n"), " asd\nasd\n  asd\n"
        )
        self.assertEqual(
            IndentTrimmer.trim_text("  asd\nasd\n   asd\n"), "  asd\nasd\n   asd\n"
        )
        self.assertEqual(
            IndentTrimmer.trim_text(" asd\n asd\n  asd\n"), "asd\nasd\n asd\n"
        )

    def test_trim_lines(self):
        self.assertEqual(
            IndentTrimmer.trim_lines(["  asd", " asd", "   asd"]),
            [" asd", "asd", "  asd"],
        )
        self.assertEqual(
            IndentTrimmer.trim_lines(["  asd", " asd", "", "   asd"]),
            [" asd", "asd", "", "  asd"],
        )
        self.assertEqual(
            IndentTrimmer.trim_lines(["  asd", "asd", "   asd", ""]),
            ["  asd", "asd", "   asd", ""],
        )
        self.assertEqual(IndentTrimmer.trim_lines([]), [])

    def test_get_line_indent(self):
        self.assertEqual(IndentTrimmer.get_line_indent("   test"), 3)
        self.assertEqual(IndentTrimmer.get_line_indent("test"), 0)
        self.assertEqual(IndentTrimmer.get_line_indent("  "), 2)
        self.assertEqual(IndentTrimmer.get_line_indent(""), 0)

    def test_trim_line(self):
        self.assertEqual(IndentTrimmer.trim_line("   test", 2), " test")
        self.assertEqual(IndentTrimmer.trim_line(" test", 2), "test")
        self.assertEqual(IndentTrimmer.trim_line("test", 2), "test")
        self.assertEqual(IndentTrimmer.trim_line("   ", 2), " ")
