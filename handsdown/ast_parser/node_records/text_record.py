"""
Wrapper for a text-only `ast.expr` node.
"""
import re
from typing import Text, Set, List, TYPE_CHECKING

from handsdown.ast_parser.node_records.expression_record import ExpressionRecord

if TYPE_CHECKING:  # pragma: no cover
    import handsdown.ast_parser.smart_ast as ast
    from handsdown.ast_parser.type_defs import Node, RenderExpr


class TextRecord(ExpressionRecord):
    """
    Wrapper for a text-only `ast.expr` node.

    Arguments:
        node -- Related AST node.
        text -- Text to represent it.
    """

    _str_split_re = re.compile(r"[\]\[ ,]")

    def __init__(self, node, text):
        # type: (ast.AST, Text) -> None
        super(TextRecord, self).__init__(node)
        self.name = text
        self.title = text

    @property
    def related_names(self):
        # type: () -> Set[Text]
        """
        A list of fake `ast.Name.id` records inside the node.

        Examples::

            TextRecord(ast_node, 'Union[Text, MyClass]').related_names
            {'Union', 'Text', 'MyClass'}

        Returns:
            A set of related names.
        """
        result = set()
        for related_name in self._str_split_re.split(self.name):
            result.add(related_name)

        return result

    def _parse(self):
        # type: () -> None
        return

    def _render_parts(self, indent=0):
        # type: (int) -> List[RenderExpr]
        return [self.name]
