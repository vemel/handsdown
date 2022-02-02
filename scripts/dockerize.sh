#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))
cd ${ROOT_PATH}

IMAGE_NAME="handsdown"
VERSION=`python -m handsdown --version`

docker build --tag ${IMAGE_NAME} .

docker tag handsdown docker.pkg.github.com/vemel/handsdown/${IMAGE_NAME}:latest
docker tag handsdown docker.pkg.github.com/vemel/handsdown/${IMAGE_NAME}:${VERSION}

docker login docker.pkg.github.com --username vemel -p $GITHUB_TOKEN
docker push docker.pkg.github.com/vemel/handsdown/${IMAGE_NAME}:latest
docker push docker.pkg.github.com/vemel/handsdown/${IMAGE_NAME}:${VERSION}
