"""
Dataclass for an imported module.
"""

from typing import Any, Text, Set, List, Generator, Dict, Optional, TYPE_CHECKING

from handsdown.utils import get_title_from_path_part
from handsdown.function_repr import FunctionRepr, ClassRepr

if TYPE_CHECKING:
    from handsdown.function_repr import TypeHintData, DefaultValueData
    from handsdown.path_finder import Path


class ModuleObjectRecord:
    """
    Dataclass for an imported module object.

    Arguments:
        source_path -- Absolute import source path.
        source_line_number -- Line number of object definition.
        output_path -- Path to output MD file.
        object -- Imported module object.
        parent -- Imported module object parent.
        import_string -- Module import string.
        level -- 0 for classes and functions, 1 for methods.
        title -- Object human-readable title.
        docstring -- Object docstring.
        is_class -- True if object is a class.
        is_related -- True if object is from a different module
        signature -- Object signature.
    """

    def __init__(
        self,
        source_path,  # type: Path
        source_line_number,  # type: int
        output_path,  # type: Path
        obj,  # type: Any
        import_string,  # type: Text
        level,  # type: int
        title,  # type: Text
        docstring,  # type: Text
        is_class,  # type: bool
        is_related,  # type: bool
        module_record,  # type: ModuleRecord
    ):
        # type: (...) -> None
        self.source_path = source_path
        self.source_line_number = source_line_number
        self.output_path = output_path
        self.obj = obj
        self.import_string = import_string
        self.level = level
        self.title = title
        self.docstring = docstring
        self.is_class = is_class
        self.is_related = is_related
        self.module_record = module_record
        self._type_hints = {}  # type: Dict[Text, TypeHintData]
        self._default_values = {}  # type: Dict[Text, DefaultValueData]

    def __repr__(self):
        # type: () -> Text
        return "<ModuleObjectRecord title={}>".format(self.title)

    @property
    def signature(self):
        # type: () -> Text
        """
        Get object signature.

        Returns:
            A string with object signature.
        """
        if isinstance(self.obj, property):
            parts = []
            if getattr(self.obj, "fget", None):
                parts.append("#property getter")
                parts.append(FunctionRepr(self.obj.fget).render())
            if getattr(self.obj, "fset", None):
                if parts:
                    parts.append("")
                parts.append("#property setter")
                parts.append(FunctionRepr(self.obj.fset).render())
            return "\n".join(parts)

        if self.is_class:
            function_repr = ClassRepr(self.obj)  # type: FunctionRepr
        else:
            function_repr = FunctionRepr(self.obj)

        result = function_repr.render()
        self._type_hints = function_repr.get_type_hints()
        self._default_values = function_repr.get_defaults()
        return result

    def get_reference_objects(self):
        # type: () -> List[ModuleObjectRecord]
        result = []
        objects = self.module_record.objects
        parent_import_string = self.import_string.rsplit(".", 1)[0]
        references = set()  # type: Set[Text]
        for type_hint in self._type_hints.values():
            references.update(type_hint.get_class_names())
        for default_value in self._default_values.values():
            references.update(default_value.get_class_names())

        for obj in objects:
            if obj is self:
                continue
            if obj.import_string == parent_import_string:
                continue
            if obj.import_string in references:
                result.append(obj)

        return result


class ModuleRecord:
    """
    Dataclass for an imported module.

    Arguments:
        source_path -- Absolute import source path.
        output_path -- Path to output MD file.
        module -- Imported module.
        title -- Human readable module title.
        import_string -- Module import string.
        objects -- List of objects in the module.
        docstring -- Module docstring.
    """

    def __init__(
        self,
        source_path,  # type: Path
        output_path,  # type: Path
        module,  # type: Any
        title,  # type: Text
        import_string,  # type: Text
        objects,  # type: List[ModuleObjectRecord]
        docstring,  # type: Text
    ):
        # type: (...) -> None
        self.source_path = source_path
        self.output_path = output_path
        self.module = module
        self.title = title
        self.import_string = import_string
        self.objects = objects
        self.docstring = docstring

    def __repr__(self):
        # type: () -> Text
        return "<ModuleRecord title={}>".format(self.title)

    def get_import_string_parts(self):
        # type: () -> List[Text]
        """
        Get parts of module `import_string`.

        Examples::

            ModuleRecord(..., import_string='my_module.utils.parsers').get_title_parts()
            ['My my_module', 'utils', 'parsers']

            ModuleRecord(..., import_string='my_module.__main__').get_title_parts()
            ['my_module', '__main__']

            ModuleRecord(..., import_string='my_module.my_lib', title='MyLibrary').get_title_parts()
            ['my_module', 'my_lib']

        Returns:
            A list of import string parts as strings.
        """
        return self.import_string.split(".")

    def get_title_parts(self):
        # type: () -> List[Text]
        """
        Get parts of module title from module import string.
        If `title` is set, last part replaced with `title`.

        Examples::

            ModuleRecord(..., import_string='my_module.utils.parsers').get_title_parts()
            ['My module', 'Utils', 'parsers']

            ModuleRecord(..., import_string='my_module.__main__').get_title_parts()
            ['My module', 'Main']

            ModuleRecord(..., import_string='my_module.my_lib', title='MyLibrary').get_title_parts()
            ['My module', 'MyLibrary']

        Returns:
            A list of title parts as strings.
        """
        parts = self.get_import_string_parts()
        result = []
        for part in parts:
            part = get_title_from_path_part(part)
            result.append(part)

        if self.title and result:
            result[-1] = self.title

        return result

    @staticmethod
    def get_reference_objects():
        # type: () -> List[ModuleObjectRecord]
        return []


class ModuleRecordList:
    """
    Aggregation of `ModuleRecord` objects.
    """

    def __init__(self):
        # type: () -> None
        self.data = []  # type: List[ModuleRecord]
        self.import_string_map = {}  # type: Dict[Text, Any]

    def find_object(self, import_string):
        # type: (Text) -> Optional[ModuleObjectRecord]
        """
        Find `ModuleObjectRecord` by it's import string.

        Arguments:
            import_string -- Object import string.

        Returns:
            Found `ModuleObjectRecord` instance or None.
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
        self.import_string_map[module_record.import_string] = module_record
        for obj in module_record.objects:
            import_string = "{}.{}".format(
                module_record.import_string, obj.import_string
            )
            self.import_string_map[import_string] = obj

    def __iter__(self):
        # type: () -> Generator[ModuleRecord, None, None]
        """
        Iterate over all added `ModuleRecord` entries.

        Yields:
            `ModuleRecord` entries.
        """
        for obj in self.data:
            yield obj
