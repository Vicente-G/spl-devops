#!/bin/bash

# $1: user name or IP address

bit8="([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"
ipv4="($bit8\.){3}$bit8"
user="[a-zA-Z0-9_]{1,32}"

validation=$(echo $1 | grep -o -E "^\<$ipv4|$user\>$")
if [[ $validation != $1 ]]; then
    echo "Invalid input"
    exit 1
fi
last | grep $1 | head -n 5