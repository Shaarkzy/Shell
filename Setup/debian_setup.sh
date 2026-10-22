#!/bin/bash

BLUE='\033[0;34m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m'


if [[ "$PWD" == /root* ]]; then
    USER_NAME="root"
else
    USER_NAME="${SUDO_USER:-$(whoami)}"
fi

USER_HOME="$(getent passwd "$USER_NAME" | cut -d: -f6)"

echo -e "\n${BLUE}BUILDING ESSENTIALS FOR PYTHON3-DEV${NC}\n"
apt-get install build-essential python3-dev -y
echo -e "\n${BLUE}DONE${NC}\n"

echo -e "\n${GREEN}INSTALLING COLORAMA 1/12${NC}\n"
apt-get install python3-colorama -y
echo -e "\n${GREEN}DONE INSTALLING COLORAMA 1/12${NC}\n"

echo -e "\n${YELLOW}INSTALLING REGEX 2/12${NC}\n"
apt-get install python3-regex -y
echo -e "\n${YELLOW}DONE INSTALLING REGEX 2/12${NC}\n"

echo -e "\n${BLUE}INSTALLING TQDM 3/12${NC}\n"
apt-get install python3-tqdm -y
echo -e "\n${BLUE}DONE INSTALLING TQDM 3/12${NC}\n"

echo -e "\n${GREEN}INSTALLING XDG 4/12${NC}\n"
apt-get install python3-xdg -y
echo -e "\n${GREEN}DONE INSTALLING XDG 4/12${NC}\n"

echo -e "\n${YELLOW}INSTALLING UUID 5/12${NC}\n"
apt-get install python3-uuid -y
echo -e "\n${YELLOW}DONE INSTALLING UUID 5/12${NC}\n"

echo -e "\n${BLUE}INSTALLING IPADDRESS 6/12${NC}\n"
apt-get install python3-ipaddress -y
echo -e "\n${BLUE}DONE INSTALLING IPADDRESS 6/12${NC}\n"

echo -e "\n${GREEN}INSTALLING REQUESTS 7/12${NC}\n"
apt-get install python3-requests -y  
echo -e "\n${GREEN}DONE INSTALLING REQUESTS 7/12${NC}\n"

echo -e "\n${BLUE}INSTALLING PHONENUMBERS 8/12${NC}\n"
apt-get install python3-phonenumbers -y
echo -e "\n${BLUE}DONE INSTALLING PHONENUMBERS 8/12${NC}\n"

echo -e "\n${GREEN}INSTALLING NETIFACES 9/12${NC}\n"
apt-get install python3-netifaces -y 
echo -e "\n${GREEN}DONE INSTALLING NETIFACES 9/12${NC}\n"

echo -e "\n${YELLOW}INSTALLING PYCRYPTODOME 10/12${NC}\n"
bash -c "./pycryptodome.sh" -y
echo -e "\n${YELLOW}DONE INSTALLING PYCRYPTODOME 10/12${NC}\n"

echo -e "\n${YELLOW}INSTALLING PROMPT TOOLKIT 11/12${NC}\n"
apt-get install python3-prompt-toolkit -y
echo -e "\n${YELLOW}DONE INSTALLING PROMPT TOOLKIT 11/12${NC}\n"

echo -e "\n${YELLOW}INSTALLING BEAUTIFULSOUP 12/12${NC}\n"
apt-get install python3-bs4 -y
echo -e "\n${YELLOW}DONE INSTALLING BEAUTIFULSOUP 12/12${NC}\n"

echo -e "\n${YELLOW}[*] RUN < root | /home/user > /Shell/Core/relink & Start Terminal By executing: shell${NC}\n"