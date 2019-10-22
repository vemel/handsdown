import ast
from typing import Text, Set, Generator, Union, TYPE_CHECKING

from abc import abstractmethod
from handsdown.sentinel import Sentinel
from handsdown.indent_trimmer import IndentTrimmer

if TYPE_CHECKING:
    from handsdown.ast_parser.module_record import ModuleRecord
    from handsdown.ast_parser.expression_record import ExpressionRecord
    from handsdown.ast_parser.expression_record import ExpressionRecord
    from handsdown.ast_parser.type_defs import RenderParts


class NodeRecord:
    LINE_LENGTH = 79
    INDENT_SPACES = 4

    LINE_BREAK = Sentinel("LINE_BREAK")
    LINE_INDENT = Sentinel("LINE_INDENT")
    LINE_UNINDENT = Sentinel("LINE_UNINDENT")
    FORCE_LINE_BREAK = Sentinel("FORCE_LINE_BREAK")
    FORCE_LINE_INDENT = Sentinel("FORCE_LINE_INDENT")
    FORCE_LINE_UNINDENT = Sentinel("FORCE_LINE_UNINDENT")
    SINGLE_LINE_SPACE = Sentinel("SINGLE_LINE_SPACE")
    MULTI_LINE_COMMA = Sentinel("MULTI_LINE_COMMA")

    def __repr__(self):
        # type: () -> Text
        return "<{} name={} import={}>".format(
            self.__class__.__name__, self.name, self.import_string
        )

    def __init__(self, node):
        # type: (Union[ast.AST, Text]) -> None
        self.name = "{}".format(dir(node))
        if isinstance(node, ast.Name):
            self.name = node.id
        if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
            self.name = node.name

        self.title = self.name
        docstring = ""
        if isinstance(
            node, (ast.AsyncFunctionDef, ast.FunctionDef, ast.ClassDef, ast.Module)
        ):
            docstring = ast.get_docstring(node) or ""

        docstring = IndentTrimmer.trim_empty_lines(docstring)
        self.docstring = IndentTrimmer.trim_text(docstring)

        self.import_string = ""
        self.node = node
        self.support_split = False
        self.parsed = False

    def iter_children(self):
        # type: () -> Generator[NodeRecord, None, None]
        pass

    @property
    def related_names(self):
        # type: () -> Set[Text]
        return set()

    @abstractmethod
    def _parse(self):
        # type: () -> None
        pass

    def parse(self):
        # type: () -> None
        if self.parsed:
            return

        self.parsed = True
        self._parse()

    @property
    def line_number(self):
        # type: () -> int
        assert isinstance(self.node, ast.AST)
        return self.node.lineno

    def render(self, indent=0):
        # type: (int) -> Text
        if not self.parsed:
            self.parse()
        lines = []
        start_multiline = False
        multiline = False
        last_line_break_index = 0
        last_indent = indent
        part_index = 0
        current_indent = indent
        parts = self._render_parts(indent)
        current_line = ""
        while True:
            if part_index == len(parts):
                if (
                    self.support_split
                    and not multiline
                    and not self.is_line_fit(current_line, indent)
                ):
                    part_index = last_line_break_index
                    current_indent = last_indent
                    current_line = ""
                    multiline = True
                    continue

                lines.append(current_line)
                break

            part = parts[part_index]

            if part is self.MULTI_LINE_COMMA:
                if multiline:
                    current_line = "{},".format(current_line)
                part_index += 1
                continue

            if part is self.SINGLE_LINE_SPACE:
                if not multiline:
                    current_line = "{} ".format(current_line)
                part_index += 1
                continue

            if not multiline and part in (
                self.LINE_INDENT,
                self.LINE_UNINDENT,
                self.LINE_BREAK,
            ):
                part_index += 1
                continue

            if part in (self.LINE_BREAK, self.FORCE_LINE_BREAK):
                if (
                    self.support_split
                    and not multiline
                    and not self.is_line_fit(current_line, indent)
                ):
                    part_index = last_line_break_index
                    current_indent = last_indent
                    current_line = ""
                    multiline = True
                    continue

                last_indent = current_indent
                if (
                    last_line_break_index != part_index
                    and part is self.FORCE_LINE_BREAK
                ):
                    multiline = start_multiline
                last_line_break_index = part_index
                if current_line:
                    lines.append(current_line)
                current_line = self.render_indent(current_indent)
                part_index += 1
                continue

            if part in (self.LINE_INDENT, self.FORCE_LINE_INDENT):
                if (
                    self.support_split
                    and not multiline
                    and not self.is_line_fit(current_line, indent)
                ):
                    part_index = last_line_break_index
                    current_indent = last_indent
                    current_line = ""
                    multiline = True
                    continue

                last_indent = current_indent
                if (
                    last_line_break_index != part_index
                    and part is self.FORCE_LINE_BREAK
                ):
                    multiline = start_multiline
                last_line_break_index = part_index

                if current_line:
                    lines.append(current_line)
                current_indent += 1
                current_line = self.render_indent(current_indent)
                part_index += 1
                continue

            if part in (self.LINE_UNINDENT, self.FORCE_LINE_UNINDENT):
                if not multiline and not self.is_line_fit(current_line, indent):
                    part_index = last_line_break_index
                    current_indent = last_indent
                    current_line = ""
                    multiline = True
                    continue

                last_indent = current_indent
                if (
                    last_line_break_index != part_index
                    and part is self.FORCE_LINE_BREAK
                ):
                    multiline = start_multiline
                last_line_break_index = part_index

                if current_line:
                    lines.append(current_line)
                current_indent -= 1
                current_line = self.render_indent(current_indent)
                part_index += 1
                continue

            if isinstance(part, str):
                current_line = "{}{}".format(current_line, part)
                part_index += 1
                continue

            if isinstance(part, NodeRecord):
                current_line = "{}{}".format(current_line, part.render(current_indent))
                part_index += 1
                continue

            raise ValueError("Unknown render part: {}".format(part))

        return "\n".join(lines)

    @abstractmethod
    def _render_parts(self, indent):
        # type: (int) -> RenderParts
        pass

    def is_line_fit(self, line, indent):
        # type: (Text, int) -> bool
        return len(line) < self.LINE_LENGTH - indent * self.INDENT_SPACES

    def render_indent(self, indent):
        # type: (int) -> Text
        return " " * indent * self.INDENT_SPACES

    def get_related_import_strings(self, module_record):
        # type: (ModuleRecord) -> Set[Text]
        result = set()  # type: Set[Text]
        related_names = self.related_names
        if not related_names:
            return result
        for related_name in related_names:
            for class_record in module_record.class_records:
                if class_record is self or self in class_record.get_public_methods():
                    continue
                if class_record.name == related_name:
                    result.add(class_record.import_string)
            for function_record in module_record.function_records:
                if function_record is self:
                    continue
                if function_record.name == related_name:
                    result.add(function_record.import_string)
            for import_record in module_record.import_records:
                match = import_record.match(related_name)
                if match:
                    result.add(match)

        return result
