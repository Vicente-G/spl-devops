#!/bin/bash

# $1: filename

name="[A-Za-z0-9._%+-]+"
domain="[A-Za-z0-9.-]+"
ext="[A-Z|a-z]{2,}"
grep -o -E "\b$name@$domain\.$ext\b" $1