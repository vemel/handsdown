#!/usr/bin/env bash
set -e

git checkout main
git push
git branch -D docs || true
git checkout docs --
git pull
git checkout main -- .github
git commit -am "Sync main"
git push
git checkout main
