"""
Helper to turn on or off `TYPE_CHECKING` to avoid sircular imports.
"""
import traceback
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from handsdown.path_finder import Path


class TypeCheckingMock:
    """
    Helper to turn on or off `TYPE_CHECKING` to avoid sircular imports.

    Returns `True` for usage from the `target_file_path`.

    Examples::

        import_string = fet_import_string_from_path(file_path)
        with patch("typing.TYPE_CHECKING", TypeCheckingMock(file_path)):
            module = importlib.import_module(import_string)

    Arguments:
        target_file_path -- Source path where `typing.TYPE_CHECKING` should be `True`
    """

    def __init__(self, target_file_path):
        # type: (Path) -> None
        self.target_file_path_str = target_file_path.as_posix()

    def __bool__(self):
        # type: () -> bool
        """
        Check if TYPE_CHECKING should be enabled.

        Returns:
            Returns `True` for usage from the `target_file_path`.
        """
        call_stack = traceback.extract_stack(limit=2)
        caller_file_path_str = call_stack[0].filename
        if caller_file_path_str == self.target_file_path_str:
            return True

        return False

    __nonzero__ = __bool__
