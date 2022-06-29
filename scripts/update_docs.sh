#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $(realpath $0)))
cd $ROOT_PATH

handsdown -o docs_local --cleanup --branch main $@
handsdown --external `git config --get remote.origin.url` --cleanup --branch main --theme=material $@
