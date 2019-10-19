#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $(realpath $0)))
cd $ROOT_PATH

pytest --cov-report term --cov=handsdown
mypy handsdown
pylint handsdown

./scripts/update_docs.sh
