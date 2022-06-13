import unittest

from handsdown.ast_parser import type_defs


class TestTypeDefs(unittest.TestCase):
    def test_init(self):
        self.assertTrue(type_defs.RenderExpr)
        self.assertTrue(type_defs.Node)
        self.assertTrue(type_defs.DirtyRenderExpr)
        self.assertTrue(type_defs.ASTIterable)
        self.assertTrue(type_defs.ASTImport)
