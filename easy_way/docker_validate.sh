#!/bin/bash

function pretty_echo {
    echo -e "\e[32m$1\e[0m"
}

[[ -d /mnt/ramdisk ]] || sudo mkdir -p /mnt/ramdisk
pretty_echo "Testing disk speed"
bash/ramdiskctl test
bash/ramdiskctl test
pretty_echo "Building docker image"
docker build --tag jcronq/ramdisk .
pretty_echo "Running docker image and testing ram-disk speed"
docker run --mount type=tmpfs,destination=/mnt/ramdisk jcronq/ramdisk
pretty_echo "The speed above should be much faster than the disk speed."
pretty_echo "Removing ramdisk"
docker ps | grep jcronq | cut -d" " -f -1 | xargs -I {} sh -c "docker stop {}"

