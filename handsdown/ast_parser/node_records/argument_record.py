from typing import List, Text, Set, Optional, TYPE_CHECKING

from handsdown.ast_parser.node_records.node_record import NodeRecord

if TYPE_CHECKING:
    import ast
    from handsdown.ast_parser.node_records.expression_record import ExpressionRecord
    from handsdown.sentinel import Sentinel
    from handsdown.ast_parser.type_defs import RenderExpr


class ArgumentRecord(NodeRecord):
    def __init__(
        self,
        node,  # type: ast.arg
        name,  # type: Text
        default=None,  # type: Optional[ExpressionRecord]
        type_hint=None,  # type: Optional[ExpressionRecord]
        prefix="",  # type: Text
    ):
        # type: (...) -> None
        super(ArgumentRecord, self).__init__(node)
        self.default = default  # type: Optional[ExpressionRecord]
        self.type_hint = type_hint
        self.prefix = prefix
        self.name = name

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
        # type: (int) -> List[RenderExpr]
        parts = []  # type: List[RenderExpr]
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
        if self.default:
            self.default.parse()
        if self.type_hint:
            self.type_hint.parse()
