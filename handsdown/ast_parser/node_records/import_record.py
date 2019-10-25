from typing import Text, Optional, List, TYPE_CHECKING

from handsdown.ast_parser.node_records.node_record import NodeRecord
import handsdown.ast_parser.smart_ast as ast

if TYPE_CHECKING:
    from handsdown.ast_parser.type_defs import RenderExpr, ASTImport


class ImportRecord(NodeRecord):
    def __init__(self, node, alias):
        # type: (ASTImport, ast.alias) -> None
        super(ImportRecord, self).__init__(node)
        self.source = None
        if isinstance(node, ast.ImportFrom):
            self.name = alias.name
            self.source = node.module
            self.local_name = alias.asname or alias.name
        if isinstance(node, ast.Import):
            self.name = alias.name
            self.local_name = alias.asname or alias.name

    def get_import_string(self):
        # type: () -> Text
        if self.source:
            return "{}.{}".format(self.source, self.name)

        return self.name

    def _render_parts(self, indent=0):
        # type: (int) -> List[RenderExpr]
        if self.source:
            if self.local_name != self.name:
                return [
                    "from {} import {} as {}".format(
                        self.source, self.name, self.local_name
                    )
                ]
            return ["from {} import {}".format(self.source, self.name)]

        if self.local_name != self.name:
            return ["import {} as {}".format(self.name, self.local_name)]

        return ["import {}".format(self.name)]

    def match(self, string):
        # type: (Text) -> Optional[Text]
        if string == self.local_name:
            return self.get_import_string()

        lookup = "{}.".format(self.local_name)
        if string.startswith(lookup):
            if self.source:
                trailing_import = string[len(lookup) :]
                return "{}.{}".format(self.get_import_string(), trailing_import)

        return None

    def _parse(self):
        # type: () -> None
        return
