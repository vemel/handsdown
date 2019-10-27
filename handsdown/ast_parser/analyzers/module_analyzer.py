"""
AST analyzer for `ast.Module` records.
"""
from typing import List, Text, TYPE_CHECKING

from handsdown.ast_parser.analyzers.base_analyzer import BaseAnalyzer
import handsdown.ast_parser.smart_ast as ast

if TYPE_CHECKING:  # pragma: no cover
    from handsdown.ast_parser.type_defs import ASTImport


class ModuleAnalyzer(BaseAnalyzer):
    """
    AST analyzer for `ast.Module` records.
    """

    def __init__(self):
        # type: () -> None
        super(ModuleAnalyzer, self).__init__()
        self.all_names = []  # type: List[Text]
        self.import_nodes = []  # type: List[ASTImport]
        self.function_nodes = []  # type: List[ast.FunctionDef]
        self.attribute_nodes = []  # type: List[ast.Assign]
        self.class_nodes = []  # type: List[ast.ClassDef]

    def visit_Import(self, node):
        # type: (ast.Import) -> None
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

    def visit_ImportFrom(self, node):
        # type: (ast.ImportFrom) -> None
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

    def visit_ClassDef(self, node):
        # type: (ast.ClassDef) -> None
        """
        Parse info about module `class ...` statements.

        Adds `node` entry to `class_nodes`.
        Skips nodes with names starting with `_`.

        Examples::

            class MyClass():
                pass

        Arguments:
            node -- AST node.
        """

        name = node.name

        # skip private classes
        if name.startswith("_"):
            return

        self.class_nodes.append(node)

    def visit_FunctionDef(self, node):
        # type: (ast.FunctionDef) -> None
        """
        Parse info about module `def ...` statements.

        Adds `node` entry to `function_nodes`.
        Skips nodes with names starting with `_`.

        Examples::

            def my_func(arg1):
                pass

        Arguments:
            node -- AST node.
        """

        name = node.name

        # skip private functions
        if name.startswith("_"):
            return

        self.function_nodes.append(node)

    def visit_Assign(self, node):
        # type: (ast.Assign) -> None
        """
        Parse info about module attribute statements.

        Adds new `ast.Assign` entry to `attribute_nodes`.
        Skips assignments to anything pther that a new variable.
        Skips multiple assignments.
        Skips assignments with names starting with `_`.
        Parses `__all__` and add all values to `all_names`

        Examples::

            MY_MODULE_ATTR = 'value'
                my_attr = "value"
            __all__ = ['MyClass', 'my_func']

            # these entries are skipped
            _MY_MODULE_ATTR = "value"
            multi_attr_1, multi_attr_2 = [1, 2]
            my_object.name = "value"
            __all__ = all_list

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
                if isinstance(element, ast.Str):
                    value = element.s
                    if isinstance(value, bytes):
                        value = value.decode("utf-8")
                    self.all_names.append(value)

        # skip private attributes
        if name.startswith("_"):
            return

        self.attribute_nodes.append(node)
