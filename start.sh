#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <main.py>"
    exit 1
fi

BLUE='\033[0;34m' # Blue Collor
NC='\033[0m' # No Color

echo -e "${BLUE}Game started..${NC}"

# Start python file
python3 "$1"

exit
