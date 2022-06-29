"""
Various project constants.
"""
import enum

# Global `logging.Logger` name.
LOGGER_NAME = "handsdown"

# Paths to exclude from docs generation.
EXCLUDE_EXPRS = ["build/*", "tests/*", "test/*", "*/__pycache__/*", ".*/*"]

# `glob.glob` expression to ind all Python sources in current directory.
SOURCES_GLOB = "**/*.py"

# Default encoding for source files
ENCODING = "utf-8"


class Theme(enum.Enum):
    RTD = "readthedocs"
    MD = "material"
