from handsdown.ast_parser import type_defs


class TestTypeDefs:
    def test_init(self):
        assert type_defs.RenderExpr
        assert type_defs.Node
        assert type_defs.ASTIterable
        assert type_defs.ASTImport
