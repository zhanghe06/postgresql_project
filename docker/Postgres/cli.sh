#!/usr/bin/env bash

docker run \
    -it \
    --rm \
    --link postgres:postgres \
    postgres:9.6 \
    psql -h postgres -U www -d demo
