#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $(realpath $0)))
cd $ROOT_PATH

poetry run handsdown -o docs_local --cleanup --branch main $@
