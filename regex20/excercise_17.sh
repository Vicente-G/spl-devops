#!/bin/bash

# $1: filename

year="[0-3]{1}[0-9]{3}"
month="(0[1-9]|1[0-2])"
day="(0[1-9]|[12][0-9]|3[01])"
grep -o -E "\b$year-$month-$day\b" $1