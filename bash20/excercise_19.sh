#!/bin/bash

while true; do
    usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
    if [[ ${usage%.*} > 90 ]]; then
        echo "High CPU usage: $usage%"
    fi
    sleep 5
done
