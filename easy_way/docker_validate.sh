#!/bin/bash

function pretty_echo {
    echo -e "\e[32m$1\e[0m"
}

pretty_echo "Building docker image"
docker build --tag jcronq/ramdisk .
pretty_echo "Running docker image and testing ram-disk speed"
docker run --mount type=tmpfs,destination=/mnt/ramdisk jcronq/ramdisk
pretty_echo "The speed above should be over 2GB/s if running in-memory"
pretty_echo "Stopping docker container"
docker ps | grep jcronq | cut -d" " -f -1 | xargs -I {} sh -c "docker stop {}"

