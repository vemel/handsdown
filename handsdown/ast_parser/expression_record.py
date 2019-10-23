import re
from typing import Text, Union, Set, TYPE_CHECKING

from handsdown.ast_parser.node_record import NodeRecord
from handsdown.ast_parser.source_generator import SourceGenerator
from handsdown.ast_parser import ast

if TYPE_CHECKING:
    from handsdown.ast_parser.type_defs import RenderParts


class ExpressionRecord(NodeRecord):
    _str_split_re = re.compile(r"[\]\[ ,]")

    def __init__(self, node):
        # type: (Union[ast.expr, Text]) -> None
        super(ExpressionRecord, self).__init__(node)
        self.result = ""
        self.analyzer = SourceGenerator()

    @property
    def related_names(self):
        # type: () -> Set[Text]
        result = set()
        if isinstance(self.node, str):
            for related_name in self._str_split_re.split(self.node):
                result.add(related_name)
        else:
            result.update(self.analyzer.related_names)
        return result

    def _parse(self):
        # type: () -> None
        if isinstance(self.node, ast.Name):
            self.name = self.node.id

        if isinstance(self.node, ast.AST):
            self.analyzer.visit(self.node)
            self.result = "".join(self.analyzer.result)
            return

        self.name = self.node
        self.result = self.node

    def _render_parts(self, indent=0):
        # type: (int) -> RenderParts
        return [self.result]
