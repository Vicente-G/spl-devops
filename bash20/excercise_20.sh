#!/bin/bash

# $1: .sh file schedule

current_tasks=$(crontab -l)
(echo $current_tasks; echo "0 0 * * * $1") | crontab -
