# -*- coding: utf-8 -*-
"""
Various project constants.
"""
import os


# Path to handsdown root directory.
HANDSDOWN_PATH = os.path.dirname(__file__)

# Path to `assets` directory from root.
ASSETS_PATH = os.path.join(HANDSDOWN_PATH, "assets")

# Global `logging.Logger` name.
LOGGER_NAME = "handsdown"

# Paths to exclude from docs generation.
EXCLUDE_EXPRS = ["build/*", "tests/*", "test/*", "*/__pycache__/*", ".*/*"]

# `glob.glob` expression to ind all Python sources in current directory.
SOURCES_GLOB = "**/*.py"

# Find in code link label.
FIND_IN_SOURCE_LABEL = "[find in source code]"
