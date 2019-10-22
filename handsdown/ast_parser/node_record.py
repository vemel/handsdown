from abc import abstractmethod
from handsdown.sentinel import Sentinel


class NodeRecord:
    LINE_LENGTH = 100
    INDENT_SPACES = 4

    LINE_BREAK = Sentinel("LINE_BREAK")
    LINE_INDENT = Sentinel("LINE_INDENT")
    LINE_UNINDENT = Sentinel("LINE_UNINDENT")
    FORCE_LINE_BREAK = Sentinel("FORCE_LINE_BREAK")
    FORCE_LINE_INDENT = Sentinel("FORCE_LINE_INDENT")
    FORCE_LINE_UNINDENT = Sentinel("FORCE_LINE_UNINDENT")

    def __init__(self, node):
        self.name = ""
        self.docstring = ""
        self.node = node
        self.related_names = set()
        self.support_split = False
        self.source_path = None

    def _parse_node(self):
        pass

    @property
    def line_number(self):
        return self.node.lineno

    def _render_one_line(self, indent):
        lines = [""]
        current_indent = indent
        for part in self._render_parts(indent):
            if part in (self.LINE_INDENT, self.LINE_UNINDENT, self.LINE_BREAK):
                continue

            if part in (self.LINE_BREAK, self.FORCE_LINE_BREAK):
                # print(self.name, current_indent)
                lines.append(self.render_indent(current_indent))
                continue

            if part in (self.LINE_INDENT, self.FORCE_LINE_INDENT):
                current_indent += 1
                lines.append(self.render_indent(current_indent))
                continue

            if part in (self.LINE_UNINDENT, self.FORCE_LINE_UNINDENT):
                current_indent -= 1
                if not lines[-1].strip():
                    lines = lines[:-1]
                lines.append(self.render_indent(current_indent))
                continue

            if isinstance(part, str):
                lines[-1] = "{}{}".format(lines[-1], part)
                continue

            lines[-1] = "{}{}".format(lines[-1], part.render(current_indent))

        return lines

    def _render_multi_line(self, indent):
        lines = [""]
        current_indent = indent
        for part in self._render_parts(indent):
            if part in (self.LINE_BREAK, self.FORCE_LINE_BREAK):
                lines.append(self.render_indent(current_indent))
                continue

            if part in (self.LINE_INDENT, self.FORCE_LINE_INDENT):
                current_indent += 1
                lines.append(self.render_indent(current_indent))
                continue

            if part in (self.LINE_UNINDENT, self.FORCE_LINE_UNINDENT):
                current_indent -= 1
                if not lines[-1].strip():
                    lines = lines[:-1]
                lines.append(self.render_indent(current_indent))
                continue

            if isinstance(part, str):
                lines[-1] = "{}{}".format(lines[-1], part)
                continue

            lines[-1] = "{}{}".format(lines[-1], part.render(current_indent))

        return lines

    def render(self, indent=0):
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
