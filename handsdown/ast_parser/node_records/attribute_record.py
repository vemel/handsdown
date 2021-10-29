"""
Wrapper for an `ast.Assign` node of a module or class attribute.
"""
from typing import List, Optional, Set

import handsdown.ast_parser.smart_ast as ast
from handsdown.ast_parser.node_records.expression_record import ExpressionRecord
from handsdown.ast_parser.node_records.node_record import NodeRecord
from handsdown.ast_parser.type_defs import RenderExpr


class AttributeRecord(NodeRecord):
    """
    Wrapper for an `ast.Assign` node of a module or class attribute.

    Arguments:
        node -- AST node.
    """

    def __init__(self, node: ast.Assign) -> None:
        super().__init__(node)
        self.default: Optional[ExpressionRecord] = None
        first_target = node.targets[0]
        assert isinstance(first_target, ast.Name)
        self.name = first_target.id
        self.title = self.name
        self.value = ExpressionRecord(node.value)

    @property
    def related_names(self) -> Set[str]:
        """
        Set of related names.
        """
        result = set()
        if self.value:
            result.update(self.value.related_names)

        return result

    def _render_parts(self, indent: int = 0) -> List[RenderExpr]:
        parts: List[RenderExpr] = []
        parts.append(self.name)
        parts.append(" = ")
        parts.append(self.value)
        return parts

    def _parse(self) -> None:
        if self.value:
            self.value.parse()

    def render(self, indent: int = 0, allow_multiline: bool = False) -> str:
        """
        Render attribute with docstring.
        """
        return f"`{self.name}` - {self.docstring}: `{self.value.render()}`"
