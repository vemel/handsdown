"""
CLI Parser.
"""
import argparse
import logging
import re
from pathlib import Path
from typing import Iterable, List
from urllib.parse import urlparse, urlunparse

import pkg_resources

from handsdown.settings import ENCODING


class CLINamespace:
    """
    Main CLI Namespace.
    """

    def __init__(
        self,
        panic: bool,
        input_path: Path,
        output_path: Path,
        toc_depth: int,
        log_level: int,
        include: Iterable[str],
        exclude: Iterable[str],
        source_code_url: str,
        source_code_path: str,
        branch: str,
        project_name: str,
        files: Iterable[Path],
        cleanup: bool,
        encoding: str,
    ) -> None:
        self.panic = panic
        self.input_path = input_path
        self.output_path = output_path
        self.log_level = log_level
        self.toc_depth = toc_depth
        self.include: List[str] = list(include)
        self.exclude: List[str] = list(exclude)
        self.source_code_url = source_code_url
        self.source_code_path = source_code_path
        self.branch = branch
        self.project_name = project_name
        self.files: List[Path] = list(files)
        self.cleanup = cleanup
        self.encoding = encoding

    def get_source_code_url(self) -> str:
        """
        Get URL to source code.

        Returns:
            URL as a string.
        """
        if not self.source_code_url:
            return ""

        result = self.source_code_url.rstrip("/")
        if self.branch:
            result = f"{result}/blob/{self.branch}"

        if self.source_code_path:
            result = f"{result}/{self.source_code_path}".rstrip("/")

        result = urlunparse(urlparse(result.rstrip("/")))
        return f"{result}/"


def git_repo(git_repo_url: str) -> str:
    """
    Validate `git_repo_url` to be a GitHub repo and converts SSH urls to HTTPS.

    Arguments:
        git_repo_url -- GitHub URL or `remote.origin.url`

    Returns:
        A GitHub URL.
    """
    if not git_repo_url:
        return git_repo_url
    https_repo_re = re.compile(r"^https://github.com/(?P<user>[^/]+)/(?P<repo>[^/]+)\.git$")
    ssh_repo_re = re.compile(r"^git@github\.com:(?P<user>[^/]+)/(?P<repo>[^/]+)\.git$")
    short_https_repo_re = re.compile(r"^https://github.com/(?P<user>[^/]+)/(?P<repo>[^/]+)/?$")
    match = https_repo_re.match(git_repo_url)
    if not match:
        match = ssh_repo_re.match(git_repo_url)
    if not match:
        match = short_https_repo_re.match(git_repo_url)
    if not match:
        raise argparse.ArgumentTypeError(f"Cannot parse Git URL {git_repo_url}")

    user = match.groupdict()["user"]
    repo = match.groupdict()["repo"]
    return f"https://github.com/{user}/{repo}/"


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
        raise argparse.ArgumentTypeError(f"Path {path.as_posix()} is not a directory")
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
        raise argparse.ArgumentTypeError(f"Path {path.as_posix()} does not exist")
    if not path.is_dir():
        raise argparse.ArgumentTypeError(f"Path {path.as_posix()} is not a directory")
    return path


def parse_args(args: Iterable[str]) -> CLINamespace:
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
    parser.add_argument(
        "include", nargs="*", help="Path expressions to include source files", default=[]
    )
    parser.add_argument(
        "--exclude", nargs="*", help="Path expressions to exclude source files", default=[]
    )
    parser.add_argument(
        "-i",
        "--input-path",
        help="Path to project root folder",
        default=Path.cwd(),
        type=existing_dir_abs_path,
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
        help="Path to output folder (default: <cwd>/docs)",
        default=Path.cwd() / "docs",
        type=dir_abs_path,
    )
    parser.add_argument(
        "--external",
        help=(
            "Build docs and config for external hosting, GitHub Pages or Read the Docs."
            " Provide the project GitHub URL here."
        ),
        dest="source_code_url",
        metavar="REPO_URL",
        default="",
        type=git_repo,
    )
    parser.add_argument(
        "--source-code-path",
        help="Path to source code in the project.",
        dest="source_code_path",
        metavar="REPO_PATH",
        default="",
        type=str,
    )
    parser.add_argument(
        "--branch",
        help="Main branch name, extends external URL with `/blob/<branch>` (default: main)",
        default="main",
    )
    parser.add_argument(
        "--toc-depth", help="Maximum depth of child modules ToC (default: 1)", default=1, type=int
    )
    parser.add_argument(
        "--cleanup", action="store_true", help="Remove orphaned auto-generated docs"
    )
    parser.add_argument(
        "-n",
        "--name",
        dest="project_name",
        help="Project name",
        default=Path.cwd().stem.capitalize(),
    )
    parser.add_argument(
        "-e",
        "--encoding",
        help=f"Input and output file encoding (default: {ENCODING})",
        default=ENCODING,
    )
    parser.add_argument("--panic", action="store_true", help="Panic and die on import error")
    parser.add_argument("-d", "--debug", action="store_true", help="Show debug messages")
    parser.add_argument("-q", "--quiet", action="store_true", help="Hide log output")
    parser.add_argument("-V", "--version", action="version", version=version)
    namespace = parser.parse_args(list(args))

    log_level = logging.INFO
    if namespace.debug:
        log_level = logging.DEBUG
    if namespace.quiet:
        log_level = logging.CRITICAL

    return CLINamespace(
        panic=namespace.panic,
        input_path=namespace.input_path,
        output_path=namespace.output_path,
        toc_depth=namespace.toc_depth,
        log_level=log_level,
        exclude=namespace.exclude,
        include=namespace.include,
        source_code_url=namespace.source_code_url,
        source_code_path=namespace.source_code_path,
        branch=namespace.branch,
        project_name=namespace.project_name,
        files=namespace.files,
        cleanup=namespace.cleanup,
        encoding=namespace.encoding,
    )
