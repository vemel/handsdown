import argparse
from pathlib import Path
from typing import Text


def abs_path(path: Text) -> Path:
    """
    Make path absolute.

    Arguments:
        path - A path to check.

    Returns:
        An absolute path.
    """
    return Path(path).absolute()


def get_cli_parser() -> argparse.ArgumentParser:
    """
    Get CLI arguments parser.

    Returns:
        An `argparse.ArgumentParser` instance.
    """
    parser = argparse.ArgumentParser(
        "handsdown", description="Docstring-based python documentation generator."
    )
    parser.add_argument(
        "-d", "--debug", action="store_true", help="Show debug messages"
    )
    parser.add_argument("-q", "--quiet", action="store_true", help="Hide log output")
    parser.add_argument(
        "-i",
        "--input-path",
        help="Path to project root folder",
        default=Path.cwd(),
        type=abs_path,
    )
    parser.add_argument(
        "--exclude", nargs="*", help="Path expressions to exclude", default=[]
    )
    parser.add_argument(
        "include", nargs="*", help="Path expressions to include", default=[]
    )
    parser.add_argument(
        "-o",
        "--output-path",
        help="Path to output folder",
        default=Path.cwd() / "docs",
        type=abs_path,
    )
    return parser
