"""
Wrapper for an `ast.expr` node.
"""
import re
from typing import List, Set

import handsdown.ast_parser.smart_ast as ast
from handsdown.ast_parser.analyzers.expression_analyzer import ExpressionAnalyzer
from handsdown.ast_parser.node_records.node_record import NodeRecord
from handsdown.ast_parser.type_defs import DirtyRenderExpr, RenderExpr


class ExpressionRecord(NodeRecord):
    """
    Wrapper for an `ast.expr` node.

    Arguments:
        node -- AST node.
    """

    _str_split_re = re.compile(r"[\]\[ ,]")

    def __init__(self, node: ast.AST) -> None:
        super().__init__(node)
        self.parts: List[DirtyRenderExpr] = []
        self.analyzer = ExpressionAnalyzer()

    @property
    def related_names(self) -> Set[str]:
        """
        Set of related names.
        """
        return set(self.analyzer.related_names)

    def _parse(self) -> None:
        if isinstance(self.node, ast.Name):
            self.name = self.node.id

        if isinstance(self.node, ast.AST):
            self.analyzer.visit(self.node)
            self.parts = self.analyzer.parts
            return

    def _render_parts(self, indent: int = 0) -> List[RenderExpr]:
        result: List[RenderExpr] = []
        for part in self.parts:
            if isinstance(part, ast.AST):
                result.append(ExpressionRecord(part))
                continue

            result.append(part)
        return result
