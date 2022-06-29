from handsdown.ast_parser.analyzers.base_analyzer import BaseAnalyzer


class TestBaseAnalyzer:
    def test_init(self):
        analyzer = BaseAnalyzer()
        assert analyzer.related_names == []
