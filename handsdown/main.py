"""
Main CLI entrypoint for `handsdown`.
"""
import sys

from handsdown.cli_parser import CLINamespace, parse_args
from handsdown.generator import Generator, GeneratorError
from handsdown.settings import EXCLUDE_EXPRS, SOURCES_GLOB
from handsdown.utils import make_title, render_asset
from handsdown.utils.logger import get_logger
from handsdown.utils.path_finder import PathFinder


def create_external_configs(namespace: CLINamespace) -> None:
    """
    Create `GitHub Pages` and `Read the Docs` configuration files.
    """
    logger = get_logger()
    configs = (
        ("gh_pages_config.yml", namespace.output_path / "_config.yml"),
        ("mkdocs.yml", namespace.input_path / "mkdocs.yml"),
        ("readthedocs.yml", namespace.input_path / ".readthedocs.yml"),
    )
    for asset_name, target_path in configs:
        if target_path.exists():
            continue
        logger.info(f"Creating {target_path.as_posix()} file")
        render_asset(
            asset_name,
            target_path,
            dict(
                source_code_url=namespace.source_code_url,
                project_name=make_title(namespace.input_path.name),
                docs_path=PathFinder(namespace.input_path)
                .relative(namespace.output_path)
                .as_posix(),
            ),
            encoding=namespace.encoding,
        )


def main() -> None:
    """
    Main entrypoint for CLI.
    """
    args = parse_args(sys.argv[1:])
    logger = get_logger(level=args.log_level)

    path_finder = (
        PathFinder(args.input_path).exclude(*(EXCLUDE_EXPRS + args.exclude)).include(*args.include)
    )

    try:
        generator = Generator(
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
