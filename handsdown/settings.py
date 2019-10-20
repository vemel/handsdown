"""
Various project constants.

Attributes:
    ASSETS_PATH -- Path to `assets` directory.
    LOGGER_NAME -- Global `logging.Logger` name.
    EXCLUDE_EXPRS -- Paths to exclude from docs generation.
    SOURCES_GLOB -- `glob.glob` expression to ind all Python sources in current directory.
"""
try:
    from pathlib import Path
except ImportError:
    from pathlib2 import Path  # type: ignore


ASSETS_PATH = Path(__file__).parent.parent / "assets"
LOGGER_NAME = "handsdown"
EXCLUDE_EXPRS = ["build/*", "tests/*", "test/*", "*/__pycache__/*", ".*/*"]
SOURCES_GLOB = "**/*.py"
