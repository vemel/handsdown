"""
Base AST analyzer.
"""
from typing import List

import handsdown.ast_parser.smart_ast as ast


class BaseAnalyzer(ast.NodeVisitor):
    """
    Base AST analyzer.

    Has lists for all objects for different analyzers.
    """

    def __init__(self) -> None:
        self.related_names: List[str] = []

    def get_docstring(self, node: ast.AST) -> str:
        """
        Get docstring from node.

        Arguments:
            node -- AST node.

        Returns:
            Docstring.
        """
        if isinstance(node, (ast.AsyncFunctionDef, ast.FunctionDef, ast.ClassDef, ast.Module)):
            return ast.get_docstring(node, clean=False) or ""
        return ""
