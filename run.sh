#!/bin/bash

docker run --rm \
  --name volbackup \
  -v /var/run/docker.sock:/var/run/docker.sock \
  volbackup