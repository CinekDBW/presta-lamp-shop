#!/bin/bash

CONTAINER=''

docker cp ./dump.sql $CONTAINER:/tmp/be_180197_init.sql
docker cp ./dump.sh $CONTAINER:/tmp/be_180197_init.sh
docker exec $CONTAINER chmod 777 /tmp/be_180197_init.sh
docker exec $CONTAINER /tmp/be_180197_init.sh
docker exec $CONTAINER rm /tmp/be_180197_init.sql
docker exec $CONTAINER rm /tmp/be_180197_init.sh