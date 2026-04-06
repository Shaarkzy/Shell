#!/bin/bash

BLUE='\033[0;34m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m'

USER_NAME="${SUDO_USER:-$USER}"
USER_HOME="$(getent passwd "$USER_NAME" | cut -d: -f6)"

echo -e "\n${BLUE}BUILDING ESSENTIALS FOR PYTHON3-DEV${NC}\n"
apt-get install build-essential python3-dev
echo -e "\n${BLUE}DONE${NC}\n"

echo -e "\n${GREEN}INSTALLING COLORAMA 1/12${NC}\n"
apt-get install python3-colorama
echo -e "\n${GREEN}DONE INSTALLING COLORAMA 1/12${NC}\n"

echo -e "\n${YELLOW}INSTALLING REGEX 2/12${NC}\n"
apt-get install python3-regex
echo -e "\n${YELLOW}DONE INSTALLING REGEX 2/12${NC}\n"

echo -e "\n${BLUE}INSTALLING TQDM 3/12${NC}\n"
apt-get install python3-tqdm
echo -e "\n${BLUE}DONE INSTALLING TQDM 3/12${NC}\n"

echo -e "\n${GREEN}INSTALLING XDG 4/12${NC}\n"
apt-get install python3-xdg
echo -e "\n${GREEN}DONE INSTALLING XDG 4/12${NC}\n"

echo -e "\n${YELLOW}INSTALLING UUID 5/12${NC}\n"
apt-get install python3-uuid
echo -e "\n${YELLOW}DONE INSTALLING UUID 5/12${NC}\n"

echo -e "\n${BLUE}INSTALLING IPADDRESS 6/12${NC}\n"
apt-get install python3-ipaddress
echo -e "\n${BLUE}DONE INSTALLING IPADDRESS 6/12${NC}\n"

echo -e "\n${GREEN}INSTALLING REQUESTS 7/12${NC}\n"
apt-get install python3-requests
echo -e "\n${GREEN}DONE INSTALLING REQUESTS 7/12${NC}\n"

echo -e "\n${BLUE}INSTALLING PHONENUMBERS 8/12${NC}\n"
apt-get install python3-phonenumbers
echo -e "\n${BLUE}DONE INSTALLING PHONENUMBERS 8/12${NC}\n"

echo -e "\n${GREEN}INSTALLING NETIFACES 9/12${NC}\n"
apt-get install python3-netifaces
echo -e "\n${GREEN}DONE INSTALLING NETIFACES 9/12${NC}\n"

echo -e "\n${YELLOW}INSTALLING PYCRYPTODOME 10/12${NC}\n"
bash -c "./pycryptodome.sh"
echo -e "\n${YELLOW}DONE INSTALLING PYCRYPTODOME 10/12${NC}\n"

echo -e "\n${YELLOW}INSTALLING PROMPT TOOLKIT 11/12${NC}\n"
apt-get install python3-prompt-toolkit
echo -e "\n${YELLOW}DONE INSTALLING PROMPT TOOLKIT 11/12${NC}\n"

echo -e "\n${YELLOW}INSTALLING BEAUTIFULSOUP 12/12${NC}\n"
apt-get install python3-bs4
echo -e "\n${YELLOW}DONE INSTALLING BEAUTIFULSOUP 12/12${NC}\n"

echo -e "\n${GREEN}[*] SETTING UP SHELL.PY${NC}"

chmod +x "$USER_HOME/Shell/Core/shell.py"
ln -sf "$USER_HOME/Shell/launcher.py" "/usr/local/bin/shell"

echo -e "\n${YELLOW}[*] IF NOT ERROR: Start Terminal By executing: shell${NC}\n"
