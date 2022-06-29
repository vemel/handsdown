"""
CLI Parser.
"""
import argparse
import logging
import re
from dataclasses import dataclass
from typing import Iterable, List
from urllib.parse import urlparse, urlunparse

import pkg_resources

from handsdown.constants import ENCODING, Theme
from handsdown.utils.nice_path import NicePath


@dataclass
class CLINamespace:
    """
    Main CLI Namespace.
    """

    panic: bool
    input_path: NicePath
    output_path: NicePath
    toc_depth: int
    log_level: int
    include: List[str]
    exclude: List[str]
    source_code_url: str
    source_code_path: NicePath
    branch: str
    project_name: str
    files: List[NicePath]
    cleanup: bool
    encoding: str
    create_configs: bool
    theme: Theme

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

        if self.source_code_path != NicePath():
            result = f"{result}/{self.source_code_path.as_posix()}".rstrip("/")

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


def abs_path(path_str: str) -> NicePath:
    """
    Validate `path_str` and make it absolute.

    Arguments:
        path_str -- A path to check.

    Returns:
        An absolute path.
    """
    return NicePath(path_str).absolute()


def dir_abs_path(path_str: str) -> NicePath:
    """
    Validate directory `path_str` and make it absolute.

    Arguments:
        path_str -- A path to check.

    Returns:
        An absolute path.

    Raises:
        argparse.ArgumentTypeError -- If path is not a directory.
    """
    path = NicePath(path_str).absolute()
    if path.exists() and not path.is_dir():
        raise argparse.ArgumentTypeError(f"Path {path} is not a directory")
    return path


def existing_dir_abs_path(path_str: str) -> NicePath:
    """
    Validate existing directory `path_str` and make it absolute.

    Arguments:
        path_str -- A path to check.

    Returns:
        An absolute path.

    Raises:
        argparse.ArgumentTypeError -- If path does not exist or is not a directory.
    """
    path = NicePath(path_str).absolute()
    if not path.exists():
        raise argparse.ArgumentTypeError(f"Path {path} does not exist")
    if not path.is_dir():
        raise argparse.ArgumentTypeError(f"Path {path} is not a directory")
    return path


def parse_theme(name: str) -> Theme:
    """
    Cast theme name to `Theme`.
    """
    try:
        return Theme(name)
    except ValueError:
        choices = ", ".join([i.value for i in Theme])
        raise argparse.ArgumentTypeError(f"Invalid theme {name}, choices are: {choices}")


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
        default=NicePath.cwd(),
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
        default=NicePath.cwd() / "docs",
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
        default=NicePath(),
        type=NicePath,
    )
    parser.add_argument(
        "--branch",
        help="Main branch name, extends external URL with `/blob/<branch>` (default: main)",
        default="main",
    )
    parser.add_argument(
        "--toc-depth", help="Maximum depth of child modules ToC (default: 3)", default=3, type=int
    )
    parser.add_argument(
        "--cleanup", action="store_true", help="Remove orphaned auto-generated docs"
    )
    parser.add_argument(
        "-n",
        "--name",
        dest="project_name",
        help="Project name",
        default=NicePath.cwd().stem.capitalize(),
    )
    parser.add_argument(
        "-e",
        "--encoding",
        help=f"Input and output file encoding (default: {ENCODING})",
        default=ENCODING,
    )
    parser.add_argument(
        "--create-configs",
        help="Create config files for deployment to RtD and GitHub Pages",
        action="store_true",
    )
    parser.add_argument(
        "-t",
        "--theme",
        choices=list(Theme),
        default=Theme.RTD,
        type=parse_theme,
        help=f"Output mkdocs theme (default: {Theme.RTD.value})",
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
        exclude=list(namespace.exclude),
        include=list(namespace.include),
        source_code_url=namespace.source_code_url,
        source_code_path=namespace.source_code_path,
        branch=namespace.branch,
        project_name=namespace.project_name,
        files=list(namespace.files),
        cleanup=namespace.cleanup,
        encoding=namespace.encoding,
        create_configs=namespace.create_configs,
        theme=namespace.theme,
    )
