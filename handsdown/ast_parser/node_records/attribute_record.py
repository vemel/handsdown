"""
Wrapper for an `ast.Assign` node of a module or class attribute.
"""
from typing import List, Optional, Set, Union

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

    def __init__(self, node: Union[ast.Assign, ast.AnnAssign]) -> None:
        super().__init__(node)
        self.default: Optional[ExpressionRecord] = None
        first_target = node.targets[0] if isinstance(node, ast.Assign) else node.target
        assert isinstance(first_target, ast.Name)
        self.name = first_target.id
        self.title = self.name
        self.value = ExpressionRecord(node.value) if node.value else None
        self.annotation = (
            ExpressionRecord(node.annotation) if isinstance(node, ast.AnnAssign) else None
        )

    @property
    def related_names(self) -> Set[str]:
        """
        Set of related names.
        """
        result = set()
        if self.value:
            result.update(self.value.related_names)

        return result

    def _render_parts(self) -> List[RenderExpr]:
        parts: List[RenderExpr] = []
        parts.append(self.name)
        if self.value is not None:
            parts.append(" = ")
            parts.append(self.value)
        return parts

    def _parse(self) -> None:
        if self.value:
            self.value.parse()

    def render(self) -> str:
        """
        Render attribute with docstring.
        """
        result = [f"`{self.name}`"]
        if self.annotation:
            result.append(f": `{self.annotation.render()}`")
        if self.docstring:
            result.append(f" - {self.docstring}")
        if self.value:
            result.append(f": {self.value.render()}")

        return "".join(result)

    def append_to(self, node_record: NodeRecord) -> None:
        """
        Append AttributeRecord to NodeRecord.
        """
        node_record.attribute_records.append(self)
