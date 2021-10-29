"""
Aggregation of `ModuleRecord` objects.
"""
from typing import Any, Dict, Iterator, List, Optional, Set

from handsdown.ast_parser.node_records.module_record import ModuleRecord
from handsdown.utils.import_string import ImportString
from handsdown.utils.logger import get_logger


class ModuleRecordList:
    """
    Aggregation of `ModuleRecord` objects.
    """

    def __init__(self) -> None:
        self._logger = get_logger()
        self.data: List[ModuleRecord] = []
        self.import_string_map: Dict[ImportString, Any] = {}

    def find_module_record(self, import_string: ImportString) -> Optional[ModuleRecord]:
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

    def get_package_names(self) -> Set[str]:
        """
        Get top level import strings.

        Returns:
            A set of top level imports as strings.
        """
        return {i.import_string.parts[0] for i in self}

    def add(self, module_record: ModuleRecord) -> None:
        """
        Add new `ModuleRecord`.

        Arguments:
            module_record -- A new `ModuleRecord`
        """
        self.data.append(module_record)
        self.import_string_map[module_record.import_string] = module_record

    def __iter__(self) -> Iterator[ModuleRecord]:
        """
        Iterate over all added `ModuleRecord` entries.

        Yields:
            `ModuleRecord` entries.
        """
        for obj in self.data:
            yield obj
