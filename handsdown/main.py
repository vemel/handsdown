from pathlib import Path
import logging

from handsdown.handsdown import Handsdown


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


def main():
    logger = get_logger(logging.DEBUG)

    repo_path = Path.cwd()
    file_paths = sorted(repo_path.glob("**/*.py"))
    generator = Handsdown(repo_path=Path.cwd(), logger=logger)
    generator.generate(file_paths)


if __name__ == "__main__":
    main()
