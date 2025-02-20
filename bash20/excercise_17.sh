#!/bin/bash

# $1: filename
# $2: old string
# $3: new string

sed -i "s/$2/$3/g" "$1"
