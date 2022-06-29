# pylint: disable=no-name-in-module
from black import format_file_contents
from black.mode import Mode
from black.parsing import InvalidInput
from black.report import NothingChanged

from handsdown.exceptions import ParserError


def blackify(content: str) -> str:
    """
    Format `content` with `black`.

    Arguments:
        content -- Python code to format.

    Returns:
        Formatted python code.

    Raises:
        ValueError -- If `content` is not a valid Python code.
    """
    file_mode = Mode(is_pyi=False, line_length=89, preview=True)
    try:
        content = format_file_contents(content, fast=True, mode=file_mode)
    except NothingChanged:
        pass
    except (IndentationError, InvalidInput) as e:
        raise ParserError(f"Cannot parse {content}: {e}") from e

    return content.rstrip("\n")
