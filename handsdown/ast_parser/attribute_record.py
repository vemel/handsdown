import ast
from typing import List, Text, Set, Union, Optional, TYPE_CHECKING

from handsdown.ast_parser.node_record import NodeRecord
from handsdown.ast_parser.expression_record import ExpressionRecord

if TYPE_CHECKING:
    from handsdown.sentinel import Sentinel


class AttributeRecord(NodeRecord):
    def __init__(self, node):
        # type: (ast.arg) -> None
        super(AttributeRecord, self).__init__(node)
        assert isinstance(self.node, ast.Assign)
        self.default = None  # type: Optional[ExpressionRecord]
        self.name = self.node.targets[0].id
        self.names = [i.id for i in self.node.targets]
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
        parts.append(", ".join(self.names))
        parts.append(" = ")
        parts.append(self.value)
        return parts

    def _parse(self):
        # type: () -> None
        if self.value:
            self.value.parse()

    def render_docstring(self):
        # type: () -> Text
        result = []
        result.append("`{}`".format(self.names[0]))
        result.append(" - ")
        result.append(self.docstring)
        result.append(": ")
        result.append("`{}`".format(self.value.render()))
        return "".join(result)
