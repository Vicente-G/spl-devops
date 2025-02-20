#!/bin/bash

# $1: filename

if [[ -f "$1" ]]; then
    echo "File exists"
else
    echo "File does not exist"
fi
