#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $(realpath $0)))
cd $ROOT_PATH

poetry run handsdown -o docs_local --cleanup --branch main $@
poetry run handsdown --external `git config --get remote.origin.url` -o docsmd --cleanup --theme material --branch main $@
rm -rf docs/*
poetry run mkdocs build
