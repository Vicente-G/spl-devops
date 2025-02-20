#!/bin/bash

# $1: directory to search over

find "$1" -type f -mtime +7 -exec rm {} +
