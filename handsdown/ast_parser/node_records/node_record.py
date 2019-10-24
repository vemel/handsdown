import ast
from typing import Text, Set, Generator, Tuple, List, Optional, TYPE_CHECKING

from abc import abstractmethod
from handsdown.sentinel import Sentinel
from handsdown.indent_trimmer import IndentTrimmer
from handsdown.utils import isinstance_str

if TYPE_CHECKING:
    from handsdown.ast_parser.node_records.module_record import ModuleRecord
    from handsdown.ast_parser.node_records.expression_record import ExpressionRecord
    from handsdown.ast_parser.node_records.attribute_record import AttributeRecord
    from handsdown.ast_parser.type_defs import RenderExpr


class NodeRecord(object):
    LINE_LENGTH = 79
    SINGLE_LINE_LENGTH = 50
    INDENT_SPACES = 4
    MAX_INDENT = 4
    ELLIPSIS = "..."

    MULTI_LINE_BREAK = Sentinel("MULTI_LINE_BREAK")
    MULTI_LINE_INDENT = Sentinel("MULTI_LINE_INDENT")
    MULTI_LINE_UNINDENT = Sentinel("MULTI_LINE_UNINDENT")
    LINE_BREAK = Sentinel("LINE_BREAK")
    LINE_INDENT = Sentinel("LINE_INDENT")
    LINE_UNINDENT = Sentinel("LINE_UNINDENT")
    SINGLE_LINE_SPACE = Sentinel("SINGLE_LINE_SPACE")
    MULTI_LINE_COMMA = Sentinel("MULTI_LINE_COMMA")

    def __repr__(self):
        # type: () -> Text
        return "<{} name={}>".format(self.__class__.__name__, self.name)

    def __init__(self, node):
        # type: (ast.AST) -> None
        self.docstring = ""
        self.import_string = ""
        self.node = node
        self.name = self.node.__class__.__name__
        self.title = ""
        self.support_split = False
        self.attribute_records = []  # type: List[AttributeRecord]
        self.parsed = False
        self._line_number = None  # type: Optional[int]

    @property
    def line_number(self):
        # type: () -> int
        if self._line_number is None:
            if isinstance_str(self.node):
                return 1
            self._line_number = self.node.lineno
        return self._line_number or 1

    @line_number.setter
    def line_number(self, value):
        # type: (int) -> None
        self._line_number = value

    def _get_docstring(self):
        # type: () -> Text
        docstring = ast.get_docstring(self.node) or ""  # type: ignore
        docstring = IndentTrimmer.trim_empty_lines(docstring)
        return IndentTrimmer.trim_text(docstring)

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

        self._parse()
        self.parsed = True

    def _render_line(self, parts, indent, allow_multiline):
        # type: (List[RenderExpr], int) -> Text
        result = []
        for part in parts:
            if part is self.SINGLE_LINE_SPACE:
                result.append(" ")

            if isinstance(part, NodeRecord):
                result.append(part.render(indent, allow_multiline))

            if isinstance(part, ("".__class__, u"".__class__)):
                if part.startswith("u'"):
                    part = part[1:]
                result.append(part)

        return "".join(result).replace("\n", " ")

    def _render_multi_line(self, parts, indent, allow_multiline):
        # type: (List[RenderExpr], int) -> Tuple[List[Text], int]
        result = []
        for part in parts:
            if part is self.MULTI_LINE_BREAK:
                result.append("\n")
                result.append(self.render_indent(indent))

            if part is self.MULTI_LINE_INDENT:
                indent += 1
                result.append("\n")
                result.append(self.render_indent(indent))

            if part is self.MULTI_LINE_UNINDENT:
                indent -= 1
                result.append("\n")
                result.append(self.render_indent(indent))

            if part is self.MULTI_LINE_COMMA:
                result.append(",")

            if isinstance(part, NodeRecord):
                result.append(part.render(indent, allow_multiline))

            if isinstance(part, ("".__class__, u"".__class__)):
                if part.startswith("u'"):
                    part = part[1:]
                result.append(part)

        lines = "".join(result).split("\n")
        return lines, indent

    def _fit_single_line(self, line):
        # type: (Text) -> Text
        if len(line) < self.SINGLE_LINE_LENGTH:
            return line
        return "{}{}".format(
            line[: self.SINGLE_LINE_LENGTH - len(self.ELLIPSIS)], self.ELLIPSIS
        )

    def render(self, indent=0, allow_multiline=False):
        # type: (int) -> Text
        if not self.parsed:
            self.parse()

        if indent > self.MAX_INDENT:
            return self.ELLIPSIS

        parts = self._render_parts(indent)
        line_parts = []
        lines = []
        current_indent = indent
        for part_index, part in enumerate(parts):
            if part not in (self.LINE_BREAK, self.LINE_INDENT, self.LINE_UNINDENT):
                line_parts.append(part)
                if part_index < len(parts) - 1:
                    continue

            result_lines = [
                self._render_line(line_parts, current_indent, allow_multiline)
            ]
            if not self.is_line_fit(result_lines[-1], current_indent):
                if not allow_multiline:
                    return self._fit_single_line("".join(result_lines))
                result_lines, current_indent = self._render_multi_line(
                    line_parts, current_indent, allow_multiline
                )

            lines.append("\n".join(result_lines))

            line_parts = []

            if not allow_multiline:
                break

            if part is self.LINE_INDENT:
                current_indent += 1
                lines.append("\n{}".format(self.render_indent(current_indent)))
            if part is self.LINE_UNINDENT:
                current_indent -= 1
                lines.append("\n{}".format(self.render_indent(current_indent)))
            if part is self.LINE_BREAK:
                lines.append("\n{}".format(self.render_indent(current_indent)))

        return "".join(lines).rstrip(" \n")

    @abstractmethod
    def _render_parts(self, indent):
        # type: (int) -> List[RenderExpr]
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

    def get_documented_attribute_strings(self):
        # type: () -> List[Text]
        result = []
        for record in self.attribute_records:
            if not record.docstring:
                continue

            line = "`{}` - {}: `{}`".format(
                record.name, record.docstring, record.value.render()
            )
            result.append(line)

        return result
