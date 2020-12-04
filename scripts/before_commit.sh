#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $(realpath $0)))
cd $ROOT_PATH

black handsdown
isort handsdown
flake8 handsdown
pytest --cov-report term --cov=handsdown
pyright handsdown
pylint handsdown

./scripts/update_docs.sh
