import ast

from abc import abstractmethod
from handsdown.sentinel import Sentinel
from handsdown.indent_trimmer import IndentTrimmer


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
        return "<{} name={} import={}>".format(
            self.__class__.__name__, self.name, self.import_string
        )

    def __init__(self, node):
        self.name = ""
        if getattr(node, "name", None):
            self.name = node.name
        if getattr(node, "id", None):
            self.name = node.id

        self.title = self.name
        docstring = ""
        try:
            docstring = ast.get_docstring(node) or ""
        except TypeError:
            pass

        docstring = IndentTrimmer.trim_empty_lines(docstring)
        self.docstring = IndentTrimmer.trim_text(docstring)

        self.import_string = ""
        self.node = node
        self.support_split = False
        self.parsed = False

    def iter_children(self):
        pass

    @property
    def related_names(self):
        return set()

    @abstractmethod
    def _parse(self):
        pass

    def parse(self):
        if self.parsed:
            return

        self.parsed = True
        self._parse()

    @property
    def line_number(self):
        return self.node.lineno

    def render(self, indent=0):
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
                    # raise ValueError(part_index, last_line_break_index, parts)
                    # print(current_line, last_line_break_index, parts, multiline)
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

            current_line = "{}{}".format(current_line, part.render(current_indent))
            part_index += 1

        return "\n".join(lines)

    @abstractmethod
    def _render_parts(self, indent):
        pass

    def is_line_fit(self, line, indent):
        return len(line) < self.LINE_LENGTH - indent * self.INDENT_SPACES

    def render_indent(self, indent):
        return " " * indent * self.INDENT_SPACES

    def get_related_import_strings(self, module_record):
        result = set()
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
