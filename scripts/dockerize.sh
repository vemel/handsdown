#!/usr/bin/env bash
set -e

VERSION=`handsdown -v`

docker build --tag handsdown --tag handsdown:latest --tag handsdown:$VERSION .
