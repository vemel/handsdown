"""
Main CLI entrypoint for `handsdown`

#### Attributes

- `EXCLUDE_EXPRS` - Path glob expressions to always exclude.
  By default: `build/*`, `tests/*`, `test/*` are excluded.
- `SOURCES_GLOB_EXPR` - Glob expr to lokkup python source files: `**/*.py`
"""

import logging

from handsdown.generator import Generator
from handsdown.path_finder import PathFinder
from handsdown.cli_parser import get_cli_parser


EXCLUDE_EXPRS = ["build/*", "tests/*", "test/*"]
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
        PathFinder(root=args.input_path, glob_expr=SOURCES_GLOB)
        .exclude(*EXCLUDE_EXPRS, *args.exclude)
        .include(*args.include)
    )

    generator = Generator(
        input_path=args.input_path,
        logger=logger,
        output_path=args.output_path,
        source_paths=path_finder.list(),
        raise_import_errors=args.panic,
    )
    generator.generate_docs()
    generator.generate_index()
    generator.cleanup_old_docs()


if __name__ == "__main__":
    main()
