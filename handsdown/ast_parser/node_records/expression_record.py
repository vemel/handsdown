import re
import ast
from typing import Text, Set, List, TYPE_CHECKING

from handsdown.ast_parser.node_records.node_record import NodeRecord
from handsdown.ast_parser.analyzers.expression_analyzer import ExpressionAnalyzer

if TYPE_CHECKING:
    from handsdown.ast_parser.type_defs import RenderExpr, DirtyRenderExpr


class ExpressionRecord(NodeRecord):
    _str_split_re = re.compile(r"[\]\[ ,]")

    def __init__(self, node):
        # type: (ast.AST) -> None
        super(ExpressionRecord, self).__init__(node)
        self.parts = []  # type: List[DirtyRenderExpr]
        self.analyzer = ExpressionAnalyzer()

    @property
    def related_names(self):
        # type: () -> Set[Text]
        return set(self.analyzer.related_names)

    def _parse(self):
        # type: () -> None
        if isinstance(self.node, ast.Name):
            self.name = self.node.id

        if isinstance(self.node, ast.AST):
            self.analyzer.visit(self.node)
            self.parts = self.analyzer.parts
            return

    def _render_parts(self, indent=0):
        # type: (int) -> List[RenderExpr]
        result = []  # type: List[RenderExpr]
        for part in self.parts:
            if isinstance(part, ast.AST):
                result.append(ExpressionRecord(part))
                continue

            result.append(part)
        return result
