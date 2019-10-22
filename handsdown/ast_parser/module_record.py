import ast

from handsdown.ast_parser.module_analyzer import ModuleAnalyzer
from handsdown.indent_trimmer import IndentTrimmer


class ModuleRecord:
    def __init__(self, source_path):
        self.source_path = source_path
        self.tree = ast.parse(source_path.read_text())
        self.class_records = []
        self.function_records = []
        self.import_records = []
        self.source_lines = self.source_path.read_text().split("\n")
        self.parsed = False

    def parse(self):
        analyzer = ModuleAnalyzer()
        analyzer.visit(self.tree)
        self.class_records = analyzer.class_records
        self.function_records = analyzer.function_records
        self.import_records = analyzer.import_records
        for import_record in self.import_records:
            import_record.render()
        for class_record in self.class_records:
            class_record.source_path = self.source_path
            for method_record in class_record.method_records:
                method_record.source_path = self.source_path
                function_lines = self._get_function_lines(method_record)
                method_record.parse_type_comments(function_lines)

        for function_record in self.function_records:
            function_record.source_path = self.source_path
            function_lines = self._get_function_lines(function_record)
            function_record.parse_type_comments(function_lines)
        self.parsed = True

    def _get_function_lines(self, function_record):
        # type: () -> List[Text]
        result = []  # type: List[Text]
        start_index = function_record.node.lineno - 1
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


if __name__ == "__main__":
    from pathlib import Path

    path = Path(__file__).parent.parent.parent / "examples" / "comment_typed.py"
    module_record = ModuleRecord(path)
    module_record.parse()
