"""
Exceptions used by the project.
"""


class GeneratorError(Exception):
    """
    Main error for `BaseGenerator`.
    """


class LoaderError(Exception):
    """
    Main error for `Loader`.
    """


class ImportStringError(Exception):
    """
    Main error for `ImportString`.
    """


class PathFinderError(Exception):
    """
    Main error for `PathFinder`.
    """


class ParserError(Exception):
    """
    Main error for source code parsing issues.
    """
