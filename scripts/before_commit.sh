#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $(realpath $0)))
cd $ROOT_PATH

# vulture handsdown --make-whitelist > vulture_whitelist.txt
poetry run vulture handsdown vulture_whitelist.txt
poetry run black handsdown --preview
poetry run isort handsdown
poetry run flake8 handsdown
poetry run npx pyright
poetry run pytest
