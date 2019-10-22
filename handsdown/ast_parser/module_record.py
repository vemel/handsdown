import ast

from handsdown.ast_parser.module_analyzer import ModuleAnalyzer
from handsdown.ast_parser.node_record import NodeRecord
from handsdown.indent_trimmer import IndentTrimmer
from handsdown.utils import make_title


class ModuleRecord(NodeRecord):
    def __init__(self, source_path, import_string):
        self.tree = ast.parse(source_path.read_text())
        super(ModuleRecord, self).__init__(self.tree)
        self.source_path = source_path
        self.class_records = []
        self.function_records = []
        self.import_records = []
        self.source_lines = self.source_path.read_text().split("\n")
        self.parsed = False
        self.main_class_lookup_name = source_path.stem.replace("_", "")
        self.name = source_path.stem
        self.title = make_title(self.name)
        self.import_string = import_string
        self._parse_node()
        self._set_import_strings()

    def get_imports(self):
        return []

    def get_title_parts(self):
        parts = self.get_import_string_parts()
        result = []
        for part in parts:
            part = make_title(part)
            result.append(part)

        if self.title and result:
            result[-1] = self.title

        return result

    def get_import_string_parts(self):
        return self.import_string.split(".")

    def iter_children(self):
        for class_record in self.class_records:
            yield (self, class_record)

            for records in class_record.iter_children():
                yield (self,) + records

        for function_record in self.function_records:
            yield (self, function_record)

    def _set_import_strings(self):
        for children in self.iter_children():
            import_string_parts = [self.import_string]
            for child in children[1:]:
                import_string_parts.append(child.name)
                if not child.import_string:
                    child.import_string = ".".join(import_string_parts)

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

    def _get_related_import_strings(self, child):
        result = set()
        if not child.related_names:
            return result

        for related_name in child.related_names:
            for import_record in self.import_records:
                match = import_record.match(related_name)
                if match:
                    result.add(match)

        return result

    def _parse_node(self):
        analyzer = ModuleAnalyzer()
        analyzer.visit(self.tree)
        self.class_records = analyzer.class_records
        self.function_records = analyzer.function_records
        self.import_records = analyzer.import_records
        for import_record in self.import_records:
            import_record.render()
        for class_record in self.class_records:
            # find real title
            if class_record.name.lower() == self.main_class_lookup_name:
                self.title = class_record.name

            class_record.related_import_strings = self._get_related_import_strings(
                class_record
            )
            class_record.source_path = self.source_path
            for method_record in class_record.method_records:
                method_record.source_path = self.source_path
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
                method_record.related_import_strings = self._get_related_import_strings(
                    method_record
                )

        for function_record in self.function_records:
            function_record.source_path = self.source_path
            function_lines = self._get_function_lines(function_record)
            function_record.parse_type_comments(function_lines)
            function_record.related_import_strings = self._get_related_import_strings(
                function_record
            )
        self.parsed = True

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
