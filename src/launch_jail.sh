#!/bin/bash

# Needed by cgroups limiting
mkdir -p /sys/fs/cgroup/{cpu,memory,pids}/NSJAIL

nsjail --config /task/nsjail.cfg 100<>/task/chall.py

