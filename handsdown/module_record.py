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
    def __init__(self):
        self.data: List[ModuleRecord] = []
        self.link_lookup: Dict[Text, Any] = {}

    def find_object(self, link: Text) -> Optional[ModuleObjectRecord]:
        return self.link_lookup.get(link)

    def get_output_file_names(self) -> Set[Text]:
        return {i.output_file_name for i in self}

    def get_package_names(self) -> Set[Text]:
        return {i.import_string.split(".")[0] for i in self}

    def add(self, record: ModuleRecord) -> None:
        self.data.append(record)
        # self.link_lookup[obj.import_string] = obj
        for obj in record.objects:
            self.link_lookup[f"{record.import_string}.{obj.import_string}"] = obj

    def __iter__(self) -> Generator[ModuleRecord, None, None]:
        for obj in self.data:
            yield obj
