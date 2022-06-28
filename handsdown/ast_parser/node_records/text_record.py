"""
Wrapper for a text-only `ast.expr` node.
"""
import re
from typing import List, Set

import handsdown.ast_parser.smart_ast as ast
from handsdown.ast_parser.node_records.expression_record import ExpressionRecord
from handsdown.ast_parser.type_defs import RenderExpr


class TextRecord(ExpressionRecord):
    """
    Wrapper for a text-only `ast.expr` node.

    Arguments:
        node -- Related AST node.
        text -- Text to represent it.
    """

    _str_split_re = re.compile(r"[\]\[ ,]")

    def __init__(self, node: ast.AST, text: str) -> None:
        super().__init__(node)
        self.name = text
        self.title = text

    @property
    def related_names(self) -> Set[str]:
        """
        A list of fake `ast.Name.id` records inside the node.

        Examples::

            TextRecord(ast_node, 'Union[str, MyClass]').related_names
            {'Union', 'str', 'MyClass'}

        Returns:
            A set of related names.
        """
        result = set()
        for related_name in self._str_split_re.split(self.name):
            result.add(related_name)

        return result

    def _parse(self) -> None:
        return

    def _render_parts(self) -> List[RenderExpr]:
        return [self.name]
