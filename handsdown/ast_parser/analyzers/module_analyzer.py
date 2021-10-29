"""
AST analyzer for `ast.Module` records.
"""
from typing import List

import handsdown.ast_parser.smart_ast as ast
from handsdown.ast_parser.analyzers.base_analyzer import BaseAnalyzer
from handsdown.ast_parser.type_defs import ASTFunctionDef, ASTImport


class ModuleAnalyzer(BaseAnalyzer):
    """
    AST analyzer for `ast.Module` records.
    """

    def __init__(self) -> None:
        super().__init__()
        self.all_names: List[str] = []
        self.import_nodes: List[ASTImport] = []
        self.function_nodes: List[ASTFunctionDef] = []
        self.attribute_nodes: List[ast.Assign] = []
        self.class_nodes: List[ast.ClassDef] = []

    def visit_Import(self, node: ast.Import) -> None:
        """
        Parse info about module `import ...` statements.

        Adds `node` to `import_nodes`.

        Examples::

            import my_module
            import my_module as my
            import my_module.my_class
            import my_module.my_class as my_class

        Arguments:
            node -- AST node.
        """
        self.import_nodes.append(node)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        """
        Parse info about module `import ... from ...` statements.

        Adds `node` to `import_nodes`.

        Examples::

            from my_module import my_class
            from my_module import my_class as new_class

        Arguments:
            node -- AST node.
        """
        self.import_nodes.append(node)

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        """
        Parse info about module `class ...` statements.

        Adds `node` entry to `class_nodes`.
        Skips nodes with names starting with `_`.

        Examples:
            ```python
            class MyClass():
                pass
            ```

        Arguments:
            node -- AST node.
        """
        name = node.name

        # skip private classes
        if name.startswith("_"):
            return

        self.class_nodes.append(node)

    def _visit_FunctionDef(self, node: ASTFunctionDef) -> None:
        name = node.name

        # skip private functions
        if name.startswith("_"):
            return

        self.function_nodes.append(node)

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        """
        Parse info about module `def ...` statements.

        Adds `node` entry to `function_nodes`.
        Skips nodes with names starting with `_`.

        Examples:
            ```python
            def my_func(arg1):
                return arg1
            ```

        Arguments:
            node -- AST node.
        """
        return self._visit_FunctionDef(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        """
        Parse info about module `def ...` statements.

        Adds `node` entry to `function_nodes`.
        Skips nodes with names starting with `_`.

        Examples:
            ```python
            async def my_func(arg1):
                return await arg1
            ```

        Arguments:
            node -- AST node.
        """
        return self._visit_FunctionDef(node)

    def visit_Assign(self, node: ast.Assign) -> None:
        """
        Parse info about module attribute statements.

        Adds new `ast.Assign` entry to `attribute_nodes`.
        Skips assignments to anything pther that a new variable.
        Skips multiple assignments.
        Skips assignments with names starting with `_`.
        Parses `__all__` and add all values to `all_names`

        Examples:
            ```python
            MY_MODULE_ATTR = 'value'
                my_attr = "value"
            __all__ = ['MyClass', 'my_func']

            # these entries are skipped
            _MY_MODULE_ATTR = "value"
            multi_attr_1, multi_attr_2 = [1, 2]
            my_object.name = "value"
            __all__ = all_list
            ```

        Arguments:
            node -- AST node.
        """
        # skip multiple assignments
        if len(node.targets) != 1:
            return
        # skip complex assignments
        if not isinstance(node.targets[0], ast.Name):
            return

        name = node.targets[0].id

        # gather public names from `__all__` directive
        if name == "__all__" and isinstance(node.value, (ast.List, ast.Tuple, ast.Set)):
            for element in node.value.elts:
                if isinstance(element, (ast.Str, ast.Constant)):
                    value = element.s
                    if isinstance(value, bytes):
                        value = value.decode("utf-8")
                    self.all_names.append(value)

        # skip private attributes
        if name.startswith("_"):
            return

        self.attribute_nodes.append(node)
