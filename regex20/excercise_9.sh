#!/bin/bash

for file in ./*; do
    if [[ -f $file ]]; then
        count=$(grep -o '\<script\>' $file | wc -l)
        if [[ $count -gt 0 ]]; then
            echo $file
        fi
    fi
done