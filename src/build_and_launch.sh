#!/bin/bash

docker build -t reverse-me-chall . && \
    docker run -d -v /sys/fs/cgroup:/sys/fs/cgroup:rw \
               -p 31337:31337 --privileged --rm reverse-me-chall

