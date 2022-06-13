#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $(realpath $0)))
cd $ROOT_PATH

# vulture handsdown --make-whitelist > vulture_whitelist.txt
vulture handsdown vulture_whitelist.txt
python -m black handsdown --preview
python -m isort handsdown
python -m flake8 handsdown
python -m pytest --cov-report term --cov=handsdown
python -m mypy handsdown
npx pyright
python -m pylint handsdown

./scripts/update_docs.sh
