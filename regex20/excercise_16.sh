#!/bin/bash

# $1: filename

method="(http|https)"
domain="[A-Za-z0-9.-]+"
ext="[A-Z|a-z]{2,}"
routing="(([\/#?]{1}[A-Za-z0-9.-=&]+)*|\/)"
grep -o -E "\b$method://$domain\.$ext$routing\b" $1