import ast
from typing import List, Text, Set, Union, Optional, TYPE_CHECKING

from handsdown.ast_parser.node_record import NodeRecord
from handsdown.ast_parser.expression_record import ExpressionRecord

if TYPE_CHECKING:
    from handsdown.sentinel import Sentinel


class ArgumentRecord(NodeRecord):
    def __init__(self, node):
        # type: (ast.arg) -> None
        super(ArgumentRecord, self).__init__(node)
        self.default = None  # type: Optional[ExpressionRecord]
        self.type_hint = self._get_type_hint()
        self.prefix = ""
        self.name = self._get_name()

    def _get_type_hint(self):
        # type: () -> Optional[ExpressionRecord]
        if isinstance(self.node, ast.Name):
            return None

        if isinstance(self.node, str):
            return None

        if isinstance(self.node, ast.arg):
            if self.node.annotation:
                return ExpressionRecord(self.node.annotation)

        return None

    def _get_name(self):
        # type: () -> Text
        if isinstance(self.node, ast.Name):
            return self.node.id

        if isinstance(self.node, str):
            return str(self.node)

        if isinstance(self.node, ast.arg):
            return self.node.arg

        return ""

    @property
    def related_names(self):
        # type: () -> Set[Text]
        result = set()  # type: Set[Text]
        if self.default:
            result.update(self.default.related_names)
        if self.type_hint:
            result.update(self.type_hint.related_names)

        return result

    def _render_parts(self, indent=0):
        # type: (int) -> List[Union[Text, Sentinel, ExpressionRecord]]
        parts = []  # type: List[Union[Text, Sentinel, ExpressionRecord]]
        if self.prefix:
            parts.append(self.prefix)
        parts.append(self.name)
        if self.type_hint:
            parts.append(": ")
            parts.append(self.type_hint)
            if self.default:
                parts.append(" = ")
                parts.append(self.default)
        elif self.default:
            parts.append("=")
            parts.append(self.default)

        return parts

    def _parse(self):
        # type: () -> None
        if self.type_hint:
            self.type_hint.parse()
