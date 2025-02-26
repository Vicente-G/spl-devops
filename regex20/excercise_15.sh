#!/bin/bash

# $1: filename

first200="[01]?[0-9]?[0-9]"
over200="2[0-4][0-9]"
last250s="25[0-5]"
bit8="$first200|$over200|$last250s"
grep -o -E "\b($bit8\.){3}$bit8\b" $1