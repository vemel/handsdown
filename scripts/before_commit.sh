#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $(realpath $0)))
cd $ROOT_PATH

mypy handsdown
pylint handsdown
pytest

./scripts/update_docs.sh
