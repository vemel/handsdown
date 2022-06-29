from handsdown.utils.strings import extract_md_title, make_title


class TestUtils:
    def test_make_title(self):
        assert make_title("my_path.py") == "My Path Py"
        assert make_title("my_title") == "My Title"
        assert make_title("__init__.py") == "Init Py"
        assert make_title("__main__") == "Module"

    def test_extract_md_title(self):
        assert extract_md_title("# test\ncontent") == ("test", "content")
        assert extract_md_title("# test\n\ncontent") == ("test", "\ncontent")
        assert extract_md_title("## test\n\ncontent") == ("", "## test\n\ncontent")
        assert extract_md_title("# test") == ("test", "")
