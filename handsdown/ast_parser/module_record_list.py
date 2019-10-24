from typing import Generator, Text, Set, Optional, Dict, List, Any, TYPE_CHECKING

from handsdown.utils import split_import_string
from handsdown.utils.logger import get_logger


if TYPE_CHECKING:
    from handsdown.ast_parser.node_records.module_record import ModuleRecord
    from handsdown.ast_parser.node_records.node_record import NodeRecord


class ModuleRecordList:
    """
    Aggregation of `ModuleRecord` objects.
    """

    def __init__(self):
        # type: () -> None
        self._logger = get_logger()
        self.data = []  # type: List[ModuleRecord]
        self.import_string_map = {}  # type: Dict[Text, Any]

    def find_module_record(self, import_string):
        # type: (Text) -> Optional[ModuleRecord]
        """
        Find `ModuleRecord` by it's import string.

        Arguments:
            import_string -- Object import string.

        Returns:
            Found `NodeRecord` instance or None.
        """
        import_string_parts = split_import_string(import_string)
        while import_string_parts:
            module_import_string = ".".join(import_string_parts)
            import_string_parts.pop()
            module_record = self.import_string_map.get(module_import_string)
            if not module_record:
                continue

            if module_record.import_string == import_string:
                return module_record

            for records in module_record.iter_records():
                record = records[-1]
                if record.import_string == import_string:
                    return module_record

        return None

    def get_package_names(self):
        # type: () -> Set[Text]
        """
        Get top level import strings.

        Returns:
            A set of top level imports as strings.
        """
        return {i.import_string.split(".")[0] for i in self}

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
