#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <main.py>"
    exit 1
fi

python3 "$1"
