import ast
from typing import List, Text, Set, Union, Optional, TYPE_CHECKING, cast

from handsdown.ast_parser.node_record import NodeRecord
from handsdown.ast_parser.expression_record import ExpressionRecord

if TYPE_CHECKING:
    from handsdown.sentinel import Sentinel


class AttributeRecord(NodeRecord):
    def __init__(self, node):
        # type: (ast.Assign) -> None
        super(AttributeRecord, self).__init__(node)
        self.node = cast(ast.Assign, self.node)
        self.default = None  # type: Optional[ExpressionRecord]
        self.target = cast(ast.Name, self.node.targets[0])
        self.name = self.target.id
        self.value = ExpressionRecord(self.node.value)

    @property
    def related_names(self):
        # type: () -> Set[Text]
        result = set()  # type: Set[Text]
        if self.value:
            result.update(self.value.related_names)

        return result

    def _render_parts(self, indent=0):
        # type: (int) -> List[Union[Text, Sentinel, ExpressionRecord]]
        parts = []  # type: List[Union[Text, Sentinel, ExpressionRecord]]
        parts.append(self.name)
        parts.append(" = ")
        parts.append(self.value)
        return parts

    def _parse(self):
        # type: () -> None
        if self.value:
            self.value.parse()
