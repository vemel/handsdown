"""
Various project constants.
"""
from pathlib import Path

# Path to handsdown root directory.
HANDSDOWN_PATH = Path(__file__).parent

# Path to `assets` directory from root.
ASSETS_PATH = HANDSDOWN_PATH / "assets"

# Global `logging.Logger` name.
LOGGER_NAME = "handsdown"

# Paths to exclude from docs generation.
EXCLUDE_EXPRS = ["build/*", "tests/*", "test/*", "*/__pycache__/*", ".*/*"]

# `glob.glob` expression to ind all Python sources in current directory.
SOURCES_GLOB = "**/*.py"

# Find in code link label.
FIND_IN_SOURCE_LABEL = "[find in source code]"
