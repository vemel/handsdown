import logging

from handsdown.generator import Generator
from handsdown.path_finder import PathFinder
from handsdown.cli_parser import get_cli_parser


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

    path_finder = PathFinder(root=args.input_path, glob_expr="**/*.py").exclude(
        "__main__.py"
    )
    if args.include:
        path_finder = path_finder.include(*args.include)

    if args.exclude:
        path_finder = path_finder.exclude(*args.exclude)

    generator = Generator(
        input_path=args.input_path,
        logger=logger,
        output_path=args.output_path,
        source_paths=path_finder.list(),
    )
    generator.generate()


if __name__ == "__main__":
    main()
