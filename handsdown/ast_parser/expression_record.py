from handsdown.ast_parser.node_record import NodeRecord
from handsdown.ast_parser.source_generator import SourceGenerator


class ExpressionRecord(NodeRecord):
    def __init__(self, node):
        super(ExpressionRecord, self).__init__(node)
        self.result = ""
        self._parse_node()

    def _parse_node(self):
        source_gen = SourceGenerator("", False)
        if isinstance(self.node, str):
            self.name = self.node
            self.related_names.add(self.node)
            self.result = self.node
        else:
            if hasattr(self.node, "name"):
                self.name = self.node.name
            if hasattr(self.node, "id"):
                self.name = self.node.id
            source_gen.visit(self.node)
            self.related_names = source_gen.related_names
            self.result = "".join(source_gen.result)

    def _render_parts(self, indent=0):
        parts = []
        parts.append(self.result)
        return parts
