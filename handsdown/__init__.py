"""
Root of `handsdown` source code.
"""
from handsdown.generator import Generator
from handsdown.path_finder import PathFinder
from handsdown.loader import LoaderError
from handsdown.version import version

name = "handsdown"
_version = version
__all__ = ["Generator", "PathFinder", "LoaderError", "name"]
