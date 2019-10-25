"""
Base class for all node records.
"""
import re
from typing import Text, Set, Tuple, List, Optional, TYPE_CHECKING

from abc import abstractmethod
from handsdown.ast_parser.enums import RenderPart
from handsdown.indent_trimmer import IndentTrimmer
import handsdown.ast_parser.smart_ast as ast

if TYPE_CHECKING:  # pragma: no cover
    from handsdown.ast_parser.node_records.module_record import ModuleRecord
    from handsdown.ast_parser.node_records.expression_record import ExpressionRecord
    from handsdown.ast_parser.node_records.attribute_record import AttributeRecord
    from handsdown.ast_parser.type_defs import RenderExpr


class NodeRecord(object):
    """
    Base class for all node records.
    """

    # RegExp to find object names in a docstring
    LOCAL_LINK_RE = re.compile(r"`+[A-Za-z]\S+`+")

    # Max length for a multi-line render result
    LINE_LENGTH = 79

    # Max length for a single-line render result
    SINGLE_LINE_LENGTH = 50

    # Amount of spaces per `indent`
    INDENT_SPACES = 4

    # Replace render resul with ellipsis on too deep indendation
    MAX_INDENT = 4

    # Ellipsis string value
    ELLIPSIS = "..."

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
        self.is_method = False
        self.support_split = False
        self.attribute_records = []  # type: List[AttributeRecord]
        self.parsed = False
        self._line_number = None  # type: Optional[int]

    @property
    def line_number(self):
        # type: () -> int
        """
        Return node line number in source.

        Returns:
            A line number startign with 1.
        """
        if self._line_number is None:
            if isinstance(self.node, str):
                return 1

            self._line_number = getattr(self.node, "lineno", 1)
        return self._line_number or 1

    @line_number.setter
    def line_number(self, value):
        # type: (int) -> None
        self._line_number = value

    def _get_docstring(self):
        # type: () -> Text
        docstring = ast.get_docstring(self.node, clean=False) or ""
        if isinstance(docstring, bytes):
            docstring = docstring.decode("utf-8")
        docstring = IndentTrimmer.trim_empty_lines(docstring)
        return IndentTrimmer.trim_text(docstring)

    @property
    def related_names(self):
        # type: () -> Set[Text]
        """
        Get a set of referenced object names in `node`.

        Returns an empty set, should be overriden by a child class.

        Returns:
            A set of referenced object name.
        """
        return set()

    @abstractmethod
    def _parse(self):
        # type: () -> None
        pass

    def parse(self):
        # type: () -> None
        """
        Get all information from a node.

        Executes only once if called multiple times.
        """
        if self.parsed:
            return

        self._parse()
        self.parsed = True

    @staticmethod
    def _render_line(parts, indent, allow_multiline):
        # type: (List[RenderExpr], int, bool) -> Text
        result = []
        for part in parts:
            if part is RenderPart.SINGLE_LINE_SPACE:
                result.append(" ")

            if isinstance(part, NodeRecord):
                result.append(part.render(indent, allow_multiline))

            if isinstance(part, str):
                result.append(part)

        return "".join(result).replace("\n", " ")

    def _render_multi_line(self, parts, indent, allow_multiline):
        # type: (List[RenderExpr], int, bool) -> Tuple[List[Text], int]
        result = []
        for part in parts:
            if part is RenderPart.MULTI_LINE_BREAK:
                result.append("\n")
                result.append(self.render_indent(indent))

            if part is RenderPart.MULTI_LINE_INDENT:
                indent += 1
                result.append("\n")
                result.append(self.render_indent(indent))

            if part is RenderPart.MULTI_LINE_UNINDENT:
                indent -= 1
                result.append("\n")
                result.append(self.render_indent(indent))

            if part is RenderPart.MULTI_LINE_COMMA:
                result.append(",")

            if isinstance(part, NodeRecord):
                result.append(part.render(indent, allow_multiline))

            if isinstance(part, str):
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
        # type: (int, bool) -> Text
        """
        Render node to a string.

        If `allow_multiline` is True, tries to fit the result into `LINE_LENGTH`,
        otherwise does not break lines and trims result to `SINGLE_LINE_LENGTH`.

        Arguments:
            indent -- Indent for lines after the first, `indent=2` means 8 spaces.
            allow_multiline -- allow line breaks in redner result.

        Returns:
            A string representation of `node`.
        """
        if not self.parsed:
            self.parse()

        if indent > self.MAX_INDENT:
            return self.ELLIPSIS

        parts = self._render_parts(indent)
        line_parts = []  # type: List[RenderExpr]
        lines = []
        current_indent = indent
        for part_index, part in enumerate(parts):
            if not isinstance(part, RenderPart) or not part.is_line_break():
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

            if part is RenderPart.LINE_INDENT:
                current_indent += 1
                lines.append("\n{}".format(self.render_indent(current_indent)))
            if part is RenderPart.LINE_UNINDENT:
                current_indent -= 1
                lines.append("\n{}".format(self.render_indent(current_indent)))
            if part is RenderPart.LINE_BREAK:
                lines.append("\n{}".format(self.render_indent(current_indent)))

        return "".join(lines).rstrip("\n")

    @abstractmethod
    def _render_parts(self, indent):
        # type: (int) -> List[RenderExpr]
        pass

    @classmethod
    def is_line_fit(cls, line, indent):
        # type: (Text, int) -> bool
        """
        Check if line fits to `LINE_LENGTH` with given `indent`.

        Examples::

            NodeRecord.is_line_fit("a" * 40, 0)
            False

            NodeRecord.is_line_fit("a" * 80, 0)
            False

            NodeRecord.is_line_fit("a" * 70, 2)
            True

            NodeRecord.is_line_fit("a" * 70, 4)
            False

        Returns:
            A string representation of indent.
        """
        return len(line) < cls.LINE_LENGTH - indent * cls.INDENT_SPACES

    @classmethod
    def render_indent(cls, indent):
        # type: (int) -> Text
        """
        Render indent to a string.

        Each indent adds `INDENT_SPACES` spaces.

        Examples::

            NodeRecord.render_indent(0)
            ""

            NodeRecord.render_indent(1)
            "    "

            NodeRecord.render_indent(4)
            "                "

        Returns:
            A string representation of indent.
        """
        return " " * indent * cls.INDENT_SPACES

    def get_related_import_strings(self, module_record):
        # type: (ModuleRecord) -> Set[Text]
        """
        Get a set of `related_names` found in module class, function,
        method and attribute records.

        Returns:
            A set of absolute import strings found.
        """
        result = set()  # type: Set[Text]
        related_names = self.related_names
        if not related_names:
            return result
        for related_name in related_names:
            for class_record in module_record.class_records:
                if self in class_record.get_public_methods():
                    continue
                if class_record.name == related_name:
                    result.add(class_record.import_string)
            for function_record in module_record.function_records:
                if function_record.name == related_name:
                    result.add(function_record.import_string)
            for import_record in module_record.import_records:
                match = import_record.match(related_name)
                if match:
                    result.add(match)
            for attribute_record in module_record.attribute_records:
                if attribute_record.name == related_name:
                    result.add(attribute_record.import_string)

        return result

    def get_documented_attribute_strings(self):
        # type: () -> List[Text]
        """
        Render each of `attribute_records` to a Markdown string.

        Includes `name`, `docstring` and `value` of an `ArgumentRecord`.

        Returns::
            A list of rendered strings.
        """
        result = []
        for record in self.attribute_records:
            if not record.docstring:
                continue

            line = "`{}` - {}: `{}`".format(
                record.name, record.docstring, record.value.render()
            )
            result.append(line)

        return result
