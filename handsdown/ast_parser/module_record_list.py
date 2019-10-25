"""
Aggregation of `ModuleRecord` objects.
"""
from typing import Generator, Text, Set, Optional, Dict, List, Any, TYPE_CHECKING

from handsdown.utils.logger import get_logger


if TYPE_CHECKING:  # pragma: no cover
    from handsdown.ast_parser.node_records.module_record import ModuleRecord
    from handsdown.ast_parser.node_records.node_record import NodeRecord
    from handsdown.utils.import_string import ImportString


class ModuleRecordList:
    """
    Aggregation of `ModuleRecord` objects.
    """

    def __init__(self):
        # type: () -> None
        self._logger = get_logger()
        self.data = []  # type: List[ModuleRecord]
        self.import_string_map = {}  # type: Dict[ImportString, Any]

    def find_module_record(self, import_string):
        # type: (ImportString) -> Optional[ModuleRecord]
        """
        Find `ModuleRecord` by it's import string.

        Arguments:
            import_string -- Object import string.

        Returns:
            Found `NodeRecord` instance or None.
        """
        while True:
            module_record = self.import_string_map.get(import_string)
            if module_record:
                return module_record

            if import_string.is_top_level():
                break

            import_string = import_string.parent

        return None

    def get_package_names(self):
        # type: () -> Set[Text]
        """
        Get top level import strings.

        Returns:
            A set of top level imports as strings.
        """
        return {i.import_string.parts[0] for i in self}

    def add(self, module_record):
        # type: (ModuleRecord) -> None
        """
        Add new `ModuleRecord`.

        Arguments:
            module_record -- A new `ModuleRecord`
        """
        self.data.append(module_record)
        self.import_string_map[module_record.import_string] = module_record

    def __iter__(self):
        # type: () -> Generator[ModuleRecord, None, None]
        """
        Iterate over all added `ModuleRecord` entries.

        Yields:
            `ModuleRecord` entries.
        """
        for obj in self.data:
            yield obj
