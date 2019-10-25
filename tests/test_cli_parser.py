# pylint: disable=missing-docstring
import unittest
import argparse
from pathlib import Path


from handsdown.cli_parser import (
    abs_path,
    git_repo,
    dir_abs_path,
    existing_dir_abs_path,
    parse_args,
)


class TestCLIParser(unittest.TestCase):
    def test_git_repo(self):
        self.assertEqual(git_repo("https://test.test"), "https://test.test")
        self.assertEqual(
            git_repo("git@github.com:user/project.git"),
            "https://github.com/user/project/blob/master/",
        )
        self.assertEqual(
            git_repo("https://github.com/myuser/project.git"),
            "https://github.com/myuser/project/blob/master/",
        )
        self.assertEqual(
            git_repo("https://github.com/myuser/project/blob/develop/"),
            "https://github.com/myuser/project/blob/develop/",
        )

    def test_abs_path(self):
        self.assertTrue(abs_path(Path("test.py")).absolute())

    def test_dir_abs_path(self):
        self.assertTrue(dir_abs_path(Path(__file__).parent).absolute())
        self.assertTrue(dir_abs_path(Path("/non/existing")).absolute())

        with self.assertRaises(argparse.ArgumentTypeError):
            dir_abs_path(Path(__file__))

    def test_existing_dir_abs_path(self):
        self.assertTrue(existing_dir_abs_path(Path(__file__).parent).absolute())

        with self.assertRaises(argparse.ArgumentTypeError):
            self.assertTrue(existing_dir_abs_path(Path("/non/existing")).absolute())

        with self.assertRaises(argparse.ArgumentTypeError):
            existing_dir_abs_path(Path(__file__))

    def test_parse_args(self):
        self.assertIsInstance(parse_args([]), argparse.Namespace)
