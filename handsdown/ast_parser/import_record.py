import ast

from handsdown.ast_parser.node_record import NodeRecord


class ImportRecord(NodeRecord):
    def __init__(self, node, alias):
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
        if self.source:
            return "{}.{}".format(self.source, self.name)

        return self.name

    def _render_parts(self, indent=0):
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
        if string == self.local_name:
            return self.get_import_string()

        lookup = "{}.".format(self.local_name)
        if string.startswith(lookup):
            if self.source:
                trailing_import = string[len(lookup) :]
                return "{}.{}".format(self.get_import_string(), trailing_import)

        return None
