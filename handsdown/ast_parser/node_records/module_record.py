import ast
from typing import List, Text, Generator, Tuple, Any, Optional, Dict, TYPE_CHECKING

from handsdown.ast_parser.analyzers.module_analyzer import ModuleAnalyzer
from handsdown.ast_parser.node_records.node_record import NodeRecord
from handsdown.indent_trimmer import IndentTrimmer
from handsdown.utils import make_title, split_import_string

if TYPE_CHECKING:
    from handsdown.ast_parser.node_records.function_record import FunctionRecord
    from handsdown.ast_parser.node_records.class_record import ClassRecord
    from handsdown.ast_parser.node_records.import_record import ImportRecord
    from handsdown.path_finder import Path


class ModuleRecord(NodeRecord):
    def __init__(self, source_path, source_lines, import_string):
        # type: (Path, List[Text], Text) -> None
        content = "\n".join(source_lines)
        self.tree = ast.parse(content)
        super(ModuleRecord, self).__init__(self.tree)
        self.source_path = source_path
        self.class_records = []  # type: List[ClassRecord]
        self.function_records = []  # type: List[FunctionRecord]
        self.import_records = []  # type: List[ImportRecord]
        self.source_lines = self.source_path.read_text().split("\n")
        self.main_class_lookup_name = source_path.stem.replace("_", "")
        self.name = split_import_string(import_string)[-1]
        self.title = make_title(self.name)
        self.import_string = import_string
        self.import_string_map = {}  # type: Dict[Text, NodeRecord]
        self.docstring = self._get_docstring()

    def get_title_parts(self):
        # type: () -> List[Text]
        parts = split_import_string(self.import_string)
        result = []
        for part in parts:
            part = make_title(part)
            result.append(part)

        if self.title and result:
            result[-1] = self.title

        return result

    def find_record(self, import_string):
        # type: (Text) -> Optional[NodeRecord]
        result = self.import_string_map.get(import_string)
        if result:
            return result

        result = self.import_string_map.get(
            "{}.{}".format(self.import_string, import_string)
        )
        if result:
            return result

        return None

    def iter_records(self):
        # type: () -> Generator[Tuple[NodeRecord, ...], None, None]
        for class_record in self.class_records:
            yield (self, class_record)

            for record in class_record.iter_records():
                yield (self, class_record, record)

        for function_record in self.function_records:
            yield (self, function_record)

    def _set_import_strings(self):
        # type: () -> None
        for children in self.iter_records():
            import_string_parts = [self.import_string]
            for child in children[1:]:
                import_string_parts.append(child.name)
                if not child.import_string:
                    import_string = ".".join(import_string_parts)
                    child.import_string = import_string
                    self.import_string_map[import_string] = child

    def _render_parts(self, indent=0):
        # type: (int) -> List[Any]
        parts = []  # type: List[Any]
        if self.import_records:
            for import_record in self.import_records:
                parts.append(import_record)
                parts.append(self.LINE_BREAK)
            parts.append(self.LINE_BREAK)
        if self.class_records:
            for class_record in self.class_records:
                parts.append(class_record)
                parts.append(self.LINE_BREAK)
            parts.append(self.LINE_BREAK)
        for function_record in self.function_records:
            parts.append(function_record)
            parts.append(self.LINE_BREAK)

        return parts

    def build_children(self):
        # type: () -> None
        analyzer = ModuleAnalyzer()
        analyzer.visit(self.tree)
        self.class_records = sorted(analyzer.class_records, key=lambda x: x.name)
        self.function_records = sorted(analyzer.function_records, key=lambda x: x.name)
        self.attribute_records = sorted(
            analyzer.attribute_records, key=lambda x: x.name
        )
        self.import_records = analyzer.import_records
        for class_record in self.class_records:
            class_record.parse()
            # find real title
            if class_record.name.lower() == self.main_class_lookup_name:
                self.title = class_record.name

        self._set_import_strings()

    def _parse(self):
        # type: () -> None

        for attribute_record in self.attribute_records:
            attribute_record.docstring = self._get_comment_docstring(attribute_record)

        for class_record in self.class_records:
            class_record.parse()
            for attribute_record in class_record.attribute_records:
                # skip private attributes
                if attribute_record.name.startswith("_"):
                    continue

                attribute_record.docstring = self._get_comment_docstring(
                    attribute_record
                )

            for method_record in class_record.method_records:
                method_record.parse()
                if method_record.is_classmethod or method_record.is_staticmethod:
                    method_record.title = "{}.{}".format(
                        class_record.title, method_record.title
                    )
                else:
                    method_record.title = "{}().{}".format(
                        class_record.title, method_record.title
                    )
                function_lines = self._get_function_def_lines(method_record)
                method_record.parse_type_comments(function_lines)

        for function_record in self.function_records:
            function_record.parse()
            function_lines = self._get_function_def_lines(function_record)
            function_record.parse_type_comments(function_lines)

    def _get_function_def_lines(self, function_record):
        # type: (FunctionRecord) -> List[Text]
        """
        Get all function definition lines for comment type
        hints lookup.

        Removes indentation.

        Arguments:
            function_record -- Function record for source lookup.

        Returns:
            Function definition lines as an array.
        """
        assert isinstance(function_record.node, ast.FunctionDef)

        result = []  # type: List[Text]
        start_index = function_record.line_number - 1
        end_index = function_record.node.body[0].lineno - 1
        result = self.source_lines[start_index:end_index]
        result = [i.rstrip("\n") for i in result]
        result = IndentTrimmer.trim_lines(result)
        return result

    def _get_comment_docstring(self, node_record):
        # type: (NodeRecord) -> Text
        """
        Get comment docstring preceding the object from the source code.

        Returns only lines starting with `#`, lines joined with a single space.

        Arguments:
            node_record -- Node record for source lookup.

        Returns:
            A docstring as a string.
        """
        assert isinstance(node_record.node, ast.Assign)

        result = []  # type: List[Text]
        start_index = node_record.node.lineno - 2
        start_line = self.source_lines[start_index].strip()
        while start_index >= 0 and start_line.startswith("#"):
            result.append(start_line[1:].strip())
            start_index -= 1
            start_line = self.source_lines[start_index].strip()

        result.reverse()
        return " ".join(result)
