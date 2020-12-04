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
