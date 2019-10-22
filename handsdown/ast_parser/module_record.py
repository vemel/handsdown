import ast

from handsdown.ast_parser.module_analyzer import ModuleAnalyzer
from handsdown.ast_parser.node_record import NodeRecord
from handsdown.indent_trimmer import IndentTrimmer
from handsdown.utils import make_title, split_import_string


class ModuleRecord(NodeRecord):
    def __init__(self, source_path, import_string):
        self.tree = ast.parse(source_path.read_text())
        super(ModuleRecord, self).__init__(self.tree)
        self.source_path = source_path
        self.class_records = []
        self.function_records = []
        self.import_records = []
        self.source_lines = self.source_path.read_text().split("\n")
        self.main_class_lookup_name = source_path.stem.replace("_", "")
        self.name = split_import_string(import_string)[-1]
        self.title = make_title(self.name)
        self.import_string = import_string
        self.import_string_map = {}

    def get_imports(self):
        return []

    def get_title_parts(self):
        parts = split_import_string(self.import_string)
        result = []
        for part in parts:
            part = make_title(part)
            result.append(part)

        if self.title and result:
            result[-1] = self.title

        return result

    def find_record(self, import_string):
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
        for class_record in self.class_records:
            yield (self, class_record)

            for records in class_record.iter_records():
                yield (self,) + records

        for function_record in self.function_records:
            yield (self, function_record)

    def _set_import_strings(self):
        for children in self.iter_records():
            import_string_parts = [self.import_string]
            for child in children[1:]:
                import_string_parts.append(child.name)
                if not child.import_string:
                    import_string = ".".join(import_string_parts)
                    child.import_string = import_string
                    self.import_string_map[import_string] = child

    def _render_parts(self, indent=0):
        parts = []
        if self.import_records:
            for import_record in self.import_records:
                parts.append(import_record)
                parts.append(self.FORCE_LINE_BREAK)
            parts.append(self.FORCE_LINE_BREAK)
        if self.class_records:
            for class_record in self.class_records:
                parts.append(class_record)
                parts.append(self.FORCE_LINE_BREAK)
            parts.append(self.FORCE_LINE_BREAK)
        for function_record in self.function_records:
            parts.append(function_record)
            parts.append(self.FORCE_LINE_BREAK)

        return parts

    def build_children(self):
        analyzer = ModuleAnalyzer()
        analyzer.visit(self.tree)
        self.class_records = sorted(analyzer.class_records, key=lambda x: x.name)
        self.function_records = sorted(analyzer.function_records, key=lambda x: x.name)
        self.import_records = analyzer.import_records
        for class_record in self.class_records:
            class_record.parse()
            # find real title
            if class_record.name.lower() == self.main_class_lookup_name:
                self.title = class_record.name

        self._set_import_strings()

    def _parse(self):
        for class_record in self.class_records:
            class_record.parse()
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
                function_lines = self._get_function_lines(method_record)
                method_record.parse_type_comments(function_lines)

        for function_record in self.function_records:
            function_record.parse()
            function_lines = self._get_function_lines(function_record)
            function_record.parse_type_comments(function_lines)

    def _get_function_lines(self, function_record):
        # type: () -> List[Text]
        result = []  # type: List[Text]
        start_index = function_record.line_number - 1
        end_index = start_index + 1
        lines_count = len(self.source_lines)
        source_lines = self.source_lines

        parentheses_count = 0
        while end_index <= lines_count:
            current_line = source_lines[end_index - 1].split("#", 1)[0].strip()
            if not current_line and parentheses_count <= 0:
                break

            no_spaces_line = current_line.replace(" ", "")
            if "):" in no_spaces_line or ")->" in no_spaces_line:
                break

            parentheses_count += current_line.count("(")
            parentheses_count -= current_line.count(")")
            end_index += 1

        while end_index < lines_count:
            current_line = source_lines[end_index].strip()
            if not current_line.startswith("#"):
                break
            end_index += 1

        result = source_lines[start_index:end_index]
        result = [i.rstrip("\n") for i in result]
        return IndentTrimmer.trim_lines(result)
