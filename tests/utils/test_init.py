# pylint: disable=missing-docstring
import unittest
from unittest.mock import patch

from handsdown.utils import extract_md_title, make_title, render_asset


class TestUtils(unittest.TestCase):
    def test_make_title(self):
        self.assertEqual(make_title("my_path.py"), "My Path Py")
        self.assertEqual(make_title("my_title"), "My Title")
        self.assertEqual(make_title("__init__.py"), "Init Py")
        self.assertEqual(make_title("__main__"), "Module")

    def test_extract_md_title(self):
        self.assertEqual(extract_md_title("# test\ncontent"), ("test", "content"))
        self.assertEqual(extract_md_title("# test\n\ncontent"), ("test", "\ncontent"))
        self.assertEqual(extract_md_title("## test\n\ncontent"), ("", "## test\n\ncontent"))
        self.assertEqual(extract_md_title("# test"), ("test", ""))

    @patch("handsdown.utils.Path")
    def test_render_asset(self, PathMock):
        target_path = PathMock("target")
        PathMock().__truediv__().read_text.return_value = "this is {title}"
        self.assertIsNone(
            render_asset(
                "mkdocs.yml",
                target_path,
                {
                    "project_name": "My title",
                    "source_code_url": "test",
                },
            )
        )
        target_path.write_text.assert_called()
