# pylint: disable=missing-docstring
import unittest
from pathlib import Path
from unittest.mock import patch

from handsdown.main import main


class TestMain(unittest.TestCase):
    @patch("handsdown.main.get_logger")
    @patch("handsdown.main.PathFinder")
    @patch("handsdown.main.Generator")
    def test_main(self, generator_mock, path_finder_mock, _get_logger_mock):

        with patch(
            "handsdown.main.sys.argv",
            [
                "handsdown",
                "-i",
                "/",
                "-o",
                "/output-path",
                "include",
                "--exclude",
                "exclude",
            ],
        ):
            self.assertIsNone(main())

        path_finder_mock.assert_called_once_with(Path("/"))
        path_finder_mock().exclude.assert_called_once_with(
            "build/*", "tests/*", "test/*", "*/__pycache__/*", ".*/*", "exclude"
        )
        path_finder_mock().exclude().include.assert_called_once_with("include")
        generator_mock.assert_called_once_with(
            input_path=Path("/"),
            output_path=Path("/output-path"),
            project_name="Handsdown",
            raise_errors=False,
            source_code_url="",
            source_paths=path_finder_mock().exclude().include().glob(),
            toc_depth=1,
            encoding="utf-8",
        )
