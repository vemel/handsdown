#!/usr/bin/env bash
set -e

IMAGE_NAME="handsdown"
VERSION=`python -m handsdown -v`

docker build --tag ${IMAGE_NAME} .

# docker login docker.pkg.github.com --username vemel -p $GITHUB_TOKEN

docker tag handsdown docker.pkg.github.com/vemel/handsdown/${IMAGE_NAME}:latest

docker push docker.pkg.github.com/vemel/handsdown/${IMAGE_NAME}:latest
