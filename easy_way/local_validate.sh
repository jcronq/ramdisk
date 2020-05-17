#!/bin/bash

function pretty_echo {
    echo -e "\e[32m$1\e[0m"
}

[[ -d /mnt/ramdisk ]] || sudo mkdir -p /mnt/ramdisk
pretty_echo "Testing disk speed"
./bash/ramdiskctl test
pretty_echo "Starting in-memory fs"
./bash/ramdiskctl start
pretty_echo "Testing ram-disk speed"
./bash/ramdiskctl test
pretty_echo "The speed above should be much faster than the disk speed."
pretty_echo "Removing ramdisk"
./bash/ramdiskctl stop
