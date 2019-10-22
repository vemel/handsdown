from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from handsdown.ast_parser.module_record import ModuleRecord
    from handsdown.ast_parser.node_record import NodeRecord


class ModuleRecordList:
    """
    Aggregation of `ModuleRecord` objects.
    """

    def __init__(self):
        # type: () -> None
        self.data = []  # type: List[ModuleRecord]
        self.import_string_map = {}  # type: Dict[Text, Any]

    def find_records(self, import_string):
        # type: (Text) -> Optional[Tuple[NodeRecord, ...]]
        """
        Find `NodeRecord` by it's import string.

        Arguments:
            import_string -- Object import string.

        Returns:
            Found `NodeRecord` instance or None.
        """
        return self.import_string_map.get(import_string)

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
        self.import_string_map[module_record.import_string] = (module_record,)
        for class_record in module_record.class_records:
            self.import_string_map[class_record.import_string] = (
                module_record,
                class_record,
            )
            for method_record in class_record.get_public_methods():
                self.import_string_map[method_record.import_string] = (
                    module_record,
                    class_record,
                    method_record,
                )
        for function_record in module_record.function_records:
            self.import_string_map[function_record.import_string] = (
                module_record,
                function_record,
            )

    def __iter__(self):
        # type: () -> Generator[ModuleRecord, None, None]
        """
        Iterate over all added `ModuleRecord` entries.

        Yields:
            `ModuleRecord` entries.
        """
        for obj in self.data:
            yield obj
