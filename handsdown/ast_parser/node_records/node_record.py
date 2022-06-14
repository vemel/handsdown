"""
Base class for all node records.
"""
from abc import abstractmethod
from typing import Iterable, List, Optional, Set

import handsdown.ast_parser.smart_ast as ast
from handsdown.ast_parser.type_defs import RenderExpr
from handsdown.utils.docstring_formatter import DocstringFormatter
from handsdown.utils.import_string import ImportString


class NodeRecord:
    """
    Base class for all node records.
    """

    def __init__(self, node: ast.AST) -> None:
        self.docstring = ""
        self.import_string = ImportString("")
        self.node = node
        self.name = self.node.__class__.__name__
        self.title = ""
        self.is_method = False
        self.attribute_records: List["NodeRecord"] = []
        self.parsed = False
        self._line_number: Optional[int] = None

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} name={self.name}>"

    @property
    def line_number(self) -> int:
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
    def line_number(self, value: int) -> None:
        self._line_number = value

    def _get_docstring(self) -> str:
        docstring = ast.get_docstring(self.node, clean=False) or ""
        if isinstance(docstring, bytes):
            docstring = docstring.decode("utf-8")

        return DocstringFormatter(docstring).render()

    @property
    def related_names(self) -> Set[str]:
        """
        Get a set of referenced object names in `node`.

        Returns an empty set, should be overriden by a child class.

        Returns:
            A set of referenced object name.
        """
        return set()

    @abstractmethod
    def _parse(self) -> None:
        pass

    def parse(self) -> None:
        """
        Get all information from a node.

        Executes only once if called multiple times.
        """
        if self.parsed:
            return

        self._parse()
        self.parsed = True

    @staticmethod
    def _render_line(parts: Iterable[RenderExpr]) -> str:
        result = []
        for part in parts:
            if isinstance(part, NodeRecord):
                result.append(part.render())

            if isinstance(part, str):
                result.append(part)

        return "".join(result).replace("\n", " ")

    def render(self) -> str:
        """
        Render node to a string.

        Returns:
            A string representation of `node`.
        """
        if not self.parsed:
            self.parse()

        parts = self._render_parts()
        line_parts: List[RenderExpr] = []
        lines = []
        for part_index, part in enumerate(parts):
            line_parts.append(part)
            if part_index < len(parts) - 1:
                continue

            result_lines = [self._render_line(line_parts)]

            lines.append("\n".join(result_lines))

            line_parts = []

        return "".join(lines).rstrip("\n")

    @abstractmethod
    def _render_parts(self) -> List[RenderExpr]:
        pass

    def get_documented_attribute_strings(self) -> List[str]:
        """
        Render each of `attribute_records` to a Markdown string.

        Includes `name`, `docstring` and `value` of an `ArgumentRecord`.

        Returns:
            A list of rendered strings.
        """
        result = []
        for record in self.attribute_records:
            if not record.docstring:
                continue

            result.append(record.render())

        return result

    @property
    def class_name(self) -> str:
        """
        Record class name.
        """
        return self.__class__.__name__
