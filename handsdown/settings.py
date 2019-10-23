# -*- coding: utf-8 -*-
"""
Various project constants.

Attributes:
    HANDSDOWN_PATH -- Path to handsdown root directory.
    ASSETS_PATH -- Path to `assets` directory from root.
    LOGGER_NAME -- Global `logging.Logger` name.
    EXCLUDE_EXPRS -- Paths to exclude from docs generation.
    SOURCES_GLOB -- `glob.glob` expression to ind all Python sources in current directory.
"""
import os


HANDSDOWN_PATH = os.path.dirname(__file__)
ASSETS_PATH = os.path.join(HANDSDOWN_PATH, "assets")
LOGGER_NAME = "handsdown"
EXCLUDE_EXPRS = ["build/*", "tests/*", "test/*", "*/__pycache__/*", ".*/*"]
SOURCES_GLOB = "**/*.py"
FIND_IN_SOURCE_LABEL = "🔍 find in source code"
