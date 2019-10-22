import ast

from handsdown.ast_parser.node_record import NodeRecord


class ImportRecord(NodeRecord):
    def __init__(self, node, alias):
        super(ImportRecord, self).__init__(node)
        self.source = node.module
        self.name = None
        self.local_name = alias.asname
        if isinstance(node, ast.ImportFrom):
            self.name = alias.name

    def render(self, indent=0):
        if self.name:
            if self.local_name:
                return "from {} import {} as {}".format(
                    self.source, self.name, self.local_name
                )
            return "from {} import {}".format(self.source, self.name)
        if self.local_name:
            return "import {} as {}".format(self.source, self.local_name)
        return "import {}".format(self.source)

    def match(self, string):
        if self.local_name:
            if string == self.local_name:
                return True

            return False

        return string.startswith(self.source)
