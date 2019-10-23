import ast
from typing import Text, Set, Generator, Union, Tuple, List, TYPE_CHECKING

from abc import abstractmethod
from handsdown.sentinel import Sentinel
from handsdown.indent_trimmer import IndentTrimmer

if TYPE_CHECKING:
    from handsdown.ast_parser.module_record import ModuleRecord
    from handsdown.ast_parser.expression_record import ExpressionRecord
    from handsdown.ast_parser.expression_record import ExpressionRecord
    from handsdown.ast_parser.type_defs import RenderParts


class NodeRecord(object):
    LINE_LENGTH = 79
    INDENT_SPACES = 4

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
        # type: (Union[ast.AST, Text]) -> None
        docstring = ""
        try:
            docstring = ast.get_docstring(node) or ""  # type: ignore
        except TypeError:
            pass

        docstring = IndentTrimmer.trim_empty_lines(docstring)
        self.docstring = IndentTrimmer.trim_text(docstring)

        self.import_string = ""
        self.node = node
        self.name = self._get_name()
        self.title = self.name
        self.support_split = False
        self.parsed = False
        self.line_number = 1
        if isinstance(self.node, ast.AST) and not isinstance(self.node, ast.Module):
            self.line_number = self.node.lineno

    def _get_name(self):
        # type: () -> Text
        if isinstance(self.node, ast.Name):
            return self.node.id
        # FIXME: hacks for py27
        if hasattr(self.node, "value"):
            return getattr(self.node, "value")
        if hasattr(self.node, "name"):
            return getattr(self.node, "name")

        return "{}".format(self.node.__class__.__name__)

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

    def _render_line(self, parts, indent):
        # type: (RenderParts, int) -> Text
        result = []
        for part in parts:
            if part is self.SINGLE_LINE_SPACE:
                result.append(" ")

            if isinstance(part, NodeRecord):
                result.append(part.render(indent))

            if isinstance(part, ("".__class__, u"".__class__)):
                if part.startswith("u'"):
                    part = part[1:]
                result.append(part)

        return "".join(result)

    def _render_multi_line(self, parts, indent):
        # type: (RenderParts, int) -> Tuple[List[Text], int]
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
                result.append(part.render(indent))

            if isinstance(part, ("".__class__, u"".__class__)):
                if part.startswith("u'"):
                    part = part[1:]
                result.append(part)

        lines = "".join(result).split("\n")
        return lines, indent

    def render(self, indent=0):
        # type: (int) -> Text
        if not self.parsed:
            self.parse()

        parts = self._render_parts(indent)
        line_parts = []
        lines = []
        current_indent = indent
        for part_index, part in enumerate(parts):
            if part not in (self.LINE_BREAK, self.LINE_INDENT, self.LINE_UNINDENT):
                line_parts.append(part)
                if part_index < len(parts) - 1:
                    continue

            result_lines = [self._render_line(line_parts, current_indent)]
            if not self.is_line_fit(result_lines[-1], current_indent):
                result_lines, current_indent = self._render_multi_line(
                    line_parts, current_indent
                )

            lines.append("\n".join(result_lines))

            line_parts = []

            if part is self.LINE_INDENT:
                current_indent += 1
                lines.append("\n{}".format(self.render_indent(current_indent)))
            if part is self.LINE_UNINDENT:
                current_indent -= 1
                lines.append("\n{}".format(self.render_indent(current_indent)))
            if part is self.LINE_BREAK:
                lines.append("\n{}".format(self.render_indent(current_indent)))

        return "".join(lines).rstrip(" \n")

        # while parts:
        #     line, part_index = self._render_line(parts, current_indent)
        #     if not self.is_line_fit(line, indent):
        #         line, part_index = self._render_multi_line(parts, current_indent)

        #     lines.append(line)

        #     break_part = parts[part_index]
        #     if break_part in (self.MULTI_LINE_INDENT, self.LINE_INDENT):
        #         current_indent += 1
        #     if break_part in (self.MULTI_LINE_UNINDENT, self.LINE_UNINDENT):
        #         current_indent -= 1

        # for part in parts:
        #     if part in (self.LINE_BREAK, self.LINE_INDENT, self.LINE_UNINDENT):
        #         line, part_index = self._render_line(line_parts, current_indent)
        #         break

        #     line_parts.append(part)

        # lines = []
        # start_multiline = False
        # multiline = False
        # last_line_break_index = 0
        # last_indent = indent
        # part_index = 0
        # current_indent = indent
        # current_line = ""
        # while True:
        #     if part_index == len(parts):
        #         if (
        #             self.support_split
        #             and not multiline
        #             and not self.is_line_fit(current_line, indent)
        #         ):
        #             part_index = last_line_break_index
        #             current_indent = last_indent
        #             current_line = ""
        #             multiline = True
        #             continue

        #         lines.append(current_line)
        #         break

        #     part = parts[part_index]

        #     if part is self.MULTI_LINE_COMMA:
        #         if multiline:
        #             current_line = "{},".format(current_line)
        #         part_index += 1
        #         continue

        #     if part is self.SINGLE_LINE_SPACE:
        #         if not multiline:
        #             current_line = "{} ".format(current_line)
        #         part_index += 1
        #         continue

        #     if not multiline and part in (
        #         self.MULTI_LINE_INDENT,
        #         self.MULTI_LINE_UNINDENT,
        #         self.MULTI_LINE_BREAK,
        #     ):
        #         part_index += 1
        #         continue

        #     if part in (self.MULTI_LINE_BREAK, self.LINE_BREAK):
        #         if (
        #             self.support_split
        #             and not multiline
        #             and not self.is_line_fit(current_line, indent)
        #         ):
        #             part_index = last_line_break_index
        #             current_indent = last_indent
        #             current_line = ""
        #             multiline = True
        #             continue

        #         last_indent = current_indent
        #         if last_line_break_index != part_index and part is self.LINE_BREAK:
        #             multiline = start_multiline
        #         last_line_break_index = part_index
        #         if current_line:
        #             lines.append(current_line)
        #         current_line = self.render_indent(current_indent)
        #         part_index += 1
        #         continue

        #     if part in (self.MULTI_LINE_INDENT, self.LINE_INDENT):
        #         if (
        #             self.support_split
        #             and not multiline
        #             and not self.is_line_fit(current_line, indent)
        #         ):
        #             part_index = last_line_break_index
        #             current_indent = last_indent
        #             current_line = ""
        #             multiline = True
        #             continue

        #         last_indent = current_indent
        #         if last_line_break_index != part_index and part is self.LINE_BREAK:
        #             multiline = start_multiline
        #         last_line_break_index = part_index

        #         if current_line:
        #             lines.append(current_line)
        #         current_indent += 1
        #         current_line = self.render_indent(current_indent)
        #         part_index += 1
        #         continue

        #     if part in (self.MULTI_LINE_UNINDENT, self.LINE_UNINDENT):
        #         if not multiline and not self.is_line_fit(current_line, indent):
        #             part_index = last_line_break_index
        #             current_indent = last_indent
        #             current_line = ""
        #             multiline = True
        #             continue

        #         last_indent = current_indent
        #         if last_line_break_index != part_index and part is self.LINE_BREAK:
        #             multiline = start_multiline
        #         last_line_break_index = part_index

        #         if current_line:
        #             lines.append(current_line)
        #         current_indent -= 1
        #         current_line = self.render_indent(current_indent)
        #         part_index += 1
        #         continue

        #     if isinstance(part, str):
        #         current_line = "{}{}".format(current_line, part)
        #         part_index += 1
        #         continue

        #     if isinstance(part, NodeRecord):
        #         current_line = "{}{}".format(current_line, part.render(current_indent))
        #         part_index += 1
        #         continue

        #     raise ValueError("Unknown render part: {}".format(part))

        # return "\n".join(lines)

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
