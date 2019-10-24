import ast
from typing import List, Text, Set, Optional, TYPE_CHECKING

from handsdown.ast_parser.node_records.node_record import NodeRecord
from handsdown.ast_parser.node_records.expression_record import ExpressionRecord

if TYPE_CHECKING:
    from handsdown.sentinel import Sentinel
    from handsdown.ast_parser.type_defs import RenderExpr


class AttributeRecord(NodeRecord):
    def __init__(self, node):
        # type: (ast.Assign) -> None
        assert isinstance(node, ast.Assign)

        super(AttributeRecord, self).__init__(node)
        self.default = None  # type: Optional[ExpressionRecord]
        first_target = node.targets[0]
        assert isinstance(first_target, ast.Name)
        self.name = first_target.id
        self.title = self.name
        self.value = ExpressionRecord(node.value)

    @property
    def related_names(self):
        # type: () -> Set[Text]
        result = set()  # type: Set[Text]
        if self.value:
            result.update(self.value.related_names)

        return result

    def _render_parts(self, indent=0):
        # type: (int) -> List[RenderExpr]
        parts = []  # type: List[RenderExpr]
        parts.append(self.name)
        parts.append(" = ")
        parts.append(self.value)
        return parts

    def _parse(self):
        # type: () -> None
        if self.value:
            self.value.parse()
