#!/bin/bash
#colour code
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[0;33m'

#detect os and setup installation
detect_os() {
    if [[ "$(uname)" == "Linux" ]]; then
    
        if [[ "$(uname -a | grep -i android)" ]]; then
            echo -e "${GREEN}INSTALLING PYTHON3 & FILE ${NC}"
            pkg install python3
	        pkg install file
            echo -e "${BLUE}DONE${NC}"
            /data/data/com.termux/files/home/Shell/Setup/android_setup.sh
            
        elif grep -Eq '^(ID|ID_LIKE)=.*debian' /etc/os-release; then
            if [[ "$PWD" == /root* ]]; then
                USER_NAME="root"
            else
                USER_NAME="${SUDO_USER:-$(whoami)}"
            fi
            USER_HOME="$(getent passwd "$USER_NAME" | cut -d: -f6)"
            echo -e "${GREEN}INSTALLING PYTHON3${NC}"
            apt-get install python3
	        apt-get install file
            echo -e "${BLUE}DONE${NC}"
            $USER_HOME/Shell/Setup/debian_setup.sh

	    else
	        echo -e "${RED}[x]No Setup File For Your Os${NC}"
        fi
    else
        echo -e "${RED}[x]Unsupported OS : Read Documentation${NC}"
    fi
}
# run function
detect_os
