#!/usr/bin/env bash

set -e

base_name="dvglab/oracle-fastapi-docker"
use_tag="${base_name}:$NAME"
use_dated_tag="${use_tag}-$(date -I)"

bash scripts/build.sh

docker tag "$use_tag" "$use_dated_tag"

bash scripts/docker-login.sh

if [ "$NAME" != "latest" ] ; then
  use_tag_short="${base_name}:$NAME_SHORT"
  docker tag "$use_tag" "$use_tag_short" 
  docker push "$use_tag_short"
fi

docker push "$use_tag"
docker push "$use_dated_tag"
