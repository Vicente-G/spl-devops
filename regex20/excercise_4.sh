#!/bin/bash

for file in *.log; do
    grep "warning" $file
done
