import argparse
from pathlib import Path

import pytest

from handsdown.cli_parser import (
    CLINamespace,
    abs_path,
    dir_abs_path,
    existing_dir_abs_path,
    git_repo,
    parse_args,
)


class TestCLIParser:
    def test_git_repo(self):
        assert git_repo("git@github.com:myuser/project.git") == "https://github.com/myuser/project/"
        assert (
            git_repo("https://github.com/myuser/project.git")
            == "https://github.com/myuser/project/"
        )
        assert git_repo("https://github.com/myuser/project") == "https://github.com/myuser/project/"
        with pytest.raises(argparse.ArgumentTypeError):
            git_repo("https://test.test")

    def test_abs_path(self):
        assert abs_path(Path("test.py").as_posix()).absolute()

    def test_dir_abs_path(self):
        assert dir_abs_path(Path(__file__).parent.as_posix()).absolute()
        assert dir_abs_path(Path("/non/existing").as_posix()).absolute()

        with pytest.raises(argparse.ArgumentTypeError):
            dir_abs_path(Path(__file__).as_posix())

    def test_existing_dir_abs_path(self):
        assert existing_dir_abs_path(Path(__file__).parent.as_posix()).absolute()

        with pytest.raises(argparse.ArgumentTypeError):
            assert existing_dir_abs_path(Path("/non/existing").as_posix()).absolute()

        with pytest.raises(argparse.ArgumentTypeError):
            existing_dir_abs_path(Path(__file__).as_posix())

    def test_parse_args(self):
        assert isinstance(parse_args([]), CLINamespace)

    def test_get_source_code_url(self):
        namespace = parse_args([])
        assert namespace.get_source_code_url() == ""

        namespace.branch = "master"
        assert namespace.get_source_code_url() == ""

        namespace.source_code_url = "path/"
        assert namespace.get_source_code_url() == "path/blob/master/"

        namespace.source_code_url = "https://github.com/author/repo"
        namespace.branch = "main"
        assert namespace.get_source_code_url() == "https://github.com/author/repo/blob/main/"

        namespace.source_code_url = ""
        assert namespace.get_source_code_url() == ""
