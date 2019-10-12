from pathlib import Path
import logging
import argparse
from typing import Text

from handsdown.generator import Generator
from handsdown.path_finder import PathFinder


def abs_path(path: Text) -> Path:
    return Path(path).absolute()


def get_parser() -> argparse.ArgumentParser:
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


def get_logger(level: int) -> logging.Logger:
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
    parser = get_parser()
    args = parser.parse_args()
    log_level = logging.INFO
    if args.debug:
        log_level = logging.DEBUG
    if args.quiet:
        log_level = logging.CRITICAL

    logger = get_logger(level=log_level)

    path_finder = PathFinder(root=args.input_path, glob_expr="**/*.py")
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
