#!/usr/bin/env zsh

set -e
set -x

kill -16 $(cat /tmp/.smart_cat_pid) || true
make upload