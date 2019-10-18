"""
Main CLI entrypoint for `handsdown`

#### Attributes

- `EXCLUDE_EXPRS` - Path glob expressions to always exclude.
  By default: `build/*`, `tests/*`, `test/*` are excluded.
- `SOURCES_GLOB_EXPR` - Glob expr to lokkup python source files: `**/*.py`
"""

import logging
import sys

from handsdown.generator import Generator, GeneratorError
from handsdown.path_finder import PathFinder
from handsdown.cli_parser import get_cli_parser


EXCLUDE_EXPRS = ["build/*", "tests/*", "test/*", "*/__pycache__/*"]
SOURCES_GLOB = "**/*.py"


def get_logger(level: int) -> logging.Logger:
    """
    Get stdout stream logger.

    Arguments:
        level -- Desired logging level.

    Returns:
        A `logging.Logger` instance.
    """
    logger = logging.Logger("handsdown")
    logger.setLevel(level)

    formatter = logging.Formatter(
        fmt="%(asctime)s %(name)s: %(levelname)-8s %(message)s", datefmt="%H:%M:%S"
    )

    handler = logging.StreamHandler()
    handler.setLevel(level)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def main() -> None:
    """
    Main entrypoint for CLI.
    """
    parser = get_cli_parser()
    args = parser.parse_args()
    log_level = logging.INFO
    if args.debug:
        log_level = logging.DEBUG
    if args.quiet:
        log_level = logging.CRITICAL

    logger = get_logger(level=log_level)

    path_finder = (
        PathFinder(args.input_path)
        .exclude(*EXCLUDE_EXPRS, *args.exclude)
        .include(*args.include)
    )

    try:
        generator = Generator(
            input_path=args.input_path,
            logger=logger,
            output_path=args.output_path,
            source_paths=path_finder.glob(SOURCES_GLOB),
            raise_errors=args.panic,
            source_code_url=args.gh_pages,
            toc_depth=args.toc_depth,
        )
        if args.files:
            for path in args.files:
                generator.generate_doc(path)
        else:
            generator.generate_docs()
            generator.generate_index()
            if args.cleanup:
                generator.cleanup_old_docs()

        if args.gh_pages:
            gh_pages_config_path = args.output_path / "_config.yml"
            if not gh_pages_config_path.exists():
                logger.info(f"Creating {gh_pages_config_path} file")
                gh_pages_config_path.write_text("theme: jekyll-theme-cayman\n")
    except GeneratorError as e:
        logger.error(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
