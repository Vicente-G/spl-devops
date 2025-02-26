#!/bin/bash

# $1: filename

grep -o '\<auto[a-z]*\>' $1
