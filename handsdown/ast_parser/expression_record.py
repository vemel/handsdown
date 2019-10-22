import re

from handsdown.ast_parser.node_record import NodeRecord
from handsdown.ast_parser.source_generator import SourceGenerator


class ExpressionRecord(NodeRecord):
    _str_split_re = re.compile(r"[\]\[ ,]")

    def __init__(self, node):
        super(ExpressionRecord, self).__init__(node)
        self.result = ""
        self.analyzer = SourceGenerator("", False)
        self._parse_node()

    @property
    def related_names(self):
        result = set()
        if isinstance(self.node, str):
            for related_name in self._str_split_re.split(self.node):
                result.add(related_name)

        result.update(self.analyzer.related_names)
        return result

    def _parse_node(self):
        if isinstance(self.node, str):
            self.name = self.node
            self.result = self.node
        else:
            if hasattr(self.node, "name"):
                self.name = self.node.name
            if hasattr(self.node, "id"):
                self.name = self.node.id
            self.analyzer.visit(self.node)
            self.result = "".join(self.analyzer.result)

    def _render_parts(self, indent=0):
        return [self.result]
