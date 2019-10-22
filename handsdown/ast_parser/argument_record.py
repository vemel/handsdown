from handsdown.ast_parser.node_record import NodeRecord
from handsdown.ast_parser.expression_record import ExpressionRecord


class ArgumentRecord(NodeRecord):
    def __init__(self, node):
        super(ArgumentRecord, self).__init__(node)
        self.name = node.arg
        self.default = None
        self.type_hint = None
        self.prefix = ""
        if node.annotation:
            self.type_hint = ExpressionRecord(node.annotation)

    def _render_parts(self, indent):
        parts = []
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
