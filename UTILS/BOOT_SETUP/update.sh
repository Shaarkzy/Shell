#!/bin/bash

GREEN='\033[0;32m'
YELLOW='\033[0;33m'
RED='\033[0;31m'
NC='\033[0m'

# Define paths
TARGET_DIR="$HOME/Shell"
TEMP_DIR="$HOME/Shell_temp"
REPO_URL="https://github.com/Shaarkzy/Shell"

# Clone the repo to a temporary directory
echo -e "${YELLOW}[!]Software Updating...${NC}"
git clone "$REPO_URL" "$TEMP_DIR" > /dev/null 2>&1

# Check if the clone was successful
if [ $? -eq 0 ]; then
    # If the main Shell directory exists, remove it
    if [ -d "$TARGET_DIR" ]; then
	#copy files before deleting
	# 1. .shellrc
	cp -r "$TARGET_DIR"/UTILS/.shellrc "$TEMP_DIR"/UTILS/.shellrc
        rm -rf "$TARGET_DIR"
    fi

    # Rename temp folder to Shell
    mv "$TEMP_DIR" "$TARGET_DIR"
    echo -e "${GREEN}[*]Update Successful${NC}"

    version="$HOME/Shell/__version__"
    if [ -f "$version" ]; then
        data=$(cat "$version")
        echo -e "${YELLOW}[!] SOFTWARE UPDATED: VERSION: ${GREEN}${data}${NC}"
        echo -e "${YELLOW}[!] PLEASE REFRESH YOUR TERMINAL${NC}"
    else
        echo -e "${RED}[x]Version File Not Found${NC}"
    fi
else
    echo -e "${RED}[x]Update Failed${NC}"
    # Optionally clean up
    [ -d "$TEMP_DIR" ] && rm -rf "$TEMP_DIR"
fi
