#!/bin/bash

# $1: filename
# $2: word to count

grep -o "$2" "$1" | wc -l
