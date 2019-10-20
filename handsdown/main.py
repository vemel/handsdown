"""
Main CLI entrypoint for `handsdown`

Attributes:

    EXCLUDE_EXPRS -- Path glob expressions to always exclude.
        By default `build/*`, `tests/*`, `test/*`, `*/__pycache__/*`, `.*/*` are excluded.
    SOURCES_GLOB -- Glob expr to lokkup python source files: `**/*.py`
"""

import logging
import sys
from typing import TYPE_CHECKING

from handsdown.generator import Generator, GeneratorError
from handsdown.path_finder import PathFinder
from handsdown.cli_parser import get_cli_parser
from handsdown.utils import render_asset, get_title_from_path_part
from handsdown.settings import LOGGER_NAME, SOURCES_GLOB, EXCLUDE_EXPRS
from handsdown.version import version


if TYPE_CHECKING:
    import argparse


def get_logger(level):
    # type: (int) -> logging.Logger
    """
    Get stdout stream logger.

    Arguments:
        level -- Desired logging level.

    Returns:
        A `logging.Logger` instance.
    """
    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(level)

    formatter = logging.Formatter(
        fmt="%(asctime)s %(name)s: %(levelname)-8s %(message)s", datefmt="%H:%M:%S"
    )

    handler = logging.StreamHandler()
    handler.setLevel(level)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def create_external_configs(namespace):
    # type: (argparse.Namespace) -> None
    """
    Create `GitHub Pages` and `Read the Docs` configuration files.
    """
    logger = logging.getLogger(LOGGER_NAME)
    configs = (
        ("gh_pages_config.yml", namespace.output_path / "_config.yml"),
        ("mkdocs.yml", namespace.input_path / "mkdocs.yml"),
        ("readthedocs.yml", namespace.input_path / ".readthedocs.yml"),
    )
    for asset_name, target_path in configs:
        if target_path.exists():
            continue
        logger.info("Creating {} file".format(target_path))
        render_asset(
            asset_name,
            target_path,
            dict(
                source_code_url=namespace.source_code_url.replace("blob/master/", ""),
                project_name=get_title_from_path_part(namespace.input_path.name),
                docs_path=PathFinder(namespace.input_path)
                .relative(namespace.output_path)
                .as_posix(),
            ),
        )


def main():
    # type: () -> None
    """
    Main entrypoint for CLI.
    """
    parser = get_cli_parser()
    args = parser.parse_args()
    if args.version:
        print(version)
        return

    log_level = logging.INFO
    if args.debug:
        log_level = logging.DEBUG
    if args.quiet:
        log_level = logging.CRITICAL

    logger = get_logger(level=log_level)

    path_finder = (
        PathFinder(args.input_path)
        .exclude(*(EXCLUDE_EXPRS + args.exclude))
        .include(*args.include)
    )

    try:
        generator = Generator(
            input_path=args.input_path,
            logger=logger,
            output_path=args.output_path,
            source_paths=path_finder.glob(SOURCES_GLOB),
            raise_errors=args.panic,
            source_code_url=args.source_code_url,
            toc_depth=args.toc_depth,
        )
        if args.files:
            for path in args.files:
                generator.generate_doc(path)
        else:
            generator.generate_docs()
            generator.generate_index()
            generator.generate_modules()
            if args.cleanup:
                generator.cleanup_old_docs()

        if args.source_code_url:
            create_external_configs(args)
    except GeneratorError as e:
        logger.error(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
