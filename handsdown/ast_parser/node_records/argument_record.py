"""
Wrapper for an `ast.arg` node.
"""
from typing import List, Text, Set, Optional, TYPE_CHECKING

from handsdown.ast_parser.node_records.node_record import NodeRecord
from handsdown.ast_parser.node_records.expression_record import ExpressionRecord
from handsdown.ast_parser.node_records.text_record import TextRecord
import handsdown.ast_parser.smart_ast as ast

if TYPE_CHECKING:  # pragma: no cover
    from handsdown.ast_parser.type_defs import RenderExpr, Node


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
        node,  # type: ast.arg
        name,  # type: Text
        type_hint=None,  # type: Optional[ast.expr]
        prefix="",  # type: Text
    ):
        # type: (...) -> None
        super(ArgumentRecord, self).__init__(node)
        self._default = None  # type: Optional[ExpressionRecord]
        self.type_hint = None  # type: Optional[ExpressionRecord]
        if type_hint:
            self.type_hint = ExpressionRecord(type_hint)
        self.prefix = prefix
        self.name = name

    @property
    def default(self):
        # type: () -> Optional[ExpressionRecord]
        """
        Default value of the argument.

        Returns:
            Default exression or None.
        """
        return self._default

    def set_default(self, node):
        # type: (Node) -> None
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
