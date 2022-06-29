"""
Main CLI entrypoint for `handsdown`.
"""
import sys
from typing import Type

from handsdown.cli_parser import CLINamespace, parse_args
from handsdown.constants import EXCLUDE_EXPRS, SOURCES_GLOB, Theme
from handsdown.exceptions import GeneratorError
from handsdown.generators.base import BaseGenerator
from handsdown.generators.material import MaterialGenerator
from handsdown.generators.rtd import RTDGenerator
from handsdown.utils.logger import get_logger
from handsdown.utils.path_finder import PathFinder


def select_generator_cls(theme: Theme) -> Type[BaseGenerator]:
    """
    Select a generator based on the theme.
    """
    return {
        Theme.RTD: RTDGenerator,
        Theme.MD: MaterialGenerator,
    }[theme]


def api(args: CLINamespace) -> None:
    path_finder = (
        PathFinder(args.input_path).exclude(*(EXCLUDE_EXPRS + args.exclude)).include(*args.include)
    )
    generator_cls = select_generator_cls(args.theme)

    generator = generator_cls(
        project_name=args.project_name,
        input_path=args.input_path,
        output_path=args.output_path,
        source_paths=path_finder.glob(SOURCES_GLOB),
        raise_errors=args.panic,
        source_code_url=args.get_source_code_url(),
        source_code_path=args.source_code_path,
        toc_depth=args.toc_depth,
        encoding=args.encoding,
    )
    if args.files:
        for path in args.files:
            generator.generate_doc(path)
    else:
        generator.generate_docs()
        generator.generate_index()
        if args.cleanup:
            generator.cleanup_old_docs()

    if args.create_configs:
        generator.generate_external_configs()


def main() -> None:
    """
    Main entrypoint for CLI.
    """
    args = parse_args(sys.argv[1:])
    logger = get_logger(level=args.log_level)

    try:
        api(args)
    except GeneratorError as e:
        logger.error(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
