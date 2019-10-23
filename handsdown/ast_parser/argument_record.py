from typing import List, Text, Set, Union, Optional, TYPE_CHECKING

from handsdown.ast_parser.node_record import NodeRecord
from handsdown.ast_parser.expression_record import ExpressionRecord
from handsdown.ast_parser import ast_version

if TYPE_CHECKING:
    from handsdown.ast_parser import ast
    from handsdown.sentinel import Sentinel


class ArgumentRecord(NodeRecord):
    def __init__(self, node):
        # type: (ast.arg) -> None
        super(ArgumentRecord, self).__init__(node)
        self.default = None  # type: Optional[ExpressionRecord]
        self.type_hint = None  # type: Optional[ExpressionRecord]
        self.prefix = ""
        if ast_version == 3:
            self.name = node.arg
            if node.annotation:
                self.type_hint = ExpressionRecord(node.annotation)
        else:
            if hasattr(node, "id"):
                self.name = getattr(node, "id")
            else:
                self.name = node

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
