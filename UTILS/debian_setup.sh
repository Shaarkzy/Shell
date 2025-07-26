#!/bin/bash

BLUE='\033[0;34m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m'
echo -e "\n${BLUE}BUILDING ESSENTIALS FOR PYTHON3-DEV${NC}\n"
apt-get install build-essential python3-dev
echo -e "\n${BLUE}DONE${NC}\n"

echo -e "\n${GREEN}INSTALLING COLORAMA 1/11${NC}\n"
apt-get install python3-colorama
echo -e "\n${GREEN}DONE INSTALLING COLORAMA 1/11${NC}\n"

echo -e "\n${YELLOW}INSTALLING REGEX 2/11${NC}\n"
apt-get install python3-regex
echo -e "\n${YELLOW}DONE INSTALLING REGEX 2/11${NC}\n"

echo -e "\n${BLUE}INSTALLING TQDM 3/11${NC}\n"
apt-get install python3-tqdm
echo -e "\n${BLUE}DONE INSTALLING TQDM 3/11${NC}\n"

echo -e "\n${GREEN}INSTALLING XDG 4/11${NC}\n"
apt-get install python3-xdg
echo -e "\n${GREEN}DONE INSTALLING XDG 4/11${NC}\n"

echo -e "\n${YELLOW}INSTALLING UUID 5/11${NC}\n"
apt-get install python3-uuid
echo -e "\n${YELLOW}DONE INSTALLING UUID 5/11${NC}\n"

echo -e "\n${BLUE}INSTALLING IPADDRESS 6/11${NC}\n"
apt-get install python3-ipaddress
echo -e "\n${BLUE}DONE INSTALLING IPADDRESS 6/11${NC}\n"

echo -e "\n${GREEN}INSTALLING REQUESTS 7/11${NC}\n"
apt-get install python3-requests
echo -e "\n${GREEN}DONE INSTALLING REQUESTS 7/11${NC}\n"

echo -e "\n${YELLOW}INSTALLING PSUTILS 8/11${NC}\n"
apt-get install python3-psutil
echo -e "\n${YELLOW}DONE INSTALLING PSUTILS 8/11${NC}\n"

echo -e "\n${BLUE}INSTALLING PHONENUMBERS 9/11${NC}\n"
apt-get install python3-phonenumbers
echo -e "\n${BLUE}DONE INSTALLING PHONENUMBERS 9/11${NC}\n"

echo -e "\n${GREEN}INSTALLING NETIFACES 10/11${NC}\n"
apt-get install python3-netifaces
echo -e "\n${GREEN}DONE INSTALLING NETIFACES 10/11${NC}\n"

echo -e "\n${YELLOW}INSTALLIBG PYCRYPTODOME 11/11${NC}\n"
bash -c "cd UTILS/BOOT* && ./pycryptodome.sh"
echo -e "\n${YELLOW}DONE INSTALLING PYCRYPTODOME 11/11${NC}\n"

echo -e "\n${GREEN}[*] SETTING UP SHELL.PY${NC}"

chmod +x shell.py
cd ~/; ln -s ~/Shell/shell.py /usr/local/bin/shell

echo -e "\n${YELLOW}[*] IF NOT ERROR: Start Terminal By executing: shell${NC}\n"
