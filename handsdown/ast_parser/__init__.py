import sys

ast_version = sys.version_info.major

try:
    if sys.version_info.major == 2:
        import typed_ast.ast2 as ast
    else:
        import typed_ast.ast3 as ast  # type: ignore
except ImportError:
    import ast  # type: ignore
