#!/bin/bash

PURPLE='\033[1;35m'
ORANGE='\033[0;33m'
NC='\033[0m'

script_name="main.py"
script_directory=$(dirname "$(readlink -f "$0")")
script_path="$script_directory/$script_name"

echo -e "${ORANGE} Running : $script_path.${NC}"
echo -e "${PURPLE} By Etib-Corp. ${NC}"
python3 $script_path "$@"