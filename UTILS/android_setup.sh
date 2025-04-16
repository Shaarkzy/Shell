#!/usr/bin/bash

BLUE='\033[0;34m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m'

echo -e "\n${BLUE}INSTALLING COLORAMA 1/12${NC}\n"
pip install colorama
echo -e "\n${BLUE}DONE INSTALLING COLORAMA 1/12${NC}\n"

echo -e "\n${GREEN}INSTALLING REGEX 2/12${NC}\n"
pip install regex
echo -e "\n${GREEN}DONE INSTALLING REGEX 2/12${NC}\n"

echo -e "\n${YELLOW}INSTALLING TQDM 3/12${NC}\n"
pip install tqdm
echo -e "\n${YELLOW}DONE INSTALLING TQDM 3/12${NC}\n"

echo -e "\n${BLUE}INSTALLING XDG 4/12${NC}\n"
pip install xdg
echo -e "\n${BLUE}DONE INSTALLING XDG 4/12${NC}\n"

echo -e "\n${GREEN}INSTALLING UUID 5/12${NC}\n"
pip install uuid
echo -e "\n${GREEN}DONE INSTALLING UUID 5/12${NC}\n"

echo -e "\n${YELLOW}INSTALLING IPADDRESSES 6/12${NC}\n"
pip install ipaddress
echo -e "\n${YELLOW}DONE INSTALLING IPADDRESSES 6/12${NC}\n"

echo -e "\n${BLUE}INSTALLING REQUESTS 7/12${NC}\n"
pip install requests
echo -e "\n${BLUE}DONE INSTALLING REQUESTS 7/12${NC}\n"

echo -e "\n${GREEN}INSTALLING PSUTILS 8/12${NC}\n"
pip install psutil
echo -e "\n${GREEN}DONE INSTALLING PSUTILS 8/12${NC}\n"

echo -e "\n${YELLOW}INSTALLING NETIFACES 9/12${NC}\n"
pip install netifaces
echo -e "\n${YELLOW}DONE INSTALLING NETIFACES 9/12${NC}\n"

echo -e "\n${BLUE}INSTALLING PHONENUMBERS 10/12${NC}\n"
pip install phonenumbers
echo -e "\n${BLUE}DONE INSTALLING PHONENUMBERS 10/12${NC}\n"

echo -e "\n${GREEN}INSTALLING PYCRYPTODOME 11/12${NC}\n"
pip install pycryptodome
echo -e "\n${GREEN}DONE INSTALLING PYCRYPTODOME 11/12${NC}\n"

echo -e "\n${BLUE}INSTALLING NEOFETCH 12/12${NC}\n"
pkg install neofetch
echo -e "\n${BLUE}DONE INSTALLING NEOFETCH 12/12${NC}\n"

echo -e "\n${BLUE}[*] SETTING UP SHELL.PY${NC}"
chmod +x shell.py
ln -s ~/Shell/shell.py /data/data/com.termux/files/usr/bin/shell
echo -e "\n${GREEN}[*] IF NOT ERROR: Start Terminal By executing : shell${NC}\n"
