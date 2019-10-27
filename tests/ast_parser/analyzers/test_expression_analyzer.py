# pylint: disable=missing-docstring
import unittest
from unittest.mock import MagicMock

from handsdown.ast_parser.analyzers.expression_analyzer import ExpressionAnalyzer


class TestClassAnalyzer(unittest.TestCase):
    def test_init(self):
        analyzer = ExpressionAnalyzer()
        self.assertEqual(analyzer.parts, [])

    def test_visit_Str(self):
        node = MagicMock()
        node.s = "value"
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_Str(node))
        self.assertEqual(analyzer.parts, ["'value'"])

        node.s = b"value"
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_Str(node))
        self.assertEqual(analyzer.parts, ["'value'"])

    def test_visit_Bytes(self):
        node = MagicMock()
        node.s = b"value"
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_Bytes(node))
        self.assertEqual(analyzer.parts, ["b'value'"])

    def test_visit_Num(self):
        node = MagicMock()
        node.n = 123.456
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_Num(node))
        self.assertEqual(analyzer.parts, ["123.456"])

    def test_visit_Name(self):
        node = MagicMock()
        node.id = "name"
        analyzer = ExpressionAnalyzer()
        self.assertIsNone(analyzer.visit_Name(node))
        self.assertEqual(analyzer.parts, ["name"])
