#!/bin/bash

backup_dir="/backup/$(date +%F)"
mkdir -p "$backup_dir"
cp /etc/*.conf "$backup_dir"
