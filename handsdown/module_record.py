from dataclasses import dataclass
from pathlib import Path
from typing import Any, Text, Set, List, Generator, Dict, Optional


@dataclass
class ModuleObjectRecord:
    """
    Representation of an imported module object.

    Arguments:
        source_path -- Absolute import source path.
        source_line_number -- Line number of object definition.
        output_file_name -- MD file name for this module.
        object -- Imported module object.
        import_string -- Module import string.
        level -- 0 for classes and functions, 1 for methods.
        title -- Object human-readable title.
    """

    source_path: Path
    source_line_number: int
    output_file_name: Text
    object: Any
    import_string: Text
    level: int
    title: Text


@dataclass
class ModuleRecord:
    """
    Representation of an imported module.

    Arguments:
        source_path -- Absolute import source path.
        output_file_name -- MD file name for this module.
        module -- Imported module.
        import_string -- Module import string.
        objects -- List of objects in the module.
    """

    source_path: Path
    output_file_name: Text
    module: Any
    import_string: Text
    objects: List[ModuleObjectRecord]


class ModuleRecordList:
    """
    Aggregation of `ModuleRecord` objects.
    """

    def __init__(self) -> None:
        self.data: List[ModuleRecord] = []
        self.import_string_map: Dict[Text, Any] = {}

    def find_object(self, import_string: Text) -> Optional[ModuleObjectRecord]:
        """
        Find `ModuleObjectRecord` by it's import string.

        Arguments:
            import_string -- Object import string.

        Returns:
            Found `ModuleObjectRecord` instance or None.
        """
        return self.import_string_map.get(import_string)

    def get_output_file_names(self) -> Set[Text]:
        """
        Get all output MD file names.

        Returns:
            A set of output names as strings.
        """
        return {i.output_file_name for i in self}

    def get_package_names(self) -> Set[Text]:
        """
        Get top level import strings.

        Returns:
            A set of top level imports as strings.
        """
        return {i.import_string.split(".")[0] for i in self}

    def add(self, module_record: ModuleRecord) -> None:
        """
        Add new `ModuleRecord`.

        Arguments:
            module_record -- A new `ModuleRecord`
        """
        self.data.append(module_record)
        for obj in module_record.objects:
            import_string = f"{module_record.import_string}.{obj.import_string}"
            self.import_string_map[import_string] = obj

    def __iter__(self) -> Generator[ModuleRecord, None, None]:
        """
        Iterate over all added `ModuleRecord` entries.

        Returns:
            A generator iterating over `ModuleRecord` entries.
        """
        for obj in self.data:
            yield obj
