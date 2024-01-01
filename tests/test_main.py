from pathlib import Path
from unittest.mock import patch

from handsdown.main import main


class TestMain:
    @patch("handsdown.main.get_logger")
    @patch("handsdown.main.PathFinder")
    @patch("handsdown.main.RTDGenerator")
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
            assert main() is None

        path_finder_mock.assert_called_once_with(Path("/"))
        path_finder_mock().exclude.assert_called_once_with("exclude")
        path_finder_mock().exclude().include.assert_called_once_with("include")
        generator_mock.assert_called_once_with(
            input_path=Path("/"),
            output_path=Path("/output-path"),
            project_name="Handsdown",
            raise_errors=False,
            source_code_url="",
            source_code_path=Path(),
            source_paths=path_finder_mock().exclude().include().glob(),
            toc_depth=3,
            encoding="utf-8",
        )
