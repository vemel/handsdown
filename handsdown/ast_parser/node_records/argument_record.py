"""
Wrapper for an `ast.arg` node.
"""
from typing import List, Optional, Set

import handsdown.ast_parser.smart_ast as ast
from handsdown.ast_parser.node_records.expression_record import ExpressionRecord
from handsdown.ast_parser.node_records.node_record import NodeRecord
from handsdown.ast_parser.node_records.text_record import TextRecord
from handsdown.ast_parser.type_defs import Node, RenderExpr


class ArgumentRecord(NodeRecord):
    """
    Wrapper for an `ast.arg` node.

    Arguments:
        node -- AST node.
        name -- Argument name.
        type_hint -- Argument type hint.
        prefix -- Prefix for arguemnt name, used for starargs.
    """

    def __init__(
        self,
        node: ast.arg,
        name: str,
        type_hint: Optional[ast.expr] = None,
        prefix: str = "",
    ) -> None:
        super().__init__(node)
        self._default: Optional[ExpressionRecord] = None
        self.type_hint: Optional[ExpressionRecord] = None
        if type_hint:
            self.type_hint = ExpressionRecord(type_hint)
        self.prefix = prefix
        self.name = name

    @property
    def default(self) -> Optional[ExpressionRecord]:
        """
        Default value of the argument.

        Returns:
            Default exression or None.
        """
        return self._default

    @property
    def required(self) -> bool:
        """
        Whether the argument is required.

        Returns:
            True if required, False otherwise.
        """
        return self._default is None

    def set_default(self, node: Node) -> None:
        """
        Set default expression from test or `ast.AST` node.

        Arguments:
            node -- Text or AST node.
        """
        if isinstance(node, str):
            self._default = TextRecord(self.node, node)
        if isinstance(node, ast.AST):
            self._default = ExpressionRecord(node)

    @property
    def related_names(self) -> Set[str]:
        """
        Set of related names.
        """
        result = set()
        if self.default:
            result.update(self.default.related_names)
        if self.type_hint:
            result.update(self.type_hint.related_names)

        return result

    def _render_parts(self) -> List[RenderExpr]:
        parts: List[RenderExpr] = []
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

    def _parse(self) -> None:
        if self.default:
            self.default.parse()
        if self.type_hint:
            self.type_hint.parse()
