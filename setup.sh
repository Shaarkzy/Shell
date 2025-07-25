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
            echo -e "${GREEN}INSTALLING PYTHON3 ${NC}"
            pkg install python3
            echo -e "${BLUE}DONE${NC}"
            ./UTILS/android_setup.sh
            
        elif [[ "$(uname -a | grep -i kali)" ]]; then
            echo -e "${GREEN}INSTALLING PYTHON3${NC}"
            apt-get install python3
            echo -e "${BLUE}DONE${NC}"
            ./UTILS/kali_setup.sh

	else
	    echo "${RED}[x]No Setup File For Your Os${NC}"
        fi
    else
        echo "${RED}[x]Unsupported OS : Read Documentation${NC}"
    fi
}
# run function
detect_os
