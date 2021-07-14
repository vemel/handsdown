"""
# CLI Parser
"""
import argparse
import re
from pathlib import Path
from typing import Iterable

import pkg_resources


def git_repo(git_repo_url: str) -> str:
    """
    Validate `git_repo_url` to be a GitHub repo and converts SSH urls to HTTPS.

    Arguments:
        git_repo_url -- GitHub URL or `remote.origin.url`

    Returns:
        A GitHub URL.
    """
    https_repo_re = re.compile(r"^https://github.com/(?P<user>[^/]+)/(?P<repo>[^/]+)\.git$")
    ssh_repo_re = re.compile(r"^git@github\.com:(?P<user>[^/]+)/(?P<repo>[^/]+)\.git$")
    short_https_repo_re = re.compile(r"^https://github.com/(?P<user>[^/]+)/(?P<repo>[^/]+)/?$")
    match = https_repo_re.match(git_repo_url)
    if match:
        return "https://github.com/{user}/{repo}/blob/master/".format(**match.groupdict())
    match = ssh_repo_re.match(git_repo_url)
    if match:
        return "https://github.com/{user}/{repo}/blob/master/".format(**match.groupdict())
    match = short_https_repo_re.match(git_repo_url)
    if match:
        return "https://github.com/{user}/{repo}/blob/master/".format(**match.groupdict())

    return git_repo_url


def abs_path(path_str: str) -> Path:
    """
    Validate `path_str` and make it absolute.

    Arguments:
        path_str -- A path to check.

    Returns:
        An absolute path.
    """
    return Path(path_str).absolute()


def dir_abs_path(path_str: str) -> Path:
    """
    Validate directory `path_str` and make it absolute.

    Arguments:
        path_str -- A path to check.

    Returns:
        An absolute path.

    Raises:
        argparse.ArgumentTypeError -- If path is not a directory.
    """
    path = Path(path_str).absolute()
    if path.exists() and not path.is_dir():
        raise argparse.ArgumentTypeError("Path {} is not a directory".format(path))
    return path


def existing_dir_abs_path(path_str: str) -> Path:
    """
    Validate existing directory `path_str` and make it absolute.

    Arguments:
        path_str -- A path to check.

    Returns:
        An absolute path.

    Raises:
        argparse.ArgumentTypeError -- If path does not exist or is not a directory.
    """
    path = Path(path_str).absolute()
    if not path.exists():
        raise argparse.ArgumentTypeError(f"Path {path} does not exist")
    if not path.is_dir():
        raise argparse.ArgumentTypeError(f"Path {path} is not a directory")
    return path


def parse_args(args: Iterable[str]) -> argparse.Namespace:
    """
    Get CLI arguments parser.

    Returns:
        An `argparse.ArgumentParser` instance.
    """
    try:
        version = pkg_resources.get_distribution("handsdown").version
    except pkg_resources.DistributionNotFound:
        version = "0.0.0"

    parser = argparse.ArgumentParser(
        "handsdown", description="Docstring-based python documentation generator."
    )
    parser.add_argument("--panic", action="store_true", help="Panic and die on import error")
    parser.add_argument(
        "-i",
        "--input-path",
        help="Path to project root folder",
        default=Path.cwd(),
        type=existing_dir_abs_path,
    )
    parser.add_argument("--exclude", nargs="*", help="Path expressions to exclude", default=[])
    parser.add_argument("include", nargs="*", help="Path expressions to include", default=[])
    parser.add_argument(
        "--cleanup", action="store_true", help="Remove orphaned auto-generated docs."
    )
    parser.add_argument(
        "-f",
        "--files",
        nargs="*",
        default=[],
        type=abs_path,
        help="List of source files to use for generation. If empty - all are used.",
    )
    parser.add_argument(
        "-o",
        "--output-path",
        help="Path to output folder",
        default=Path.cwd() / "docs",
        type=dir_abs_path,
    )
    parser.add_argument(
        "--external",
        help=(
            "Build docs and config for external hosting, GitHub Pages or Read the Docs."
            " Provide the project GitHub .../blob/master/ URL here."
        ),
        dest="source_code_url",
        metavar="REPO_URL",
        default=None,
        type=git_repo,
    )
    parser.add_argument(
        "--toc-depth", help="Maximum depth of child modules ToC", default=1, type=int
    )
    parser.add_argument("-d", "--debug", action="store_true", help="Show debug messages")
    parser.add_argument(
        "-n",
        "--name",
        dest="project_name",
        help="Project name",
        default=Path.cwd().stem.capitalize(),
    )
    parser.add_argument("-q", "--quiet", action="store_true", help="Hide log output")
    parser.add_argument("-V", "--version", action="version", version=version)
    return parser.parse_args(list(args))
