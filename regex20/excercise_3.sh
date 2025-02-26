#!/bin/bash

# $1: filename

grep -o "error" $1 | wc -l
