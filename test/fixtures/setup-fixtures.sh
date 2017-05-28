#!/usr/bin/env bash

echo "Setup fixtures..."
for l in $(ls /docker-entrypoint-initdb.d/*.sql | sort); do
  echo "> $(dirname $l)"
  cat $l | mysql;
done
