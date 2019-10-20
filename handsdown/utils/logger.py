import logging
from typing import Optional

from handsdown.settings import LOGGER_NAME


def get_logger(level=None):
    # type: (Optional[int]) -> logging.Logger
    """
    Get stdout stream logger.

    Arguments:
        level -- Desired logging level.

    Returns:
        A `logging.Logger` instance.
    """
    logger = logging.getLogger(LOGGER_NAME)
    if level is not None:
        logger.setLevel(level)

    formatter = logging.Formatter(
        fmt="%(asctime)s %(name)s: %(levelname)-8s %(message)s", datefmt="%H:%M:%S"
    )

    if not logger.handlers:
        handler = logging.StreamHandler()
        if level is not None:
            handler.setLevel(level)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
