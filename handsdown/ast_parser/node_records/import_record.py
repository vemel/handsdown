"""
Wrapper for an `ast.Import` and `ast.ImportFrom` nodes.
"""
from typing import List, Optional

import handsdown.ast_parser.smart_ast as ast
from handsdown.ast_parser.node_records.node_record import NodeRecord
from handsdown.ast_parser.type_defs import ASTImport, RenderExpr
from handsdown.utils.import_string import ImportString


class ImportRecord(NodeRecord):
    """
    Wrapper for an `ast.Import` and `ast.ImportFrom` nodes.

    Arguments:
        node -- AST node.
        alias -- AST node with import alias.
    """

    def __init__(self, node: ASTImport, alias: ast.alias) -> None:
        super().__init__(node)
        self.source = None
        if isinstance(node, ast.ImportFrom):
            self.name = alias.name
            self.source = node.module
            self.local_name = alias.asname or alias.name
        if isinstance(node, ast.Import):
            self.name = alias.name
            self.local_name = alias.asname or alias.name

    def get_import_string(self) -> ImportString:
        """
        Get import string from a node.

        Returns:
            An absolute import string.
        """
        if self.source:
            return ImportString(self.source) + self.name

        return ImportString(self.name)

    def _render_parts(self) -> List[RenderExpr]:
        if self.source:
            if self.local_name != self.name:
                return [f"from {self.source} import {self.name} as {self.local_name}"]
            return [f"from {self.source} import {self.name}"]

        if self.local_name != self.name:
            return [f"import {self.name} as {self.local_name}"]

        return [f"import {self.name}"]

    def match(self, name: str) -> Optional[ImportString]:
        """
        Check if `name` matches or stats with a local name.

        Examples:
            ```python
            import_node = ast.parse('from my_module import Name as LocalName')
            import_record = ImportRecord(import_node)

            import_record.match('LocalName')
            True

            import_record.match('LocalName.child')
            True

            import_record.match('OtherName')
            False

            import_record.match('LocalNameOther')
            False
            ```

        Returns:
            True if name is imported object itself on one of his children.
        """
        if name == self.local_name:
            return self.get_import_string()

        lookup = f"{self.local_name}."
        if name.startswith(lookup):
            if self.source:
                trailing_import = name[len(lookup) :]
                return ImportString(f"{self.get_import_string()}.{trailing_import}")

        return None

    def _parse(self) -> None:
        return
